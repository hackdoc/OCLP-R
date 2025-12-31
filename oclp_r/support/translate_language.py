from ..constants import Constants
"""
def xxx():
    if self.language_point==1:
        trans={...}
        return trans
    elif self.language_point==0:
        trans={...}
        return trans
"""
class TranslateLanguage:
    def __init__(self, global_constants: Constants) -> None:
        self.constants: Constants = global_constants
        self.language_point = self.constants.language_choose
    def gengrate_smbios(self):
        if self.language_point==1:
            trans={
                "Unknown SMBIOS for spoofing:":"Unknown SMBIOS for spoofing:",
                "- Failed to find FirmwareFeatures, falling back on defaults":"- Failed to find FirmwareFeatures, falling back on defaults",
            }
            return trans
        elif self.language_point==0:
            trans={
                "Unknown SMBIOS for spoofing:":"未知 SMBIOS 用于 spoofing：",
                "- Failed to find FirmwareFeatures, falling back on defaults":"- 未找到 FirmwareFeatures，回退到默认值",
            }
            return trans
    def arguements(self):
        if self.language_point==1:
            trans={
                "Set Validation Mode": "Set Validation Mode",
                "- Running from Installer Sandbox, blocking OS updaters":"- Running from Installer Sandbox, blocking OS updaters",
                "Set System Volume patching":"Set System Volume patching",
                "Set System Volume unpatching":"Set System Volume unpatching",
                "Set Auto patching":"Set Auto patching",
                "Preparing host for macOS update":"Preparing host for macOS update",
                "No update staged, skipping":"No update staged, skipping",
                "Preparing for update to":"Preparing for update to",
                "Another instance of OS caching is running, exiting":"Another instance of OS caching is running, exiting",
                "- Failed to load plist for":"- Failed to load plist for",
                "- Removing":"- Removing",
                "- Using custom model:":"- Using custom model:",
                """Your model is not supported by this patcher for running unsupported OSes!"

If you plan to create the USB for another machine, please select the "Change Model" option in the menu.""":"""Your model is not supported by this patcher for running unsupported OSes!"

If you plan to create the USB for another machine, please select the "Change Model" option in the menu.""",
                "- Using detected model:":"- Using detected model:",
                "- Set verbose configuration":"- Set verbose configuration",
                "- Set OpenCore DEBUG configuration":"- Set OpenCore DEBUG configuration",
                "- Set kext DEBUG configuration":"- Set kext DEBUG configuration",
                "- Set HidePicker configuration":"- Set HidePicker configuration",
                "- Set Disable SIP configuration":"- Set Disable SIP configuration",
                "- Set Disable SecureBootModel configuration":"- Set Disable SecureBootModel configuration",
                "- Set Vault configuration":"- Set Vault configuration",
                "- Set FireWire Boot configuration":"- Set FireWire Boot configuration",
                "- Set NVMe Boot configuration":"- Set NVMe Boot configuration",
                "- Set Wake on WLAN configuration":"- Set Wake on WLAN configuration",
                "- Set Disable Thunderbolt configuration":"- Set Disable Thunderbolt configuration",
                "- Forcing SurPlus override configuration":"- Forcing SurPlus override configuration",
                "- Set Moderate SMBIOS Patching configuration":"- Set Moderate SMBIOS Patching configuration",
                "- Unknown SMBIOS arg passed:":"- Unknown SMBIOS arg passed:",
                "- Building for natively supported model":"- Building for natively supported model",
                "Cleaning /Library/Extensions":"Cleaning /Library/Extensions",
                "Failed to load plist for":"Failed to load plist for",
                "Set OpenCore Build":"Set OpenCore Build",
                "Initializing Download Frame":"Initializing Download Frame",
                "Initializing Build Frame":"Initializing Build Frame",
                "Generating About frame":"Generating About frame",
                "Initializing KDK Download Frame":"Initializing KDK Download Frame",
                "Initializing NewMetallibDownloadFrame":"Initializing NewMetallibDownloadFrame",
                "Initializing macOS Installer Download Frame":"Initializing macOS Installer Download Frame",
                "Initializing Prepare Update Frame":"Initializing Prepare Update Frame",
                "Initializing Root Patch Display Frame":"Initializing Root Patch Display Frame",
                "Initializing Main Menu Frame":"Initializing Main Menu Frame",
                "Initializing Settings Frame":"Initializing Settings Frame",
                "Initializing Update Frame":"Initializing Update Frame",
                "Initializing Root Patching Frame":"Initializing Root Patching Frame",
                "Initializing Help Frame":"Initializing Help Frame",
                "Initializing macOS Installer Flash Frame":"Initializing macOS Installer Flash Frame",
                "User cancelled download":"User cancelled download",
                "User cancelled update":"User cancelled update",
                "No staged update found":"No staged update found",
                "Staged update found: {0} ({1})":"Staged update found: {0} ({1})",
                "KDK required":"KDK required",
                "MetallibSupportPkg required":"MetallibSupportPkg required",
                "No additional resources required":"No additional resources required",
                "KDK download complete, validating with hdiutil":"KDK download complete, validating with hdiutil",
                "KDK checksum validation passed":"KDK checksum validation passed",
                "Mounting KDK":"Mounting KDK",
                "KDK installed successfully":"KDK installed successfully",
                "Failed to install KDK":"Failed to install KDK",
                "Metallib installed successfully":"Metallib installed successfully",
                "Failed to install Metallib":"Failed to install Metallib",
                "KDK missing, generating KDK download frame":"KDK missing, generating KDK download frame",
                "KDK download complete, validating with hdiutil":"KDK download complete, validating with hdiutil",
                "KDK download complete":"KDK download complete",
                "MetallibSupportPkg missing, generating Metallib download frame":"MetallibSupportPkg missing, generating Metallib download frame",
                "Metallib download complete, installing Metallib PKG":"Metallib download complete, installing Metallib PKG",
                "Metallib installation complete":"Metallib installation complete",
                "User cancelled OS caching":"User cancelled OS caching",
                "No applicable patches available":"No applicable patches available",
                "Available patches:":"Available patches:",
                "Checking if new patches are needed":"Checking if new patches are needed",
                "Starting root patching":"Starting root patching",
                "Reverting root patches":"Reverting root patches",
                "No new patches detected for system":"No new patches detected for system",
                "Update URL: {url}":"Update URL: {url}",
                "Update Version: {version_label}":"Update Version: {version_label}",
                "Extracting nightly update":"Extracting nightly update",
                "Installing update: {path}":"Installing update: {path}",
                "Launching update: '{path}'":"Launching update: '{path}'",
                "New version: {version}":"New version: {version}",
                "Skipping OpenCore and root volume patch update...":"Skipping OpenCore and root volume patch update...",
                "Updating OpenCore and root volume patches...":"Updating OpenCore and root volume patches...",
                "Commit URLs differ":"Commit URLs differ",
                "Commit URLs: {urls}":"Commit URLs: {urls}",
                "Patch {patch} not installed":"Patch {patch} not installed",
                "Using Real Model: {model}":"Using Real Model: {model}",
                "Using Custom Model: {model}":"Using Custom Model: {model}",
                "user_download_file:{path}":"user_download_file:{path}",
                "Choose Path: {path}":"Choose Path: {path}",
                "Updating Local Setting: {variable} = {value}":"Updating Local Setting: {variable} = {value}",
                "Updating Global Setting: {variable} = {value}":"Updating Global Setting: {variable} = {value}",
                "Updating System Defaults: {variable} = {value} ({type})":"Updating System Defaults: {variable} = {value} ({type})",
                "Updating System Defaults (root): {variable} = {value} ({type})":"Updating System Defaults (root): {variable} = {value} ({type})",
                "Updating FU Status: Enabled":"Updating FU Status: Enabled",
                "Updating FU Status: Partial":"Updating FU Status: Partial",
                "Updating FU Status: Disabled":"Updating FU Status: Disabled",
                "Updating GPU Selection: {gpu_choice}":"Updating GPU Selection: {gpu_choice}",
                "Saving constants to {pathname}":"Saving constants to {pathname}",
                "macOS installer validated":"macOS installer validated",
                "Installer(s) found:":"Installer(s) found:",
                "Selected installer: {name} ({version} ({build}))":"Selected installer: {name} ({version} ({build}))",
                "Available disks:":"Available disks:",
                "Selected macOS DMG {version} ({build})":"Selected macOS DMG {version} ({build})",
                "Selected macOS {version} ({build})":"Selected macOS {version} ({build})"
            }
        elif self.language_point==0:
            trans = {
                "Set Validation Mode": "设置验证模式",
                "- Running from Installer Sandbox, blocking OS updaters": "- 从安装程序沙箱运行，阻止操作系统更新程序",
                "Set System Volume patching": "设置系统卷修补",
                "Set System Volume unpatching": "设置系统卷取消修补",
                "Set Auto patching": "设置自动修补",
                "Preparing host for macOS update": "准备主机以进行 macOS 更新",
                "No update staged, skipping": "没有暂存的更新，跳过",
                "Preparing for update to": "准备更新到",
                "Another instance of OS caching is running, exiting": "另一个操作系统缓存实例正在运行，退出",
                "- Failed to load plist for": "- 无法加载 plist 文件",
                "- Removing": "- 正在删除",
                "- Using custom model:": "- 使用自定义型号：",
                """Your model is not supported by this patcher for running unsupported OSes!"

If you plan to create the USB for another machine, please select the "Change Model" option in the menu.""": """您的型号不受此修补程序支持以运行不支持的操作系统！

如果您计划为另一台机器创建 USB，请在菜单中选择"更改型号"选项。""",
                "- Using detected model:": "- 使用检测到的型号：",
                "- Set verbose configuration": "- 设置详细配置",
                "- Set OpenCore DEBUG configuration": "- 设置 OpenCore 调试配置",
                "- Set kext DEBUG configuration": "- 设置 kext 调试配置",
                "- Set HidePicker configuration": "- 设置隐藏选择器配置",
                "- Set Disable SIP configuration": "- 设置禁用 SIP 配置",
                "- Set Disable SecureBootModel configuration": "- 设置禁用安全启动模型配置",
                "- Set Vault configuration": "- 设置 Vault 配置",
                "- Set FireWire Boot configuration": "- 设置 FireWire 启动配置",
                "- Set NVMe Boot configuration": "- 设置 NVMe 启动配置",
                "- Set Wake on WLAN configuration": "- 设置无线局域网唤醒配置",
                "- Set Disable Thunderbolt configuration": "- 设置禁用 Thunderbolt 配置",
                "- Forcing SurPlus override configuration": "- 强制 SurPlus 覆盖配置",
                "- Set Moderate SMBIOS Patching configuration": "- 设置适度 SMBIOS 修补配置",
                "- Unknown SMBIOS arg passed:": "- 传递了未知的 SMBIOS 参数：",
                "- Building for natively supported model": "- 为原生支持的型号构建",
                "Cleaning /Library/Extensions":"正在清理/Library/Extensions",
                "Failed to load plist for":"加载plist失败：",
                "Set OpenCore Build":"设置OpenCore构建",
                "Initializing Download Frame":"正在初始化下载框架",
                "Initializing Build Frame":"正在初始化构建框架",
                "Generating About frame":"正在生成关于框架",
                "Initializing KDK Download Frame":"正在初始化KDK下载框架",
                "Initializing NewMetallibDownloadFrame":"正在初始化NewMetallibDownloadFrame",
                "Initializing macOS Installer Download Frame":"正在初始化macOS安装程序下载框架",
                "Initializing Prepare Update Frame":"正在初始化准备更新框架",
                "Initializing Root Patch Display Frame":"正在初始化根补丁显示框架",
                "Initializing Main Menu Frame":"正在初始化主菜单框架",
                "Initializing Settings Frame":"正在初始化设置框架",
                "Initializing Update Frame":"正在初始化更新框架",
                "Initializing Root Patching Frame":"正在初始化根补丁框架",
                "Initializing Help Frame":"正在初始化帮助框架",
                "Initializing macOS Installer Flash Frame":"正在初始化macOS安装程序闪存框架",
                "User cancelled download":"用户取消了下载",
                "User cancelled update":"用户取消了更新",
                "No staged update found":"未找到暂存的更新",
                "Staged update found: {0} ({1})":"找到暂存的更新: {0} ({1})",
                "KDK required":"需要KDK",
                "MetallibSupportPkg required":"需要MetallibSupportPkg",
                "No additional resources required":"不需要额外的资源",
                "KDK download complete, validating with hdiutil":"KDK下载完成，正在用hdiutil验证",
                "KDK checksum validation passed":"KDK校验和验证通过",
                "Mounting KDK":"正在挂载KDK",
                "KDK installed successfully":"KDK安装成功",
                "Failed to install KDK":"安装KDK失败",
                "Metallib installed successfully":"Metallib安装成功",
                "Failed to install Metallib":"安装Metallib失败",
                "KDK missing, generating KDK download frame":"缺少KDK，正在生成KDK下载框架",
                "KDK download complete":"KDK下载完成",
                "MetallibSupportPkg missing, generating Metallib download frame":"缺少MetallibSupportPkg，正在生成Metallib下载框架",
                "Metallib download complete, installing Metallib PKG":"Metallib下载完成，正在安装Metallib PKG",
                "Metallib installation complete":"Metallib安装完成",
                "User cancelled OS caching":"用户取消了系统缓存",
                "No applicable patches available":"没有可用的适用补丁",
                "Available patches:":"可用补丁:",
                "Checking if new patches are needed":"检查是否需要新补丁",
                "Starting root patching":"开始根补丁",
                "Reverting root patches":"还原根补丁",
                "No new patches detected for system":"系统未检测到新补丁",
                "Update URL: {url}":"更新URL: {url}",
                "Update Version: {version_label}":"更新版本: {version_label}",
                "Extracting nightly update":"正在提取夜间更新",
                "Installing update: {path}":"正在安装更新: {path}",
                "Launching update: '{path}'":"正在启动更新: '{path}'",
                "New version: {version}":"新版本: {version}",
                "Skipping OpenCore and root volume patch update...":"跳过OpenCore和根卷补丁更新...",
                "Updating OpenCore and root volume patches...":"正在更新OpenCore和根卷补丁...",
                "Commit URLs differ":"提交URL不同",
                "Commit URLs: {urls}":"提交URL: {urls}",
                "Patch {patch} not installed":"补丁 {patch} 未安装",
                "Using Real Model: {model}":"使用真实型号: {model}",
                "Using Custom Model: {model}":"使用自定义型号: {model}",
                "user_download_file:{path}":"user_download_file:{path}",
                "Choose Path: {path}":"选择路径: {path}",
                "Updating Local Setting: {variable} = {value}":"正在更新本地设置: {variable} = {value}",
                "Updating Global Setting: {variable} = {value}":"正在更新全局设置: {variable} = {value}",
                "Updating System Defaults: {variable} = {value} ({type})":"正在更新系统默认值: {variable} = {value} ({type})",
                "Updating System Defaults (root): {variable} = {value} ({type})":"正在更新系统默认值(root): {variable} = {value} ({type})",
                "Updating FU Status: Enabled":"正在更新FU状态: 已启用",
                "Updating FU Status: Partial":"正在更新FU状态: 部分",
                "Updating FU Status: Disabled":"正在更新FU状态: 已禁用",
                "Updating GPU Selection: {gpu_choice}":"正在更新GPU选择: {gpu_choice}",
                "Saving constants to {pathname}":"正在保存常量到 {pathname}",
                "macOS installer validated":"macOS安装程序已验证",
                "Installer(s) found:":"找到安装程序:",
                "Selected installer: {name} ({version} ({build}))":"已选择安装程序: {name} ({version} ({build}))",
                "Available disks:":"可用磁盘:",
                "Selected macOS DMG {version} ({build})":"已选择macOS DMG {version} ({build})",
                "Selected macOS {version} ({build})":"已选择macOS {version} ({build})"
            }
            trans = {
                "Set Validation Mode": "设置验证模式",
                "- Running from Installer Sandbox, blocking OS updaters": "- 从安装程序沙箱运行，阻止操作系统更新程序",
                "Set System Volume patching": "设置系统卷修补",
                "Set System Volume unpatching": "设置系统卷取消修补",
                "Set Auto patching": "设置自动修补",
                "Preparing host for macOS update": "准备主机以进行 macOS 更新",
                "No update staged, skipping": "没有暂存的更新，跳过",
                "Preparing for update to": "准备更新到",
                "Another instance of OS caching is running, exiting": "另一个操作系统缓存实例正在运行，退出",
                "- Failed to load plist for": "- 无法加载 plist 文件",
                "- Removing": "- 正在删除",
                "- Using custom model:": "- 使用自定义型号：",
                """Your model is not supported by this patcher for running unsupported OSes!"

If you plan to create the USB for another machine, please select the "Change Model" option in the menu.""": """您的型号不受此修补程序支持以运行不支持的操作系统！

如果您计划为另一台机器创建 USB，请在菜单中选择"更改型号"选项。""",
                "- Using detected model:": "- 使用检测到的型号：",
                "- Set verbose configuration": "- 设置详细配置",
                "- Set OpenCore DEBUG configuration": "- 设置 OpenCore 调试配置",
                "- Set kext DEBUG configuration": "- 设置 kext 调试配置",
                "- Set HidePicker configuration": "- 设置隐藏选择器配置",
                "- Set Disable SIP configuration": "- 设置禁用 SIP 配置",
                "- Set Disable SecureBootModel configuration": "- 设置禁用安全启动模型配置",
                "- Set Vault configuration": "- 设置 Vault 配置",
                "- Set FireWire Boot configuration": "- 设置 FireWire 启动配置",
                "- Set NVMe Boot configuration": "- 设置 NVMe 启动配置",
                "- Set Wake on WLAN configuration": "- 设置无线局域网唤醒配置",
                "- Set Disable Thunderbolt configuration": "- 设置禁用 Thunderbolt 配置",
                "- Forcing SurPlus override configuration": "- 强制 SurPlus 覆盖配置",
                "- Set Moderate SMBIOS Patching configuration": "- 设置适度 SMBIOS 修补配置",
                "- Unknown SMBIOS arg passed:": "- 传递了未知的 SMBIOS 参数：",
                "- Building for natively supported model": "- 为原生支持的型号构建",
                "Cleaning /Library/Extensions":"正在清理/Library/Extensions",
                "Failed to load plist for":"加载plist失败：",
                "Set OpenCore Build":"设置OpenCore构建"
            }
        return trans
    
    def kdk_handler(self):
        if self.language_point==1:
            trans={
                "Could not contact KDK API":"Could not contact KDK API",
                "Could not fetch KDK list":"Could not fetch KDK list",
                "Pulling KDK list from KdkSupportPkg API":"Pulling KDK list from KdkSupportPkg API",
                "KDKs are not required for macOS Monterey or older":"KDKs are not required for macOS Monterey or older",
                "KDK already installed ({0}), skipping":"KDK already installed ({0}), skipping",
                "Failed to fetch KDK list, falling back to local KDK matching":"Failed to fetch KDK list, falling back to local KDK matching",
                "Checking for KDKs loosely matching {0}":"Checking for KDKs loosely matching {0}",
                "Found matching KDK: {0}":"Found matching KDK: {0}",
                "Couldn't find KDK matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a KDK.":"Couldn't find KDK matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a KDK.",
                "No direct match found for {0}, falling back to closest match":"No direct match found for {0}, falling back to closest match",
                "Closest Match: {0} ({1})":"Closest Match: {0} ({1})",
                "Direct match found for {0} ({1})":"Direct match found for {0} ({1})",
                "Following KDK is recommended:":"Following KDK is recommended:",
                "- KDK Build: {0}":"- KDK Build: {0}",
                "- KDK Version: {0}":"- KDK Version: {0}",
                "- KDK URL: {0}":"- KDK URL: {0}",
                "No download required, KDK already installed":"No download required, KDK already installed",
                "Could not retrieve KDK catalog, no KDK to download":"Could not retrieve KDK catalog, no KDK to download",
                "Returning DownloadObject for KDK: {0}":"Returning DownloadObject for KDK: {0}",
                "Failed to generate KDK Info.plist: {0}":"Failed to generate KDK Info.plist: {0}",
                "Corrupted KDK found ({0}), removing due to missing SystemVersion.plist":"Corrupted KDK found ({0}), removing due to missing SystemVersion.plist",
                "Corrupted KDK found ({0}), removing due to missing ProductBuildVersion":"Corrupted KDK found ({0}), removing due to missing ProductBuildVersion",
                "pkg receipt missing for {0}, falling back to legacy validation":"pkg receipt missing for {0}, falling back to legacy validation",
                "Corrupted KDK found ({0}), removing due to missing file: {1}":"Corrupted KDK found ({0}), removing due to missing file: {1}",
                "Corrupted KDK found, removing due to missing: {0}":"Corrupted KDK found, removing due to missing: {0}",
                "Found KDK backup: {0}":"Found KDK backup: {0}",
                "Attempting KDK restoration":"Attempting KDK restoration",
                "Successfully restored KDK":"Successfully restored KDK",
                "KDK restoration skipped, running in passive mode":"KDK restoration skipped, running in passive mode",
                "KDK does not exist: {0}":"KDK does not exist: {0}",
                "Error: Kernel Debug Kit checksum verification failed!":"Error: Kernel Debug Kit checksum verification failed!",
                "Kernel Debug Kit checksum verification failed, please try again.\n\nIf this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)":"Kernel Debug Kit checksum verification failed, please try again.\n\nIf this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)",
                "Kernel Debug Kit checksum verified":"Kernel Debug Kit checksum verified",
                "Installing KDK package: {0}":"Installing KDK package: {0}",
                "- This may take a while...":"- This may take a while...",
                "Failed to install KDK:":"Failed to install KDK:",
                "Extracting downloaded KDK disk image":"Extracting downloaded KDK disk image",
                "Failed to mount KDK:":"Failed to mount KDK:",
                "Failed to find KDK package in DMG, likely corrupted!!!":"Failed to find KDK package in DMG, likely corrupted!!!",
                "Successfully installed KDK":"Successfully installed KDK",
                "KDK does not exist, cannot create backup":"KDK does not exist, cannot create backup",
                "KDK Info.plist does not exist, cannot create backup":"KDK Info.plist does not exist, cannot create backup",
                "Malformed KDK Info.plist provided, cannot create backup":"Malformed KDK Info.plist provided, cannot create backup",
                "Creating backup: {0}":"Creating backup: {0}",
                "Backup already exists, skipping":"Backup already exists, skipping",
                "Failed to create KDK backup:":"Failed to create KDK backup:",
                "Cleaning unused KDKs":"Cleaning unused KDKs"
            }
        elif self.language_point==0:
            trans={
                "Could not contact KDK API":"无法联系 KDK API",
                "Pulling KDK list from KdkSupportPkg API":"从 KdkSupportPkg API 获取 KDK 列表",
                "Could not fetch KDK list":"无法获取 KDK 列表",
                "KDKs are not required for macOS Monterey or older":"macOS Monterey 或更早版本不需要 KDK",
                "KDK already installed ({0}), skipping":"KDK 已安装 ({0})，跳过",
                "Failed to fetch KDK list, falling back to local KDK matching":"获取 KDK 列表失败，回退到本地 KDK 匹配",
                "Checking for KDKs loosely matching {0}":"检查与 {0} 松散匹配的 KDK",
                "Found matching KDK: {0}":"找到匹配的 KDK: {0}",
                "Couldn't find KDK matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a KDK.":"找不到与 {0} ({1}) 或 {2} 匹配的 KDK。\n请确保您有网络连接或手动安装 KDK。",
                "No direct match found for {0}, falling back to closest match":"未找到 {0} 的直接匹配，回退到最接近的匹配",
                "Closest Match: {0} ({1})":"最接近的匹配: {0} ({1})",
                "Direct match found for {0} ({1})":"找到 {0} ({1}) 的直接匹配",
                "Following KDK is recommended:":"建议使用以下 KDK:",
                "- KDK Build: {0}":"- KDK 构建版本: {0}",
                "- KDK Version: {0}":"- KDK 版本: {0}",
                "- KDK URL: {0}":"- KDK URL: {0}",
                "No download required, KDK already installed":"不需要下载，KDK 已安装",
                "Could not retrieve KDK catalog, no KDK to download":"无法检索 KDK 目录，没有可下载的 KDK",
                "Returning DownloadObject for KDK: {0}":"返回 KDK 的 DownloadObject: {0}",
                "Failed to generate KDK Info.plist: {0}":"生成 KDK Info.plist 失败: {0}",
                "Corrupted KDK found ({0}), removing due to missing SystemVersion.plist":"发现损坏的 KDK ({0})，由于缺少 SystemVersion.plist 而移除",
                "Corrupted KDK found ({0}), removing due to missing ProductBuildVersion":"发现损坏的 KDK ({0})，由于缺少 ProductBuildVersion 而移除",
                "pkg receipt missing for {0}, falling back to legacy validation":"{0} 的 pkg 收据缺失，回退到传统验证",
                "Corrupted KDK found ({0}), removing due to missing file: {1}":"发现损坏的 KDK ({0})，由于缺少文件 {1} 而移除",
                "Corrupted KDK found, removing due to missing: {0}":"发现损坏的 KDK，由于缺少 {0} 而移除",
                "Found KDK backup: {0}":"找到 KDK 备份: {0}",
                "Attempting KDK restoration":"尝试恢复 KDK",
                "Successfully restored KDK":"成功恢复 KDK",
                "KDK restoration skipped, running in passive mode":"跳过 KDK 恢复，以被动模式运行",
                "KDK does not exist: {0}":"KDK 不存在: {0}",
                "Error: Kernel Debug Kit checksum verification failed!":"错误: Kernel Debug Kit 校验和验证失败!",
                "Kernel Debug Kit checksum verification failed, please try again.\n\nIf this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)":"Kernel Debug Kit 校验和验证失败，请重试。\n\n如果问题持续存在，请确保您在稳定的网络连接上下载（例如：以太网）",
                "Kernel Debug Kit checksum verified":"Kernel Debug Kit 校验和已验证",
                "Installing KDK package: {0}":"正在安装 KDK 包: {0}",
                "- This may take a while...":"- 这可能需要一段时间...",
                "Failed to install KDK:":"安装 KDK 失败:",
                "Extracting downloaded KDK disk image":"正在提取下载的 KDK 磁盘映像",
                "Failed to mount KDK:":"挂载 KDK 失败:",
                "Failed to find KDK package in DMG, likely corrupted!!!":"在 DMG 中找不到 KDK 包，可能已损坏!!!",
                "Successfully installed KDK":"成功安装 KDK",
                "KDK does not exist, cannot create backup":"KDK 不存在，无法创建备份",
                "KDK Info.plist does not exist, cannot create backup":"KDK Info.plist 不存在，无法创建备份",
                "Malformed KDK Info.plist provided, cannot create backup":"提供的 KDK Info.plist 格式错误，无法创建备份",
                "Creating backup: {0}":"正在创建备份: {0}",
                "Backup already exists, skipping":"备份已存在，跳过",
                "Failed to create KDK backup:":"创建 KDK 备份失败:",
                "Cleaning unused KDKs":"正在清理未使用的 KDK"
            }
        return trans
    def logging_handler(self):
        if self.language_point==1:
            trans={
                "Failed to create Hackdoc folder: {0}":"Failed to create Hackdoc folder: {0}",
                "Failed to initialize logging framework: {0}":"Failed to initialize logging framework: {0}",
                "Retrying without logging to file...":"Retrying without logging to file...",
                "# OCLP-R ({0}) #":"# OCLP-R ({0}) #",
                "Log file set:":"Log file set:",
                "Failed to display crash report dialog: {0}":"Failed to display crash report dialog: {0}",
                "OCLP-R encountered the following internal error:\n\n":"OCLP-R encountered the following internal error:\n\n",
                "\n\nReveal log file?":"\n\nReveal log file?",
                "Host Properties:":"Host Properties:",
                "  XNU Version: {0}.{1}":"  XNU Version: {0}.{1}",
                "  XNU Build: {0}":"  XNU Build: {0}",
                "  macOS Version: {0}":"  macOS Version: {0}",
                "Debug Properties:":"Debug Properties:",
                "  Effective User ID: {0}":"  Effective User ID: {0}",
                "  Effective Group ID: {0}":"  Effective Group ID: {0}",
                "  Real User ID: {0}":"  Real User ID: {0}",
                "  Real Group ID: {0}":"  Real Group ID: {0}",
                "  Arguments passed to Patcher:":"  Arguments passed to Patcher:",
                "Failed to delete log file: {0}":"Failed to delete log file: {0}"
            }
        elif self.language_point==0:
            trans={
                "Failed to create Hackdoc folder: {0}":"创建 Hackdoc 文件夹失败: {0}",
                "Failed to initialize logging framework: {0}":"初始化日志框架失败: {0}",
                "Retrying without logging to file...":"重试不记录到文件...",
                "# OCLP-R ({0}) #":"# OCLP-R ({0}) #",
                "Log file set:":"日志文件已设置:",
                "Failed to display crash report dialog: {0}":"显示崩溃报告对话框失败: {0}",
                "OCLP-R encountered the following internal error:\n\n":"OCLP-R 遇到以下内部错误:\n\n",
                "\n\nReveal log file?":"\n\n显示日志文件?",
                "Host Properties:":"主机属性:",
                "  XNU Version: {0}.{1}":"  XNU 版本: {0}.{1}",
                "  XNU Build: {0}":"  XNU 构建: {0}",
                "  macOS Version: {0}":"  macOS 版本: {0}",
                "Debug Properties:":"调试属性:",
                "  Effective User ID: {0}":"  有效用户 ID: {0}",
                "  Effective Group ID: {0}":"  有效组 ID: {0}",
                "  Real User ID: {0}":"  实际用户 ID: {0}",
                "  Real Group ID: {0}":"  实际组 ID: {0}",
                "  Arguments passed to Patcher:":"  传递给补丁程序的参数:",
                "Failed to delete log file: {0}":"删除日志文件失败: {0}"
            }
        return trans
    def macos_installer_handler(self):
        if self.language_point==1:
            trans={
                "Extracting macOS installer from InstallAssistant.pkg":"Extracting macOS installer from InstallAssistant.pkg",
                "Failed to install InstallAssistant":"Failed to install InstallAssistant",
                "InstallAssistant installed":"InstallAssistant installed",
                "Creating temporary directory at {0}":"Creating temporary directory at {0}",
                "Not enough free space to create installer.sh":"Not enough free space to create installer.sh",
                "{0} available, {1} required":"{0} available, {1} required",
                "Failed to copy installer to {0}":"Failed to copy installer to {0}",
                "Installer has broken code signature":"Installer has broken code signature"
            }
        elif self.language_point==0:
            trans={
                "Extracting macOS installer from InstallAssistant.pkg":"正在从 InstallAssistant.pkg 提取 macOS 安装程序",
                "Failed to install InstallAssistant":"无法安装 InstallAssistant",
                "InstallAssistant installed":"InstallAssistant 已安装",
                "Creating temporary directory at {0}":"正在 {0} 创建临时目录",
                "Not enough free space to create installer.sh":"没有足够的可用空间来创建 installer.sh",
                "{0} available, {1} required":"可用空间 {0}，需要 {1}",
                "Failed to copy installer to {0}":"无法将安装程序复制到 {0}",
                "Installer has broken code signature":"安装程序的代码签名已损坏"
            }
        return trans
    def metallib_handler(self):
        if self.language_point==1:
            trans={
                "MetallibSupportPkg is not required for macOS Sonoma or older":"MetallibSupportPkg is not required for macOS Sonoma or older",
                "metallib already installed ({0}), skipping":"metallib already installed ({0}), skipping",
                "Pulling metallib list from MetallibSupportPkg API":"Pulling metallib list from MetallibSupportPkg API",
                "Could not contact MetallibSupportPkg API":"Could not contact MetallibSupportPkg API",
                "Could not fetch Metallib list":"Could not fetch Metallib list",
                "Cannot get file size {0}: {1}":"Cannot get file size {0}: {1}",
                "Failed to fetch metallib list, falling back to local metallib matching":"Failed to fetch metallib list, falling back to local metallib matching",
                "Checking for metallibs loosely matching {0}":"Checking for metallibs loosely matching {0}",
                "Found matching metallib: {0}":"Found matching metallib: {0}",
                "Couldn't find metallib matching {0} or {1}, please install one manually":"Couldn't find metallib matching {0} or {1}, please install one manually",
                "Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a metallib.":"Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a metallib.",
                "No metallibs found for {0} ({1})":"No metallibs found for {0} ({1})",
                "No direct match found for {0}, falling back to closest match":"No direct match found for {0}, falling back to closest match",
                "Closest Match: {0} ({1})":"Closest Match: {0} ({1})",
                "Direct match found for {0} ({1})":"Direct match found for {0} ({1})",
                "Following metallib is recommended:":"Following metallib is recommended:",
                "- metallib Build: {0}":"- metallib Build: {0}",
                "- metallib Version: {0}":"- metallib Version: {0}",
                "- metallib URL: {0}":"- metallib URL: {0}",
                "- metallib size: {0}":"- metallib size: {0}",
                "No download required, metallib already installed":"No download required, metallib already installed",
                "Could not retrieve metallib catalog, no metallib to download":"Could not retrieve metallib catalog, no metallib to download",
                "Returning DownloadObject for metallib: {0}":"Returning DownloadObject for metallib: {0}",
                "Cannot install metallib, no metallib was successfully retrieved":"Cannot install metallib, no metallib was successfully retrieved",
                "No installation required, metallib already installed":"No installation required, metallib already installed"
            }
        elif self.language_point==0:
            trans={
                "MetallibSupportPkg is not required for macOS Sonoma or older":"macOS Sonoma 或更早版本不需要 MetallibSupportPkg",
                "metallib already installed ({0}), skipping":"metallib 已安装 ({0})，跳过",
                "Pulling metallib list from MetallibSupportPkg API":"正在从 MetallibSupportPkg API 获取 metallib 列表",
                "Could not contact MetallibSupportPkg API":"无法联系 MetallibSupportPkg API",
                "Could not fetch Metallib list":"无法获取 Metallib 列表",
                "Cannot get file size {0}: {1}":"无法获取文件大小 {0}: {1}",
                "Failed to fetch metallib list, falling back to local metallib matching":"获取 metallib 列表失败，回退到本地 metallib 匹配",
                "Checking for metallibs loosely matching {0}":"检查与 {0} 松散匹配的 metallib",
                "Found matching metallib: {0}":"找到匹配的 metallib: {0}",
                "Couldn't find metallib matching {0} or {1}, please install one manually":"找不到与 {0} 或 {1} 匹配的 metallib，请手动安装一个",
                "Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.\nPlease ensure you have a network connection or manually install a metallib.":"无法联系 MetallibSupportPkg API，且没有安装与 {0} ({1}) 或 {2} 匹配的 metallib。\n请确保您有网络连接或手动安装 metallib。",
                "No metallibs found for {0} ({1})":"找不到适用于 {0} ({1}) 的 metallib",
                "No direct match found for {0}, falling back to closest match":"未找到 {0} 的直接匹配，回退到最接近的匹配",
                "Closest Match: {0} ({1})":"最接近的匹配: {0} ({1})",
                "Direct match found for {0} ({1})":"找到 {0} ({1}) 的直接匹配",
                "Following metallib is recommended:":"建议使用以下 metallib:",
                "- metallib Build: {0}":"- metallib 构建版本: {0}",
                "- metallib Version: {0}":"- metallib 版本: {0}",
                "- metallib URL: {0}":"- metallib URL: {0}",
                "- metallib size: {0}":"- metallib 大小: {0}",
                "No download required, metallib already installed":"不需要下载，metallib 已安装",
                "Could not retrieve metallib catalog, no metallib to download":"无法检索 metallib 目录，没有可下载的 metallib",
                "Returning DownloadObject for metallib: {0}":"返回 metallib 的 DownloadObject: {0}",
                "Cannot install metallib, no metallib was successfully retrieved":"无法安装 metallib，没有成功检索到 metallib",
                "No installation required, metallib already installed":"不需要安装，metallib 已安装"
            }
        return trans
    def network_handler(self):
        if self.language_point==1:
            trans={
                "Inactive":"Inactive",
                "Downloading":"Downloading",
                "Error":"Error",
                "Complete":"Complete",
                "Error calling requests.get":"Error calling requests.get",
                "Error calling requests.post":"Error calling requests.post",
                "Starting download: {0}":"Starting download: {0}",
                "Download already in progress":"Download already in progress",
                "Error determining file size {0}: {1}":"Error determining file size {0}: {1}",
                "Assuming file size is 0":"Assuming file size is 0",
                "Resuming download from {0}: {1}":"Resuming download from {0}: {1}",
                "Deleting existing file: {0}":"Deleting existing file: {0}",
                "Creating directory: {0}":"Creating directory: {0}",
                "Not enough free space to download {0}, need {1}, have {2}":"Not enough free space to download {0}, need {1}, have {2}",
                "Error preparing working directory {0}: {1}":"Error preparing working directory {0}: {1}",
                "- Directory ready: {0}":"- Directory ready: {0}",
                "Failed to save download progress: {0}":"Failed to save download progress: {0}",
                "Failed to load download progress: {0}":"Failed to load download progress: {0}",
                "Failed to clear progress file: {0}":"Failed to clear progress file: {0}",
                "No network connection":"No network connection",
                "Resuming download from byte {0}":"Resuming download from byte {0}",
                "Download stopped":"Download stopped",
                "Download complete: {0}":"Download complete: {0}",
                "Stats:":"Stats:",
                "- Downloaded size: {0}":"- Downloaded size: {0}",
                "- Time elapsed: {0:.2f} seconds":"- Time elapsed: {0:.2f} seconds",
                "- Speed: {0}/s":"- Speed: {0}/s",
                "- Location: {0}":"- Location: {0}",
                "Error downloading {0}: {1}":"Error downloading {0}: {1}",
                "Deleted partially downloaded file: {0}":"Deleted partially downloaded file: {0}",
                "Deleted progress file: {0}":"Deleted progress file: {0}",
                "Failed to delete temporary files: {0}":"Failed to delete temporary files: {0}",
                "Downloaded {0} of {1}":"Downloaded {0} of {1}",
                "Downloaded {0:.2f}% of {1} ({2}/s) ({3:.2f} seconds remaining)":"Downloaded {0:.2f}% of {1} ({2}/s) ({3:.2f} seconds remaining)",
            }
        elif self.language_point==0:
            trans={
                "Inactive":"未下载",
                "Downloading":"正在下载",
                "Error":"错误",
                "Complete":"完成",
                "Error calling requests.get":"调用 requests.get 错误",
                "Error calling requests.post":"调用 requests.post 错误",
                "Starting download: {0}":"正在开始下载: {0}",
                "Download already in progress":"下载已经在进行中",
                "Error determining file size {0}: {1}":"确定文件大小错误 {0}: {1}",
                "Assuming file size is 0":"假设文件大小为 0",
                "Resuming download from {0}: {1}":"从 {0} 恢复下载: {1}",
                "Deleting existing file: {0}":"正在删除现有文件: {0}",
                "Creating directory: {0}":"正在创建目录: {0}",
                "Not enough free space to download {0}, need {1}, have {2}":"没有足够的可用空间下载 {0}，需要 {1}，已有 {2}",
                "Error preparing working directory {0}: {1}":"准备工作目录错误 {0}: {1}",
                "- Directory ready: {0}":"- 目录已准备好: {0}",
                "Failed to save download progress: {0}":"保存下载进度失败: {0}",
                "Failed to load download progress: {0}":"加载下载进度失败: {0}",
                "Failed to clear progress file: {0}":"清除进度文件失败: {0}",
                "No network connection":"没有网络连接",
                "Resuming download from byte {0}":"从字节 {0} 恢复下载",
                "Download stopped":"下载已停止",
                "Download complete: {0}":"下载完成: {0}",
                "Stats:":"统计信息:",
                "- Downloaded size: {0}":"- 已下载大小: {0}",
                "- Time elapsed: {0:.2f} seconds":"- 耗时: {0:.2f} 秒",
                "- Speed: {0}/s":"- 速度: {0}/秒",
                "- Location: {0}":"- 位置: {0}",
                "Error downloading {0}: {1}":"下载错误 {0}: {1}",
                "Deleted partially downloaded file: {0}":"已删除部分下载的文件: {0}",
                "Deleted progress file: {0}":"已删除进度文件: {0}",
                "Failed to delete temporary files: {0}":"删除临时文件失败: {0}",
                "Downloaded {0} of {1}":"已下载 {0} ，共 {1}",
                "Downloaded {0:.2f}% of {1} ({2}/s) ({3:.2f} seconds remaining)":"已下载 {0:.2f}% ，共 {1} ，速度 {2} ，剩余时间 {3:.2f} 秒",
            }
        return trans
    def private(self):
        if self.language_point==1:
            trans={
                "writing":"writing",
                "File {0} not found":"File {0} not found",
                "Invalid JSON in file {0}":"Invalid JSON in file {0}"
            }
        elif self.language_point==0:
            trans={
                "writing":"正在写入",
                "File {0} not found":"文件 {0} 未找到",
                "Invalid JSON in file {0}":"文件 {0} 中的 JSON 无效"
            }
        return trans
    def reroute_payloads(self):
        if self.language_point==1:
            trans={
                "Running in compiled binary, switching to tmp directory":"Running in compiled binary, switching to tmp directory",
                "New payloads location: {0}":"New payloads location: {0}",
                "Creating payloads directory":"Creating payloads directory",
                "Mounted payloads.dmg":"Mounted payloads.dmg",
                "Failed to mount payloads.dmg":"Failed to mount payloads.dmg",
                "Unmounting personal {0}":"Unmounting personal {0}",
                "Unmounting {0} at: {1}":"Unmounting {0} at: {1}"
            }
        elif self.language_point==0:
            trans={
                "Running in compiled binary, switching to tmp directory":"正在运行编译后的二进制文件，切换到临时目录",
                "New payloads location: {0}":"新的 payloads 位置: {0}",
                "Creating payloads directory":"正在创建 payloads 目录",
                "Mounted payloads.dmg":"已挂载 payloads.dmg",
                "Failed to mount payloads.dmg":"无法挂载 payloads.dmg",
                "Unmounting personal {0}":"正在卸载个人 {0}",
                "Unmounting {0} at: {1}":"正在卸载 {0} 于: {1}"
            }
        return trans
    def subprocess_wrapper(self):
        if self.language_point==1:
            trans={
                "Subprocess failed.":"Subprocess failed.",
                "    Command: {0}":"    Command: {0}",
                "    Return Code: {0}":"    Return Code: {0}",
                "        Likely Enum: {0}":"        Likely Enum: {0}",
                "    Standard Output:":"    Standard Output:",
                "        None":"        None",
                "    Standard Error:":"    Standard Error:",
                "File not found: {0}":"File not found: {0}"
            }
        elif self.language_point==0:
            trans={
                "Subprocess failed.":"子进程失败。",
                "    Command: {0}":"    命令: {0}",
                "    Return Code: {0}":"    返回代码: {0}",
                "        Likely Enum: {0}":"        可能的枚举: {0}",
                "    Standard Output:":"    标准输出:",
                "        None":"        无",
                "    Standard Error:":"    标准错误:",
                "File not found: {0}":"文件未找到: {0}"
            }
        return trans
    def updates(self):
        if self.language_point==1:
            trans={
                "Found asset: {0}":"Found asset: {0}"
            }
        elif self.language_point==0:
            trans={
                "Found asset: {0}":"找到资产: {0}"
            }
        return trans
    def utilities(self):
        if self.language_point==1:
            trans={
                "Disabling Idle Sleep":"Disabling Idle Sleep",
                "Re-enabling Idle Sleep":"Re-enabling Idle Sleep",
                "Killing Process: {0} - {1}":"Killing Process: {0} - {1}"
            }
        elif self.language_point==0:
            trans={
                "Disabling Idle Sleep":"正在禁用空闲睡眠",
                "Re-enabling Idle Sleep":"正在重新启用空闲睡眠",
                "Killing Process: {0} - {1}":"正在终止进程: {0} - {1}"
            }
        return trans
    
    def validation(self):
        if self.language_point==1:
            trans={
                "Validating predefined model: {model}":"Validating predefined model: {model}",
                "Error on build!":"Error on build!",
                "Validation failed for predefined model: {model}":"Validation failed for predefined model: {model}",
                "Validation succeeded for predefined model: {model}":"Validation succeeded for predefined model: {model}",
                "Validating dumped model: {model}":"Validating dumped model: {model}",
                "Unknown PatchType: {install_type}":"Unknown PatchType: {install_type}",
                "{install_file} used with {install_type}, are you certain this is correct?":"{install_file} used with {install_type}, are you certain this is correct?",
                "File not found: {source_file}":"File not found: {source_file}",
                "Failed to find {source_file}":"Failed to find {source_file}",
                "Validating against Darwin {major_kernel}.{minor_kernel}":"Validating against Darwin {major_kernel}.{minor_kernel}",
                "Failed to generate patchset plist":"Failed to generate patchset plist",
                "Failed to unmount Universal-Binaries.dmg":"Failed to unmount Universal-Binaries.dmg",
                "Failed to download Universal-Binaries.dmg":"Failed to download Universal-Binaries.dmg",
                "Validating Root Patch File integrity":"Validating Root Patch File integrity",
                "Failed to mount Universal-Binaries.dmg":"Failed to mount Universal-Binaries.dmg",
                "Mounted Universal-Binaries.dmg":"Mounted Universal-Binaries.dmg",
                "Validating SNB Board ID patcher":"Validating SNB Board ID patcher",
                "Unused files found:":"Unused files found:"
            }
        elif self.language_point==0:
            trans={
                "Validating predefined model: {model}":"正在验证预定义模型: {model}",
                "Error on build!":"构建时出错!",
                "Validation failed for predefined model: {model}":"预定义模型验证失败: {model}",
                "Validation succeeded for predefined model: {model}":"预定义模型验证成功: {model}",
                "Validating dumped model: {model}":"正在验证转储模型: {model}",
                "Unknown PatchType: {install_type}":"未知的 PatchType: {install_type}",
                "{install_file} used with {install_type}, are you certain this is correct?":"{install_file} 与 {install_type} 一起使用，您确定这是正确的吗?",
                "File not found: {source_file}":"找不到文件: {source_file}",
                "Failed to find {source_file}":"找不到 {source_file}",
                "Validating against Darwin {major_kernel}.{minor_kernel}":"正在验证 Darwin {major_kernel}.{minor_kernel}",
                "Failed to generate patchset plist":"生成补丁集 plist 失败",
                "Failed to unmount Universal-Binaries.dmg":"无法卸载 Universal-Binaries.dmg",
                "Failed to download Universal-Binaries.dmg":"下载 Universal-Binaries.dmg 失败",
                "Validating Root Patch File integrity":"正在验证 Root Patch 文件完整性",
                "Failed to mount Universal-Binaries.dmg":"无法挂载 Universal-Binaries.dmg",
                "Mounted Universal-Binaries.dmg":"已挂载 Universal-Binaries.dmg",
                "Validating SNB Board ID patcher":"正在验证 SNB Board ID 补丁",
                "Unused files found:":"找到未使用的文件:"
            }
        return trans
    
    def arguments(self):
        if self.language_point==1:
            trans={"Set Validation Mode":"Set Validation Mode",
                    "Set System Volume patching":"Set System Volume patching",
                    "- Running from Installer Sandbox, blocking OS updaters":"- Running from Installer Sandbox, blocking OS updaters",
                    "Set System Volume unpatching":"Set System Volume unpatching",
                    "Set Auto patching":"Set Auto patching",
                    "Preparing host for macOS update":"Preparing host for macOS update",
                    "No update staged, skipping":"No update staged, skipping",
                    "Preparing for update to":"Preparing for update to",
                    "Another instance of OS caching is running, exiting":"Another instance of OS caching is running, exiting",
                    "Cleaning /Library/Extensions":"Cleaning /Library/Extensions",
                    "- Failed to load plist for":"- Failed to load plist for",
                    "- Removing":"- Removing",
                    "Set OpenCore Build":"Set OpenCore Build",
                    "- Using custom model:":"- Using custom model:",
                    "Your model is not supported by this patcher for running unsupported OSes!\n\nIf you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.":"Your model is not supported by this patcher for running unsupported OSes!\n\nIf you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.",
                    "- Using detected model:":"- Using detected model:",
                    "- Set verbose configuration":"- Set verbose configuration",
                    "- Set OpenCore DEBUG configuration":"- Set OpenCore DEBUG configuration",
                    "- Set kext DEBUG configuration":"- Set kext DEBUG configuration",
                    "- Set HidePicker configuration":"- Set HidePicker configuration",
                    "- Set Disable SIP configuration":"- Set Disable SIP configuration",
                    "- Set Disable SecureBootModel configuration":"- Set Disable SecureBootModel configuration",
                    "- Set Vault configuration":"- Set Vault configuration",
                    "- Set FireWire Boot configuration":"- Set FireWire Boot configuration",
                    "- Set NVMe Boot configuration":"- Set NVMe Boot configuration",
                    "- Set Wake on WLAN configuration":"- Set Wake on WLAN configuration",
                    "- Set Disable Thunderbolt configuration":"- Set Disable Thunderbolt configuration",
                    "- Forcing SurPlus override configuration":"- Forcing SurPlus override configuration",
                    "- Set Moderate SMBIOS Patching configuration":"- Set Moderate SMBIOS Patching configuration",
                    "- Unknown SMBIOS arg passed:":"- Unknown SMBIOS arg passed:",
                    "- Building for natively supported model":"- Building for natively supported model"
                    }
        elif self.language_point==0:
            trans={"Set Validation Mode":"设置验证模式",
                    "Set System Volume patching":"设置系统卷补丁",
                    "- Running from Installer Sandbox, blocking OS updaters":"- 从安装程序沙箱运行，阻止系统更新程序",
                    "Set System Volume unpatching":"设置系统卷取消补丁",
                    "Set Auto patching":"设置自动补丁",
                    "Preparing host for macOS update":"正在准备主机进行 macOS 更新",
                    "No update staged, skipping":"没有暂存的更新，跳过",
                    "Preparing for update to":"正在准备更新到",
                    "Another instance of OS caching is running, exiting":"另一个系统缓存实例正在运行，退出",
                    "Cleaning /Library/Extensions":"正在清理 /Library/Extensions",
                    "- Failed to load plist for":"- 无法加载 plist 文件:",
                    "- Removing":"- 正在移除",
                    "Set OpenCore Build":"设置 OpenCore 构建",
                    "- Using custom model:":"- 使用自定义模型:",
                    "Your model is not supported by this patcher for running unsupported OSes!\n\nIf you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.":"您的模型不支持此补丁程序运行不受支持的操作系统!\n\n如果您计划为另一台机器创建 USB，请在菜单中选择\"更改模型\"选项。",
                    "- Using detected model:":"- 使用检测到的模型:",
                    "- Set verbose configuration":"- 设置详细配置",
                    "- Set OpenCore DEBUG configuration":"- 设置 OpenCore DEBUG 配置",
                    "- Set kext DEBUG configuration":"- 设置 kext DEBUG 配置",
                    "- Set HidePicker configuration":"- 设置 HidePicker 配置",
                    "- Set Disable SIP configuration":"- 设置禁用 SIP 配置",
                    "- Set Disable SecureBootModel configuration":"- 设置禁用 SecureBootModel 配置",
                    "- Set Vault configuration":"- 设置 Vault 配置",
                    "- Set FireWire Boot configuration":"- 设置 FireWire 启动配置",
                    "- Set NVMe Boot configuration":"- 设置 NVMe 启动配置",
                    "- Set Wake on WLAN configuration":"- 设置 WLAN 唤醒配置",
                    "- Set Disable Thunderbolt configuration":"- 设置禁用 Thunderbolt 配置",
                    "- Forcing SurPlus override configuration":"- 强制 SurPlus 覆盖配置",
                    "- Set Moderate SMBIOS Patching configuration":"- 设置适度 SMBIOS 补丁配置",
                    "- Unknown SMBIOS arg passed:":"- 传递了未知的 SMBIOS 参数:",
                    "- Building for natively supported model":"- 为原生支持的模型构建"
                    }
        return trans
    
   
    
    def defaults(self):
        if self.language_point==1:
            trans={
                "Error: Unable to read global settings file":"Error: Unable to read global settings file",
                "Global settings type mismatch for":"Global settings type mismatch for",
                "vs":"vs",
                "Removing":"Removing",
                "from global settings":"from global settings",
                "Setting":"Setting",
                "to":"to"
            }
        elif self.language_point==0:
            trans={
                "Error: Unable to read global settings file":"错误: 无法读取全局设置文件",
                "Global settings type mismatch for":"全局设置类型不匹配",
                "vs":"与",
                "Removing":"正在移除",
                "from global settings":"从全局设置中",
                "Setting":"正在设置",
                "to":"为"
            }
        return trans
    
    def generate_smbios(self):
        if self.language_point==1:
            trans={
                "- Failed to find FirmwareFeatures, falling back on defaults":"- Failed to find FirmwareFeatures, falling back on defaults"
            }
        elif self.language_point==0:
            trans={
                "- Failed to find FirmwareFeatures, falling back on defaults":"- 找不到 FirmwareFeatures，回退到默认值"
            }
        return trans
    
    def global_settings(self):
        if self.language_point==1:
            trans={
                "Error: Unable to read global settings file":"Error: Unable to read global settings file",
                "Failed to write to global settings":"Failed to write to global settings",
                "Failed to write to global settings file":"Failed to write to global settings file",
                "Permission error: Unable to write to global settings file":"Permission error: Unable to write to global settings file",
                "Error: Unable to delete defaults plist":"Error: Unable to delete defaults plist"
            }
        elif self.language_point==0:
            trans={
                "Error: Unable to read global settings file":"错误: 无法读取全局设置文件",
                "Failed to write to global settings":"无法写入全局设置",
                "Failed to write to global settings file":"无法写入全局设置文件",
                "Permission error: Unable to write to global settings file":"权限错误: 无法写入全局设置文件",
                "Error: Unable to delete defaults plist":"错误: 无法删除默认设置 plist"
            }
        return trans
    
    def install(self):
        if self.language_point==1:
            trans={
                "Mounting partition:":"Mounting partition:",
                "Mount failed":"Mount failed",
                "EFI failed to mount!":"EFI failed to mount!",
                "Removing preexisting EFI/OC folder":"Removing preexisting EFI/OC folder",
                "Removing preexisting System folder":"Removing preexisting System folder",
                "Removing preexisting boot.efi":"Removing preexisting boot.efi",
                "Copying OpenCore onto EFI partition":"Copying OpenCore onto EFI partition",
                "Converting Bootstrap to BOOTx64.efi":"Converting Bootstrap to BOOTx64.efi",
                "Adding SD Card icon":"Adding SD Card icon",
                "Adding SSD icon":"Adding SSD icon",
                "Adding External USB Drive icon":"Adding External USB Drive icon",
                "Adding Internal Drive icon":"Adding Internal Drive icon",
                "Cleaning install location":"Cleaning install location",
                "Unmounting EFI partition":"Unmounting EFI partition",
                "OpenCore transfer complete":"OpenCore transfer complete"
            }
        elif self.language_point==0:
            trans={
                "Mounting partition:":"正在挂载分区:",
                "Mount failed":"挂载失败",
                "EFI failed to mount!":"EFI 挂载失败!",
                "Removing preexisting EFI/OC folder":"正在移除已存在的 EFI/OC 文件夹",
                "Removing preexisting System folder":"正在移除已存在的 System 文件夹",
                "Removing preexisting boot.efi":"正在移除已存在的 boot.efi",
                "Copying OpenCore onto EFI partition":"正在将 OpenCore 复制到 EFI 分区",
                "Converting Bootstrap to BOOTx64.efi":"正在将 Bootstrap 转换为 BOOTx64.efi",
                "Adding SD Card icon":"正在添加 SD 卡图标",
                "Adding SSD icon":"正在添加 SSD 图标",
                "Adding External USB Drive icon":"正在添加外部 USB 驱动器图标",
                "Adding Internal Drive icon":"正在添加内部驱动器图标",
                "Cleaning install location":"正在清理安装位置",
                "Unmounting EFI partition":"正在卸载 EFI 分区",
                "OpenCore transfer complete":"OpenCore 传输完成"
            }
        return trans
    
    def integrity_verification(self):
        if self.language_point==1:
            trans={
                "File":"File",
                "does not exist":"does not exist",
                "is not a file":"is not a file",
                "Chunk":"Chunk",
                "checksum status FAIL: chunk sum":"checksum status FAIL: chunk sum",
                "calculated sum":"calculated sum"
            }
        elif self.language_point==0:
            trans={
                "File":"文件",
                "does not exist":"不存在",
                "is not a file":"不是文件",
                "Chunk":"分块",
                "checksum status FAIL: chunk sum":"校验和状态失败: 分块和",
                "calculated sum":"计算和"
            }
        return trans
    
    def gui_KDK_download(self):
        if self.language_point==1:
            trans={
                "Fetching KDKs":"Fetching KDKs",
                "Choose KDK Version":"Choose KDK Version",
                "Choose KDKs":"Choose KDKs",
                "Cannot find any KDKs on Github":"Cannot find any KDKs on Github",
                "Failed to download KDKs Catalog from Hackdoc":"Failed to download KDKs Catalog from Hackdoc",
                "Download":"Download",
                "Choose KDKs":"Choose KDKs",
                "Copy Link":"Copy Link",
                "Copy KDK Download Link":"Copy KDK Download Link",
                "Return to Main Menu":"Return to Main Menu",
                "Show Older/Beta Versions":"Show Older/Beta Versions",
                "Download link copied to clipboard":"Download link copied to clipboard",
                "Tahoe Beta":"Tahoe Beta",
                "Sequoia":"Sequoia",
                "Sonoma":"Sonoma",
                "Ventura":"Ventura"
            }
        elif self.language_point==0:
            trans={
                "Fetching KDKs":"正在获取 KDK",
                "Choose KDK Version":"选择 KDK 版本",
                "Choose KDKs":"选择 KDK",
                "Cannot find any KDKs on Github":"在 Github 上找不到任何 KDK",
                "Failed to download KDKs Catalog from Hackdoc":"无法从 Hackdoc 下载 KDK 目录",
                "Download":"下载",
                "Choose KDKs":"选择 KDK",
                "Copy Link":"复制链接",
                "Copy KDK Download Link":"复制 KDK 下载链接",
                "Return to Main Menu":"返回主菜单",
                "Show Older/Beta Versions":"显示旧版本/测试版",
                "Download link copied to clipboard":"下载链接已复制到剪贴板",
                "Tahoe Beta":"Tahoe 测试版",
                "Sequoia":"Sequoia",
                "Sonoma":"Sonoma",
                "Ventura":"Ventura"
            }
        return trans
    
    def gui_about(self):
        if self.language_point==1:
            trans={
                "About":"About",
                "OCLP-R":"OCLP-R",
                "Version":"Version",
                "I just wanted to relax, but I got addicted to it.":"I just wanted to relax, but I got addicted to it.",
                "I just wanted to protect the last hackintosh.":"I just wanted to protect the last hackintosh."
            }
        elif self.language_point==0:
            trans={
                "About":"关于",
                "OCLP-R":"OCLP-R",
                "Version":"版本",
                "I just wanted to relax, but I got addicted to it.":"我只是想放松一下，但我上瘾了。",
                "I just wanted to protect the last hackintosh.":"我只是想保护最后一个黑苹果。"
            }
        return trans
    
    def gui_build(self):
        if self.language_point==1:
            trans={
                "Build and Install OpenCore":"Build and Install OpenCore",
                "Model:":"Model:",
                "🔩 Install OpenCore":"🔩 Install OpenCore",
                "Return to Main Menu":"Return to Main Menu",
                "An error occurred while building OpenCore":"An error occurred while building OpenCore",
                "Error building OpenCore":"Error building OpenCore",
                "Would you like to install OpenCore now?":"Would you like to install OpenCore now?",
                "Finished building your OpenCore configuration!":"Finished building your OpenCore configuration!",
                "Install to disk":"Install to disk",
                "View build log":"View build log",
                "An internal error occurred while building:\n":"An internal error occurred while building:\n",
                "If you continue to see this error, delete the following file and restart the application:":"If you continue to see this error, delete the following file and restart the application:",
                "Path: /Users/Shared/.com.hackdoc.oclp-r.plist":"Path: /Users/Shared/.com.hackdoc.oclp-r.plist"
            }
        elif self.language_point==0:
            trans={
                "Build and Install OpenCore":"构建并安装 OpenCore",
                "Model:":"机型:",
                "🔩 Install OpenCore":"🔩 安装 OpenCore",
                "Return to Main Menu":"返回主菜单",
                "An error occurred while building OpenCore":"构建 OpenCore 时发生错误",
                "Error building OpenCore":"构建 OpenCore 错误",
                "Would you like to install OpenCore now?":"现在要安装 OpenCore 吗？",
                "Finished building your OpenCore configuration!":"已完成构建您的 OpenCore 配置！",
                "Install to disk":"安装到磁盘",
                "View build log":"查看构建日志",
                "An internal error occurred while building:\n":"构建时发生内部错误:\n",
                "If you continue to see this error, delete the following file and restart the application:":"如果您继续看到此错误，请删除以下文件并重新启动应用程序:",
                "Path: /Users/Shared/.com.hackdoc.oclp-r.plist":"路径: /Users/Shared/.com.hackdoc.oclp-r.plist"
            }
        return trans
    
    def gui_cache_os_update(self):
        if self.language_point==1:
            trans={
                "Preparing for macOS Software Update":"Preparing for macOS Software Update",
                "This may take a few minutes.":"This may take a few minutes.",
                "OCLP-R has detected that a macOS update is being downloaded:":"OCLP-R has detected that a macOS update is being downloaded:",
                "The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.":"The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.",
                "This may take a few minutes, the patcher will exit when it is done.":"This may take a few minutes, the patcher will exit when it is done.",
                "OCLP-R":"OCLP-R",
                "&Ok":"&Ok",
                "&Cancel":"&Cancel",
                "User cancelled OS caching":"User cancelled OS caching"
            }
        elif self.language_point==0:
            trans={
                "Preparing for macOS Software Update":"正在准备 macOS 软件更新",
                "This may take a few minutes.":"这可能需要几分钟时间。",
                "OCLP-R has detected that a macOS update is being downloaded:":"OCLP-R 检测到正在下载 macOS 更新:",
                "The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.":"补丁程序需要为更新准备系统，并将下载更新后可能需要的任何其他资源。",
                "This may take a few minutes, the patcher will exit when it is done.":"这可能需要几分钟时间，补丁程序完成后将退出。",
                "OCLP-R":"OCLP-R",
                "&Ok":"&确定",
                "&Cancel":"&取消",
                "User cancelled OS caching":"用户取消了系统缓存"
            }
        return trans
    
    def gui_download(self):
        if self.language_point==1:
            trans={
                "Downloading: ":"Downloading: ",
                "Preparing download":"Preparing download",
                "Cancel":"Cancel",
                "Download failed: ":"Download failed: ",
                "Are you sure you want to cancel the download?":"Are you sure you want to cancel the download?",
                "Cancel Download":"Cancel Download",
                "Cancelling download, please wait...":"Cancelling download, please wait...",
                "Cancelling":"Cancelling",
                "User cancelled download":"User cancelled download"
            }
        elif self.language_point==0:
            trans={
                "Downloading: ":"正在下载: ",
                "Preparing download":"正在准备下载",
                "Cancel":"取消",
                "Download failed: ":"下载失败: ",
                "Are you sure you want to cancel the download?":"您确定要取消下载吗？",
                "Cancel Download":"取消下载",
                "Cancelling download, please wait...":"正在取消下载，请稍候...",
                "Cancelling":"取消中",
                "User cancelled download":"用户取消了下载"
            }
        return trans
    
    def gui_entry(self):
        if self.language_point==1:
            trans={
                "Entry point set:":"Entry point set:",
                "Cleaning up wxPython GUI":"Cleaning up wxPython GUI"
            }
        elif self.language_point==0:
            trans={
                "Entry point set:":"入口点已设置:",
                "Cleaning up wxPython GUI":"正在清理 wxPython GUI"
            }
        return trans
    
    def gui_help(self):
        if self.language_point==1:
            trans={
                "Patcher Resources":"Patcher Resources",
                "Following resources are available:":"Following resources are available:",
                "Official Guide":"Official Guide",
                "Official Phone Support":"Official Phone Support",
                "Community Discord Server":"Community Discord Server",
                "Return to Main Menu":"Return to Main Menu"
            }
        elif self.language_point==0:
            trans={
                "Patcher Resources":"补丁程序资源",
                "Following resources are available:":"以下资源可用:",
                "Official Guide":"官方指南",
                "Official Phone Support":"官方电话支持",
                "Community Discord Server":"社区 Discord 服务器",
                "Return to Main Menu":"返回主菜单"
            }
        return trans
    
    def gui_install_oc(self):
        if self.language_point==1:
            trans={
                "Install OpenCore":"Install OpenCore",
                "Fetching information on local disks...":"Fetching information on local disks...",
                "Select disk to install OpenCore onto:":"Select disk to install OpenCore onto:",
                "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT":"Missing disks? Ensure they're FAT32 or formatted as GUID/GPT",
                "Search for disks again":"Search for disks again",
                "Return to Main Menu":"Return to Main Menu",
                "Note: Blue represent the disk OpenCore is currently booted from":"Note: Blue represent the disk OpenCore is currently booted from",
                "Failed to find any applicable disks":"Failed to find any applicable disks",
                "Volumes on ":"Volumes on ",
                "Installing OpenCore to ":"Installing OpenCore to ",
                "OpenCore has finished installing to disk.\n\nWould you like to update your root patches next?":"OpenCore has finished installing to disk.\n\nWould you like to update your root patches next?",
                "Success":"Success",
                "OpenCore has finished installing to disk.\n\nYou will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.\n\nWould you like to reboot?":"OpenCore has finished installing to disk.\n\nYou will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.\n\nWould you like to reboot?",
                "OpenCore has finished installing to disk.\n\nYou can eject the drive, insert it into the ":"OpenCore has finished installing to disk.\n\nYou can eject the drive, insert it into the ",
                ", reboot, hold the Option key and select OpenCore/Boot EFI's option.":", reboot, hold the Option key and select OpenCore/Boot EFI's option.",
                "An internal error occurred while installing:\n":"An internal error occurred while installing:\n"
            }
        elif self.language_point==0:
            trans={
                "Install OpenCore":"安装 OpenCore",
                "Fetching information on local disks...":"正在获取本地磁盘信息...",
                "Select disk to install OpenCore onto:":"选择要安装 OpenCore 的磁盘:",
                "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT":"缺少磁盘？请确保它们是 FAT32 格式或格式化为 GUID/GPT",
                "Search for disks again":"再次搜索磁盘",
                "Return to Main Menu":"返回主菜单",
                "Note: Blue represent the disk OpenCore is currently booted from":"注: 蓝色代表当前引导 OpenCore 的磁盘",
                "Failed to find any applicable disks":"找不到任何适用的磁盘",
                "Volumes on ":"上的卷 ",
                "Installing OpenCore to ":"正在安装 OpenCore 到 ",
                "OpenCore has finished installing to disk.\n\nWould you like to update your root patches next?":"OpenCore 已完成安装到磁盘。\n\n接下来要更新您的根补丁吗？",
                "Success":"成功",
                "OpenCore has finished installing to disk.\n\nYou will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.\n\nWould you like to reboot?":"OpenCore 已完成安装到磁盘。\n\n您需要重启并按住 Option 键，然后选择 OpenCore/Boot EFI 选项。\n\n要重启吗？",
                "OpenCore has finished installing to disk.\n\nYou can eject the drive, insert it into the ":"OpenCore 已完成安装到磁盘。\n\n您可以弹出驱动器，将其插入 ",
                ", reboot, hold the Option key and select OpenCore/Boot EFI's option.":", 重启，按住 Option 键，然后选择 OpenCore/Boot EFI 选项。",
                "An internal error occurred while installing:\n":"安装过程中发生内部错误:\n"
            }
        return trans
    
    def gui_macos_installer_download(self):
        if self.language_point==1:
            trans={
                "Create macOS Installer":"Create macOS Installer",
                "Download macOS Installer":"Download macOS Installer",
                "Use existing macOS Installer":"Use existing macOS Installer",
                "Download DMGs":"Download DMGs",
                "Return to Main Menu":"Return to Main Menu",
                "Finding Available Software":"Finding Available Software",
                "Finding Available DMG":"Finding Available DMG",
                "Failed to download Installer Catalog from Apple":"Failed to download Installer Catalog from Apple",
                "Select DMGs from SimpleHac":"Select DMGs from SimpleHac",
                "Select DMGs":"Select DMGs",
                "Failed to download dmgs from SimpleHac":"Failed to download dmgs from SimpleHac",
                "Fetching installer catalog: {seed_type}":"Fetching installer catalog: {seed_type}",
                "JSON data:":"JSON data:",
                "Download":"Download",
                "Copy Link":"Copy Link",
                "Show Older/Beta Versions":"Show Older/Beta Versions",
                "Download link copied to clipboard":"Download link copied to clipboard",
                "Download DMG":"Download DMG",
                "Potential Issues":"Potential Issues",
                "View Github Issue":"View Github Issue",
                "Download Anyways":"Download Anyways",
                "Cancel":"Cancel",
                "Insufficient Space":"Insufficient Space",
                "Validating macOS Installer":"Validating macOS Installer",
                "Validating chunk 0 of 0":"Validating chunk 0 of 0",
                "Chunklist validation failed: Hash mismatch on {chunk_obj.current_chunk}":"Chunklist validation failed: Hash mismatch on {chunk_obj.current_chunk}",
                "This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)":"This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)",
                "Corrupted Installer!":"Corrupted Installer!",
                "Extracting macOS Installer":"Extracting macOS Installer",
                "May take a few minutes...":"May take a few minutes...",
                "Successfully extracted macOS installer":"Successfully extracted macOS installer",
                "Failed to extract macOS installer":"Failed to extract macOS installer",
                "An error occurred while extracting the macOS installer. Could be due to a corrupted installer":"An error occurred while extracting the macOS installer. Could be due to a corrupted installer",
                "Finished extracting the installer, would you like to continue and create a macOS installer?":"Finished extracting the installer, would you like to continue and create a macOS installer?",
                "Create macOS Installer?":"Create macOS Installer?"
            }
        elif self.language_point==0:
            trans={
                "Create macOS Installer":"创建 macOS 安装程序",
                "Download macOS Installer":"下载 macOS 安装程序",
                "Use existing macOS Installer":"使用现有 macOS 安装程序",
                "Download DMGs":"下载 DMG",
                "Return to Main Menu":"返回主菜单",
                "Finding Available Software":"查找可用软件",
                "Finding Available DMG":"查找可用 DMG",
                "Failed to download Installer Catalog from Apple":"无法从 Apple 下载安装程序目录",
                "Select DMGs from SimpleHac":"从 SimpleHac 选择 DMG",
                "Select DMGs":"选择 DMG",
                "Failed to download dmgs from SimpleHac":"无法从 SimpleHac 下载 dmgs",
                "Fetching installer catalog: {seed_type}":"正在获取安装程序目录: {seed_type}",
                "JSON data:":"JSON数据:",
                "Download":"下载",
                "Copy Link":"复制链接",
                "Show Older/Beta Versions":"显示旧版本/测试版",
                "Download link copied to clipboard":"下载链接已复制到剪贴板",
                "Download DMG":"下载 DMG",
                "Potential Issues":"潜在问题",
                "View Github Issue":"查看 Github 问题",
                "Download Anyways":"仍然下载",
                "Cancel":"取消",
                "Insufficient Space":"空间不足",
                "Validating macOS Installer":"正在验证 macOS 安装程序",
                "Validating chunk 0 of 0":"正在验证分块 0/0",
                "Chunklist validation failed: Hash mismatch on {chunk_obj.current_chunk}":"分块列表验证失败：{chunk_obj.current_chunk} 上的哈希不匹配",
                "This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)":"这通常发生在不稳定连接（如 WiFi 或蜂窝网络）上下载时。\n\n请尝试在稳定连接（如以太网）上重新下载",
                "Corrupted Installer!":"损坏的安装程序！",
                "Extracting macOS Installer":"正在提取 macOS 安装程序",
                "May take a few minutes...":"可能需要几分钟...",
                "Successfully extracted macOS installer":"成功提取 macOS 安装程序",
                "Failed to extract macOS installer":"提取 macOS 安装程序失败",
                "An error occurred while extracting the macOS installer. Could be due to a corrupted installer":"提取 macOS 安装程序时发生错误。可能是由于损坏的安装程序",
                "Finished extracting the installer, would you like to continue and create a macOS installer?":"安装程序提取完成，是否要继续创建 macOS 安装程序？",
                "Create macOS Installer?":"创建 macOS 安装程序？"
            }
        return trans
    
    def gui_macos_installer_flash(self):
        if self.language_point==1:
            trans={
                "Fetching local macOS Installers":"Fetching local macOS Installers",
                "Select local macOS Installer":"Select local macOS Installer",
                "No installers found in '/Applications'":"No installers found in '/Applications'",
                "Return to Main Menu":"Return to Main Menu",
                "Fetching information on local disks":"Fetching information on local disks",
                "Select local disk":"Select local disk",
                "Selected USB will be erased, please backup any data":"Selected USB will be erased, please backup any data",
                "No disks found":"No disks found",
                "Search for disks again":"Search for disks again",
                "Are you sure you want to erase '{disk['name']}'?\nAll data will be lost, this cannot be undone.":"Are you sure you want to erase '{disk['name']}'?\nAll data will be lost, this cannot be undone.",
                "Confirmation":"Confirmation",
                "Creating Installer: {installer['Short Name']}":"Creating Installer: {installer['Short Name']}",
                "Creating macOS installers can take 30min+ on slower USB drives.":"Creating macOS installers can take 30min+ on slower USB drives.",
                "We will notify you when the installer is ready.":"We will notify you when the installer is ready.",
                "Bytes Written: 0.00 MB":"Bytes Written: 0.00 MB",
                "Failed to prepare resources, cannot continue.":"Failed to prepare resources, cannot continue.",
                "Error":"Error",
                "Validating Installer Integrity...":"Validating Installer Integrity...",
                "Failed to validate installer, cannot continue.\n This can generally happen due to a faulty USB drive, as flashing is an intensive process that can trigger hardware faults not normally seen. \n\n{error_message}":"Failed to validate installer, cannot continue.\n This can generally happen due to a faulty USB drive, as flashing is an intensive process that can trigger hardware faults not normally seen. \n\n{error_message}",
                "Corrupted Installer!":"Corrupted Installer!",
                "Successfully created the macOS installer!":"Successfully created the macOS installer!",
                "If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"If you want to install OpenCore to this USB, you will need to change the Target Model in settings",
                "Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}":"Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}"
            }
        elif self.language_point==0:
            trans={
                "Fetching local macOS Installers":"正在获取本地 macOS 安装程序",
                "Select local macOS Installer":"选择本地 macOS 安装程序",
                "No installers found in '/Applications'":"在 '/Applications' 中未找到安装程序",
                "Return to Main Menu":"返回主菜单",
                "Fetching information on local disks":"正在获取本地磁盘信息",
                "Select local disk":"选择本地磁盘",
                "Selected USB will be erased, please backup any data":"选中的 USB 将被擦除，请备份所有数据",
                "No disks found":"未找到磁盘",
                "Search for disks again":"再次搜索磁盘",
                "Are you sure you want to erase '{disk['name']}'?\nAll data will be lost, this cannot be undone.":"您确定要擦除 '{disk['name']}' 吗？\n所有数据将丢失，此操作无法撤销。",
                "Confirmation":"确认",
                "Creating Installer: {installer['Short Name']}":"正在创建安装程序: {installer['Short Name']}",
                "Creating macOS installers can take 30min+ on slower USB drives.":"在较慢的 USB 驱动器上创建 macOS 安装程序可能需要 30 分钟以上。",
                "We will notify you when the installer is ready.":"安装程序准备就绪时我们会通知您。",
                "Bytes Written: 0.00 MB":"已写入字节: 0.00 MB",
                "Failed to prepare resources, cannot continue.":"准备资源失败，无法继续。",
                "Error":"错误",
                "Validating Installer Integrity...":"正在验证安装程序完整性...",
                "Failed to validate installer, cannot continue.\n This can generally happen due to a faulty USB drive, as flashing is an intensive process that can trigger hardware faults not normally seen. \n\n{error_message}":"验证安装程序失败，无法继续。\n这通常是由于 USB 驱动器故障导致的，因为刷写是一个密集型过程，可能会触发通常看不到的硬件故障。\n\n{error_message}",
                "Corrupted Installer!":"损坏的安装程序！",
                "Successfully created the macOS installer!":"成功创建 macOS 安装程序！",
                "If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"如果您想将 OpenCore 安装到此 USB，您需要在设置中更改目标机型",
                "Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}":"创建 macOS 安装程序失败\n\n输出: {output}\n\n错误: {error}"
            }
        return trans
    
    def gui_main_menu(self):
        if self.language_point==1:
            trans={
                "Build and Install OpenCore":"Build and Install OpenCore",
                "Prepares provided drive to be able\nto boot unsupported OSes.\nUse on installers or internal drives.":"Prepares provided drive to be able\nto boot unsupported OSes.\nUse on installers or internal drives.",
                "Create macOS Installer":"Create macOS Installer",
                "Download and flash a macOS\nInstaller for your system.":"Download and flash a macOS\nInstaller for your system.",
                "KDK Download":"KDK Download",
                "Provide KDK download\nfor your system.(macOS 13 with OCLP)":"Provide KDK download\nfor your system.(macOS 13 with OCLP)",
                "⚙️ Settings":"⚙️ Settings",
                "Post-Install Root Patch":"Post-Install Root Patch",
                "Installs hardware drivers and\npatches for your system after\ninstalling a new version of macOS.":"Installs hardware drivers and\npatches for your system after\ninstalling a new version of macOS.",
                "MetalLib Download":"MetalLib Download",
                "Provide MetalLib for your system.\nThis is required for Metal3802 devices.\n(macOS 15+ Needs!)":"Provide MetalLib for your system.\nThis is required for Metal3802 devices.\n(macOS 15+ Needs!)",
                "Support":"Support",
                "Resources for OpenCore Legacy\nPatcher.":"Resources for OpenCore Legacy\nPatcher.",
                "Unsupported Configuration Detected!":"Unsupported Configuration Detected!",
                "We found you are currently booting OpenCore built for a different unit: {self.constants.computer.build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.":"We found you are currently booting OpenCore built for a different unit: {self.constants.computer.build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.",
                "Update successful!":"Update successful!",
                "OCLP-R has been updated to the latest version: {self.constants.patcher_version}\n\nWould you like to update OpenCore and your root volume patches?":"OCLP-R has been updated to the latest version: {self.constants.patcher_version}\n\nWould you like to update OpenCore and your root volume patches?",
                "A new version of OCLP-R is available!":"A new version of OCLP-R is available!",
                "OCLP-R {oclp_version} is now available - You have {self.constants.patcher_version}{' (Nightly)' if not self.constants.commit_info[0].startswith('refs/tags') else ''}. Would you like to update?":"OCLP-R {oclp_version} is now available - You have {self.constants.patcher_version}{' (Nightly)' if not self.constants.commit_info[0].startswith('refs/tags') else ''}. Would you like to update?",
                "Unable to fetch changelog\n\nPlease check the Github page for more information about this release.":"Unable to fetch changelog\n\nPlease check the Github page for more information about this release.",
                "Dismiss":"Dismiss",
                "View on GitHub":"View on GitHub",
                "Download and Install":"Download and Install"
            }
        elif self.language_point==0:
            trans={
                "Build and Install OpenCore":"构建并安装 OpenCore",
                "Prepares provided drive to be able\nto boot unsupported OSes.\nUse on installers or internal drives.":"准备提供的驱动器以启动不支持的操作系统。\n用于安装程序或内部驱动器。",
                "Create macOS Installer":"创建 macOS 安装程序",
                "Download and flash a macOS\nInstaller for your system.":"下载并刷写 macOS\n安装程序到您的系统。",
                "KDK Download":"下载 KDK",
                "Provide KDK download\nfor your system.(macOS 13 with OCLP)":"为您的系统提供 KDK 下载。\n(macOS 13 配合 OCLP 使用)",
                "⚙️ Settings":"⚙️ 设置",
                "Post-Install Root Patch":"安装后根补丁",
                "Installs hardware drivers and\npatches for your system after\ninstalling a new version of macOS.":"在安装新版本的 macOS 后\n为您的系统安装硬件驱动程序和补丁。",
                "MetalLib Download":"下载 MetalLib",
                "Provide MetalLib for your system.\nThis is required for Metal3802 devices.\n(macOS 15+ Needs!)":"为您的系统提供 MetalLib。\n这是 Metal3802 设备所必需的。\n(macOS 15+ 需要！)",
                "Support":"支持",
                "Resources for OpenCore Legacy\nPatcher.":"OpenCore Legacy Patcher\n资源。",
                "Unsupported Configuration Detected!":"检测到不支持的配置！",
                "We found you are currently booting OpenCore built for a different unit: {self.constants.computer.build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.":"我们发现您当前正在引导为不同设备构建的 OpenCore：{self.constants.computer.build_model}\n\n我们构建的配置是为匹配单个设备的，不能与不同的 Mac 混合使用或重复使用。\n\n请构建并安装一个新的 OpenCore 配置，然后重启您的 Mac。",
                "Update successful!":"更新成功！",
                "OCLP-R has been updated to the latest version: {self.constants.patcher_version}\n\nWould you like to update OpenCore and your root volume patches?":"OCLP-R 已更新到最新版本：{self.constants.patcher_version}\n\n您是否要更新 OpenCore 和根卷补丁？",
                "A new version of OCLP-R is available!":"OCLP-R 有新版本可用！",
                "OCLP-R {oclp_version} is now available - You have {self.constants.patcher_version}{' (Nightly)' if not self.constants.commit_info[0].startswith('refs/tags') else ''}. Would you like to update?":"OCLP-R {oclp_version} 现已可用 - 您当前版本是 {self.constants.patcher_version}{' (Nightly)' if not self.constants.commit_info[0].startswith('refs/tags') else ''}。您是否要更新？",
                "Unable to fetch changelog\n\nPlease check the Github page for more information about this release.":"无法获取更新日志\n\n请查看 Github 页面了解有关此版本的更多信息。",
                "Dismiss":"关闭",
                "View on GitHub":"在 GitHub 上查看",
                "Download and Install":"下载并安装"
            }
        return trans
    
    def gui_metallib_download(self):
        if self.language_point==1:
            trans={
                "Fetching Metallibs":"Fetching Metallibs",
                "Choose Metallib Version":"Choose Metallib Version",
                "Choose Metallib":"Choose Metallib",
                "Failed to download Metallib message from Github":"Failed to download Metallib message from Github",
                "Download":"Download",
                "Copy Link":"Copy Link",
                "Download Selected Metallib":"Download Selected Metallib",
                "Copy Metallib Download Link":"Copy Metallib Download Link",
                "Return to Main Menu":"Return to Main Menu",
                "Show Older/Beta Version":"Show Older/Beta Version",
                "Download link copied to clipboard":"Download link copied to clipboard",
                "Fetch Metal Libraries Error: {e}":"Fetch Metal Libraries Error: {e}",
                "Error":"Error"
            }
        elif self.language_point==0:
            trans={
                "Fetching Metallibs":"正在获取 Metallib",
                "Choose Metallib Version":"选择 Metallib 版本",
                "Choose Metallib":"选择 Metallib",
                "Failed to download Metallib message from Github":"无法从 Github 下载 Metallib 消息",
                "Download":"下载",
                "Copy Link":"复制链接",
                "Download Selected Metallib":"下载选定的 Metallib",
                "Copy Metallib Download Link":"复制 Metallib 下载链接",
                "Return to Main Menu":"返回主菜单",
                "Show Older/Beta Version":"显示旧版本/测试版",
                "Download link copied to clipboard":"下载链接已复制到剪贴板",
                "Fetch Metal Libraries Error: {e}":"获取 Metal 库时出错: {e}",
                "Error":"错误"
            }
        return trans
    
    def gui_settings(self):
        if self.language_point==1:
            trans={
                "Target Model":"Target Model",
                "Host Model":"Host Model",
                "Overrides Mac Model the Patcher will build for.":"Overrides Mac Model the Patcher will build for.",
                "Build":"Build",
                "General":"General",
                "FireWire Booting":"FireWire Booting",
                "Enable booting macOS from\nFireWire drives.":"Enable booting macOS from\nFireWire drives.",
                "XHCI Booting":"XHCI Booting",
                "Enable booting macOS from add-in\nUSB 3.0 expansion cards on systems\nwithout native support.":"Enable booting macOS from add-in\nUSB 3.0 expansion cards on systems\nwithout native support.",
                "NVMe Booting":"NVMe Booting",
                "Enable booting macOS from NVMe\ndrives on systems without native\nsupport.\nNote: Requires Firmware support\nfor OpenCore to load from NVMe.":"Enable booting macOS from NVMe\ndrives on systems without native\nsupport.\nNote: Requires Firmware support\nfor OpenCore to load from NVMe.",
                "OpenCore Vaulting":"OpenCore Vaulting",
                "Digitally sign OpenCore to prevent\ntampering or corruption.":"Digitally sign OpenCore to prevent\ntampering or corruption.",
                "Show OpenCore Boot Picker":"Show OpenCore Boot Picker",
                "When disabled, users can hold ESC to\nshow picker in the firmware.":"When disabled, users can hold ESC to\nshow picker in the firmware.",
                "Boot Picker Timeout":"Boot Picker Timeout",
                "Timeout before boot picker selects default\nentry in seconds.\nSet to 0 for no timeout.":"Timeout before boot picker selects default\nentry in seconds.\nSet to 0 for no timeout.",
                "MacPro3,1/Xserve2,1 Workaround":"MacPro3,1/Xserve2,1 Workaround",
                "Limits to 4 threads max on these units.\nRequired for macOS Sequoia and later.":"Limits to 4 threads max on these units.\nRequired for macOS Sequoia and later.",
                "Debug":"Debug",
                "Verbose":"Verbose",
                "Verbose output during boot.":"Verbose output during boot.",
                "Kext Debugging":"Kext Debugging",
                "Use DEBUG variants of kexts and\nenables additional kernel logging.":"Use DEBUG variants of kexts and\nenables additional kernel logging.",
                "OpenCore Debugging":"OpenCore Debugging",
                "Use DEBUG variant of OpenCore\nand enables additional logging.":"Use DEBUG variant of OpenCore\nand enables additional logging.",
                "Extras":"Extras",
                "General (Continued)":"General (Continued)",
                "Wake on WLAN":"Wake on WLAN",
                "Disabled by default due to\nperformance degradation\non some systems from wake.\nOnly applies to BCM943224, 331,\n360 and 3602 chipsets.":"Disabled by default due to\nperformance degradation\non some systems from wake.\nOnly applies to BCM943224, 331,\n360 and 3602 chipsets.",
                "Disable Thunderbolt":"Disable Thunderbolt",
                "For MacBookPro11,x with faulty\nPCHs that may crash sporadically.":"For MacBookPro11,x with faulty\nPCHs that may crash sporadically.",
                "Windows GMUX":"Windows GMUX",
                "Allow iGPU to be exposed in Windows\nfor dGPU-based MacBooks.":"Allow iGPU to be exposed in Windows\nfor dGPU-based MacBooks.",
                "Disable CPUFriend":"Disable CPUFriend",
                "Disables power management helper\nfor unsupported models.":"Disables power management helper\nfor unsupported models.",
                "Disable mediaanalysisd service":"Disable mediaanalysisd service",
                "For systems that are the primary iCloud\nPhoto Library host with a 3802-based GPU,\nthis may aid in prolonged idle stability.":"For systems that are the primary iCloud\nPhoto Library host with a 3802-based GPU,\nthis may aid in prolonged idle stability.",
                "Allow AppleALC Audio":"Allow AppleALC Audio",
                "Allow AppleALC to manage audio\nif applicable.\nOnly disable if your host lacks\na GOP ROM.":"Allow AppleALC to manage audio\nif applicable.\nOnly disable if your host lacks\na GOP ROM.",
                "NVRAM WriteFlash":"NVRAM WriteFlash",
                "Allow OpenCore to write to NVRAM.\nDisable on systems with faulty or\ndegraded NVRAM.":"Allow OpenCore to write to NVRAM.\nDisable on systems with faulty or\ndegraded NVRAM.",
                "3rd Party NVMe PM":"3rd Party NVMe PM",
                "Enable non-stock NVMe power\nmanagement in macOS.":"Enable non-stock NVMe power\nmanagement in macOS.",
                "3rd Party SATA PM":"3rd Party SATA PM",
                "Enable non-stock SATA power\nmanagement in macOS.":"Enable non-stock SATA power\nmanagement in macOS.",
                "APFS Trim":"APFS Trim",
                "Recommended for all users, however faulty\nSSDs may benefit from disabling this.":"Recommended for all users, however faulty\nSSDs may benefit from disabling this.",
                "Advanced":"Advanced",
                "Miscellaneous":"Miscellaneous",
                "Disable Firmware Throttling":"Disable Firmware Throttling",
                "Disables firmware-based throttling\ncaused by missing hardware.\nEx. Missing Display, Battery, etc.":"Disables firmware-based throttling\ncaused by missing hardware.\nEx. Missing Display, Battery, etc.",
                "Software DeMUX":"Software DeMUX",
                "Enable software based DeMUX\nfor MacBookPro8,2 and MacBookPro8,3.\nPrevents faulty dGPU from turning on.\nNote: Requires associated NVRAM arg:\n'gpu-power-prefs'.":"Enable software based DeMUX\nfor MacBookPro8,2 and MacBookPro8,3.\nPrevents faulty dGPU from turning on.\nNote: Requires associated NVRAM arg:\n'gpu-power-prefs'.",
                "FeatureUnlock":"FeatureUnlock",
                "Enabled":"Enabled",
                "Partial":"Partial",
                "Disabled":"Disabled",
                "Configure FeatureUnlock level.\nRecommend lowering if your system\nexperiences memory instability.":"Configure FeatureUnlock level.\nRecommend lowering if your system\nexperiences memory instability.",
                "Hibernation Work-around":"Hibernation Work-around",
                "Only load minimum EFI drivers\nto prevent hibernation issues.\nNote: This may break booting from\nexternal drives.":"Only load minimum EFI drivers\nto prevent hibernation issues.\nNote: This may break booting from\nexternal drives.",
                "Graphics":"Graphics",
                "AMD GOP Injection":"AMD GOP Injection",
                "Inject AMD GOP for boot screen\nsupport on PC GPUs.":"Inject AMD GOP for boot screen\nsupport on PC GPUs.",
                "Nvidia GOP Injection":"Nvidia GOP Injection",
                "Inject Nvidia Kepler GOP for boot\nscreen support on PC GPUs.":"Inject Nvidia Kepler GOP for boot\nscreen support on PC GPUs.",
                "Graphics Override":"Graphics Override",
                "None":"None",
                "Nvidia Kepler":"Nvidia Kepler",
                "AMD GCN":"AMD GCN",
                "AMD Polaris":"AMD Polaris",
                "AMD Lexa":"AMD Lexa",
                "AMD Navi":"AMD Navi",
                "Override detected/assumed GPU on\nsocketed MXM-based iMacs.":"Override detected/assumed GPU on\nsocketed MXM-based iMacs.",
                "Security":"Security",
                "Kernel Security":"Kernel Security",
                "Disable Library Validation":"Disable Library Validation",
                "Required for loading modified\nsystem files from root patching.":"Required for loading modified\nsystem files from root patching.",
                "Disable AMFI":"Disable AMFI",
                "Extended version of 'Disable\nLibrary Validation', required\nfor systems with deeper\nroot patches.":"Extended version of 'Disable\nLibrary Validation', required\nfor systems with deeper\nroot patches.",
                "Secure Boot Model":"Secure Boot Model",
                "Set Apple Secure Boot Model Identifier\nto matching T2 model if spoofing.\nNote: Incompatible with Root Patching.":"Set Apple Secure Boot Model Identifier\nto matching T2 model if spoofing.\nNote: Incompatible with Root Patching.",
                "System Integrity Protection":"System Integrity Protection",
                "SMBIOS":"SMBIOS",
                "Model Spoofing":"Model Spoofing",
                "SMBIOS Spoof Level":"SMBIOS Spoof Level",
                "None":"None",
                "Minimal":"Minimal",
                "Moderate":"Moderate",
                "Advanced":"Advanced",
                "Supported Levels:\n   - None: No spoofing.\n   - Minimal: Overrides Board ID.\n   - Moderate: Overrides Model.\n   - Advanced: Overrides Model and serial.":"Supported Levels:\n   - None: No spoofing.\n   - Minimal: Overrides Board ID.\n   - Moderate: Overrides Model.\n   - Advanced: Overrides Model and serial.",
                "SMBIOS Spoof Model":"SMBIOS Spoof Model",
                "Default":"Default",
                "Set Mac Model to spoof to.":"Set Mac Model to spoof to.",
                "Allow spoofing native Macs":"Allow spoofing native Macs",
                "Allow OpenCore to spoof natively\nsupported Macs.\nPrimarily used for enabling\nUniversal Control on unsupported Macs":"Allow OpenCore to spoof natively\nsupported Macs.\nPrimarily used for enabling\nUniversal Control on unsupported Macs",
                "Serial Spoofing":"Serial Spoofing",
                "Patch":"Patch",
                "Patch-General":"Patch-General",
                "TeraScale 2 Acceleration":"TeraScale 2 Acceleration",
                "Enable AMD TeraScale 2 GPU\nAcceleration on MacBookPro8,2 and\nMacBookPro8,3.\nBy default this is disabled due to\ncommon GPU failures on these models.":"Enable AMD TeraScale 2 GPU\nAcceleration on MacBookPro8,2 and\nMacBookPro8,3.\nBy default this is disabled due to\ncommon GPU failures on these models.",
                "Audio Patch choice":"Audio Patch choice",
                "AppleHDA":"AppleHDA",
                "VoodooHDA":"VoodooHDA",
                "   - AppleALC: AppleALC patch on Tahoe.\n   - VoodooHDA: VoodooHDA patch ,\n  on Monterey and newer.\n  Not recommended.":"   - AppleALC: AppleALC patch on Tahoe.\n   - VoodooHDA: VoodooHDA patch ,\n  on Monterey and newer.\n  Not recommended.",
                "Allow Tahoe Modern USB Patch":"Allow Tahoe Modern USB Patch",
                "When enabled, this will patch the Old USB\nextensions on Tahoe.":"When enabled, this will patch the Old USB\nextensions on Tahoe.",
                "Allow APFS Patch For Non-T2":"Allow APFS Patch For Non-T2",
                "When enabled, this will patch the apfs.efi\non Tahoe.":"When enabled, this will patch the apfs.efi\non Tahoe.",
                "AppleHDA.kext Version":"AppleHDA.kext Version",
                "Non-Metal":"Non-Metal",
                "Non-Metal Settings":"Non-Metal Settings",
                "Log out required to apply changes to SkyLight":"Log out required to apply changes to SkyLight",
                "Dark Menu Bar":"Dark Menu Bar",
                "If Beta Menu Bar is enabled,\nmenu bar colour will dynamically":"If Beta Menu Bar is enabled,\nmenu bar colour will dynamically",
                "Beta Blur":"Beta Blur",
                "Control window blur behaviour.":"Control window blur behaviour.",
                "Beach Ball Cursor Workaround":"Beach Ball Cursor Workaround",
                "Control beach ball cursor behaviour.":"Control beach ball cursor behaviour.",
                "Beta Menu Bar":"Beta Menu Bar",
                "Supports dynamic colour changes.":"Supports dynamic colour changes.",
                "Disable Beta Rim":"Disable Beta Rim",
                "Control Window Rim rendering.":"Control Window Rim rendering.",
                "Disable Color Widgets Enforcement":"Disable Color Widgets Enforcement",
                "Control Color Desktop Widgets Enforcement.":"Control Color Desktop Widgets Enforcement.",
                "App":"App",
                "General":"General",
                "Allow native models":"Allow native models",
                "Allow OpenCore to be installed\non natively supported Macs.\nNote this will not allow unsupported\nmacOS versions to be installed on\nyour system.":"Allow OpenCore to be installed\non natively supported Macs.\nNote this will not allow unsupported\nmacOS versions to be installed on\nyour system.",
                "Ignore App Updates":"Ignore App Updates",
                "Github Proxy":"Github Proxy",
                "Default":"Default",
                "SimpleHac":"SimpleHac",
                "gh-proxy":"gh-proxy",
                "ghfast":"ghfast",
                "Default : https://dortania.github.io/\nSimpleHac : https://next.oclpapi.simplehac.cn/\ngh-proxy : https://gh-proxy.com/\nghfast : https://ghfast.top/":"Default : https://dortania.github.io/\nSimpleHac : https://next.oclpapi.simplehac.cn/\ngh-proxy : https://gh-proxy.com/\nghfast : https://ghfast.top/",
                "Disable Reporting":"Disable Reporting",
                "When enabled, patcher will not\nreport any info to Hackdoc.":"When enabled, patcher will not\nreport any info to Hackdoc.",
                "Remove Unused KDKs":"Remove Unused KDKs",
                "When enabled, the app will remove\nunused Kernel Debug Kits from the system\nduring root patching.":"When enabled, the app will remove\nunused Kernel Debug Kits from the system\nduring root patching.",
                "Manually Download KDKs and\nMetallibs":"Manually Download KDKs and\nMetallibs",
                "When enabled, patcher will allow\nyou download KDKs and metallibs manually.":"When enabled, patcher will allow\nyou download KDKs and metallibs manually.",
                "Misc":"Misc",
                "Choose Download Path":"Choose Download Path",
                "Developer":"Developer",
                "Validation":"Validation",
                "Install latest nightly build 🧪":"Install latest nightly build 🧪",
                "If you're already here, I assume you're ok\nbricking your system 🧱.\nCheck CHANGELOG before blindly updating.":"If you're already here, I assume you're ok\nbricking your system 🧱.\nCheck CHANGELOG before blindly updating.",
                "Trigger Exception":"Trigger Exception",
                "Export constants":"Export constants",
                "Export constants.py values to a txt file.":"Export constants.py values to a txt file.",
                "Developer Root Volume Patching":"Developer Root Volume Patching",
                "Mount Root Volume":"Mount Root Volume",
                "Life's too short to type 'sudo mount -o\nnobrowse -t apfs /dev/diskXsY\n/System/Volumes/Update/mnt1' every time.":"Life's too short to type 'sudo mount -o\nnobrowse -t apfs /dev/diskXsY\n/System/Volumes/Update/mnt1' every time.",
                "Save Root Volume":"Save Root Volume",
                "Rebuild kernel cache and bless snapshot 🙏":"Rebuild kernel cache and bless snapshot 🙏",
                "Statistics":"Statistics",
                "Populate Stats":"Populate Stats",
                "Return":"Return"
            }
        elif self.language_point==0:
            trans={
                "Target Model":"目标机型",
                "Host Model":"主机机型",
                "Overrides Mac Model the Patcher will build for.":"覆盖补丁程序将构建的 Mac 机型。",
                "Build":"构建",
                "General":"常规",
                "FireWire Booting":"FireWire 启动",
                "Enable booting macOS from\nFireWire drives.":"启用从 FireWire 驱动器启动 macOS。",
                "XHCI Booting":"XHCI 启动",
                "Enable booting macOS from add-in\nUSB 3.0 expansion cards on systems\nwithout native support.":"在没有原生支持的系统上启用从添加的\nUSB 3.0 扩展卡启动 macOS。",
                "NVMe Booting":"NVMe 启动",
                "Enable booting macOS from NVMe\ndrives on systems without native\nsupport.\nNote: Requires Firmware support\nfor OpenCore to load from NVMe.":"在没有原生支持的系统上启用从 NVMe\n驱动器启动 macOS。\n注：需要固件支持才能从 NVMe 加载 OpenCore。",
                "OpenCore Vaulting":"OpenCore 加密",
                "Digitally sign OpenCore to prevent\ntampering or corruption.":"对 OpenCore 进行数字签名以防止\n篡改或损坏。",
                "Show OpenCore Boot Picker":"显示 OpenCore 启动选择器",
                "When disabled, users can hold ESC to\nshow picker in the firmware.":"禁用时，用户可以按住 ESC 键在固件中\n显示选择器。",
                "Boot Picker Timeout":"启动选择器超时",
                "Timeout before boot picker selects default\nentry in seconds.\nSet to 0 for no timeout.":"启动选择器选择默认项前的超时时间（秒）。\n设置为 0 表示无超时。",
                "MacPro3,1/Xserve2,1 Workaround":"MacPro3,1/Xserve2,1 解决方法",
                "Limits to 4 threads max on these units.\nRequired for macOS Sequoia and later.":"在这些设备上限制最多 4 个线程。\nmacOS Sequoia 及更高版本需要。",
                "Debug":"调试",
                "Verbose":"详细输出",
                "Verbose output during boot.":"启动期间显示详细输出。",
                "Kext Debugging":"Kext 调试",
                "Use DEBUG variants of kexts and\nenables additional kernel logging.":"使用 kext 的 DEBUG 变体并启用\n额外的内核日志记录。",
                "OpenCore Debugging":"OpenCore 调试",
                "Use DEBUG variant of OpenCore\nand enables additional logging.":"使用 OpenCore 的 DEBUG 变体并启用\n额外的日志记录。",
                "Extras":"额外",
                "General (Continued)":"常规（续）",
                "Wake on WLAN":"无线局域网唤醒",
                "Disabled by default due to\nperformance degradation\non some systems from wake.\nOnly applies to BCM943224, 331,\n360 and 3602 chipsets.":"默认禁用，因为某些系统从唤醒状态\n恢复时性能会下降。\n仅适用于 BCM943224、331、360 和 3602 芯片组。",
                "Disable Thunderbolt":"禁用 Thunderbolt",
                "For MacBookPro11,x with faulty\nPCHs that may crash sporadically.":"适用于带有可能偶尔崩溃的\n故障 PCH 的 MacBookPro11,x。",
                "Windows GMUX":"Windows GMUX",
                "Allow iGPU to be exposed in Windows\nfor dGPU-based MacBooks.":"允许 iGPU 在 Windows 中暴露，\n适用于基于 dGPU 的 MacBook。",
                "Disable CPUFriend":"禁用 CPUFriend",
                "Disables power management helper\nfor unsupported models.":"禁用不支持机型的电源管理助手。",
                "Disable mediaanalysisd service":"禁用 mediaanalysisd 服务",
                "For systems that are the primary iCloud\nPhoto Library host with a 3802-based GPU,\nthis may aid in prolonged idle stability.":"对于作为主要 iCloud 照片库主机且\n带有 3802 系列 GPU 的系统，\n这可能有助于延长空闲稳定性。",
                "Allow AppleALC Audio":"允许 AppleALC 音频",
                "Allow AppleALC to manage audio\nif applicable.\nOnly disable if your host lacks\na GOP ROM.":"允许 AppleALC 在适用时管理音频。\n仅在主机缺少 GOP ROM 时禁用。",
                "NVRAM WriteFlash":"NVRAM 写入",
                "Allow OpenCore to write to NVRAM.\nDisable on systems with faulty or\ndegraded NVRAM.":"允许 OpenCore 写入 NVRAM。\n在 NVRAM 故障或降级的系统上禁用。",
                "3rd Party NVMe PM":"第三方 NVMe 电源管理",
                "Enable non-stock NVMe power\nmanagement in macOS.":"在 macOS 中启用非原厂 NVMe 电源管理。",
                "3rd Party SATA PM":"第三方 SATA 电源管理",
                "Enable non-stock SATA power\nmanagement in macOS.":"在 macOS 中启用非原厂 SATA 电源管理。",
                "APFS Trim":"APFS Trim",
                "Recommended for all users, however faulty\nSSDs may benefit from disabling this.":"建议所有用户使用，但有故障的 SSD\n可能受益于禁用此功能。",
                "Advanced":"高级",
                "Miscellaneous":"杂项",
                "Disable Firmware Throttling":"禁用固件限制",
                "Disables firmware-based throttling\ncaused by missing hardware.\nEx. Missing Display, Battery, etc.":"禁用由缺少硬件引起的基于固件的限制。\n例如：缺少显示器、电池等。",
                "Software DeMUX":"软件 DeMUX",
                "Enable software based DeMUX\nfor MacBookPro8,2 and MacBookPro8,3.\nPrevents faulty dGPU from turning on.\nNote: Requires associated NVRAM arg:\n'gpu-power-prefs'.":"为 MacBookPro8,2 和 MacBookPro8,3 启用基于软件的 DeMUX。\n防止故障 dGPU 开启。\n注：需要关联的 NVRAM 参数：\n'gpu-power-prefs'。",
                "FeatureUnlock":"FeatureUnlock",
                "Enabled":"已启用",
                "Partial":"部分",
                "Disabled":"已禁用",
                "Configure FeatureUnlock level.\nRecommend lowering if your system\nexperiences memory instability.":"配置 FeatureUnlock 级别。\n如果系统出现内存不稳定，建议降低级别。",
                "Hibernation Work-around":"休眠解决方法",
                "Only load minimum EFI drivers\nto prevent hibernation issues.\nNote: This may break booting from\nexternal drives.":"仅加载最少的 EFI 驱动程序以防止休眠问题。\n注：这可能会破坏从外部驱动器启动。",
                "Graphics":"图形",
                "AMD GOP Injection":"AMD GOP 注入",
                "Inject AMD GOP for boot screen\nsupport on PC GPUs.":"为 PC GPU 注入 AMD GOP 以支持启动屏幕。",
                "Nvidia GOP Injection":"Nvidia GOP 注入",
                "Inject Nvidia Kepler GOP for boot\nscreen support on PC GPUs.":"为 PC GPU 注入 Nvidia Kepler GOP 以支持启动屏幕。",
                "Graphics Override":"图形覆盖",
                "None":"无",
                "Nvidia Kepler":"Nvidia Kepler",
                "AMD GCN":"AMD GCN",
                "AMD Polaris":"AMD Polaris",
                "AMD Lexa":"AMD Lexa",
                "AMD Navi":"AMD Navi",
                "Override detected/assumed GPU on\nsocketed MXM-based iMacs.":"覆盖基于 MXM 插槽的 iMac 上检测到/假设的 GPU。",
                "Security":"安全",
                "Kernel Security":"内核安全",
                "Disable Library Validation":"禁用库验证",
                "Required for loading modified\nsystem files from root patching.":"从根补丁加载修改后的系统文件所需。",
                "Disable AMFI":"禁用 AMFI",
                "Extended version of 'Disable\nLibrary Validation', required\nfor systems with deeper\nroot patches.":"'禁用库验证'的扩展版本，\n具有较深根补丁的系统需要。",
                "Secure Boot Model":"安全启动模型",
                "Set Apple Secure Boot Model Identifier\nto matching T2 model if spoofing.\nNote: Incompatible with Root Patching.":"如果进行欺骗，将 Apple 安全启动模型标识符\n设置为匹配的 T2 模型。\n注：与根补丁不兼容。",
                "System Integrity Protection":"系统完整性保护",
                "SMBIOS":"SMBIOS",
                "Model Spoofing":"机型欺骗",
                "SMBIOS Spoof Level":"SMBIOS 欺骗级别",
                "None":"无",
                "Minimal":"最小",
                "Moderate":"适度",
                "Advanced":"高级",
                "Supported Levels:\n   - None: No spoofing.\n   - Minimal: Overrides Board ID.\n   - Moderate: Overrides Model.\n   - Advanced: Overrides Model and serial.":"支持的级别：\n   - 无：不进行欺骗。\n   - 最小：覆盖 Board ID。\n   - 适度：覆盖机型。\n   - 高级：覆盖机型和序列号。",
                "SMBIOS Spoof Model":"SMBIOS 欺骗机型",
                "Default":"默认",
                "Set Mac Model to spoof to.":"设置要欺骗的 Mac 机型。",
                "Allow spoofing native Macs":"允许欺骗原生 Mac",
                "Allow OpenCore to spoof natively\nsupported Macs.\nPrimarily used for enabling\nUniversal Control on unsupported Macs":"允许 OpenCore 欺骗原生支持的 Mac。\n主要用于在不支持的 Mac 上启用通用控制。",
                "Serial Spoofing":"序列号欺骗",
                "Patch":"补丁",
                "Patch-General":"补丁-通用",
                "TeraScale 2 Acceleration":"TeraScale 2 加速",
                "Enable AMD TeraScale 2 GPU\nAcceleration on MacBookPro8,2 and\nMacBookPro8,3.\nBy default this is disabled due to\ncommon GPU failures on these models.":"在 MacBookPro8,2 和 MacBookPro8,3 上启用 AMD TeraScale 2 GPU 加速。\n默认禁用，因为这些机型常见 GPU 故障。",
                "Audio Patch choice":"音频补丁选择",
                "AppleHDA":"AppleHDA",
                "VoodooHDA":"VoodooHDA",
                "   - AppleALC: AppleALC patch on Tahoe.\n   - VoodooHDA: VoodooHDA patch ,\n  on Monterey and newer.\n  Not recommended.":"   - AppleALC: Tahoe 上的 AppleALC 补丁。\n   - VoodooHDA: VoodooHDA 补丁，\n  在 Monterey 及更高版本上。\n  不推荐。",
                "Allow Tahoe Modern USB Patch":"允许 Tahoe 现代 USB 补丁",
                "When enabled, this will patch the Old USB\nextensions on Tahoe.":"启用时，这将修补 Tahoe 上的旧 USB 扩展。",
                "Allow APFS Patch For Non-T2":"允许非 T2 设备的 APFS 补丁",
                "When enabled, this will patch the apfs.efi\non Tahoe.":"启用时，这将修补 Tahoe 上的 apfs.efi。",
                "AppleHDA.kext Version":"AppleHDA.kext 版本",
                "Non-Metal":"非 Metal",
                "Non-Metal Settings":"非 Metal 设置",
                "Log out required to apply changes to SkyLight":"应用更改到 SkyLight 需要注销",
                "Dark Menu Bar":"深色菜单栏",
                "If Beta Menu Bar is enabled,\nmenu bar colour will dynamically":"如果启用了测试版菜单栏，\n菜单栏颜色将动态变化",
                "Beta Blur":"测试版模糊",
                "Control window blur behaviour.":"控制窗口模糊行为。",
                "Beach Ball Cursor Workaround":"沙滩球光标解决方法",
                "Control beach ball cursor behaviour.":"控制沙滩球光标行为。",
                "Beta Menu Bar":"测试版菜单栏",
                "Supports dynamic colour changes.":"支持动态颜色变化。",
                "Disable Beta Rim":"禁用测试版边框",
                "Control Window Rim rendering.":"控制窗口边框渲染。",
                "Disable Color Widgets Enforcement":"禁用颜色小组件强制",
                "Control Color Desktop Widgets Enforcement.":"控制彩色桌面小组件强制。",
                "App":"应用",
                "General":"常规",
                "Allow native models":"允许原生机型",
                "Allow OpenCore to be installed\non natively supported Macs.\nNote this will not allow unsupported\nmacOS versions to be installed on\nyour system.":"允许在原生支持的 Mac 上安装 OpenCore。\n请注意，这不会允许在您的系统上\n安装不支持的 macOS 版本。",
                "Ignore App Updates":"忽略应用更新",
                "Github Proxy":"Github 代理",
                "Default":"默认",
                "SimpleHac":"SimpleHac",
                "gh-proxy":"gh-proxy",
                "ghfast":"ghfast",
                "Default : https://dortania.github.io/\nSimpleHac : https://next.oclpapi.simplehac.cn/\ngh-proxy : https://gh-proxy.com/\nghfast : https://ghfast.top/":"默认 : https://dortania.github.io/\nSimpleHac : https://next.oclpapi.simplehac.cn/\ngh-proxy : https://gh-proxy.com/\nghfast : https://ghfast.top/",
                "Disable Reporting":"禁用报告",
                "When enabled, patcher will not\nreport any info to Hackdoc.":"启用时，补丁程序不会向 Hackdoc 报告任何信息。",
                "Remove Unused KDKs":"移除未使用的 KDK",
                "When enabled, the app will remove\nunused Kernel Debug Kits from the system\nduring root patching.":"启用时，应用程序将在根补丁期间\n从系统中移除未使用的内核调试工具包。",
                "Manually Download KDKs and\nMetallibs":"手动下载 KDK 和 Metallib",
                "When enabled, patcher will allow\nyou download KDKs and metallibs manually.":"启用时，补丁程序将允许您手动下载 KDK 和 metallib。",
                "Misc":"杂项",
                "Choose Download Path":"选择下载路径",
                "Developer":"开发者",
                "Validation":"验证",
                "Install latest nightly build 🧪":"安装最新的夜间构建 🧪",
                "If you're already here, I assume you're ok\nbricking your system 🧱.\nCheck CHANGELOG before blindly updating.":"如果你已经在这里，我假设你愿意\n让你的系统变砖 🧱。\n在盲目更新前查看 CHANGELOG。",
                "Trigger Exception":"触发异常",
                "Export constants":"导出常量",
                "Export constants.py values to a txt file.":"将 constants.py 值导出到 txt 文件。",
                "Developer Root Volume Patching":"开发者根卷补丁",
                "Mount Root Volume":"挂载根卷",
                "Life's too short to type 'sudo mount -o\nnobrowse -t apfs /dev/diskXsY\n/System/Volumes/Update/mnt1' every time.":"人生苦短，何必每次都输入 'sudo mount -o\nnobrowse -t apfs /dev/diskXsY\n/System/Volumes/Update/mnt1'。",
                "Save Root Volume":"保存根卷",
                "Rebuild kernel cache and bless snapshot 🙏":"重建内核缓存并祝福快照 🙏",
                "Statistics":"统计信息",
                "Populate Stats":"填充统计信息",
                "Return":"返回"
            }
        return trans
    
    def gui_support(self):
        if self.language_point==1:
            trans={
                "&About OCLP-R":"&About OCLP-R",
                "&Reveal Log File":"&Reveal Log File",
                "During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.":"During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.",
                "Internal Error occurred!":"Internal Error occurred!",
                "Reboot to apply?":"Reboot to apply?",
                "Reboot":"Reboot",
                "Ignore":"Ignore"
            }
        elif self.language_point==0:
            trans={
                "&About OCLP-R":"&关于 OCLP-R",
                "&Reveal Log File":"&显示日志文件",
                "During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.":"在解包我们的内部文件时，我们似乎遇到了错误。\n\n如果您继续看到此错误，请尝试重启并重新下载应用程序。",
                "Internal Error occurred!":"发生内部错误！",
                "Reboot to apply?":"是否重启应用？",
                "Reboot":"重启",
                "Ignore":"忽略"
            }
        return trans
    
    def gui_sys_patch_display(self):
        if self.language_point==1:
            trans={
                "No root patch updates needed!\n\nWould you like to reboot to apply the new OpenCore build?":"No root patch updates needed!\n\nWould you like to reboot to apply the new OpenCore build?",
                "Post-Install Menu":"Post-Install Menu",
                "Initializing Root Patch Display Frame":"Initializing Root Patch Display Frame",
                "Fetching patches for host":"Fetching patches for host",
                "Available patches for your system:":"Available patches for your system:",
                "No patches required":"No patches required",
                "All applicable patches already installed":"All applicable patches already installed",
                "Cannot patch due to the following reasons:":"Cannot patch due to the following reasons:",
                "Root Volume last patched:":"Root Volume last patched:",
                "Start Root Patching":"Start Root Patching",
                "Revert Root Patches":"Revert Root Patches",
                "Return to Main Menu":"Return to Main Menu",
                "No staged update found":"No staged update found",
                "KDK required":"KDK required",
                "Available patches:":"Available patches:",
                "Starting root patching":"Starting root patching",
                "Reverting root patches":"Reverting root patches",
                "- Commit URLs differ":"- Commit URLs differ",
                "- Commit URLs:":"- Commit URLs:",
                "not installed":"not installed",
                "No new patches detected for system":"No new patches detected for system",
                "- Patch":"- Patch",
            }
        elif self.language_point==0:
            trans={
                "Initializing Root Patch Display Frame":"初始化根卷补丁显示框架",
                "No root patch updates needed!\n\nWould you like to reboot to apply the new OpenCore build?":"没有需要根卷补丁的更新!\n\n是否重启以应用新的 OpenCore 构建？",
                "Post-Install Menu":"安装驱动补丁",
                "Fetching patches for host":"正在获取补丁",
                "Available patches for your system:":"您系统可用的补丁：",
                "No patches required":"不需要补丁",
                "All applicable patches already installed":"所有适用的补丁已安装",
                "Cannot patch due to the following reasons:":"由于以下原因无法补丁：",
                "Root Volume last patched:":"根卷最后补丁时间：",
                "Start Root Patching":"开始根卷补丁",
                "Revert Root Patches":"还原根卷补丁",
                "Return to Main Menu":"返回主菜单",
                "No staged update found":"未找到暂存的更新",
                "KDK required":"需要KDK",
                "Available patches:":"可用补丁：",
                "Starting root patching":"开始根补丁",
                "Reverting root patches":"还原根补丁",
                "- Commit URLs differ":"- 提交 URL 不同",
                "- Commit URLs:":"- 提交 URL 为：",
                "- Patch":"- 补丁：",
                "not installed":"未安装",
                "No new patches detected for system":"没有新的系统补丁",
            }
        return trans
    
    def gui_sys_patch_start(self):
        if self.language_point==1:
            trans={
                "Downloading Kernel Debug Kit":"Downloading Kernel Debug Kit",
                "Fetching KDK database...":"Fetching KDK database...",
                "KDK download failed: ":"KDK download failed: ",
                "Validating KDK: ":"Validating KDK: ",
                "Checking if checksum is valid...":"Checking if checksum is valid...",
                "KDK checksum validation failed: ":"KDK checksum validation failed: ",
                "Downloading Metal Libraries":"Downloading Metal Libraries",
                "Fetching MetallibSupportPkg database...":"Fetching MetallibSupportPkg database...",
                "Metallib download failed: ":"Metallib download failed: ",
                "Installing Metallib: ":"Installing Metallib: ",
                "Installing MetallibSupportPkg PKG...":"Installing MetallibSupportPkg PKG...",
                "Metallib installation failed: ":"Metallib installation failed: ",
                "Root Patching":"Root Patching",
                "Revert Root Patches":"Revert Root Patches",
                "Root Patching will patch the following:":"Root Patching will patch the following:",
                "No patches to apply":"No patches to apply",
                "Reverting to last sealed snapshot":"Reverting to last sealed snapshot",
                "Return to Main Menu":"Return to Main Menu",
                "Root Patcher finished successfully!\n\nWould you like to reboot now?":"Root Patcher finished successfully!\n\nWould you like to reboot now?",
                "Root Patcher finished successfully!\nIf you were prompted to open System Settings to authorize new kexts, this can be ignored. Your system is ready once restarted.\n\nWould you like to reboot now?":"Root Patcher finished successfully!\nIf you were prompted to open System Settings to authorize new kexts, this can be ignored. Your system is ready once restarted.\n\nWould you like to reboot now?",
                "We just finished installing the patches to your Root Volume!\n\nHowever, Apple requires users to manually approve the kernel extensions installed before they can be used next reboot.\n\nWould you like to open System Preferences?":"We just finished installing the patches to your Root Volume!\n\nHowever, Apple requires users to manually approve the kernel extensions installed before they can be used next reboot.\n\nWould you like to open System Preferences?",
                "Open System Preferences?":"Open System Preferences?",
                "Open System Preferences":"Open System Preferences",
                "Ignore":"Ignore"
            }
        elif self.language_point==0:
            trans={
                "Downloading Kernel Debug Kit":"正在下载内核调试工具包",
                "Fetching KDK database...":"正在获取 KDK 数据库...",
                "KDK download failed: ":"KDK 下载失败：",
                "Validating KDK: ":"正在验证 KDK：",
                "Checking if checksum is valid...":"正在检查校验和是否有效...",
                "KDK checksum validation failed: ":"KDK 校验和验证失败：",
                "Downloading Metal Libraries":"正在下载 Metal 库",
                "Fetching MetallibSupportPkg database...":"正在获取 MetallibSupportPkg 数据库...",
                "Metallib download failed: ":"Metallib 下载失败：",
                "Installing Metallib: ":"正在安装 Metallib：",
                "Installing MetallibSupportPkg PKG...":"正在安装 MetallibSupportPkg 包...",
                "Metallib installation failed: ":"Metallib 安装失败：",
                "Root Patching":"根卷补丁",
                "Revert Root Patches":"还原根卷补丁",
                "Root Patching will patch the following:":"根卷补丁将修补以下内容：",
                "No patches to apply":"没有补丁可应用",
                "Reverting to last sealed snapshot":"正在还原到最后一个密封快照",
                "Return to Main Menu":"返回主菜单",
                "Root Patcher finished successfully!\n\nWould you like to reboot now?":"根卷补丁成功完成！\n\n您现在想要重启吗？",
                "Root Patcher finished successfully!\nIf you were prompted to open System Settings to authorize new kexts, this can be ignored. Your system is ready once restarted.\n\nWould you like to reboot now?":"根卷补丁成功完成！\n如果您被提示打开系统设置以授权新的 kext，这可以忽略。您的系统重启后即可使用。\n\n您现在想要重启吗？",
                "We just finished installing the patches to your Root Volume!\n\nHowever, Apple requires users to manually approve the kernel extensions installed before they can be used next reboot.\n\nWould you like to open System Preferences?":"我们刚刚完成了对您根卷的补丁安装！\n\n但是，Apple 要求用户手动批准安装的内核扩展，然后才能在下次重启时使用它们。\n\n您想要打开系统偏好设置吗？",
                "Open System Preferences?":"打开系统偏好设置？",
                "Open System Preferences":"打开系统偏好设置",
                "Ignore":"忽略"
            }
        return trans
    
    def gui_update(self):
        if self.language_point==1:
            trans={
                "Failed to get update info":"Failed to get update info",
                "Critical Error":"Critical Error",
                "Preparing download...":"Preparing download...",
                "Failed to download update. If you continue to have this issue, please manually download OCLP-R off Github":"Failed to download update. If you continue to have this issue, please manually download OCLP-R off Github",
                "Extracting update...":"Extracting update...",
                "Installing update...":"Installing update...",
                "Update complete!":"Update complete!",
                " has been installed to:":" has been installed to:",
                "Launching update shortly...":"Launching update shortly...",
                "Closing old process in ":"Closing old process in ",
                " seconds":" seconds"
            }
        elif self.language_point==0:
            trans={
                "Failed to get update info":"获取更新信息失败",
                "Critical Error":"严重错误",
                "Preparing download...":"正在准备下载...",
                "Failed to download update. If you continue to have this issue, please manually download OCLP-R off Github":"下载更新失败。如果您继续遇到此问题，请手动从 Github 下载 OCLP-R",
                "Extracting update...":"正在提取更新...",
                "Installing update...":"正在安装更新...",
                "Update complete!":"更新完成！",
                " has been installed to:":" 已安装到：",
                "Launching update shortly...":"即将启动更新...",
                "Closing old process in ":"正在关闭旧进程，倒计时 ",
                " seconds":" 秒"
            }
        return trans
    