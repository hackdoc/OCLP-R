import Foundation

struct RunResult {
    let exitCode: Int32
    let lines: [String]
    let resultData: Data?

    var succeeded: Bool { exitCode == 0 }
}

enum PythonBridgeError: LocalizedError {
    case noPythonFound

    var errorDescription: String? {
        switch self {
        case .noPythonFound:
            return "No compatible Python 3 interpreter was found."
        }
    }
}

/// Thin shell that drives the existing Python patcher as a subprocess.
/// Read-only queries emit a JSON envelope on stdout; heavy operations stream
/// their log lines and are judged by their exit code.
struct PythonBridge {

    private static let resultBegin = "@@OCLPR_RESULT_BEGIN@@"
    private static let resultEnd = "@@OCLPR_RESULT_END@@"

    let pythonURL: URL
    let workingDirectory: URL
    let scriptURL: URL

    init(pythonURL: URL? = nil,
         workingDirectory: URL = AppConfig.repoRoot,
         scriptURL: URL = AppConfig.launcherScript) {
        self.pythonURL = pythonURL ?? PythonBridge.findPython()
        self.workingDirectory = workingDirectory
        self.scriptURL = scriptURL
    }

    // MARK: - Locating the interpreter

    static func findPython() -> URL {
        let candidates = ["python3.14", "python3.13", "python3.12", "python3.11", "python3.10", "python3"]
        for name in candidates {
            if let url = which(name) { return url }
        }
        // Framework fallbacks (python.org installs)
        for version in [(3, 14), (3, 13), (3, 12), (3, 11), (3, 10)] {
            let path = "/Library/Frameworks/Python.framework/Versions/\(version.0).\(version.1)/bin/python\(version.0).\(version.1)"
            let url = URL(fileURLWithPath: path)
            if FileManager.default.isExecutableFile(atPath: path) { return url }
        }
        return URL(fileURLWithPath: "/usr/bin/python3")
    }

    private static func which(_ name: String) -> URL? {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/which")
        process.arguments = [name]
        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = Pipe()
        do {
            try process.run()
            process.waitUntilExit()
        } catch {
            return nil
        }
        guard process.terminationStatus == 0 else { return nil }
        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        let path = String(data: data, encoding: .utf8)?
            .trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        return path.isEmpty ? nil : URL(fileURLWithPath: path)
    }

    // MARK: - Running

    /// Launch the patcher and stream its output line by line.
    /// - Parameter onLine: invoked on the main queue for each log line.
    func run(_ args: [String], onLine: ((String) -> Void)? = nil) async -> RunResult {
        let process = Process()
        process.executableURL = pythonURL
        process.arguments = [scriptURL.path] + args
        process.currentDirectoryURL = workingDirectory
        process.standardInput = FileHandle.nullDevice

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        do {
            try process.run()
        } catch {
            return RunResult(exitCode: -1, lines: [], resultData: nil)
        }

        var lines: [String] = []
        var envelope = Data()
        var inEnvelope = false

        do {
            for try await line in pipe.fileHandleForReading.bytes.lines {
                lines.append(line)
                if let onLine {
                    DispatchQueue.main.async { onLine(line) }
                }
                if line == Self.resultBegin { inEnvelope = true; continue }
                if line == Self.resultEnd { inEnvelope = false; continue }
                if inEnvelope { envelope.append(Data((line + "\n").utf8)) }
            }
        } catch {
            // Ignore read failures; the exit code still tells us the outcome.
        }

        process.waitUntilExit()

        return RunResult(
            exitCode: process.terminationStatus,
            lines: lines,
            resultData: envelope.isEmpty ? nil : envelope
        )
    }

    // MARK: - High-level helpers

    func hostInfo() async -> HostInfo? {
        let result = await run(["--print_info"])
        guard let data = result.resultData else {
            NSLog("OCLPR: --print_info produced no result envelope (exit \(result.exitCode))")
            return nil
        }
        do {
            return try JSONDecoder.snakeCase.decode(HostInfo.self, from: data)
        } catch {
            NSLog("OCLPR: failed to decode host info: \(error)")
            return nil
        }
    }

    func listDisks() async -> [Disk] {
        let result = await run(["--list_disks"])
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DisksResponse.self, from: data),
              response.ok else { return [] }
        return Array(response.disks.values).sorted { $0.disk < $1.disk }
    }

    func listPartitions(disk: String) async -> [Partition] {
        let result = await run(["--list_partitions", disk])
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(PartitionsResponse.self, from: data),
              response.ok,
              let partitions = response.partitions else { return [] }
        return Array(partitions.values).sorted { $0.partition < $1.partition }
    }

    func installOC(partition: String, onLine: ((String) -> Void)? = nil) async -> InstallResponse? {
        let result = await run(["--install_oc", partition], onLine: onLine)
        guard let data = result.resultData else { return nil }
        return try? JSONDecoder.snakeCase.decode(InstallResponse.self, from: data)
    }

    func detectPatches() async -> PatchesInfo? {
        let result = await run(["--print_patches"])
        guard let data = result.resultData else { return nil }
        return try? JSONDecoder.snakeCase.decode(PatchesInfo.self, from: data)
    }

    // MARK: - Download catalogs

    func listInstallers() async -> [InstallerItem] {
        let result = await run(["--list_installers"])
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(InstallersResponse.self, from: data),
              response.ok else { return [] }
        return response.installers ?? []
    }

    func listKDK() async -> [DownloadItem] {
        await downloadList("--list_kdk")
    }

    func listMetallib() async -> [DownloadItem] {
        await downloadList("--list_metallib")
    }

    func listIPSW() async -> [DownloadItem] {
        await downloadList("--list_ipsw")
    }

    private func downloadList(_ arg: String) async -> [DownloadItem] {
        let result = await run([arg])
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadListResponse.self, from: data),
              response.ok else { return [] }
        return response.items ?? []
    }

    func listLocalInstallers() async -> [LocalInstaller] {
        let result = await run(["--list_local_installers"])
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(LocalInstallersResponse.self, from: data),
              response.ok else { return [] }
        return response.installers ?? []
    }

    // MARK: - Download / extract / flash

    /// Download a file, streaming progress (via `@@P@@` lines) and log lines.
    func download(url: String, path: String, size: Int? = nil,
                  onProgress: @escaping (DownloadProgress) -> Void,
                  onLine: ((String) -> Void)? = nil) async -> DownloadResult? {
        var payload: [String: Any] = ["url": url, "path": path]
        if let size { payload["size"] = size }

        guard let json = try? JSONSerialization.data(withJSONObject: payload),
              let jsonString = String(data: json, encoding: .utf8) else { return nil }

        let result = await run(["--download", jsonString]) { line in
            if line.hasPrefix("@@P@@ ") {
                let body = String(line.dropFirst(6))
                if let data = body.data(using: .utf8),
                   let progress = try? JSONDecoder().decode(DownloadProgress.self, from: data) {
                    onProgress(progress)
                }
            }
            onLine?(line)
        }
        guard let data = result.resultData else { return nil }
        return try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data)
    }

    func extractInstaller(pkgPath: String, onLine: ((String) -> Void)? = nil) async -> Bool {
        let result = await run(["--extract_installer", pkgPath], onLine: onLine)
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data) else { return false }
        return response.ok
    }

    func validateInstaller(integrityURL: String,
                           onProgress: @escaping (DownloadProgress) -> Void,
                           onLine: ((String) -> Void)? = nil) async -> Bool {
        let result = await run(["--validate_installer", integrityURL]) { line in
            if line.hasPrefix("@@P@@ ") {
                if let data = String(line.dropFirst(6)).data(using: .utf8),
                   let progress = try? JSONDecoder().decode(DownloadProgress.self, from: data) {
                    onProgress(progress)
                }
            }
            onLine?(line)
        }
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data) else { return false }
        return response.ok
    }

    func verifySHA1(path: String, sha1: String,
                    onProgress: @escaping (DownloadProgress) -> Void,
                    onLine: ((String) -> Void)? = nil) async -> Bool {
        let payload = ["path": path, "sha1": sha1]
        guard let json = try? JSONSerialization.data(withJSONObject: payload),
              let jsonString = String(data: json, encoding: .utf8) else { return false }
        let result = await run(["--verify_sha1", jsonString]) { line in
            if line.hasPrefix("@@P@@ ") {
                if let data = String(line.dropFirst(6)).data(using: .utf8),
                   let progress = try? JSONDecoder().decode(DownloadProgress.self, from: data) {
                    onProgress(progress)
                }
            }
            onLine?(line)
        }
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data) else { return false }
        return response.ok
    }

    // MARK: - Update / OS cache

    func checkUpdates() async -> UpdateInfo? {
        let result = await run(["--check_updates"])
        guard let data = result.resultData else { return nil }
        return try? JSONDecoder.snakeCase.decode(UpdateInfo.self, from: data)
    }

    func installUpdate(url: String, version: String, onLine: ((String) -> Void)? = nil) async -> Bool {
        let payload = ["url": url, "version": version]
        guard let json = try? JSONSerialization.data(withJSONObject: payload),
              let jsonString = String(data: json, encoding: .utf8) else { return false }
        let result = await run(["--install_update", jsonString], onLine: onLine)
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data) else { return false }
        return response.ok
    }

    func cacheOSHeadless(onLine: ((String) -> Void)? = nil) async -> Bool {
        let result = await run(["--cache_os_headless"], onLine: onLine)
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(CacheResult.self, from: data) else { return false }
        return response.ok
    }

    func flashInstaller(path: String, disk: String, onLine: ((String) -> Void)? = nil) async -> Bool {
        let payload = ["installer_path": path, "disk": disk]
        guard let json = try? JSONSerialization.data(withJSONObject: payload),
              let jsonString = String(data: json, encoding: .utf8) else { return false }
        let result = await run(["--flash_installer", jsonString], onLine: onLine)
        guard let data = result.resultData,
              let response = try? JSONDecoder.snakeCase.decode(DownloadResult.self, from: data) else { return false }
        return response.ok
    }
}
