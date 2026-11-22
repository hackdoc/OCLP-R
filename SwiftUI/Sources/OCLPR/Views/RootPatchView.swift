import SwiftUI

struct RootPatchView: View {
    @EnvironmentObject private var state: AppState
    @StateObject private var log = OperationLog()
    @State private var patchesInfo: PatchesInfo?
    @State private var detecting = true
    @State private var detectError: String?

    var body: some View {
        VStack(spacing: 16) {
            if detecting {
                Spacer()
                VStack(spacing: 12) {
                    ProgressView()
                        .controlSize(.large)
                    Text("Detecting required patches…")
                        .foregroundStyle(.secondary)
                }
                Spacer()
            } else if log.isRunning || log.finished {
                LogConsoleView(title: "Patch Log", log: log)
                    .frame(maxHeight: .infinity)
                statusBar
            } else if let error = detectError {
                Spacer()
                ContentUnavailableView("Detection failed", systemImage: "exclamationmark.triangle", description: Text(error))
                Spacer()
            } else {
                patchSummary
            }
        }
        .padding(20)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .navigationTitle("Post-Install Root Patch")
        .task { await loadPatches() }
    }

    // MARK: - Detection result

    private var patchSummary: some View {
        VStack(spacing: 16) {
            if let info = patchesInfo {
                ScrollView {
                    VStack(spacing: 12) {
                        if info.patches.isEmpty {
                            Card {
                                VStack(spacing: 8) {
                                    Image(systemName: "checkmark.circle")
                                        .font(.system(size: 34))
                                        .foregroundStyle(.green)
                                    Text("No patches required for this model")
                                        .font(.headline)
                                    Text("Your hardware is fully supported by this version of macOS.")
                                        .font(.callout)
                                        .foregroundStyle(.secondary)
                                }
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 12)
                            }
                        } else {
                            Card(title: "Root Patching will patch the following") {
                                ForEach(info.patches, id: \.self) { patch in
                                    Label(patch, systemImage: "checkmark.circle.fill")
                                        .foregroundStyle(.green)
                                        .frame(maxWidth: .infinity, alignment: .leading)
                                }
                            }
                        }

                        if let blockers = info.blockers, !blockers.isEmpty {
                            Card(title: "Cannot patch due to the following reasons") {
                                ForEach(blockers, id: \.self) { blocker in
                                    Label(blocker, systemImage: "exclamationmark.triangle.fill")
                                        .foregroundStyle(.orange)
                                        .frame(maxWidth: .infinity, alignment: .leading)
                                }
                            }
                        }

                        if let last = info.lastPatched {
                            Card {
                                LabeledContent("Root Volume last patched") {
                                    Text("\(last.version), \(last.date)")
                                        .foregroundStyle(.secondary)
                                }
                            }
                        }
                    }
                }

                HStack(spacing: 12) {
                    Spacer()

                    Button {
                        run(["--patch_sys_vol"])
                    } label: {
                        Label("Start Root Patching", systemImage: "checkmark.seal.fill")
                            .frame(minWidth: 180)
                    }
                    .buttonStyle(.borderedProminent)
                    .controlSize(.large)
                    .disabled(!info.canPatch || info.patches.isEmpty)

                    Button {
                        run(["--unpatch_sys_vol"])
                    } label: {
                        Label("Revert Root Patches", systemImage: "arrow.uturn.backward")
                            .frame(minWidth: 180)
                    }
                    .controlSize(.large)
                    .disabled(!info.canUnpatch)

                    Spacer()
                }
            }
        }
    }

    private var statusBar: some View {
        HStack {
            if log.finished {
                Text(log.succeeded ? "Completed." : "Finished with errors.")
                    .foregroundStyle(log.succeeded ? .green : .red)
            } else {
                ProgressView().controlSize(.small)
                Text("Working…").foregroundStyle(.secondary)
            }
            Spacer()
        }
    }

    // MARK: - Actions

    private func loadPatches() async {
        detecting = true
        detectError = nil
        defer { detecting = false }

        guard let info = await state.bridge.detectPatches() else {
            detectError = "Could not read patch information from the patcher."
            return
        }
        if !info.ok {
            detectError = info.error ?? "Patch detection failed."
            return
        }
        patchesInfo = info
    }

    private func run(_ args: [String]) {
        log.reset()
        log.isRunning = true
        Task {
            let result = await state.bridge.run(args) { line in
                log.append(line)
            }
            log.isRunning = false
            log.finished = true
            log.succeeded = result.succeeded
        }
    }
}
