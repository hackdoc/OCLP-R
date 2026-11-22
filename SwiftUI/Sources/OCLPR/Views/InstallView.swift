import SwiftUI

struct InstallView: View {
    @EnvironmentObject private var state: AppState
    let onBack: () -> Void

    enum Phase { case disks, partitions, installing }

    @State private var phase: Phase = .disks
    @State private var disks: [Disk] = []
    @State private var partitions: [Partition] = []
    @State private var selectedDisk: Disk?
    @State private var loading = false
    @StateObject private var log = OperationLog()

    var body: some View {
        VStack(spacing: 16) {
            switch phase {
            case .disks:
                diskList
            case .partitions:
                partitionList
            case .installing:
                installView
            }
        }
        .padding(20)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .navigationTitle("Install OpenCore")
        .task {
            if disks.isEmpty && phase == .disks { await loadDisks() }
        }
    }

    // MARK: - Disk selection

    private var diskList: some View {
        VStack(spacing: 16) {
            Card(title: "Select a disk",
                 subtitle: "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT.") {
                if loading {
                    HStack(spacing: 8) {
                        ProgressView().controlSize(.small)
                        Text("Fetching disks…").foregroundStyle(.secondary)
                    }
                } else if disks.isEmpty {
                    Text("No applicable disks found.")
                        .foregroundStyle(.secondary)
                } else {
                    VStack(spacing: 2) {
                        ForEach(disks) { disk in
                            DeviceRow(title: disk.disk, subtitle: disk.name, trailing: disk.size) {
                                Task { await loadPartitions(for: disk) }
                            }
                        }
                    }
                }
            }

            HStack {
                Button("Search again") { Task { await loadDisks() } }
                Spacer()
                Button("Back") { onBack() }
            }
        }
    }

    // MARK: - Partition selection

    private var partitionList: some View {
        VStack(spacing: 16) {
            Card(title: "Volumes on \(selectedDisk?.disk ?? "")") {
                if loading {
                    HStack(spacing: 8) {
                        ProgressView().controlSize(.small)
                        Text("Fetching partitions…").foregroundStyle(.secondary)
                    }
                } else if partitions.isEmpty {
                    Text("No applicable partitions found.")
                        .foregroundStyle(.secondary)
                } else {
                    VStack(spacing: 2) {
                        ForEach(partitions) { partition in
                            DeviceRow(title: partition.partition,
                                      subtitle: partition.name,
                                      trailing: partition.size) {
                                startInstall(partition)
                            }
                        }
                    }
                }
            }

            HStack {
                Button("Back") { phase = .disks }
                Spacer()
            }
        }
    }

    // MARK: - Installing

    private var installView: some View {
        VStack(spacing: 12) {
            LogConsoleView(title: "Install Log", log: log)
                .frame(maxHeight: .infinity)

            HStack {
                if log.finished {
                    Text(log.succeeded ? "Installation complete." : "Installation failed.")
                        .foregroundStyle(log.succeeded ? .green : .red)
                }
                Spacer()
                Button("Back") { onBack() }
                    .disabled(log.isRunning)
            }
        }
    }

    // MARK: - Actions

    private func loadDisks() async {
        loading = true
        defer { loading = false }
        disks = await state.bridge.listDisks()
    }

    private func loadPartitions(for disk: Disk) async {
        selectedDisk = disk
        phase = .partitions
        loading = true
        defer { loading = false }
        partitions = await state.bridge.listPartitions(disk: disk.disk)
    }

    private func startInstall(_ partition: Partition) {
        phase = .installing
        log.reset()
        log.isRunning = true
        Task {
            let response = await state.bridge.installOC(partition: partition.partition) { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = response?.ok ?? false
        }
    }
}

/// Borderless row used inside a Card, with hover feedback.
struct DeviceRow: View {
    let title: String
    let subtitle: String
    let trailing: String
    let action: () -> Void

    @State private var hovering = false

    var body: some View {
        Button(action: action) {
            HStack(spacing: 10) {
                Image(systemName: "externaldrive")
                    .foregroundStyle(.secondary)
                VStack(alignment: .leading, spacing: 2) {
                    Text(title).fontWeight(.medium)
                    if !subtitle.isEmpty {
                        Text(subtitle).font(.caption).foregroundStyle(.secondary)
                    }
                }
                Spacer()
                Text(trailing).font(.callout).foregroundStyle(.secondary)
                Image(systemName: "chevron.right")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 8)
            .background(
                RoundedRectangle(cornerRadius: 8, style: .continuous)
                    .fill(.quaternary)
                    .opacity(hovering ? 1 : 0)
            )
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .onHover { hovering = $0 }
    }
}
