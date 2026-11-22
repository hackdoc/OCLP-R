import SwiftUI

struct BuildView: View {
    @EnvironmentObject private var state: AppState
    @StateObject private var log = OperationLog()
    @State private var showInstall = false
    @State private var isBuilding = false

    var body: some View {
        Group {
            if showInstall {
                InstallView(onBack: { showInstall = false })
            } else {
                buildPane
            }
        }
        .navigationTitle("Build and Install OpenCore")
    }

    // MARK: - Build pane

    private var buildPane: some View {
        VStack(spacing: 20) {
            VStack(spacing: 6) {
                Text("Build and Install OpenCore")
                    .font(.title2.bold())
                Label(state.effectiveModel, systemImage: "macbook.and.iphone")
                    .foregroundStyle(.secondary)
            }
            .padding(.top, 8)

            if isBuilding || log.finished {
                LogConsoleView(title: "Build Log", log: log)
                    .frame(maxHeight: .infinity)
                actionBar
            } else {
                optionsSummary
                Spacer()
                buildButton
                Spacer()
            }
        }
        .padding(24)
    }

    private var buildButton: some View {
        VStack(spacing: 12) {
            Button {
                startBuild()
            } label: {
                Label("Build OpenCore", systemImage: "hammer")
                    .frame(minWidth: 220)
            }
            .buttonStyle(.borderedProminent)
            .controlSize(.large)
            .disabled(!state.canBuild)

            if !state.canBuild {
                Label("This model is not supported for building OpenCore. Choose a supported target model in Settings.",
                      systemImage: "exclamationmark.triangle")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .frame(maxWidth: 420)
            }
        }
    }

    private var optionsSummary: some View {
        Card(title: "Build options") {
            if buildOptions.isEmpty {
                Text("Build with default settings")
                    .font(.callout)
                    .foregroundStyle(.secondary)
            } else {
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 150), spacing: 8, alignment: .leading)],
                          alignment: .leading, spacing: 8) {
                    ForEach(buildOptions, id: \.self) { option in
                        Label(option, systemImage: "checkmark.circle.fill")
                            .font(.caption)
                            .padding(.horizontal, 10)
                            .padding(.vertical, 5)
                            .background(.quaternary, in: Capsule())
                    }
                }
            }
        }
        .frame(maxWidth: 560)
    }

    private var actionBar: some View {
        HStack {
            if isBuilding {
                ProgressView().controlSize(.small)
                Text("Building…").foregroundStyle(.secondary)
            } else if log.finished {
                Text(log.succeeded ? "Build completed." : "Build failed.")
                    .foregroundStyle(log.succeeded ? .green : .red)
                    .fontWeight(.medium)
            }
            Spacer()

            if log.finished {
                if !log.succeeded {
                    Button("Rebuild") { startBuild() }
                }
                if log.succeeded {
                    Button {
                        showInstall = true
                    } label: {
                        Label("Install to disk", systemImage: "externaldrive")
                    }
                    .buttonStyle(.borderedProminent)
                }
            }
        }
    }

    // MARK: - Actions

    private func startBuild() {
        log.reset()
        log.isRunning = true
        isBuilding = true

        Task {
            let result = await state.bridge.run(state.buildArguments()) { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = result.succeeded
            isBuilding = false
            if !result.succeeded {
                log.append("")
                log.append("Build failed with exit code \(result.exitCode).")
            }
        }
    }

    private var buildOptions: [String] {
        var options: [String] = []
        if state.verbose { options.append("Verbose") }
        if state.debugOC { options.append("OpenCore DEBUG") }
        if state.debugKext { options.append("Kext DEBUG") }
        if state.hidePicker { options.append("Hide picker") }
        if state.disableSIP { options.append("Disable SIP") }
        if state.secureBootModel { options.append("Secure Boot Model") }
        if state.vault { options.append("Vault") }
        if state.firewire { options.append("FireWire") }
        if state.xhciBoot { options.append("XHCI boot") }
        if state.nvme { options.append("NVMe boot") }
        if state.wlan { options.append("Wake on WLAN") }
        if state.disableTB { options.append("Disable Thunderbolt") }
        if state.forceSurplus { options.append("Force SurPlus") }
        if state.supportAll { options.append("Native models") }
        if state.smbiosSpoof != .none { options.append("SMBIOS: \(state.smbiosSpoof.rawValue)") }
        return options
    }
}
