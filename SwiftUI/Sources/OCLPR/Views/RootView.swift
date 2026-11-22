import SwiftUI

struct RootView: View {
    @EnvironmentObject private var state: AppState
    @State private var selection: SidebarItem? = .build
    @State private var columnVisibility: NavigationSplitViewVisibility = .all

    var body: some View {
        NavigationSplitView(columnVisibility: $columnVisibility) {
            SidebarView(selection: $selection)
        } detail: {
            detail(for: selection)
        }
        .navigationSplitViewStyle(.balanced)
        .task {
            if state.hostInfo == nil {
                await state.refreshHostInfo()
            }
        }
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button {
                    Task { await state.refreshHostInfo() }
                } label: {
                    Label("Refresh", systemImage: "arrow.clockwise")
                }
                .disabled(state.isLoadingInfo)
                .help("Refresh host information")
            }
        }
    }

    @ViewBuilder
    private func detail(for item: SidebarItem?) -> some View {
        switch item {
        case .build:
            BuildView()
        case .installer:
            MacOSInstallerView()
        case .kdk:
            DownloadCatalogView(kind: .kdk)
        case .metallib:
            DownloadCatalogView(kind: .metallib)
        case .ipsw:
            DownloadCatalogView(kind: .ipsw)
        case .rootPatch:
            RootPatchView()
        case .settings:
            SettingsView()
        case .help:
            HelpView()
        case nil:
            ContentUnavailableView("Select an action", systemImage: "sidebar.left")
        }
    }
}
