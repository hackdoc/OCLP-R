import Foundation

// MARK: - Models returned by the Python bridge

/// Heterogeneous JSON scalar used by the settings payload.
enum SettingValue: Codable, Hashable {
    case bool(Bool)
    case int(Int)
    case string(String)

    var boolValue: Bool? { if case .bool(let v) = self { return v }; return nil }
    var intValue: Int? { if case .int(let v) = self { return v }; return nil }
    var stringValue: String? { if case .string(let v) = self { return v }; return nil }

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let value = try? container.decode(Bool.self) {
            self = .bool(value)
        } else if let value = try? container.decode(Int.self) {
            self = .int(value)
        } else if let value = try? container.decode(String.self) {
            self = .string(value)
        } else {
            throw DecodingError.typeMismatch(
                SettingValue.self,
                .init(codingPath: decoder.codingPath, debugDescription: "Unsupported setting value")
            )
        }
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        switch self {
        case .bool(let value): try container.encode(value)
        case .int(let value): try container.encode(value)
        case .string(let value): try container.encode(value)
        }
    }
}

struct HostInfo: Codable {
    let patcherName: String
    let patcherVersion: String
    let detectedOs: Int
    let detectedOsVersion: String
    let detectedOsBuild: String
    let hostModel: String
    let hostIsHackintosh: Bool
    let hostCanBuild: Bool
    let bootedOcDisk: String?
    let voodooPatchAlready: Bool?
    let hdauPatchAlready: Bool?
    let supportedModels: [String]
    let settings: [String: SettingValue]?
    let globalSettings: [String: SettingValue]?
    let copyright: String?
    let guideLink: String?
    let discordLink: String?
    let repoLink: String?

    var displayModel: String { hostModel }
}

struct UpdateInfo: Codable {
    let ok: Bool
    let updateAvailable: Bool
    let version: String?
    let link: String?
    let githubLink: String?
    let error: String?
}

struct CacheResult: Codable {
    let ok: Bool
    let build: String?
    let version: String?
    let messages: [String]?
    let error: String?
}

struct Disk: Codable, Identifiable, Hashable {
    let disk: String
    let name: String
    let size: String
    var id: String { disk }
}

struct DisksResponse: Codable {
    let ok: Bool
    let disks: [String: Disk]
    let error: String?
}

struct Partition: Codable, Identifiable, Hashable {
    let partition: String
    let name: String
    let size: String
    var id: String { partition }
}

struct PartitionsResponse: Codable {
    let ok: Bool
    let disk: String?
    let partitions: [String: Partition]?
    let error: String?
}

struct InstallResponse: Codable {
    let ok: Bool
    let partition: String?
}

struct PatchesInfo: Codable {
    let ok: Bool
    let canPatch: Bool
    let canUnpatch: Bool
    let patches: [String]
    let blockers: [String]?
    let lastPatched: LastPatched?
    let error: String?
}

struct LastPatched: Codable {
    let version: String
    let date: String
}

enum SMBIOSLevel: String, CaseIterable, Identifiable, Hashable {
    case none = "None"
    case minimal = "Minimal"
    case moderate = "Moderate"
    case advanced = "Advanced"

    var id: String { rawValue }
    var label: String { rawValue }
}

extension JSONDecoder {
    static var snakeCase: JSONDecoder {
        let decoder = JSONDecoder()
        decoder.keyDecodingStrategy = .convertFromSnakeCase
        return decoder
    }
}

// MARK: - Downloads

struct InstallerItem: Codable, Identifiable, Hashable {
    let title: String?
    let version: String?
    let build: String?
    let catalog: String?
    let url: String?
    let size: Int?
    let integrityURL: String?
    let integritySize: Int?
    let xnuMajor: Int?
    let problems: [String]?

    var id: String { url ?? "\(build ?? "")-\(version ?? "")" }
}

struct InstallersResponse: Codable {
    let ok: Bool
    let installers: [InstallerItem]?
    let error: String?
}

struct DownloadItem: Codable, Identifiable, Hashable {
    let name: String?
    let version: String?
    let build: String?
    let date: String?
    let url: String?
    let size: Int?
    let releasedate: String?
    let signed: Bool?
    let sha1: String?

    var id: String { url ?? "\(name ?? "")-\(build ?? "")-\(version ?? "")" }
    var displayName: String {
        name ?? "\(version ?? "") (\(build ?? ""))"
    }
}

struct DownloadListResponse: Codable {
    let ok: Bool
    let items: [DownloadItem]?
    let error: String?
}

struct LocalInstaller: Codable, Identifiable, Hashable {
    let path: String
    let name: String
    var id: String { path }
}

struct LocalInstallersResponse: Codable {
    let ok: Bool
    let installers: [LocalInstaller]?
}

struct DownloadProgress: Codable {
    let percent: Double
    let speed: Double
    let downloaded: Int
    let total: Int
}

struct DownloadResult: Codable {
    let ok: Bool
    let path: String?
    let error: String?
}
