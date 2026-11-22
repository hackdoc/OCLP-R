import SwiftUI

struct HelpView: View {
    @EnvironmentObject private var state: AppState

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                Card {
                    VStack(spacing: 10) {
                        Image(systemName: "externaldrive.badge.checkmark")
                            .font(.system(size: 44))
                            .foregroundStyle(.blue)
                        Text("OCLP-R")
                            .font(.title.bold())
                        if let version = state.hostInfo?.patcherVersion {
                            Text("Version \(version)")
                                .foregroundStyle(.secondary)
                        }
                        if let copyright = state.hostInfo?.copyright, !copyright.isEmpty {
                            Text(copyright)
                                .font(.caption)
                                .foregroundStyle(.tertiary)
                        }
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 8)
                }

                Card(title: "Resources") {
                    VStack(alignment: .leading, spacing: 10) {
                        if let guide = state.hostInfo?.guideLink, !guide.isEmpty {
                            Link(destination: URL(string: guide)!) {
                                Label("OpenCore Legacy Patcher Guide", systemImage: "book")
                            }
                        }
                        if let discord = state.hostInfo?.discordLink, !discord.isEmpty {
                            Link(destination: URL(string: discord)!) {
                                Label("Community Discord Server", systemImage: "bubble.left.and.bubble.right")
                            }
                        }
                        if let repo = state.hostInfo?.repoLink, !repo.isEmpty {
                            Link(destination: URL(string: repo)!) {
                                Label("OCLP-R on GitHub", systemImage: "link")
                            }
                        }
                    }
                }

                Card(title: "Reveal log file") {
                    Button("Reveal Log File") {
                        if let log = logFileURL {
                            NSWorkspace.shared.activateFileViewerSelecting([log])
                        }
                    }
                    .buttonStyle(.bordered)
                }
            }
            .padding(20)
        }
        .navigationTitle("Support")
    }

    private var logFileURL: URL? {
        let dir = FileManager.default.homeDirectoryForCurrentUser
            .appendingPathComponent("Library/Logs/Hackdoc")
        let files = (try? FileManager.default.contentsOfDirectory(at: dir, includingPropertiesForKeys: nil))?
            .filter { $0.pathExtension == "log" }
            .sorted { $0.lastPathComponent > $1.lastPathComponent }
        return files?.first
    }
}
