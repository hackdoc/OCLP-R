import SwiftUI
import Combine

/// Small view model that accumulates streamed log output on the main thread.
@MainActor
final class OperationLog: ObservableObject {
    @Published var text = ""
    @Published var isRunning = false
    @Published var finished = false
    @Published var succeeded = false

    var lineCount: Int {
        text.isEmpty ? 0 : text.split(separator: "\n", omittingEmptySubsequences: false).count
    }

    func reset() {
        text = ""
        isRunning = false
        finished = false
        succeeded = false
    }

    func append(_ line: String) {
        text += line + "\n"
    }
}

/// Card-style console: rounded, borderless, no divider lines.
struct LogConsoleView: View {
    let title: String
    @ObservedObject var log: OperationLog

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack(spacing: 6) {
                Text(title)
                    .font(.headline)
                Text("· \(log.lineCount) lines")
                    .font(.headline)
                    .foregroundStyle(.secondary)
                Spacer()
                if log.isRunning {
                    ProgressView().controlSize(.small)
                }
            }

            if log.text.isEmpty {
                Text("Log not loaded yet")
                    .font(.callout)
                    .foregroundStyle(.secondary)
                    .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
            } else {
                ScrollViewReader { proxy in
                    ScrollView {
                        Text(log.text)
                            .font(.system(.caption, design: .monospaced))
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .textSelection(.enabled)
                            .padding(.bottom, 2)
                            .id("bottom")
                    }
                    .onChange(of: log.text) { _, _ in
                        proxy.scrollTo("bottom", anchor: .bottom)
                    }
                }
            }
        }
        .padding(16)
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
        .background(
            RoundedRectangle(cornerRadius: 12, style: .continuous)
                .fill(.regularMaterial)
        )
    }
}
