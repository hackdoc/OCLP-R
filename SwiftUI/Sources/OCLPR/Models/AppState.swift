import Foundation
import Combine

@MainActor
final class AppState: ObservableObject {

    let bridge = PythonBridge()

    // Host info populated from `--print_info`
    @Published var hostInfo: HostInfo?
    @Published var isLoadingInfo = false
    @Published var infoError: String?

    // MARK: - Build tab
    @Published var targetModel: String?          // nil == host model
    @Published var verbose = false
    @Published var debugOC = false
    @Published var debugKext = false
    @Published var hidePicker = false
    @Published var ocTimeout = 5
    @Published var firewire = false
    @Published var xhciBoot = false
    @Published var nvme = false
    @Published var vault = false

    // MARK: - Extras tab
    @Published var wlan = false
    @Published var disableTB = false
    @Published var dgpuSwitch = false
    @Published var disallowCPUFriend = false
    @Published var disableMediaanalysisd = false

    // MARK: - Advanced tab
    @Published var nvramWrite = true
    @Published var allowNvmeFixing = true
    @Published var allowThirdPartyDrives = true
    @Published var apfsTrimTimeout = true
    @Published var disableFWThrottle = false
    @Published var softwareDemux = false
    @Published var disableConnectDrivers = false
    @Published var amdGopInjection = false
    @Published var nvidiaKeplerGopInjection = false
    @Published var forceSurplus = false

    // MARK: - Security tab
    @Published var disableSIP = false
    @Published var secureBootModel = false
    @Published var disableCSLV = false
    @Published var disableAMFI = false

    // MARK: - SMBIOS tab
    @Published var smbiosSpoof: SMBIOSLevel = .none
    @Published var overrideSMBIOS = "Default"
    @Published var allowNativeSpoofs = false

    // MARK: - Patch tab
    @Published var audioType = "AppleHDA"
    @Published var allowUSBPatch = false
    @Published var allowIntelWifiPatch = false
    @Published var applehdaVersion = "15.6"

    // MARK: - App tab
    @Published var supportAll = false
    @Published var ignoreUpdates = false
    @Published var disableAnalytics = false
    @Published var shouldNukeKDKs = true
    @Published var manuallyDownloadKDK = false

    private var settingsLoaded = false
    private var savedGUI: [String: Any] = [:]
    private var savedGlobal: [String: Any] = [:]
    private var saveCancellable: AnyCancellable?

    init() {
        // Persist (debounced) whenever any setting changes.
        saveCancellable = objectWillChange
            .debounce(for: .milliseconds(400), scheduler: RunLoop.main)
            .sink { [weak self] in self?.persistSettings() }
    }

    var effectiveModel: String {
        targetModel ?? hostInfo?.hostModel ?? "Unknown"
    }

    /// Whether OpenCore can be built for the current (target) model.
    /// Mirrors the wx GUI's host_can_build() logic: an explicit target model or
    /// "Allow OpenCore on native models" always enables building.
    var canBuild: Bool {
        if targetModel != nil { return true }
        if supportAll { return true }
        return hostInfo?.hostCanBuild ?? false
    }

    // MARK: - Host info

    func refreshHostInfo() async {
        isLoadingInfo = true
        infoError = nil
        defer { isLoadingInfo = false }
        if let info = await bridge.hostInfo() {
            if !settingsLoaded {
                applySettings(from: info)
                settingsLoaded = true
                // Baseline: nothing is written until the user changes a value.
                savedGUI = guiSettings()
                savedGlobal = globalSettings()
            }
            hostInfo = info
        } else {
            infoError = "Could not read host information from the patcher."
        }
    }

    // MARK: - Build arguments

    func buildArguments() -> [String] {
        var args = ["--build"]
        if let model = targetModel { args += ["--model", model] }
        if verbose { args.append("--verbose") }
        if debugOC { args.append("--debug_oc") }
        if debugKext { args.append("--debug_kext") }
        if hidePicker { args.append("--hide_picker") }
        if disableSIP { args.append("--disable_sip") }
        if !secureBootModel { args.append("--disable_smb") }
        if vault { args.append("--vault") }
        if firewire { args.append("--firewire") }
        if nvme { args.append("--nvme") }
        if wlan { args.append("--wlan") }
        if disableTB { args.append("--disable_tb") }
        if forceSurplus { args.append("--force_surplus") }
        if supportAll { args.append("--support_all") }
        switch smbiosSpoof {
        case .none: break
        case .minimal: args += ["--smbios_spoof", "Minimal"]
        case .moderate: args += ["--smbios_spoof", "Moderate"]
        case .advanced: args += ["--smbios_spoof", "Advanced"]
        }
        return args
    }

    // MARK: - Settings load/save

    private func applySettings(from info: HostInfo) {
        let s = info.settings ?? [:]

        func bool(_ key: String, _ fallback: Bool) -> Bool { s[key]?.boolValue ?? fallback }
        func int(_ key: String, _ fallback: Int) -> Int { s[key]?.intValue ?? fallback }
        func str(_ key: String, _ fallback: String) -> String { s[key]?.stringValue ?? fallback }

        verbose = bool("verbose_debug", verbose)
        debugOC = bool("opencore_debug", debugOC)
        debugKext = bool("kext_debug", debugKext)
        hidePicker = !bool("showpicker", !hidePicker)
        ocTimeout = int("oc_timeout", ocTimeout)
        firewire = bool("firewire_boot", firewire)
        xhciBoot = bool("xhci_boot", xhciBoot)
        nvme = bool("nvme_boot", nvme)
        vault = bool("vault", vault)

        wlan = bool("enable_wake_on_wlan", wlan)
        disableTB = bool("disable_tb", disableTB)
        dgpuSwitch = bool("dGPU_switch", dgpuSwitch)
        disallowCPUFriend = bool("disallow_cpufriend", disallowCPUFriend)
        disableMediaanalysisd = bool("disable_mediaanalysisd", disableMediaanalysisd)

        nvramWrite = bool("nvram_write", nvramWrite)
        allowNvmeFixing = bool("allow_nvme_fixing", allowNvmeFixing)
        allowThirdPartyDrives = bool("allow_3rd_party_drives", allowThirdPartyDrives)
        apfsTrimTimeout = bool("apfs_trim_timeout", apfsTrimTimeout)
        disableFWThrottle = bool("disable_fw_throttle", disableFWThrottle)
        softwareDemux = bool("software_demux", softwareDemux)
        disableConnectDrivers = bool("disable_connectdrivers", disableConnectDrivers)
        amdGopInjection = bool("amd_gop_injection", amdGopInjection)
        nvidiaKeplerGopInjection = bool("nvidia_kepler_gop_injection", nvidiaKeplerGopInjection)
        forceSurplus = bool("force_surplus", forceSurplus)

        disableSIP = !bool("sip_status", !disableSIP)
        secureBootModel = bool("secure_status", secureBootModel)
        disableCSLV = bool("disable_cs_lv", disableCSLV)
        disableAMFI = bool("disable_amfi", disableAMFI)

        smbiosSpoof = SMBIOSLevel(rawValue: str("serial_settings", smbiosSpoof.rawValue)) ?? smbiosSpoof
        overrideSMBIOS = str("override_smbios", overrideSMBIOS)
        allowNativeSpoofs = bool("allow_native_spoofs", allowNativeSpoofs)

        audioType = str("audio_type", audioType)
        allowUSBPatch = bool("allow_usb_patch", allowUSBPatch)
        allowIntelWifiPatch = bool("allow_intel_wifi_patch", allowIntelWifiPatch)
        applehdaVersion = str("applehda_version", applehdaVersion)

        supportAll = bool("allow_oc_everywhere", supportAll)
        manuallyDownloadKDK = bool("manually_download_kdk", manuallyDownloadKDK)

        if let globals = info.globalSettings {
            ignoreUpdates = globals["IgnoreAppUpdates"]?.boolValue ?? ignoreUpdates
            disableAnalytics = globals["DisableCrashAndAnalyticsReporting"]?.boolValue ?? disableAnalytics
            shouldNukeKDKs = globals["ShouldNukeKDKs"]?.boolValue ?? shouldNukeKDKs
        }
    }

    private func persistSettings() {
        guard settingsLoaded else { return }

        let gui = guiSettings()
        let global = globalSettings()

        // Only write keys the user actually changed since the last load/save,
        // so settings stored by the wx GUI (and unrelated preferences in the
        // same plist) are left untouched.
        let changedGUI = gui.filter { !Self.sameValue($0.value, savedGUI[$0.key]) }
        let changedGlobal = global.filter { !Self.sameValue($0.value, savedGlobal[$0.key]) }
        guard !changedGUI.isEmpty || !changedGlobal.isEmpty else { return }

        SettingsStore.write(gui: changedGUI, global: changedGlobal)
        savedGUI.merge(gui) { _, new in new }
        savedGlobal.merge(global) { _, new in new }
    }

    private static func sameValue(_ lhs: Any?, _ rhs: Any?) -> Bool {
        switch (lhs, rhs) {
        case let (l as Bool, r as Bool): return l == r
        case let (l as Int, r as Int): return l == r
        case let (l as String, r as String): return l == r
        default: return lhs == nil && rhs == nil
        }
    }

    private func guiSettings() -> [String: Any] {
        [
            "verbose_debug": verbose,
            "opencore_debug": debugOC,
            "kext_debug": debugKext,
            "showpicker": !hidePicker,
            "oc_timeout": ocTimeout,
            "firewire_boot": firewire,
            "xhci_boot": xhciBoot,
            "nvme_boot": nvme,
            "vault": vault,
            "enable_wake_on_wlan": wlan,
            "disable_tb": disableTB,
            "dGPU_switch": dgpuSwitch,
            "disallow_cpufriend": disallowCPUFriend,
            "disable_mediaanalysisd": disableMediaanalysisd,
            "nvram_write": nvramWrite,
            "allow_nvme_fixing": allowNvmeFixing,
            "allow_3rd_party_drives": allowThirdPartyDrives,
            "apfs_trim_timeout": apfsTrimTimeout,
            "disable_fw_throttle": disableFWThrottle,
            "software_demux": softwareDemux,
            "disable_connectdrivers": disableConnectDrivers,
            "amd_gop_injection": amdGopInjection,
            "nvidia_kepler_gop_injection": nvidiaKeplerGopInjection,
            "force_surplus": forceSurplus,
            "sip_status": !disableSIP,
            "secure_status": secureBootModel,
            "disable_cs_lv": disableCSLV,
            "disable_amfi": disableAMFI,
            "serial_settings": smbiosSpoof.rawValue,
            "override_smbios": overrideSMBIOS,
            "allow_native_spoofs": allowNativeSpoofs,
            "audio_type": audioType,
            "allow_usb_patch": allowUSBPatch,
            "allow_intel_wifi_patch": allowIntelWifiPatch,
            "applehda_version": applehdaVersion,
            "allow_oc_everywhere": supportAll,
            "manually_download_kdk": manuallyDownloadKDK,
        ]
    }

    private func globalSettings() -> [String: Any] {
        [
            "IgnoreAppUpdates": ignoreUpdates,
            "DisableCrashAndAnalyticsReporting": disableAnalytics,
            "ShouldNukeKDKs": shouldNukeKDKs,
        ]
    }
}
