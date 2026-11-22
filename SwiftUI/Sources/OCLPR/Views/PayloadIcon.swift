import SwiftUI
import AppKit

/// Loads the `.icns` artwork bundled in the OCLP-R payloads and maps macOS
/// versions / build numbers to the right icon (same mapping the wx GUI uses).
enum PayloadIcon {

    static var directory: URL {
        AppConfig.repoRoot.appendingPathComponent("payloads/Icon/AppIcons")
    }

    static func nsImage(_ name: String) -> NSImage? {
        NSImage(contentsOf: directory.appendingPathComponent(name))
    }

    /// macOS version icon for a Darwin kernel major / build prefix.
    static func macosIconName(kernelMajor: Int) -> String {
        switch kernelMajor {
        case 20: return "BigSur.icns"
        case 21: return "Monterey.icns"
        case 22: return "Ventura.icns"
        case 23: return "Sonoma.icns"
        case 24: return "Sequoia.icns"
        case 25, 26, 27, 28: return "Tahoe.icns"
        default: return "Generic.icns"
        }
    }

    /// Package icon (KDK / Metallib) for a Darwin kernel major / build prefix.
    static func packageIconName(kernelMajor: Int) -> String {
        switch kernelMajor {
        case 20: return "Package11.icns"
        case 21: return "Package12.icns"
        case 22: return "Package13.icns"
        case 23: return "Package14.icns"
        case 24: return "Package15.icns"
        case 25, 26, 27, 28: return "Package26.icns"
        default: return "Package.icns"
        }
    }

    /// First two digits of a build string ("25G422" -> 25), or nil.
    static func kernelMajor(fromBuild build: String?) -> Int {
        guard let build, build.count >= 2, let value = Int(build.prefix(2)) else { return -1 }
        return value
    }
}

/// Renders a payload `.icns` as a scalable image, with an SF Symbol fallback.
struct PayloadIconView: View {
    let name: String
    var fallback: String = "app.dashed"

    var body: some View {
        if let ns = PayloadIcon.nsImage(name) {
            Image(nsImage: ns)
                .resizable()
                .interpolation(.high)
                .scaledToFit()
        } else {
            Image(systemName: fallback)
                .foregroundStyle(.secondary)
        }
    }
}
