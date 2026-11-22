import Foundation

/// Reads/writes the shared OCLP-R settings plist used by both front-ends.
///
/// Layout matches the wxPython GUI:
/// - build/patch options are stored as `GUI:<constants attribute>` (bool/int/str)
/// - App-tab options are stored under plain keys (`IgnoreAppUpdates`, …)
///
/// Values are loaded through the Python bridge (`--print_info`) so the UI always
/// shows the effective settings; writes are applied directly to the plist, which
/// is the exact same file and format the Python side reads at startup.
enum SettingsStore {
    static let url = URL(fileURLWithPath: "/Users/Shared/.com.hackdoc.oclp-r.plist")

    static func write(gui: [String: Any], global: [String: Any]) {
        var plist: [String: Any] = [:]
        if let data = try? Data(contentsOf: url),
           let existing = try? PropertyListSerialization.propertyList(from: data, format: nil) as? [String: Any] {
            plist = existing
        }

        for (key, value) in gui {
            plist["GUI:\(key)"] = value
        }
        for (key, value) in global {
            plist[key] = value
        }

        do {
            let data = try PropertyListSerialization.data(fromPropertyList: plist, format: .xml, options: 0)
            try data.write(to: url, options: .atomic)
        } catch {
            NSLog("OCLPR: failed to write settings plist: \(error)")
        }
    }

    static func exists() -> Bool {
        FileManager.default.fileExists(atPath: url.path)
    }
}
