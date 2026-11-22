import SwiftUI

@main
struct OCLPRApp: App {
    @StateObject private var state = AppState()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(state)
                .frame(minWidth: 780, minHeight: 540)
        }
        .windowResizability(.contentSize)
    }
}
