import SwiftUI

struct SettingsView: View {
    @EnvironmentObject private var state: AppState

    @State private var updateInfo: UpdateInfo?
    @State private var checkingUpdates = false
    @State private var cachingOS = false
    @StateObject private var updateLog = OperationLog()

    var body: some View {
        VStack(spacing: 0) {
            Card(title: "Target Model",
                 subtitle: "Overrides the Mac model the patcher builds for.") {
                Picker("Target Model", selection: $state.targetModel) {
                    Text("Host Model").tag(nil as String?)
                    if let models = state.hostInfo?.supportedModels, !models.isEmpty {
                        Section("Supported") {
                            ForEach(models, id: \.self) { model in
                                Text(model).tag(Optional(model))
                            }
                        }
                    }
                }
                .pickerStyle(.menu)
                .labelsHidden()
                .frame(maxWidth: 260, alignment: .leading)
            }
            .padding([.horizontal, .top], 16)
            .padding(.bottom, 8)

            TabView {
                buildTab
                    .tabItem { Label("Build", systemImage: "externaldrive") }
                extrasTab
                    .tabItem { Label("Extras", systemImage: "plus.circle") }
                advancedTab
                    .tabItem { Label("Advanced", systemImage: "wrench.and.screwdriver") }
                securityTab
                    .tabItem { Label("Security", systemImage: "lock") }
                smbiosTab
                    .tabItem { Label("SMBIOS", systemImage: "cpu") }
                patchTab
                    .tabItem { Label("Patch", systemImage: "bandage") }
                appTab
                    .tabItem { Label("App", systemImage: "app") }
            }
        }
        .navigationTitle("Settings")
    }

    private func page<Content: View>(@ViewBuilder _ content: () -> Content) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 12) {
                content()
            }
            .padding(16)
            .frame(maxWidth: .infinity, alignment: .leading)
        }
    }

    // MARK: - Build

    private var buildTab: some View {
        page {
            Card(title: "Booting") {
                CardToggle(title: "FireWire boot", subtitle: "Boot macOS from FireWire drives.", isOn: $state.firewire)
                CardToggle(title: "XHCI boot", subtitle: "Boot from add-in USB 3.0 cards.", isOn: $state.xhciBoot)
                CardToggle(title: "NVMe boot", subtitle: "Boot from NVMe drives without native support.", isOn: $state.nvme)
            }
            Card(title: "OpenCore") {
                CardToggle(title: "OpenCore Vaulting", subtitle: "Digitally sign OpenCore to prevent tampering.", isOn: $state.vault)
                CardToggle(title: "Show OpenCore boot picker", subtitle: "When off, hold ESC in firmware to show it.", isOn: Binding(
                    get: { !state.hidePicker },
                    set: { state.hidePicker = !$0 }
                ))
                integerRow(title: "Boot picker timeout", value: $state.ocTimeout, range: 0...60, unit: "seconds")
            }
            Card(title: "Debug") {
                CardToggle(title: "Verbose boot", subtitle: "Show verbose output during boot (-v).", isOn: $state.verbose)
                CardToggle(title: "Kext DEBUG", subtitle: "Use DEBUG kexts with extra kernel logging.", isOn: $state.debugKext)
                CardToggle(title: "OpenCore DEBUG", subtitle: "Use the DEBUG variant of OpenCore.", isOn: $state.debugOC)
            }
        }
    }

    // MARK: - Extras

    private var extrasTab: some View {
        page {
            Card(title: "Wireless") {
                CardToggle(title: "Wake on WLAN",
                           subtitle: "Only for BCM943224, 331, 360 and 3602 chipsets.",
                           isOn: $state.wlan)
            }
            Card(title: "Thunderbolt") {
                CardToggle(title: "Disable Thunderbolt",
                           subtitle: "For MacBookPro11,x with faulty PCHs.",
                           isOn: $state.disableTB)
            }
            Card(title: "Display") {
                CardToggle(title: "Windows GMUX",
                           subtitle: "Expose the iGPU in Windows for dGPU-based MacBooks.",
                           isOn: $state.dgpuSwitch)
            }
            Card(title: "System") {
                CardToggle(title: "Disable CPUFriend",
                           subtitle: "Disable the power management helper for unsupported models.",
                           isOn: $state.disallowCPUFriend)
                CardToggle(title: "Disable mediaanalysisd",
                           subtitle: "For systems that are the primary iCloud account.",
                           isOn: $state.disableMediaanalysisd)
            }
        }
    }

    // MARK: - Advanced

    private var advancedTab: some View {
        page {
            Card(title: "Drives") {
                CardToggle(title: "Write to NVRAM", subtitle: "Write boot properties to hardware NVRAM.", isOn: $state.nvramWrite)
                CardToggle(title: "Allow NVMe kernel-space patches", isOn: $state.allowNvmeFixing)
                CardToggle(title: "Allow third-party drives", subtitle: "Enable the ThirdPartyDrives quirk.", isOn: $state.allowThirdPartyDrives)
                CardToggle(title: "APFS trim timeout", subtitle: "Set the APFS trim timeout.", isOn: $state.apfsTrimTimeout)
            }
            Card(title: "Boot") {
                CardToggle(title: "Disable firmware throttling", subtitle: "Disable MSR power control / XCPM.", isOn: $state.disableFWThrottle)
                CardToggle(title: "Software demux", subtitle: "Enable the software demux patch set.", isOn: $state.softwareDemux)
                CardToggle(title: "Disable ConnectDrivers", subtitle: "Fixes hibernation issues.", isOn: $state.disableConnectDrivers)
            }
            Card(title: "Graphics") {
                CardToggle(title: "AMD GOP injection", isOn: $state.amdGopInjection)
                CardToggle(title: "NVIDIA Kepler GOP injection", isOn: $state.nvidiaKeplerGopInjection)
            }
            Card(title: "Misc") {
                CardToggle(title: "Force SurPlus", subtitle: "Apply SurPlus in all newer OSes.", isOn: $state.forceSurplus)
            }
        }
    }

    // MARK: - Security

    private var securityTab: some View {
        page {
            Card(title: "System Integrity Protection") {
                CardToggle(title: "Disable SIP", isOn: $state.disableSIP)
            }
            Card(title: "Kernel Security") {
                CardToggle(title: "Secure Boot Model",
                           subtitle: "Matching T2 model when spoofing. Incompatible with root patching.",
                           isOn: $state.secureBootModel)
                CardToggle(title: "Disable Library Validation",
                           subtitle: "Required for loading modified system files from root patching.",
                           isOn: $state.disableCSLV)
                CardToggle(title: "Disable AMFI",
                           subtitle: "Deeper root patch support for affected systems.",
                           isOn: $state.disableAMFI)
            }
        }
    }

    // MARK: - SMBIOS

    private var smbiosTab: some View {
        page {
            Card(title: "Model Spoofing") {
                Picker("SMBIOS spoof level", selection: $state.smbiosSpoof) {
                    ForEach(SMBIOSLevel.allCases) { level in
                        Text(level.label).tag(level)
                    }
                }
                .pickerStyle(.segmented)

                Picker("SMBIOS spoof model", selection: $state.overrideSMBIOS) {
                    Text("Default").tag("Default")
                    if let models = state.hostInfo?.supportedModels, !models.isEmpty {
                        Divider()
                        ForEach(models, id: \.self) { model in
                            Text(model).tag(model)
                        }
                    }
                }
                .pickerStyle(.menu)

                CardToggle(title: "Allow spoofing native Macs",
                           subtitle: "Primarily for enabling Universal Control on unsupported Macs.",
                           isOn: $state.allowNativeSpoofs)
            }
        }
    }

    // MARK: - Patch

    private var patchTab: some View {
        page {
            Card(title: "Audio") {
                Picker("Audio patch", selection: $state.audioType) {
                    ForEach(["AppleHDA", "VoodooHDA", "HDAUniversal", "None"], id: \.self) {
                        Text($0).tag($0)
                    }
                }
                .pickerStyle(.segmented)

                Picker("AppleHDA.kext version", selection: $state.applehdaVersion) {
                    ForEach(["15.6", "26.0 Beta 1"], id: \.self) {
                        Text($0).tag($0)
                    }
                }
                .pickerStyle(.menu)
            }
            Card(title: "Patches") {
                CardToggle(title: "Allow Tahoe modern USB patch (deprecated)",
                           subtitle: "Patch the old USB extensions on Tahoe.",
                           isOn: $state.allowUSBPatch)
                CardToggle(title: "Allow Intel Wi-Fi patch",
                           subtitle: "Patch Wi-Fi on Ventura kexts.",
                           isOn: $state.allowIntelWifiPatch)
            }
        }
    }

    // MARK: - App

    private var appTab: some View {
        page {
            Card(title: "General") {
                CardToggle(title: "Allow OpenCore on native models",
                           subtitle: "Only for Macs that natively support the OS you wish to run.",
                           isOn: $state.supportAll)
                CardToggle(title: "Ignore app updates", isOn: $state.ignoreUpdates)
                CardToggle(title: "Disable reporting",
                           subtitle: "Do not send crash/analytics reports.",
                           isOn: $state.disableAnalytics)
                CardToggle(title: "Remove unused KDKs",
                           subtitle: "Remove unused Kernel Debug Kits during root patching.",
                           isOn: $state.shouldNukeKDKs)
                CardToggle(title: "Manually download KDKs and Metallibs", isOn: $state.manuallyDownloadKDK)
            }
            Card(title: "Update") {
                VStack(alignment: .leading, spacing: 10) {
                    if let updateInfo {
                        if updateInfo.updateAvailable {
                            Label("Version \(updateInfo.version ?? "") is available.", systemImage: "arrow.down.circle.fill")
                                .foregroundStyle(.blue)
                            HStack {
                                Button("Download & Install") {
                                    installUpdate(updateInfo)
                                }
                                .buttonStyle(.borderedProminent)
                                if let github = updateInfo.githubLink, let url = URL(string: github) {
                                    Link("View on GitHub", destination: url)
                                }
                            }
                        } else {
                            Label("You are up to date.", systemImage: "checkmark.circle.fill")
                                .foregroundStyle(.green)
                        }
                    }

                    HStack {
                        Button("Check for Updates") { checkForUpdates() }
                            .disabled(checkingUpdates)
                        if checkingUpdates {
                            ProgressView().controlSize(.small)
                        }
                        Spacer()
                    }

                    Divider()

                    Button("Cache OS Update") { cacheOSUpdate() }
                        .disabled(cachingOS)

                    if updateLog.finished || updateLog.isRunning {
                        LogConsoleView(title: "Update Log", log: updateLog)
                            .frame(maxHeight: 200)
                    }
                }
            }
            Card(title: "About") {
                HStack {
                    Text("Version")
                    Spacer()
                    Text(state.hostInfo?.patcherVersion ?? "—")
                        .foregroundStyle(.secondary)
                }
            }
        }
    }

    // MARK: - Helpers

    private func integerRow(title: String, value: Binding<Int>, range: ClosedRange<Int>, unit: String) -> some View {
        HStack {
            Text(title)
            Spacer()
            Stepper(value: value, in: range) {
                Text("\(value.wrappedValue) \(unit)")
                    .monospacedDigit()
                    .foregroundStyle(.secondary)
            }
            .fixedSize()
        }
    }

    // MARK: - Update / cache

    private func checkForUpdates() {
        checkingUpdates = true
        updateInfo = nil
        Task {
            updateInfo = await state.bridge.checkUpdates()
            checkingUpdates = false
        }
    }

    private func installUpdate(_ info: UpdateInfo) {
        guard let url = info.link else { return }
        updateLog.reset()
        updateLog.isRunning = true
        Task {
            let ok = await state.bridge.installUpdate(url: url, version: info.version ?? "") { line in
                updateLog.append(line)
            }
            updateLog.isRunning = false
            updateLog.finished = true
            updateLog.succeeded = ok
        }
    }

    private func cacheOSUpdate() {
        cachingOS = true
        updateLog.reset()
        updateLog.isRunning = true
        Task {
            let ok = await state.bridge.cacheOSHeadless { line in
                updateLog.append(line)
            }
            cachingOS = false
            updateLog.isRunning = false
            updateLog.finished = true
            updateLog.succeeded = ok
        }
    }
}
