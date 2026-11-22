import Foundation

enum AppConfig {
    /// Root of the OCLP-R checkout (contains OCLP-R-GUI.command and oclp_r/).
    static var repoRoot: URL {
        // 1. Explicit override
        if let override = ProcessInfo.processInfo.environment["OCLPR_REPO"], !override.isEmpty {
            return URL(fileURLWithPath: override)
        }
        // 2. Baked into the app bundle by make-app.sh
        if let baked = Bundle.main.infoDictionary?["OCLPRRepoRoot"] as? String, !baked.isEmpty {
            return URL(fileURLWithPath: baked)
        }
        // 3. Search upward from the working directory
        if let found = searchUpward(from: URL(fileURLWithPath: FileManager.default.currentDirectoryPath)) {
            return found
        }
        // 4. Search upward from the executable
        if let exe = Bundle.main.executableURL,
           let found = searchUpward(from: exe.deletingLastPathComponent()) {
            return found
        }
        return URL(fileURLWithPath: FileManager.default.currentDirectoryPath)
    }

    static var launcherScript: URL {
        repoRoot.appendingPathComponent("OCLP-R-GUI.command")
    }

    private static func searchUpward(from start: URL) -> URL? {
        var dir = start
        for _ in 0..<10 {
            if FileManager.default.fileExists(atPath: dir.appendingPathComponent("OCLP-R-GUI.command").path) {
                return dir
            }
            dir = dir.deletingLastPathComponent()
        }
        return nil
    }
}
