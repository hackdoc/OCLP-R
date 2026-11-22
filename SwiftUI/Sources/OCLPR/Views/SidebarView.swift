import SwiftUI

enum SidebarItem: String, CaseIterable, Identifiable, Hashable {
    case build = "Build and Install OpenCore"
    case installer = "Create macOS Installer"
    case kdk = "KDK Download"
    case metallib = "Metallib Download"
    case ipsw = "IPSW Download"
    case rootPatch = "Post-Install Root Patch"
    case settings = "Settings"
    case help = "Support"

    var id: String { rawValue }

    var icon: String {
        switch self {
        case .build: return "externaldrive.badge.plus"
        case .installer: return "arrow.down.circle"
        case .kdk: return "ladybug"
        case .metallib: return "cube"
        case .ipsw: return "shippingbox"
        case .rootPatch: return "wrench.and.screwdriver"
        case .settings: return "gearshape"
        case .help: return "questionmark.circle"
        }
    }

    /// Payload `.icns` to use instead of the SF Symbol, where available.
    var icnsName: String? {
        switch self {
        case .installer: return "OC-Installer.icns"
        case .kdk: return "Package.icns"
        case .metallib: return "Package.icns"
        case .ipsw: return "Tahoe.icns"
        default: return nil
        }
    }
}

struct SidebarView: View {
    @EnvironmentObject private var state: AppState
    @Binding var selection: SidebarItem?

    var body: some View {
        List(selection: $selection) {
            Section {
                row(.build)
                row(.rootPatch)
            }
            Section("Downloads") {
                row(.installer)
                row(.kdk)
                row(.metallib)
                row(.ipsw)
            }
            Section {
                row(.settings)
                row(.help)
            }
        }
        .listStyle(.sidebar)
        .navigationTitle("OCLP-R")
        .safeAreaInset(edge: .bottom) { footer }
    }

    private func row(_ item: SidebarItem) -> some View {
        HStack(spacing: 6) {
            if let icns = item.icnsName {
                PayloadIconView(name: icns)
                    .frame(width: 18, height: 18)
            } else {
                Image(systemName: item.icon)
                    .frame(width: 18, height: 18)
            }
            Text(item.rawValue)
        }
        .tag(item)
        .disabled(item == .build && !state.canBuild)
    }

    private var footer: some View {
        VStack(spacing: 6) {
            Divider()
            if let info = state.hostInfo {
                VStack(spacing: 2) {
                    Text("Model: \(state.effectiveModel)")
                        .font(.caption.weight(.medium))
                    Text("macOS \(info.detectedOsVersion)")
                        .font(.caption2)
                        .foregroundStyle(.secondary)
                }
            } else if state.isLoadingInfo {
                ProgressView().controlSize(.small)
            }
        }
        .padding(.horizontal, 10)
        .padding(.bottom, 8)
    }
}
