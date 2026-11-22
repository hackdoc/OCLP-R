import SwiftUI
import AppKit

// MARK: - Shared helpers

func copyToClipboard(_ text: String) {
    NSPasteboard.general.clearContents()
    NSPasteboard.general.setString(text, forType: .string)
}

enum DownloadKind {
    case kdk, metallib, ipsw

    var title: String {
        switch self {
        case .kdk: return "KDK Download"
        case .metallib: return "Metallib Download"
        case .ipsw: return "IPSW Download"
        }
    }

    var emptyHint: String {
        switch self {
        case .kdk: return "No Kernel Debug Kits available."
        case .metallib: return "No MetallibSupportPkg packages available."
        case .ipsw: return "No IPSW images available."
        }
    }
}

func humanBytes(_ bytes: Int) -> String {
    ByteCountFormatter.string(fromByteCount: Int64(bytes), countStyle: .file)
}

func downloadFilename(from url: String) -> String {
    URL(string: url)?.lastPathComponent ?? "download"
}

/// Directory where user-facing downloads (KDK / Metallib / IPSW) are stored.
var downloadDirectory: URL {
    get {
        if let saved = UserDefaults.standard.string(forKey: "downloadDirectory"), !saved.isEmpty {
            return URL(fileURLWithPath: saved)
        }
        return FileManager.default.urls(for: .downloadsDirectory, in: .userDomainMask).first
            ?? FileManager.default.homeDirectoryForCurrentUser
    }
    set {
        UserDefaults.standard.set(newValue.path, forKey: "downloadDirectory")
    }
}

@MainActor
func chooseDownloadDirectory() {
    let panel = NSOpenPanel()
    panel.canChooseDirectories = true
    panel.canChooseFiles = false
    panel.allowsMultipleSelection = false
    panel.prompt = "Choose"
    panel.message = "Choose where to save downloads."
    if panel.runModal() == .OK, let url = panel.url {
        downloadDirectory = url
    }
}

// MARK: - Progress bar

struct DownloadProgressView: View {
    let progress: DownloadProgress?

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            if let progress {
                ProgressView(value: max(0, min(progress.percent, 100)), total: 100)
                HStack {
                    Text("\(progress.percent, specifier: "%.1f")%")
                        .monospacedDigit()
                    if progress.speed > 0 {
                        Text("· \(humanBytes(Int(progress.speed)))/s")
                            .monospacedDigit()
                    }
                    Spacer()
                    Text("\(humanBytes(progress.downloaded)) of \(humanBytes(progress.total))")
                        .monospacedDigit()
                        .foregroundStyle(.secondary)
                }
                .font(.caption)
            } else {
                ProgressView()
                    .controlSize(.small)
            }
        }
    }
}

// MARK: - Generic catalog download (KDK / Metallib / IPSW)

struct DownloadCatalogView: View {
    @EnvironmentObject private var state: AppState
    let kind: DownloadKind

    @State private var items: [DownloadItem] = []
    @State private var selected: DownloadItem?
    @State private var loading = true
    @State private var error: String?
    @State private var downloading = false
    @State private var progress: DownloadProgress?
    @StateObject private var log = OperationLog()

    var body: some View {
        VStack(spacing: 16) {
            if loading {
                Spacer()
                ProgressView("Fetching catalog…")
                Spacer()
            } else if let error, items.isEmpty {
                Spacer()
                ContentUnavailableView("Catalog unavailable", systemImage: "wifi.exclamationmark", description: Text(error))
                Spacer()
            } else if items.isEmpty {
                Spacer()
                ContentUnavailableView("Nothing available", systemImage: "tray", description: Text(kind.emptyHint))
                Spacer()
            } else {
                catalogList
            }
        }
        .padding(20)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .navigationTitle(kind.title)
        .task { await load() }
    }

    private var catalogList: some View {
        VStack(spacing: 12) {
            List(items, selection: $selected) { item in
                HStack(spacing: 12) {
                    PayloadIconView(name: iconName(for: item))
                        .frame(width: 30, height: 30)
                    VStack(alignment: .leading, spacing: 3) {
                        Text(item.displayName)
                            .fontWeight(.medium)
                        if let build = item.build, !build.isEmpty {
                            Text("Build \(build)")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                        HStack(spacing: 8) {
                            if let size = item.size, size > 0 {
                                Text(humanBytes(size))
                            }
                            if let date = item.date, !date.isEmpty {
                                Text(String(date.prefix(10)))
                            }
                        }
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                    }
                    Spacer()
                }
                .padding(.vertical, 2)
                .tag(item)
            }
            .listStyle(.inset)

            actionBar
        }
    }

    private var actionBar: some View {
        VStack(spacing: 12) {
            if downloading || log.finished {
                DownloadProgressView(progress: progress)

                if log.text.contains("@") || !log.text.isEmpty {
                    LogConsoleView(title: "Download Log", log: log)
                        .frame(maxHeight: 180)
                }
            }

            HStack {
                if let selected {
                    VStack(alignment: .leading, spacing: 2) {
                        Text(selected.displayName).fontWeight(.medium)
                        if let size = selected.size, size > 0 {
                            Text(humanBytes(size)).font(.caption).foregroundStyle(.secondary)
                        }
                    }
                } else {
                    Text("Select an item to download")
                        .foregroundStyle(.secondary)
                }
                Spacer()
                Button {
                    chooseDownloadDirectory()
                } label: {
                    Image(systemName: "folder")
                }
                .help("Choose download location")
                Button {
                    if let url = selected?.url { copyToClipboard(url) }
                } label: {
                    Image(systemName: "doc.on.doc")
                }
                .help("Copy link")
                .disabled(selected?.url == nil)
                Button {
                    if let selected { startDownload(selected) }
                } label: {
                    Label("Download", systemImage: "arrow.down.circle")
                }
                .buttonStyle(.borderedProminent)
                .disabled(selected == nil || downloading)
            }

            Text("Downloads: \(downloadDirectory.path)")
                .font(.caption2)
                .foregroundStyle(.tertiary)
                .frame(maxWidth: .infinity, alignment: .trailing)
        }
    }

    private func iconName(for item: DownloadItem) -> String {
        let major = PayloadIcon.kernelMajor(fromBuild: item.build)
        switch kind {
        case .kdk, .metallib:
            return PayloadIcon.packageIconName(kernelMajor: major)
        case .ipsw:
            return PayloadIcon.macosIconName(kernelMajor: major)
        }
    }

    private func load() async {
        loading = true
        error = nil
        defer { loading = false }
        switch kind {
        case .kdk: items = await state.bridge.listKDK()
        case .metallib: items = await state.bridge.listMetallib()
        case .ipsw: items = await state.bridge.listIPSW()
        }
        if items.isEmpty { error = "Could not fetch the catalog." }
    }

    private func startDownload(_ item: DownloadItem) {
        guard let url = item.url else { return }
        let path = downloadDirectory.appendingPathComponent(downloadFilename(from: url)).path

        downloading = true
        progress = nil
        log.reset()
        log.isRunning = true

        Task {
            let result = await state.bridge.download(url: url, path: path, size: item.size) { p in
                progress = p
            } onLine: { line in
                log.append(line)
            }

            // Verify IPSW SHA1 checksum after download (#4)
            if kind == .ipsw, result?.ok == true, let sha1 = item.sha1, !sha1.isEmpty {
                log.append("Verifying SHA1 checksum…")
                let valid = await state.bridge.verifySHA1(path: path, sha1: sha1) { p in
                    progress = p
                } onLine: { line in
                    log.append(line)
                }
                log.succeeded = valid
                log.append(valid ? "SHA1 checksum verified." : "SHA1 checksum mismatch!")
            }

            downloading = false
            log.isRunning = false
            log.finished = true
        }
    }
}

// MARK: - macOS Installer (download → extract → flash)

struct MacOSInstallerView: View {
    @EnvironmentObject private var state: AppState

    enum Phase { case catalog, downloading, validating, ready, flashing }

    @State private var phase: Phase = .catalog
    @State private var installers: [InstallerItem] = []
    @State private var selected: InstallerItem?
    @State private var loading = true
    @State private var error: String?
    @State private var progress: DownloadProgress?
    @StateObject private var log = OperationLog()
    @State private var downloadedPath: String?
    @State private var downloadedIntegrityURL: String?

    var body: some View {
        VStack(spacing: 16) {
            switch phase {
            case .catalog:
                catalog
            case .downloading:
                downloading
            case .validating:
                validating
            case .ready:
                ready
            case .flashing:
                FlashInstallerView(onBack: { phase = .ready })
            }
        }
        .padding(20)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .navigationTitle("Create macOS Installer")
        .task { if phase == .catalog && installers.isEmpty { await load() } }
    }

    private var catalog: some View {
        VStack(spacing: 12) {
            if loading {
                Spacer()
                ProgressView("Fetching installer catalog…")
                Spacer()
            } else if installers.isEmpty {
                Spacer()
                ContentUnavailableView("Catalog unavailable", systemImage: "wifi.exclamationmark", description: Text(error ?? "Could not fetch the installer catalog."))
                Spacer()
            } else {
                List(installers, selection: $selected) { item in
                    HStack(spacing: 12) {
                        PayloadIconView(name: PayloadIcon.macosIconName(kernelMajor: item.xnuMajor ?? -1))
                            .frame(width: 30, height: 30)
                        VStack(alignment: .leading, spacing: 3) {
                            Text(item.title ?? item.version ?? "macOS")
                                .fontWeight(.medium)
                            HStack {
                                Text("\(item.version ?? "") (\(item.build ?? ""))")
                                if let size = item.size, size > 0 { Text("· \(humanBytes(size))") }
                            }
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        }
                        Spacer()
                    }
                    .padding(.vertical, 2)
                    .tag(item)
                }
                .listStyle(.inset)

                compatibilityWarning

                HStack {
                    Text(selected?.title ?? "Select an installer")
                        .foregroundStyle(selected == nil ? .secondary : .primary)
                    Spacer()
                    Button {
                        if let url = selected?.url { copyToClipboard(url) }
                    } label: {
                        Image(systemName: "doc.on.doc")
                    }
                    .help("Copy link")
                    .disabled(selected?.url == nil)
                    Button {
                        if let selected { startDownload(selected) }
                    } label: {
                        Label("Download", systemImage: "arrow.down.circle")
                    }
                    .buttonStyle(.borderedProminent)
                    .disabled(selected == nil)
                }
            }
        }
    }

    @ViewBuilder
    private var compatibilityWarning: some View {
        if let problems = selected?.problems, !problems.isEmpty {
            VStack(alignment: .leading, spacing: 4) {
                Label("Your model may not be fully supported by this installer.", systemImage: "exclamationmark.triangle.fill")
                    .foregroundStyle(.orange)
                    .font(.callout.weight(.medium))
                ForEach(problems, id: \.self) { problem in
                    Text("• \(problem)")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(12)
            .background(.orange.opacity(0.1), in: RoundedRectangle(cornerRadius: 8))
        }
    }

    private var downloading: some View {
        VStack(spacing: 16) {
            DownloadProgressView(progress: progress)
            LogConsoleView(title: "Download Log", log: log)
                .frame(maxHeight: .infinity)
            HStack {
                if log.finished {
                    Text(log.succeeded ? "Download complete." : "Download failed.")
                        .foregroundStyle(log.succeeded ? .green : .red)
                }
                Spacer()
                if log.finished {
                    if log.succeeded {
                        Button("Continue") {
                            if downloadedIntegrityURL != nil {
                                startValidate()
                            } else {
                                phase = .ready
                            }
                        }
                        .buttonStyle(.borderedProminent)
                    } else {
                        Button("Back") { phase = .catalog }
                    }
                }
            }
        }
    }

    private var validating: some View {
        VStack(spacing: 16) {
            DownloadProgressView(progress: progress)
            LogConsoleView(title: "Validation Log", log: log)
                .frame(maxHeight: .infinity)
            HStack {
                if log.finished {
                    Text(log.succeeded ? "Installer validated." : "Validation failed.")
                        .foregroundStyle(log.succeeded ? .green : .red)
                }
                Spacer()
                if log.finished {
                    if log.succeeded {
                        Button("Continue") { phase = .ready }
                            .buttonStyle(.borderedProminent)
                    } else {
                        Button("Back") { phase = .catalog }
                    }
                }
            }
        }
    }

    private var ready: some View {
        VStack(spacing: 16) {
            Card(title: "Installer ready") {
                VStack(alignment: .leading, spacing: 8) {
                    Label("The InstallAssistant package is ready.", systemImage: "checkmark.circle.fill")
                        .foregroundStyle(.green)
                    Text("Extract it to /Applications, then flash it to a USB drive.")
                        .font(.callout)
                        .foregroundStyle(.secondary)
                }
            }

            HStack(spacing: 12) {
                Button {
                    extract()
                } label: {
                    Label("Extract to /Applications", systemImage: "square.and.arrow.down")
                }
                .buttonStyle(.borderedProminent)

                Button {
                    phase = .flashing
                } label: {
                    Label("Flash to disk", systemImage: "externaldrive")
                }

                Spacer()
            }

            if log.finished || log.isRunning {
                LogConsoleView(title: "Log", log: log)
                    .frame(maxHeight: .infinity)
            } else {
                Spacer()
            }
        }
    }

    private func load() async {
        loading = true
        defer { loading = false }
        installers = await state.bridge.listInstallers()
        if installers.isEmpty { error = "Could not fetch the installer catalog." }
    }

    private func startDownload(_ item: InstallerItem) {
        guard let url = item.url else { return }
        let path = AppConfig.repoRoot.appendingPathComponent("payloads/InstallAssistant.pkg").path
        downloadedPath = path
        downloadedIntegrityURL = item.integrityURL

        phase = .downloading
        progress = nil
        log.reset()
        log.isRunning = true

        Task {
            let result = await state.bridge.download(url: url, path: path, size: item.size) { p in
                progress = p
            } onLine: { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = result?.ok ?? false
        }
    }

    private func startValidate() {
        guard let integrityURL = downloadedIntegrityURL else { return }
        phase = .validating
        progress = nil
        log.reset()
        log.isRunning = true

        Task {
            let ok = await state.bridge.validateInstaller(integrityURL: integrityURL) { p in
                progress = p
            } onLine: { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = ok
        }
    }

    private func extract() {
        guard let path = downloadedPath else { return }
        log.reset()
        log.isRunning = true
        Task {
            let ok = await state.bridge.extractInstaller(pkgPath: path) { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = ok
        }
    }
}

// MARK: - Flash installer to disk

struct FlashInstallerView: View {
    @EnvironmentObject private var state: AppState
    let onBack: () -> Void

    enum Phase { case installers, disks, flashing }

    @State private var phase: Phase = .installers
    @State private var installers: [LocalInstaller] = []
    @State private var disks: [Disk] = []
    @State private var selectedInstaller: LocalInstaller?
    @State private var selectedDisk: Disk?
    @State private var loading = false
    @StateObject private var log = OperationLog()

    var body: some View {
        Group {
            switch phase {
            case .installers:
                installerList
            case .disks:
                diskList
            case .flashing:
                flashing
            }
        }
        .navigationTitle("Flash Installer")
        .task { if installers.isEmpty && phase == .installers { await loadInstallers() } }
    }

    private var installerList: some View {
        VStack(spacing: 16) {
            Card(title: "Select a local installer") {
                if loading {
                    HStack { ProgressView().controlSize(.small); Text("Scanning /Applications…").foregroundStyle(.secondary) }
                } else if installers.isEmpty {
                    Text("No installed macOS installers found. Extract one first.")
                        .foregroundStyle(.secondary)
                } else {
                    VStack(spacing: 2) {
                        ForEach(installers) { installer in
                            DeviceRow(title: installer.name, subtitle: installer.path, trailing: "") {
                                selectedInstaller = installer
                                phase = .disks
                                Task { await loadDisks() }
                            }
                        }
                    }
                }
            }
            HStack {
                Button("Back") { onBack() }
                Spacer()
            }
        }
    }

    private var diskList: some View {
        VStack(spacing: 16) {
            Card(title: "Select a destination disk", subtitle: "⚠️ The selected disk will be erased.") {
                if loading {
                    HStack { ProgressView().controlSize(.small); Text("Fetching disks…").foregroundStyle(.secondary) }
                } else if disks.isEmpty {
                    Text("No applicable disks found.").foregroundStyle(.secondary)
                } else {
                    VStack(spacing: 2) {
                        ForEach(disks) { disk in
                            DeviceRow(title: disk.disk, subtitle: disk.name, trailing: disk.size) {
                                selectedDisk = disk
                                startFlash()
                            }
                        }
                    }
                }
            }
            HStack {
                Button("Back") { phase = .installers }
                Spacer()
            }
        }
    }

    private var flashing: some View {
        VStack(spacing: 12) {
            Text("Creating macOS installer…")
                .font(.title2.bold())
            LogConsoleView(title: "Flash Log", log: log)
                .frame(maxHeight: .infinity)
            HStack {
                if log.finished {
                    Text(log.succeeded ? "Done." : "Failed.")
                        .foregroundStyle(log.succeeded ? .green : .red)
                }
                Spacer()
                Button("Back") { onBack() }
                    .disabled(log.isRunning)
            }
        }
    }

    private func loadInstallers() async {
        loading = true
        defer { loading = false }
        installers = await state.bridge.listLocalInstallers()
    }

    private func loadDisks() async {
        loading = true
        defer { loading = false }
        disks = await state.bridge.listDisks()
    }

    private func startFlash() {
        guard let installer = selectedInstaller, let disk = selectedDisk else { return }
        phase = .flashing
        log.reset()
        log.isRunning = true
        Task {
            let ok = await state.bridge.flashInstaller(path: installer.path, disk: disk.disk) { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = ok
        }
    }
}
