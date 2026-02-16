from ..constants import Constants
from plistlib import load
from pathlib import Path
import logging

class TranslateLanguage:
    def __init__(self, global_constants: Constants = None) -> None:
        self.file_name:              str = ".com.hackdoc.oclp-r.plist"
        self.global_settings_folder: str = "/Users/Shared"
        self.global_settings_plist:  str = f"{self.global_settings_folder}/{self.file_name}"
        try:
            self.plist = load(Path(self.global_settings_plist).open("rb"))
            self.language_point = self.plist["GUI:language_option"]
        except Exception:
            self.language_point = "English"
        
    def application_entry(self):
        if self.language_point=="English":
            trans={
                "Current working directory:":"Current working directory:",
                "Current working directory was invalid, switched to:":"Current working directory was invalid, switched to:",
                "Detected arguments, switching to CLI mode":"Detected arguments, switching to CLI mode",
                "Main entry point":"Main entry point",
            }
            return trans
        elif self.language_point=="简体中文":
            trans={
                "Current working directory:":"当前工作目录：",
                "Current working directory was invalid, switched to:":"当前工作目录无效，已切换到：",
                "Detected arguments, switching to CLI mode":"检测到参数，切换到CLI模式",
                "Main entry point":"主入口点",
            }
            return trans
    def gengrate_smbios(self):
        if self.language_point=="English":
            trans={
                "Unknown SMBIOS for spoofing:":"Unknown SMBIOS for spoofing:",
                "- Failed to find FirmwareFeatures, falling back on defaults":"- Failed to find FirmwareFeatures, falling back on defaults",
            }
            return trans
        elif self.language_point=="简体中文":
            trans={
                "Unknown SMBIOS for spoofing:":"未知 SMBIOS 用于 spoofing:",
                "- Failed to find FirmwareFeatures, falling back on defaults":"- 未找到 FirmwareFeatures, 回退到默认值",
            }
            return trans
    def arguements(self):
        if self.language_point=="English":
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
        elif self.language_point=="简体中文":
            trans = {
                "Set Validation Mode": "设置验证模式",
                "- Running from Installer Sandbox, blocking OS updaters": "- 从安装程序沙箱运行, 阻止操作系统更新程序",
                "Set System Volume patching": "设置系统卷修补",
                "Set System Volume unpatching": "设置系统卷取消修补",
                "Set Auto patching": "设置自动修补",
                "Preparing host for macOS update": "准备主机以进行 macOS 更新",
                "No update staged, skipping": "没有暂存的更新, 跳过",
                "Preparing for update to": "准备更新到",
                "Another instance of OS caching is running, exiting": "另一个操作系统缓存实例正在运行, 退出",
                "- Failed to load plist for": "- 无法加载 plist 文件",
                "- Removing": "- 正在删除",
                "- Using custom model:":"- 使用自定义型号:",
                """Your model is not supported by this patcher for running unsupported OSes!"

If you plan to create the USB for another machine, please select the "Change Model" option in the menu.""": """您的型号不受此修补程序支持以运行不支持的操作系统!

如果您计划为另一台机器创建 USB，请在菜单中选择"更改型号"选项。""",
                "- Using detected model:":"- 使用检测到的型号:",
                "- Set verbose configuration": "- 设置详细配置",
                "- Set OpenCore DEBUG configuration": "- 设置 OpenCore 调试配置",
                "- Set kext DEBUG configuration": "- 设置 kext 调试配置",
                "- Set HidePicker configuration": "- 设置隐藏选择器配置",
                "- Set Disable SIP configuration": "- 设置禁用 SIP 配置",
                "- Set Disable SecureBootModel configuration": "- 设置禁用安全启动机型配置",
                "- Set Vault configuration": "- 设置 Vault 配置",
                "- Set FireWire Boot configuration": "- 设置 FireWire 启动配置",
                "- Set NVMe Boot configuration": "- 设置 NVMe 启动配置",
                "- Set Wake on WLAN configuration": "- 设置无线局域网唤醒配置",
                "- Set Disable Thunderbolt configuration": "- 设置禁用 Thunderbolt 配置",
                "- Forcing SurPlus override configuration": "- 强制 SurPlus 覆盖配置",
                "- Set Moderate SMBIOS Patching configuration": "- 设置适度 SMBIOS 修补配置",
                "- Unknown SMBIOS arg passed:":"- 传递了未知的 SMBIOS 参数:",
                "- Building for natively supported model": "- 为原生支持的型号构建",
                "Cleaning /Library/Extensions":"正在清理/Library/Extensions",
                "Failed to load plist for":"加载plist失败: ",
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
                "KDK download complete, validating with hdiutil":"KDK下载完成, 正在用hdiutil验证",
                "KDK checksum validation passed":"KDK校验和验证通过",
                "Mounting KDK":"正在挂载KDK",
                "KDK installed successfully":"KDK安装成功",
                "Failed to install KDK":"安装KDK失败",
                "Metallib installed successfully":"Metallib安装成功",
                "Failed to install Metallib":"安装Metallib失败",
                "KDK missing, generating KDK download frame":"缺少KDK, 正在生成KDK下载框架",
                "KDK download complete":"KDK下载完成",
                "MetallibSupportPkg missing, generating Metallib download frame":"缺少MetallibSupportPkg, 正在生成Metallib下载框架",
                "Metallib download complete, installing Metallib PKG":"Metallib下载完成, 正在安装Metallib PKG",
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
                "user_download_file:{path}":"用户下载的文件: {path}",
                "Choose Path: {path}":"选择路径: {path}",
                "Choose":"选择",
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
                "- Running from Installer Sandbox, blocking OS updaters": "- 从安装程序沙箱运行, 阻止操作系统更新程序",
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
                "- Set Disable SecureBootModel configuration": "- 设置禁用安全启动机型配置",
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
                "Failed to load plist for":"加载plist失败:",
                "Set OpenCore Build":"设置OpenCore构建"
            }
        return trans
    
    def kdk_handler(self):
        if self.language_point=="English":
            trans={
                "This is macOS beta's KDK":"This is macOS beta's KDK",
                "Could not contact KDK API":"Could not contact KDK API",
                "Could not fetch KDK list":"Could not fetch KDK list",
                "Pulling KDK list from KdkSupportPkg API":"Pulling KDK list from KdkSupportPkg API",
                "KDKs are not required for macOS Monterey or older":"KDKs are not required for macOS Monterey or older",
                "KDK already installed ({0}), skipping":"KDK already installed ({0}), skipping",
                "Failed to fetch KDK list, falling back to local KDK matching":"Failed to fetch KDK list, falling back to local KDK matching",
                "Checking for KDKs loosely matching {0}":"Checking for KDKs loosely matching {0}",
                "Found matching KDK: {0}":"Found matching KDK: {0}",
                "Couldn't find KDK matching {0} ({1}) or {2} was installed.":"Couldn't find KDK matching {0} ({1}) or {2} was installed.",
                "Please ensure you have a network connection or manually install a KDK.":"Please ensure you have a network connection or manually install a KDK.",
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
                "Kernel Debug Kit checksum verification failed, please try again.":"Kernel Debug Kit checksum verification failed, please try again.",
                "":"",
                "If this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)":"If this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)",
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
        elif self.language_point=="简体中文":
            trans={
                "This is macOS beta's KDK":"这是macOS beta的KDK",
                "Could not contact KDK API":"无法联系 KDK API",
                "Pulling KDK list from KdkSupportPkg API":"从 KdkSupportPkg API 获取 KDK 列表",
                "Could not fetch KDK list":"无法获取 KDK 列表",
                "KDKs are not required for macOS Monterey or older":"macOS Monterey 或更早版本不需要 KDK",
                "KDK already installed ({0}), skipping":"KDK 已安装 ({0}), 跳过",
                "Failed to fetch KDK list, falling back to local KDK matching":"获取 KDK 列表失败, 回退到本地 KDK 匹配",
                "Checking for KDKs loosely matching {0}":"检查与 {0} 松散匹配的 KDK",
                "Found matching KDK: {0}":"找到匹配的 KDK: {0}",
                "Couldn't find KDK matching {0} ({1}) or {2} was installed.":"找不到与 {0} ({1}) 或 {2} 匹配的 KDK.",
                "Please ensure you have a network connection or manually install a KDK.":"请确保您有网络连接或手动安装 KDK.",
                "No direct match found for {0}, falling back to closest match":"未找到 {0} 的直接匹配, 回退到最接近的匹配",
                "Closest Match: {0} ({1})":"最接近的匹配: {0} ({1})",
                "Direct match found for {0} ({1})":"找到 {0} ({1}) 的直接匹配",
                "Following KDK is recommended:":"建议使用以下 KDK:",
                "- KDK Build: {0}":"- KDK 构建版本: {0}",
                "- KDK Version: {0}":"- KDK 版本: {0}",
                "- KDK URL: {0}":"- KDK URL: {0}",
                "No download required, KDK already installed":"不需要下载, KDK 已安装",
                "Could not retrieve KDK catalog, no KDK to download":"无法检索 KDK 目录, 没有可下载的 KDK",
                "Returning DownloadObject for KDK: {0}":"返回 KDK 的 DownloadObject: {0}",
                "Failed to generate KDK Info.plist: {0}":"生成 KDK Info.plist 失败: {0}",
                "Corrupted KDK found ({0}), removing due to missing SystemVersion.plist":"发现损坏的 KDK ({0}), 由于缺少 SystemVersion.plist 而移除",
                "Corrupted KDK found ({0}), removing due to missing ProductBuildVersion":"发现损坏的 KDK ({0}), 由于缺少 ProductBuildVersion 而移除",
                "pkg receipt missing for {0}, falling back to legacy validation":"{0} 的 pkg 收据缺失, 回退到传统验证",
                "Corrupted KDK found ({0}), removing due to missing file: {1}":"发现损坏的 KDK ({0}), 由于缺少文件 {1} 而移除",
                "Corrupted KDK found, removing due to missing: {0}":"发现损坏的 KDK, 由于缺少 {0} 而移除",
                "Found KDK backup: {0}":"找到 KDK 备份: {0}",
                "Attempting KDK restoration":"尝试恢复 KDK",
                "Successfully restored KDK":"成功恢复 KDK",
                "KDK restoration skipped, running in passive mode":"跳过 KDK 恢复, 以被动模式运行",
                "KDK does not exist: {0}":"KDK 不存在: {0}",
                "Error: Kernel Debug Kit checksum verification failed!":"错误: Kernel Debug Kit 校验和验证失败!",
                "Kernel Debug Kit checksum verification failed, please try again.":"Kernel Debug Kit 校验和验证失败, 请重试.",
                "":"",
                "If this continues to fail, ensure you're downloading on a stable network connection (ie. Ethernet)":"如果问题持续存在, 请确保您在稳定的网络连接上下载 (例如: 以太网)",
                "Kernel Debug Kit checksum verified":"Kernel Debug Kit 校验和已验证",
                "Installing KDK package: {0}":"正在安装 KDK 包: {0}",
                "- This may take a while...":"- 这可能需要一段时间...",
                "Failed to install KDK:":"安装 KDK 失败:",
                "Extracting downloaded KDK disk image":"正在提取下载的 KDK 磁盘映像",
                "Failed to mount KDK:":"挂载 KDK 失败:",
                "Failed to find KDK package in DMG, likely corrupted!!!":"在 DMG 中找不到 KDK 包, 可能已损坏!!!",
                "Successfully installed KDK":"成功安装 KDK",
                "KDK does not exist, cannot create backup":"KDK 不存在, 无法创建备份",
                "KDK Info.plist does not exist, cannot create backup":"KDK Info.plist 不存在, 无法创建备份",
                "Malformed KDK Info.plist provided, cannot create backup":"提供的 KDK Info.plist 格式错误, 无法创建备份",
                "Creating backup: {0}":"正在创建备份: {0}",
                "Backup already exists, skipping":"备份已存在, 跳过",
                "Failed to create KDK backup:":"创建 KDK 备份失败:",
                "Cleaning unused KDKs":"正在清理未使用的 KDK"
            }
        return trans
    def logging_handler(self):
        if self.language_point=="English":
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
                "Failed to delete log file: {0}":"Failed to delete log file: {0}",
                "Uncaught exception in main thread":"Uncaught exception in main thread",
                "Uncaught exception in spawned thread":"Uncaught exception in spawned thread",
                'display dialog "{error_msg}" with title "OCLP-R ({self.constants.patcher_version})" buttons {{"Yes", "No"}} default button "Yes" with icon caution':'display dialog "{error_msg}" with title "OCLP-R ({self.constants.patcher_version})" buttons {{"Yes", "No"}} default button "Yes" with icon caution',
            }
        elif self.language_point=="简体中文":
            trans={
                "Uncaught exception in spawned thread":"未捕获的子线程异常",
                'display dialog "{error_msg}" with title "OCLP-R ({self.constants.patcher_version})" buttons {{"Yes", "No"}} default button "Yes" with icon caution':'显示标题为"OCLP-R ({self.constants.patcher_version})"的对话框"{error_msg}"，按钮为“是”和“否”，默认按钮为"是"，并带有警告图标.',
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
                "Failed to delete log file: {0}":"删除日志文件失败: {0}",
                "Uncaught exception in main thread":"未捕获的主线程异常",
            }
        return trans
    def macos_installer_handler(self):
        if self.language_point=="English":
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
        elif self.language_point=="简体中文":
            trans={
                "Extracting macOS installer from InstallAssistant.pkg":"正在从 InstallAssistant.pkg 提取 macOS 安装程序",
                "Failed to install InstallAssistant":"无法安装 InstallAssistant",
                "InstallAssistant installed":"InstallAssistant 已安装",
                "Creating temporary directory at {0}":"正在 {0} 创建临时目录",
                "Not enough free space to create installer.sh":"没有足够的可用空间来创建 installer.sh",
                "{0} available, {1} required":"可用空间 {0}, 需要 {1}",
                "Failed to copy installer to {0}":"无法将安装程序复制到 {0}",
                "Installer has broken code signature":"安装程序的代码签名已损坏"
            }
        return trans
    def metallib_handler(self):
        if self.language_point=="English":
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
                "Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.":"Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.",
                "Please ensure you have a network connection or manually install a metallib.":"Please ensure you have a network connection or manually install a metallib.",
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
        elif self.language_point=="简体中文":
            trans={
                "MetallibSupportPkg is not required for macOS Sonoma or older":"macOS Sonoma 或更早版本不需要 MetallibSupportPkg",
                "metallib already installed ({0}), skipping":"metallib 已安装 ({0}), 跳过",
                "Pulling metallib list from MetallibSupportPkg API":"正在从 MetallibSupportPkg API 获取 metallib 列表",
                "Could not contact MetallibSupportPkg API":"无法联系 MetallibSupportPkg API",
                "Could not fetch Metallib list":"无法获取 Metallib 列表",
                "Cannot get file size {0}: {1}":"无法获取文件大小 {0}: {1}",
                "Failed to fetch metallib list, falling back to local metallib matching":"获取 metallib 列表失败, 回退到本地 metallib 匹配",
                "Checking for metallibs loosely matching {0}":"检查与 {0} 松散匹配的 metallib",
                "Found matching metallib: {0}":"找到匹配的 metallib: {0}",
                "Couldn't find metallib matching {0} or {1}, please install one manually":"找不到与 {0} 或 {1} 匹配的 metallib, 请手动安装一个",
                "Could not contact MetallibSupportPkg API, and no metallib matching {0} ({1}) or {2} was installed.":"无法联系 MetallibSupportPkg API, 且没有安装与 {0} ({1}) 或 {2} 匹配的 metallib.",
                "Please ensure you have a network connection or manually install a metallib.":"请确保您有网络连接或手动安装 metallib.",
                "No metallibs found for {0} ({1})":"找不到适用于 {0} ({1}) 的 metallib",
                "No direct match found for {0}, falling back to closest match":"未找到 {0} 的直接匹配, 回退到最接近的匹配",
                "Closest Match: {0} ({1})":"最接近的匹配: {0} ({1})",
                "Direct match found for {0} ({1})":"找到 {0} ({1}) 的直接匹配",
                "Following metallib is recommended:":"建议使用以下 metallib:",
                "- metallib Build: {0}":"- metallib 构建版本: {0}",
                "- metallib Version: {0}":"- metallib 版本: {0}",
                "- metallib URL: {0}":"- metallib URL: {0}",
                "- metallib size: {0}":"- metallib 大小: {0}",
                "No download required, metallib already installed":"不需要下载, metallib 已安装",
                "Could not retrieve metallib catalog, no metallib to download":"无法检索 metallib 目录, 没有可下载的 metallib",
                "Returning DownloadObject for metallib: {0}":"返回 metallib 的 DownloadObject: {0}",
                "Cannot install metallib, no metallib was successfully retrieved":"无法安装 metallib, 没有成功检索到 metallib",
                "No installation required, metallib already installed":"不需要安装, metallib 已安装"
            }
        return trans
    def network_handler(self):
        if self.language_point=="English":
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
        elif self.language_point=="简体中文":
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
                "Not enough free space to download {0}, need {1}, have {2}":"没有足够的可用空间下载 {0}, 需要 {1}, 已有 {2}",
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
                "Downloaded {0} of {1}":"已下载 {0} ,共 {1}",
                "Downloaded {0:.2f}% of {1} ({2}/s) ({3:.2f} seconds remaining)":"已下载 {0:.2f}% ,共 {1} ,速度 {2} ,剩余时间 {3:.2f} 秒",
            }
        return trans
    def private(self):
        if self.language_point=="English":
            trans={
                "writing":"writing",
                "File {0} not found":"File {0} not found",
                "Invalid JSON in file {0}":"Invalid JSON in file {0}"
            }
        elif self.language_point=="简体中文":
            trans={
                "writing":"正在写入",
                "File {0} not found":"文件 {0} 未找到",
                "Invalid JSON in file {0}":"文件 {0} 中的 JSON 无效"
            }
        return trans
    def reroute_payloads(self):
        if self.language_point=="English":
            trans={
                "Running in compiled binary, switching to tmp directory":"Running in compiled binary, switching to tmp directory",
                "New payloads location: {0}":"New payloads location: {0}",
                "Creating payloads directory":"Creating payloads directory",
                "Mounted payloads.dmg":"Mounted payloads.dmg",
                "Failed to mount payloads.dmg":"Failed to mount payloads.dmg",
                "Unmounting personal {0}":"Unmounting personal {0}",
                "Unmounting {0} at: {1}":"Unmounting {0} at: {1}"
            }
        elif self.language_point=="简体中文":
            trans={
                "Running in compiled binary, switching to tmp directory":"正在运行编译后的二进制文件，切换到临时目录",
                "New payloads location: {0}":"新的 payloads 位置: {0}",
                "Creating payloads directory":"正在创建 payloads 目录",
                "Mounted payloads.dmg":"已挂载 payloads.dmg",
                "Failed to mount payloads.dmg":"无法挂载 payloads.dmg",
                "Unmounting personal {0}":"正在卸载 {0}",
                "Unmounting {0} at: {1}":"正在卸载 {0} 于: {1}"
            }
        return trans
    def subprocess_wrapper(self):
        if self.language_point=="English":
            trans={
                "Subprocess failed.":"Subprocess failed.",
                "    Command: {0}":"    Command: {0}",
                "    Return Code: {0}":"    Return Code: {0}",
                "        Likely Enum: {0}":"        Likely Enum: {0}",
                "    Standard Output:":"    Standard Output:",
                "        None":"        None",
                "    Standard Error:":"    Standard Error:",
                "File not found: {0}":"File not found: {0}",
                "process_failed_with_exit_code: {0}":"process_failed_with_exit_code: {0}",
            }
        elif self.language_point=="简体中文":
            trans={
                "Subprocess failed.":"子进程失败.",
                "    Command: {0}":"    命令: {0}",
                "    Return Code: {0}":"    返回代码: {0}",
                "        Likely Enum: {0}":"        可能的枚举: {0}",
                "    Standard Output:":"    标准输出:",
                "        None":"        无",
                "    Standard Error:":"    标准错误:",
                "File not found: {0}":"文件未找到: {0}",
                "process_failed_with_exit_code: {0}":"进程以退出代码 {0} 失败",
            }
        return trans
    def updates(self):
        if self.language_point=="English":
            trans={
                "Found asset: {0}":"Found asset: {0}",
                "Invalid version number for binary":"Invalid version number for binary",
            }
        elif self.language_point=="简体中文":
            trans={
                "Found asset: {0}":"找到assets: {0}",
                "Invalid version number for binary":"无效的二进制版本号",
            }
        return trans
    
    def utilities(self):
        if self.language_point=="English":
            trans={
                "FileVault is Off":"FileVault is Off",
                "Over a month":"Over a month",
                "Over a year":"Over a year",
                "Indeterminate time ":"Indeterminate time ",
                "Less than a minute ":"Less than a minute ", 
                "Disabling Idle Sleep":"Disabling Idle Sleep",
                "Re-enabling Idle Sleep":"Re-enabling Idle Sleep",
                "Killing Process: {0} - {1}":"Killing Process: {0} - {1}",
                # dmg_mount.py
                "- PatcherSupportPkg resources missing, Patcher likely corrupted!!!":"- PatcherSupportPkg resources missing, Patcher likely corrupted!!!",
                "- Failed to mount Universal-Binaries.dmg":"- Failed to mount Universal-Binaries.dmg",
                "- Mounted Universal-Binaries.dmg":"- Mounted Universal-Binaries.dmg",
                "- Found HackdocInternal resources, mounting...":"- Found HackdocInternal resources, mounting...",
                "- Failed to mount HackdocInternal resources":"- Failed to mount HackdocInternal resources",
                "- Mounted HackdocInternal resources":"- Mounted HackdocInternal resources",
                "- Failed to merge HackdocInternal resources":"- Failed to merge HackdocInternal resources",
                "- Local PatcherSupportPkg resources available, continuing...":"- Local PatcherSupportPkg resources available, continuing...",
                
                # files.py
                "  - Skipping {file_name}, cannot locate {source_folder}":"  - Skipping {file_name}, cannot locate {source_folder}",
                "  - Installing: {file_name}":"  - Installing: {file_name}",
                "  - Found existing {file_name}, overwriting...":"  - Found existing {file_name}, overwriting...",
                "  - Removing: {file_name}":"  - Removing: {file_name}",
                
                # kdk_merge.py
                "- Matching KDK determined to already be merged, skipping":"- Matching KDK determined to already be merged, skipping",
                "- Backing up IOHIDEventDriver CodeSignature":"- Backing up IOHIDEventDriver CodeSignature",
                "- Restoring IOHIDEventDriver CodeSignature":"- Restoring IOHIDEventDriver CodeSignature",
                "  - CodeSignature folder missing, creating":"  - CodeSignature folder missing, creating",
                "- Merging KDK with Root Volume: {kdk_name}":"- Merging KDK with Root Volume: {kdk_name}",
                "- Failed to merge KDK with Root Volume":"- Failed to merge KDK with Root Volume",
                "- Successfully merged KDK with Root Volume":"- Successfully merged KDK with Root Volume",
                "Failed to install KDK":"Failed to install KDK",
                "Unable to get KDK info: {error_msg}":"Unable to get KDK info: {error_msg}",
                "Could not retrieve KDK: {error_msg}":"Could not retrieve KDK: {error_msg}",
                "Could not download KDK: {error_msg}":"Could not download KDK: {error_msg}",
                "KDK checksum validation failed: {error_msg}":"KDK checksum validation failed: {error_msg}",
                "KDK was not installed, but should have been: {error_msg}":"KDK was not installed, but should have been: {error_msg}",
                "Unable to find Kernel Debug Kit":"Unable to find Kernel Debug Kit",
                "- Unable to find Kernel Debug Kit":"- Unable to find Kernel Debug Kit",
                "- Found KDK at: {kdk_path}":"- Found KDK at: {kdk_path}"
            }
        elif self.language_point=="简体中文":
            trans={
                "FileVault is Off":"文件保险箱已关闭",
                "Over a month":"超过一个月",
                "Over a year":"超过一年",
                "Indeterminate time ":"时间不确定 ",
                "Less than a minute ":"不到一分钟 ", 
                "Disabling Idle Sleep":"正在禁用休眠",
                "Re-enabling Idle Sleep":"正在重新启用休眠",
                "Killing Process: {0} - {1}":"正在终止进程: {0} - {1}",
                # dmg_mount.py
                "- PatcherSupportPkg resources missing, Patcher likely corrupted!!!":"- PatcherSupportPkg 资源缺失，修补程序可能已损坏！！！",
                "- Failed to mount Universal-Binaries.dmg":"- 挂载 Universal-Binaries.dmg 失败",
                "- Mounted Universal-Binaries.dmg":"- 已挂载 Universal-Binaries.dmg",
                "- Found HackdocInternal resources, mounting...":"- 找到 HackdocInternal 资源，正在挂载...",
                "- Failed to mount HackdocInternal resources":"- 挂载 HackdocInternal 资源失败",
                "- Mounted HackdocInternal resources":"- 已挂载 HackdocInternal 资源",
                "- Failed to merge HackdocInternal resources":"- 合并 HackdocInternal 资源失败",
                "- Local PatcherSupportPkg resources available, continuing...":"- 本地 PatcherSupportPkg 资源可用，继续...",
                
                # files.py
                "  - Skipping {file_name}, cannot locate {source_folder}":"  - 跳过 {file_name}，无法定位 {source_folder}",
                "  - Installing: {file_name}":"  - 正在安装: {file_name}",
                "  - Found existing {file_name}, overwriting...":"  - 找到现有 {file_name}，正在覆盖...",
                "  - Removing: {file_name}":"  - 正在删除: {file_name}",
                
                # kdk_merge.py
                "- Matching KDK determined to already be merged, skipping":"- 匹配的 KDK 已确定已合并，跳过",
                "- Backing up IOHIDEventDriver CodeSignature":"- 正在备份 IOHIDEventDriver 代码签名",
                "- Restoring IOHIDEventDriver CodeSignature":"- 正在恢复 IOHIDEventDriver 代码签名",
                "  - CodeSignature folder missing, creating":"  - 代码签名文件夹缺失，正在创建",
                "- Merging KDK with Root Volume: {kdk_name}":"- 正在将 KDK 与根卷合并: {kdk_name}",
                "- Failed to merge KDK with Root Volume":"- 将 KDK 与根卷合并失败",
                "- Successfully merged KDK with Root Volume":"- 成功将 KDK 与根卷合并",
                "Failed to install KDK":"安装 KDK 失败",
                "Unable to get KDK info: {error_msg}":"无法获取 KDK 信息: {error_msg}",
                "Could not retrieve KDK: {error_msg}":"无法检索 KDK: {error_msg}",
                "Could not download KDK: {error_msg}":"无法下载 KDK: {error_msg}",
                "KDK checksum validation failed: {error_msg}":"KDK 校验和验证失败: {error_msg}",
                "KDK was not installed, but should have been: {error_msg}":"KDK 未安装，但应该已安装: {error_msg}",
                "Unable to find Kernel Debug Kit":"无法找到内核调试工具包",
                "- Unable to find Kernel Debug Kit":"- 无法找到内核调试工具包",
                "- Found KDK at: {kdk_path}":"- 在 {kdk_path} 找到 KDK"
            }
        return trans
    
    def validation(self):
        if self.language_point=="English":
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
        elif self.language_point=="简体中文":
            trans={
                "Validating predefined model: {model}":"正在验证预定义机型: {model}",
                "Error on build!":"构建时出错!",
                "Validation failed for predefined model: {model}":"预定义机型验证失败: {model}",
                "Validation succeeded for predefined model: {model}":"预定义机型验证成功: {model}",
                "Validating dumped model: {model}":"正在验证已转储的机型： {model}",
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
        if self.language_point=="English":
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
                    "Your model is not supported by this patcher for running unsupported OSes!":"Your model is not supported by this patcher for running unsupported OSes!",
                    "":"",
                    "If you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.":"If you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.",
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
        elif self.language_point=="简体中文":
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
                    "- Using custom model:":"- 使用自定义机型:",
                    "Your model is not supported by this patcher for running unsupported OSes!\n\nIf you plan to create the USB for another machine, please select the \"Change Model\" option in the menu.":"您的机型不支持此补丁程序运行不受支持的操作系统!\n\n如果您计划为另一台机器创建 USB，请在菜单中选择\"更改机型\"选项。",
                    "- Using detected model:":"- 使用检测到的机型:",
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
                    "- Building for natively supported model":"- 为原生支持的机型构建"
                    }
        return trans
    
   
    
    def defaults(self):
        if self.language_point=="English":
            trans={
                "Error: Unable to read global settings file":"Error: Unable to read global settings file",
                "Global settings type mismatch for":"Global settings type mismatch for",
                "vs":"vs",
                "Removing":"Removing",
                "from global settings":"from global settings",
                "Setting":"Setting",
                "to":"to"
            }
        elif self.language_point=="简体中文":
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
        if self.language_point=="English":
            trans={
                "- Failed to find FirmwareFeatures, falling back on defaults":"- Failed to find FirmwareFeatures, falling back on defaults"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Failed to find FirmwareFeatures, falling back on defaults":"- 找不到 FirmwareFeatures，回退到默认值"
            }
        return trans
    
    def global_settings(self):
        if self.language_point=="English":
            trans={
                "Error: Unable to read global settings file":"Error: Unable to read global settings file",
                "Failed to write to global settings":"Failed to write to global settings",
                "Failed to write to global settings file":"Failed to write to global settings file",
                "Permission error: Unable to write to global settings file":"Permission error: Unable to write to global settings file",
                "Error: Unable to delete defaults plist":"Error: Unable to delete defaults plist",
                "Developed by Dortania and Hackdoc":"Developed by Dortania and Hackdoc",
            }
        elif self.language_point=="简体中文":
            trans={
                "Developed by Dortania and Hackdoc":"开发人员: Dortania 和 Hackdoc",
                "Error: Unable to read global settings file":"错误: 无法读取全局设置文件",
                "Failed to write to global settings":"无法写入全局设置",
                "Failed to write to global settings file":"无法写入全局设置文件",
                "Permission error: Unable to write to global settings file":"权限错误: 无法写入全局设置文件",
                "Error: Unable to delete defaults plist":"错误: 无法删除默认设置 plist"
            }
        return trans
    
    def install(self):
        if self.language_point=="English":
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
        elif self.language_point=="简体中文":
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
        if self.language_point=="English":
            trans={
                "File":"File",
                "does not exist":"does not exist",
                "is not a file":"is not a file",
                "Chunk":"Chunk",
                "checksum status FAIL: chunk sum":"checksum status FAIL: chunk sum",
                "calculated sum":"calculated sum"
            }
        elif self.language_point=="简体中文":
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
        if self.language_point=="English":
            trans={
                "Error":"Error",
                "Fetching KDK ERROR: ":"Fetching KDK ERROR: ",
                "Initializing KDK Download Frame":"Initializing KDK Download Frame",
                "Fetching KDKs":"Fetching KDKs",
                "Choose KDK Version":"Choose KDK Version",
                "Choose KDKs":"Choose KDKs",
                "Cannot find any KDKs on Github":"Cannot find any KDKs on Github",
                "Failed to download KDKs Catalog from Dortania":"Failed to download KDKs Catalog from Dortania",
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
                "Ventura":"Ventura",
                "Failed to detect OS build: ":"Failed to detect OS build: ",
                "Available installers on Dortania":"Available installers on Dortania",
            }
        elif self.language_point=="简体中文":
            trans={
                "Failed to detect OS build: ":"无法检测操作系统版本: ",
                "Error":"错误",
                "Fetching KDK ERROR: ":"获取 KDK 错误: ",
                "Initializing KDK Download Frame":"初始化 KDK 下载窗口",
                "Fetching KDKs":"正在获取 KDK",
                "Choose KDK Version":"选择 KDK 版本",
                "Choose KDKs":"选择 KDK",
                "Cannot find any KDKs on Github":"在 Github 上找不到任何 KDK",
                "Failed to download KDKs Catalog from Dortania":"无法从 Dortania 下载 KDK 目录",
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
                "Ventura":"Ventura",
                "Available installers on Dortania":"Dortania 上可用的安装器",
            }
        return trans
    
    def gui_about(self):
        if self.language_point=="English":
            trans={
                "Generating About frame":"Generating About frame",
                "About":"About",
                "OCLP-R":"OCLP-R",
                "Version":"Version",
                "I just wanted to relax, but I got addicted to it.":"I just wanted to relax, but I got addicted to it.",
                "I just wanted to protect the last hackintosh.":"I just wanted to protect the last hackintosh."
            }
        elif self.language_point=="简体中文":
            trans={
                "Generating About frame":"生成关于窗口",
                "About":"关于",
                "OCLP-R":"OCLP-R",
                "Version":"版本",
                "I just wanted to relax, but I got addicted to it.":"我只是想放松一下，但我上瘾了。",
                "I just wanted to protect the last hackintosh.":"我只是想守着黑苹果最后的Tahoe."
            }
        return trans
    
    def gui_build(self):
        if self.language_point=="English":
            trans={
                "Initializing Build Frame":"Initializing Build Frame",
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
        elif self.language_point=="简体中文":
            trans={
                "Initializing Build Frame":"初始化构建窗口",
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
        if self.language_point=="English":
            trans={
                "KDK installed successfully":"KDK installed successfully",
                "Failed to install KDK":"Failed to install KDK",
                "KDK download path does not exist":"KDK download path does not exist",
                "Mounting KDK":"Mounting KDK",
                "KDK checksum validation passed":"KDK checksum validation passed",
                "KDK checksum validation failed":"KDK checksum validation failed",
                "KDK download complete, validating with hdiutil":"KDK download complete, validating with hdiutil",
                "No additional resources required":"No additional resources required",
                "MetallibSupportPkg required":"MetallibSupportPkg required",
                "KDK Required":"KDK Required",
                "KDK Build {0}":"KDK Build {0}",
                "Metallib Build {0}":"Metallib Build {0}",
                "No staged update found":"No staged update found",
                "Staged update found:{0} ({1})":"Staged update found:{0} ({1})",
                "Initializing Prepare Update Frame":"Initializing Prepare Update Frame",
                "Preparing for macOS Software Update":"Preparing for macOS Software Update",
                "This may take a few minutes.":"This may take a few minutes.",
                "OCLP-R has detected that a macOS update is being downloaded:":"OCLP-R has detected that a macOS update is being downloaded:",
                "The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.":"The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.",
                "This may take a few minutes, the patcher will exit when it is done.":"This may take a few minutes, the patcher will exit when it is done.",
                "OCLP-R":"OCLP-R",
                "&Ok":"&Ok",
                "&Cancel":"&Cancel",
                "User cancelled OS caching":"User cancelled OS caching",
                "Failed to install Metallib":"Failed to install Metallib",
                "Metallib installed successfully":"Metallib installed successfully",
            }
        elif self.language_point=="简体中文":
            trans={
                "Failed to install Metallib":"安装 Metallib 失败",
                "Metallib installed successfully":"Metallib 安装成功",
                "KDK installed successfully":"KDK 安装成功",
                "Failed to install KDK":"安装 KDK 失败",
                "KDK download path does not exist":"KDK 下载路径不存在",
                "Mounting KDK":"挂载 KDK",
                "KDK checksum validation passed":"KDK checksum 验证通过",
                "KDK checksum validation failed":"KDK checksum 验证失败",
                "KDK download complete, validating with hdiutil":"KDK 下载完成，正在使用 hdiutil 验证",
                "KDK Build {0}":"KDK 构建 {0}",
                "Metallib Build {0}":"Metallib 构建 {0}",
                "No additional resources required":"不需要其他资源",
                "MetallibSupportPkg required":"需要 MetalLibSupportPkg",
                "KDK Required":"需要 KDK",
                "Staged update found:{0} ({1})":"暂存更新已找到:{0} ({1})",
                "No staged update found":"未找到暂存更新",
                "Initializing Prepare Update Frame":"初始化准备更新窗口",
                "Preparing for macOS Software Update":"正在准备 macOS 软件更新",
                "This may take a few minutes.":"这可能需要几分钟时间。",
                "OCLP-R has detected that a macOS update is being downloaded:":"OCLP-R 检测到正在下载 macOS 更新:",
                "The patcher needs to prepare the system for the update, and will download any additional resources it may need post-update.":"补丁程序需要为更新准备系统，并将下载更新后可能需要的任何其他资源。",
                "This may take a few minutes, the patcher will exit when it is done.":"这可能需要几分钟时间，补丁程序完成后将退出。",
                "OCLP-R":"OCLP-R",
                "&Ok":"&Ok",
                "&Cancel":"&Cancel",
                "User cancelled OS caching":"User cancelled OS caching",
                "_downloaded_":"downloaded",
            }
        return trans
    
    def gui_download(self):
        if self.language_point=="English":
            trans={
                "downloaded":"downloaded",
                "{0} left - {1} of {2} ({3}/s)":"{0} left - {1} of {2} ({3}/s)",
                "Error":"Error",
                "Initializing Download Frame":"Initializing Download Frame",
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
        elif self.language_point=="简体中文":
            trans={
                "downloaded":"已下载",
                "Error":"错误",
                "{0} left - {1} of {2} ({3}/s)":"剩余 {0} - {1} 中的 {2} ({3}/s)",
                "Initializing Download Frame":"初始化下载窗口",
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
        if self.language_point=="English":
            trans={
                "Entry point set:":"Entry point set:",
                "Cleaning up wxPython GUI":"Cleaning up wxPython GUI"
            }
        elif self.language_point=="简体中文":
            trans={
                "Entry point set:":"入口点已设置:",
                "Cleaning up wxPython GUI":"正在清理 wxPython GUI"
            }
        return trans
    
    def gui_help(self):
        if self.language_point=="English":
            trans={
                "Initializing Help Frame":"Initializing Help Frame",
                "Patcher Resources":"Patcher Resources",
                "Following resources are available:":"Following resources are available:",
                "Official Guide":"Official Guide",
                "Official Phone Support":"Official Phone Support",
                "Community Discord Server":"Community Discord Server",
                "Return to Main Menu":"Return to Main Menu"
            }
        elif self.language_point=="简体中文":
            trans={
                "Initializing Help Frame":"初始化帮助窗口",
                "Patcher Resources":"补丁程序资源",
                "Following resources are available:":"以下资源可用:",
                "Official Guide":"官方指南",
                "Official Phone Support":"官方电话支持",
                "Community Discord Server":"社区 Discord 服务器",
                "Return to Main Menu":"返回主菜单"
            }
        return trans
    
    def gui_install_oc(self):
        if self.language_point=="English":
            trans={
                "Initializing Install OpenCore Frame":"Initializing Install OpenCore Frame",
                "Install OpenCore":"Install OpenCore",
                "Checking if booted disk is present:":"Checking if booted disk is present:",
                "Fetching information on local disks...":"Fetching information on local disks...",
                "Select disk to install OpenCore onto:":"Select disk to install OpenCore onto:",
                "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT":"Missing disks? Ensure they're FAT32 or formatted as GUID/GPT",
                "Search for disks again":"Search for disks again",
                "Return to Main Menu":"Return to Main Menu",
                "Note: Blue represent the disk OpenCore is currently booted from":"Note: Blue represent the disk OpenCore is currently booted from",
                "Failed to find any applicable disks":"Failed to find any applicable disks",
                "Volumes on ":"Volumes on ",
                "Installing OpenCore to ":"Installing OpenCore to ",
                "OpenCore has finished installing to disk.":"OpenCore has finished installing to disk.",
                "Would you like to update your root patches next?":"Would you like to update your root patches next?",
                "Success":"Success",
                "You will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.":"You will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.",
                "Would you like to reboot?":"Would you like to reboot?",
                "You can eject the drive, insert it into the ":"You can eject the drive, insert it into the ",
                ", reboot, hold the Option key and select OpenCore/Boot EFI's option.":", reboot, hold the Option key and select OpenCore/Boot EFI's option.",
                "An internal error occurred while installing:\n":"An internal error occurred while installing:\n",
                "Available disks:":"Available disks:",
                "Available partitions for ":"Available partitions for ",
            }
        elif self.language_point=="简体中文":
            trans={
                "Available partitions for ":"Available partitions for ",
                "Available disks:":"可用磁盘:",
                "Initializing Install OpenCore Frame":"初始化安装 OpenCore 窗口",
                "Checking if booted disk is present:":"检查当前引导磁盘是否存在:",
                "Install OpenCore":"安装 OpenCore",
                "Fetching information on local disks...":"正在获取本地磁盘信息...",
                "Select disk to install OpenCore onto:":"选择要安装 OpenCore 的磁盘:",
                "Missing disks? Ensure they're FAT32 or formatted as GUID/GPT":"缺少磁盘？请确保它们是 FAT32 格式或格式化为 GUID/GPT",
                "Search for disks again":"再次搜索磁盘",
                "Return to Main Menu":"返回主菜单",
                "Note: Blue represent the disk OpenCore is currently booted from":"注: 蓝色代表当前引导 OpenCore 的磁盘",
                "Failed to find any applicable disks":"找不到任何适用的磁盘",
                "Volumes on ":"该卷在 ",
                "Installing OpenCore to ":"正在安装 OpenCore 到 ",
                "OpenCore has finished installing to disk.":"OpenCore 已完成安装到磁盘。",
                "Would you like to update your root patches next?":"接下来要更新您的根补丁吗？",
                "Success":"成功",
                "You will need to reboot and hold the Option key and select OpenCore/Boot EFI's option.":"您需要重启并按住 Option 键，然后选择 OpenCore/Boot EFI 选项。",
                "Would you like to reboot?":"要重启吗？",
                "You can eject the drive, insert it into the ":"您可以弹出驱动器，将其插入 ",
                ", reboot, hold the Option key and select OpenCore/Boot EFI's option.":", 重启，按住 Option 键，然后选择 OpenCore/Boot EFI 选项。",
                "An internal error occurred while installing:\n":"安装过程中发生内部错误:\n"
            }
        return trans
    
    def gui_macos_installer_download(self):
        if self.language_point=="English":
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
                "Chunklist validation failed: Hash mismatch on {0}":"Chunklist validation failed: Hash mismatch on {0}",
                "This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)":"This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)",
                "Corrupted Installer!":"Corrupted Installer!",
                "Extracting macOS Installer":"Extracting macOS Installer",
                "May take a few minutes...":"May take a few minutes...",
                "Successfully extracted macOS installer":"Successfully extracted macOS installer",
                "Failed to extract macOS installer":"Failed to extract macOS installer",
                "An error occurred while extracting the macOS installer. Could be due to a corrupted installer":"An error occurred while extracting the macOS installer. Could be due to a corrupted installer",
                "Finished extracting the installer, would you like to continue and create a macOS installer?":"Finished extracting the installer, would you like to continue and create a macOS installer?",
                "Create macOS Installer?":"Create macOS Installer?",
                "Initializing macOS Installer Download Frame":"Initializing macOS Installer Download Frame",
                "AES Key Fetch Failed,status code:":"AES Key Fetch Failed,status code:",
                "API REQUEST FAILED,status_code:":"API REQUEST FAILED,status_code:",
                "DMG data got it!":"DMG data got it!",
                "DMG data failed":"DMG data failed",
                "REQUEST ERROR:":"REQUEST ERROR:",
                "Failed to detect OS build:":"Failed to detect OS build:",
                "All entries":"All entries",
                "Latest only":"Latest only",
                "Can't get AES Keys":"Can't get AES Keys",
                "Error":"Error",
                "No dmgs found on SimpleHac":"No dmgs found on SimpleHac",
                "Download the selected DMGs.":"Download the selected DMGs.",
                "Available installers on SUCatalog":"Available installers on SUCatalog",
                "No installers found on SUCatalog":"No installers found on SUCatalog",
                "Download the selected macOS Installer.":"Download the selected macOS Installer.",
                "Copy the download link of the selected macOS Installer.":"Copy the download link of the selected macOS Installer.",
                "Selected macOS":"Selected macOS",
                "Lack of internal Keyboard/Trackpad in macOS installer.":"Lack of internal Keyboard/Trackpad in macOS installer.",
                "Lack of internal Keyboard/Mouse in macOS installer.":"Lack of internal Keyboard/Mouse in macOS installer.",
                "Potential Issues":"Potential Issues",
                "Insufficient space to download and extract: {0} available vs {1} required":"Insufficient space to download and extract: {0} available vs {1} required",
                "Select macOS Installer":"Select macOS Installer",
                "Validating chunk {0} of {1}":"Validating chunk {0} of {1}",
                "macOS installer validated":"macOS installer validated",
                "Available installers on SimpleHac":"Available installers on SimpleHac",
                "Copy the download link of the selected DMG.":"Copy the download link of the selected DMG.",
                "Create macOS Installer":"Create macOS Installer",
                "Your model ({model}) may not be fully supported by this installer. You may encounter the following issues:\n\n{problems}\n\nFor more information, see associated page. Otherwise, we recommend using macOS Monterey":"Your model ({model}) may not be fully supported by this installer. You may encounter the following issues:\n\n{problems}\n\nFor more information, see associated page. Otherwise, we recommend using macOS Monterey",
                "Selected macOS DMG {version} ({build})":"Selected macOS DMG {version} ({build})",
                "Select Path":"Select Path",
                "Cannot write to the selected directory.":"Cannot write to the selected directory.",
                "Read-only Directory":"Read-only Directory",
                "Selected directory: {save_path}":"Selected directory: {save_path}",
            }
        elif self.language_point=="简体中文":
            trans={
                "Potential Issues":"潜在问题",
                "Copy the download link of the selected DMG.":"复制选中的 DMG 文件的下载链接。",
                "Validating chunk {0} of {1}":"验证 macOS 安装程序的第 {0} 个块，共 {1} 个块",
                "Insufficient space to download and extract: {0} available vs {1} required":"下载和提取 macOS 安装程序所需的空间不足：{0} 可用 vs {1} 必需",
                "macOS installer validated":"macOS 安装程序已验证",
                "Select macOS Installer":"选择 macOS 安装程序",
                "Your model ({model}) may not be fully supported by this installer. You may encounter the following issues:\n\n{problems}\n\nFor more information, see associated page. Otherwise, we recommend using macOS Monterey":"您的模型 ({model}) 可能不被此安装程序完全支持。您可能会遇到以下问题：\n\n{problems}\n\n有关更多信息，请参阅关联页面。否则，我们建议使用 macOS Monterey",
                "Lack of internal Keyboard/Mouse in macOS installer.":"macOS 安装程序中缺少内部键盘/鼠标。",
                "Lack of internal Keyboard/Trackpad in macOS installer.":"macOS 安装程序中缺少内部键盘/触控板。",
                "Selected macOS":"选中的 macOS",
                "Download the selected macOS Installer.":"下载选中的 macOS 安装程序。",
                "Copy the download link of the selected macOS Installer.":"复制选中的 macOS 安装程序的下载链接。",
                "No installers found on SUCatalog":"SUCatalog 上未找到安装程序",
                "Available installers on SUCatalog":"SUCatalog 上可用的安装程序",
                "Download the selected DMGs.":"下载选中的 DMG 文件。",
                "No dmgs found on SimpleHac":"SimpleHac 上未找到 dmgs",
                "Error":"错误",
                "Can't get AES Keys":"无法获取 AES 密钥",
                "All entries":"所有条目",
                "Latest only":"最新版本",
                "Failed to detect OS build:":"无法检测操作系统版本:",
                "REQUEST ERROR:":"请求错误:",
                "DMG data failed":"DMG 数据获取失败",
                "DMG data got it!":"已获取 DMG 数据！",
                "API REQUEST FAILED,status_code:":"API 请求失败，状态码:",
                "AES Key Fetch Failed,status code:":"AES 密钥获取失败，状态码:",
                "Initializing macOS Installer Download Frame":"初始化 macOS 安装程序下载框架",
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
                "Chunklist validation failed: Hash mismatch on {0}":"分块列表验证失败：{0} 上的哈希不匹配",
                "This generally happens when downloading on unstable connections such as WiFi or cellular.\n\nPlease try redownloading again on a stable connection (ie. Ethernet)":"这通常发生在不稳定连接（如 WiFi 或蜂窝网络）上下载时。\n\n请尝试在稳定连接（如以太网）上重新下载",
                "Corrupted Installer!":"损坏的安装程序！",
                "Extracting macOS Installer":"正在提取 macOS 安装程序",
                "May take a few minutes...":"可能需要几分钟...",
                "Successfully extracted macOS installer":"成功提取 macOS 安装程序",
                "Failed to extract macOS installer":"提取 macOS 安装程序失败",
                "An error occurred while extracting the macOS installer. Could be due to a corrupted installer":"提取 macOS 安装程序时发生错误。可能是由于损坏的安装程序",
                "Finished extracting the installer, would you like to continue and create a macOS installer?":"安装程序提取完成，是否要继续创建 macOS 安装程序？",
                "Create macOS Installer?":"创建 macOS 安装程序？",
                "Create macOS Installer":"创建 macOS 安装程序",
                "Available installers on SimpleHac":"SimpleHac 上可用的安装程序",
                "Selected macOS DMG {version} ({build})":"已选择 macOS DMG {version} ({build})",
                "Select Path":"选择路径",
                "Cannot write to the selected directory.":"无法写入选择的目录。",
                "Read-only Directory":"只读目录",
                "Selected directory: {save_path}":"已选择目录: {save_path}",
            }
        return trans
    
    def gui_macos_installer_flash(self):
        if self.language_point=="English":
            trans={
                "Initializing macOS Installer Flash Frame":"Initializing macOS Installer Flash Frame",
                "Fetching local macOS Installers":"Fetching local macOS Installers",
                "Select local macOS Installer":"Select local macOS Installer",
                "No installers found in '/Applications'":"No installers found in '/Applications'",
                "Return to Main Menu":"Return to Main Menu",
                "Fetching information on local disks":"Fetching information on local disks",
                "Select local disk":"Select local disk",
                "Selected USB will be erased, please backup any data":"Selected USB will be erased, please backup any data",
                "No disks found":"No disks found",
                "Search for disks again":"Search for disks again",
                "Are you sure you want to erase '{0}'?\nAll data will be lost, this cannot be undone.":"Are you sure you want to erase '{0}'?\nAll data will be lost, this cannot be undone.",
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
                "Requires":"Requires",
                "Selected disk:":"Selected disk:",
                "Available disks:":"Available disks:",
                "Selected installer: {name} ({version} ({build}))":"Selected installer: {name} ({version} ({build}))",
                "Creating Installer: {installer_name}":"Creating Installer: {installer_name}",  
                "Flashing {0} to {1}":"Flashing {0} to {1}",
                "Bytes Written: {0:.2f} MB":"Bytes Written: {0:.2f} MB",
                "Creating macOS installer":"Creating macOS installer",
                "Failed to flash installer, cannot continue.":"Failed to flash installer, cannot continue.",
                "installer.sh contents:":"installer.sh contents:",
                "Failed to create macOS installer":"Failed to create macOS installer",
                "Successfully created macOS installer":"Successfully created macOS installer",
                "Installing Root Patcher to drive":"Installing Root Patcher to drive",
                "Failed to download Install.pkg":"Failed to download Install.pkg",
                "Installer unsupported, requires Big Sur or newer":"Installer unsupported, requires Big Sur or newer",
                "Initiating KDK download":"Initiating KDK download",
                "Build:":"Build:",
                "Version:":"Version:",
                "Working Directory:":"Working Directory:",
                "Failed to retrieve KDK":"Failed to retrieve KDK",
                "Stock Install.pkg is missing on Github, falling back to Nightly":"Stock Install.pkg is missing on Github, falling back to Nightly",
                "Not enough disk space to download and install KDK":"Not enough disk space to download and install KDK",
                "Attempting to download locally first":"Attempting to download locally first",
                "Not enough disk space to install KDK, skipping":"Not enough disk space to install KDK, skipping",
                "Failed to download KDK":"Failed to download KDK",
                "KDK missing:":"KDK missing:",
                "Mounting KDK":"Mounting KDK",
                "Failed to mount KDK":"Failed to mount KDK",
                "Copying KDK":"Copying KDK",
                "Unmounting KDK":"Unmounting KDK",
                "Failed to unmount KDK":"Failed to unmount KDK",
                "Removing KDK Disk Image":"Removing KDK Disk Image",
                "Initiating Metallib download":"Initiating Metallib download",
                "Failed to retrieve Metallib":"Failed to retrieve Metallib",
                "Not enough disk space to download and install Metallib":"Not enough disk space to download and install Metallib",
                "Failed to download Metallib":"Failed to download Metallib",
                "Validating installer pkg":"Validating installer pkg",
                "Metallib missing:":"Metallib missing:",
                "Installer pkg validated":"Installer pkg validated",
                "Failed to find":"Failed to find",
                "Installer created successfully, would you like to continue and Install OpenCore to this disk?":"Installer created successfully, would you like to continue and Install OpenCore to this disk?",
                "Installer created successfully! If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"Installer created successfully! If you want to install OpenCore to this USB, you will need to change the Target Model in settings",
                "If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"If you want to install OpenCore to this USB, you will need to change the Target Model in settings",
                "Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}":"Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}",
                "Installer(s) found:":"Installer(s) found:",
            }
        elif self.language_point=="简体中文":
            trans={
                "Initiating KDK download":"正在初始化 KDK 下载",
                "Installer pkg validated":"安装程序包验证成功",
                "Failed to download KDK":"无法下载 KDK",
                "Metallib missing:":"Metallib 缺失:",
                "Failed to find":"无法找到",
                "Validating installer pkg":"正在验证安装程序包",
                "Mounting KDK":"正在挂载 KDK (KDK本身是个DMG文件,内部是PKG)",
                "Initiating Metallib download":"正在初始化 Metallib 下载",
                "Failed to retrieve Metallib":"无法检索 Metallib",
                "Failed to mount KDK":"无法挂载 KDK",
                "Failed to download Metallib":"无法下载 Metallib",
                "Not enough disk space to download and install Metallib":"下载和安装 Metallib 所需的磁盘空间不足",
                "Copying KDK":"正在复制 KDK",
                "Unmounting KDK":"正在卸载 KDK",
                "Removing KDK Disk Image":"正在删除 KDK 磁盘镜像",
                "Failed to unmount KDK":"无法卸载 KDK",
                "Build:":"版本构建:",
                "KDK missing:":"KDK 缺失:",
                "Version:":"版本:",
                "Working Directory:":"工作目录:",
                "Failed to retrieve KDK":"无法检索 KDK",
                "Not enough disk space to install KDK, skipping":"安装 KDK 所需的磁盘空间不足,正在跳过",
                "Not enough disk space to download and install KDK":"下载和安装 KDK 所需的磁盘空间不足",
                "Attempting to download locally first":"正在尝试本地下载",
                "Stock Install.pkg is missing on Github, falling back to Nightly":"在 Github 上的 Stock Install.pkg 缺失，正在回退到 Nightly 版本",
                "Creating macOS installer":"正在创建 macOS 安装程序",
                "Failed to download Install.pkg":"无法下载 Install.pkg",
                "Installer unsupported, requires Big Sur or newer":"安装程序不支持，需要 Big Sur 或更新版本",
                "Installing Root Patcher to drive":"正在安装根卷补丁到磁盘",
                "installer.sh contents:":"installer.sh 内容:",
                "Failed to create macOS installer":"无法创建 macOS 安装程序",
                "Installer created successfully! If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"安装程序创建成功！如果要将 OpenCore 安装到此 USB 上，您需要在设置中更改目标模型。",
                "Selected installer: {name} ({version} ({build}))":"选择的安装程序: {name} ({version} ({build}))",
                "Initializing macOS Installer Flash Frame":"初始化制作 macOS 启动盘框架",
                "Fetching local macOS Installers":"正在获取本地 macOS 安装程序",
                "Requires":"需要",
                "Available disks:":"可用磁盘:",
                "Failed to flash installer, cannot continue.":"无法继续刷写安装程序，可能是由于 USB 驱动器故障导致的。",
                "Flashing {0} to {1}":"正在将 {0} 刷写到 {1}",
                "Bytes Written: {0:.2f} MB":"已写入字节: {0:.2f} MB",
                "Creating Installer: {installer_name}":"正在创建安装程序: {installer_name}",
                "Selected disk:":"选中的磁盘:",
                "Select local macOS Installer":"选择本地 macOS 安装程序",
                "No installers found in '/Applications'":"在 '/Applications' 中未找到安装程序",
                "Return to Main Menu":"返回主菜单",
                "Fetching information on local disks":"正在获取本地磁盘信息",
                "Select local disk":"选择本地磁盘",
                "Selected USB will be erased, please backup any data":"选中的 USB 将被擦除，请备份所有数据",
                "No disks found":"未找到磁盘",
                "Search for disks again":"再次搜索磁盘",
                "Are you sure you want to erase '{0}'?\nAll data will be lost, this cannot be undone.":"您确定要擦除 '{0}' 吗？\n所有数据将丢失，此操作无法撤销。",
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
                "Successfully created macOS installer":"成功创建 macOS 安装程序",
                "Installer created successfully, would you like to continue and Install OpenCore to this disk?":"安装程序创建成功，是否继续将 OpenCore 安装到此磁盘？",
                "If you want to install OpenCore to this USB, you will need to change the Target Model in settings":"如果您想将 OpenCore 安装到此 USB，您需要在设置中更改目标机型",
                "Failed to create macOS installer\n\nOutput: {output}\n\nError: {error}":"创建 macOS 安装程序失败\n\n输出: {output}\n\n错误: {error}",
                "Installer(s) found:":"找到安装程序:",
            }
        return trans
    
    def gui_main_menu(self):
        if self.language_point=="English":
            trans={
                "Initializing Main Menu Frame":'Initializing Main Menu Frame',
                "Build and Install OpenCore":"Build and Install OpenCore",
                "Prepares provided drive to be able":"Prepares provided drive to be able",
                "to boot unsupported OSes.":"to boot unsupported OSes.",
                "Use on installers or internal drives.":"Use on installers or internal drives.",
                "Create macOS Installer":"Create macOS Installer",
                "Download and flash a macOS":"Download and flash a macOS",
                "Installer for your system.":"Installer for your system.",
                "KDK Download":"KDK Download",
                "Provide KDK download":"Provide KDK download",
                "for your system.":"for your system.",
                "⚙️ Settings":"⚙️ Settings",
                "Post-Install Root Patch":"Post-Install Root Patch",
                "Installs hardware drivers and":"Installs hardware drivers and",
                "patches for your system after":"Patches for your system after",
                "installing a new version of macOS.":"installing a new version of macOS.",
                "MetalLib Download":"MetalLib Download",
                "Provide MetalLib for your system.":"Provide MetalLib for your system.",
                "This is required for Metal3802 devices.":"This is required for Metal3802 devices",
                "Support":"Support",
                "Resources for OpenCore Legacy":"Resources for OpenCore Legacy",
                "Patcher.":"Patcher.",
                "Unsupported Configuration Detected!":"Unsupported Configuration Detected!",
                "We found you are currently booting OpenCore built for a different unit: {build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.":"We found you are currently booting OpenCore built for a different unit: {self.constants.computer.build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.",
                "Update successful!":"Update successful!",
                "OCLP-R has been updated to the latest version: {patcher_version}\n\nWould you like to update OpenCore and your root volume patches?":"OCLP-R has been updated to the latest version: {patcher_version}\n\nWould you like to update OpenCore and your root volume patches?",
                "A new version of OCLP-R is available!":"A new version of OCLP-R is available!",
                "OCLP-R {oclp_version} is now available - You have {patcher_version}. Would you like to update?":"OCLP-R {oclp_version} is now available - You have {patcher_version}. Would you like to update?",
                "Unable to fetch changelog\n\nPlease check the Github page for more information about this release.":"Unable to fetch changelog\n\nPlease check the Github page for more information about this release.",
                "Dismiss":"Dismiss",
                "View on GitHub":"View on GitHub",
                "Download and Install":"Download and Install",
                "Model: " :"Model: ",
                "Skipping OpenCore and root volume patch update...":"Skipping OpenCore and root volume patch update...",
                """## Unable to fetch changelog

Please check the Github page for more information about this release.""":"""## Unable to fetch changelog

Please check the Github page for more information about this release.""",
            }
        elif self.language_point=="简体中文":
            trans={
                """## Unable to fetch changelog

Please check the Github page for more information about this release.""":"""
无法获取更新日志

请检查 Github 页面以获取更多关于此版本的信息。
""",
                "Model: ":"机型: ",
                "Initializing Main Menu Frame":'初始化主菜单框架',
                "Build and Install OpenCore":"构建并安装 OpenCore 引导",
                "Prepares provided drive to be able":"准备提供的驱动器以",
                "to boot unsupported OSes.":"用于启动不支持的操作系统。",
                "Use on installers or internal drives.":"用于安装程序或内部驱动器。",
                "Create macOS Installer":"创建 macOS 安装程序",
                "Download and flash a macOS":"下载并刷写 macOS",
                "Installer for your system.":"安装程序为您的系统。",
                "KDK Download":"下载 KDK",
                "Provide KDK download":"为您的系统",
                "for your system.":"提供 KDK 下载",#为了调整语序进行的更改
                "⚙️ Settings":"⚙️ 设置",
                "Post-Install Root Patch":"安装驱动补丁",
                "Installs hardware drivers and":"在安装新版本的 macOS 后",
                "patches for your system after":"为您的系统安装硬件",
                "installing a new version of macOS.":"驱动程序和补丁。",#调整语序
                "MetalLib Download":"下载 MetalLib",
                "Provide MetalLib for your system.":"为您的系统提供 MetalLib.",
                "This is required for Metal3802 devices.":"这是 Metal3802 设备所必需的.",
                "Support":"获取支持",
                "Resources for OpenCore Legacy":"OpenCore Legacy Patcher",
                "Patcher.":"的资源。",
                "Unsupported Configuration Detected!":"检测到不支持的配置！",
                "We found you are currently booting OpenCore built for a different unit: {build_model}\n\nWe builds configs to match individual units and cannot be mixed or reused with different Macs.\n\nPlease Build and Install a new OpenCore config, and reboot your Mac.":"我们发现您当前正在引导为不同设备构建的 OpenCore：{self.constants.computer.build_model}\n\n我们构建的配置是为匹配单个设备的，不能与不同的 Mac 混合使用或重复使用。\n\n请构建并安装一个新的 OpenCore 配置，然后重启您的 Mac。",
                "Update successful!":"更新成功！",
                "OCLP-R has been updated to the latest version: {patcher_version}\n\nWould you like to update OpenCore and your root volume patches?":"OCLP-R 已更新到最新版本：{patcher_version}\n\n您是否要更新 OpenCore 和根卷补丁？",
                "A new version of OCLP-R is available!":"OCLP-R 有新版本可用！",
                "OCLP-R {oclp_version} is now available - You have {patcher_version}. Would you like to update?":"OCLP-R {oclp_version} 现已可用 - 您当前版本是 {patcher_version}。您是否要更新？",
                "Unable to fetch changelog\n\nPlease check the Github page for more information about this release.":"无法获取更新日志\n\n请查看 Github 页面了解有关此版本的更多信息。",
                "Dismiss":"关闭",
                "View on GitHub":"在 GitHub 上查看",
                "Download and Install":"下载并安装",
                "Skipping OpenCore and root volume patch update...":"跳过 OpenCore 和根卷补丁更新...",
                "Updating OpenCore and root volume patches...":"Updating OpenCore and root volume patches...",
                
            }
        return trans
    
    def gui_metallib_download(self):
        if self.language_point=="English":
            trans={
                "Cannot find any installers":"Cannot find any installers",
                "Updating OpenCore and root volume patches...":"更新 OpenCore 和根卷补丁...",
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
                "Error":"Error",
                "Initializing NewMetallibDownloadFrame":"Initializing NewMetallibDownloadFrame",
                "Failed to detect OS build: {e}":"Failed to detect OS build: {e}",
                "Available installers on Github":"Available installers on Github",
                "All entries":"All entries",
                "Latest only":"Latest only",
            }
        elif self.language_point=="简体中文":
            trans={
                "Cannot find any installers":"无法找到任何安装程序",
                "All entries":"所有条目",
                "Latest only":"仅最新版本",
                "Available installers on Github":"在 Github 上可用的安装程序",
                "Failed to detect OS build: {e}":"无法检测操作系统构建: {e}",
                "Initializing NewMetallibDownloadFrame":"初始化新的 Metallib 下载框架",
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
        if self.language_point=="English":
            trans={
                "Target Model":"Target Model",
                "Host Model":"Host Model",
                "Overrides Mac Model the Patcher will build for.":"Overrides Mac Model the Patcher will build for.",
                "Build":"Build",
                "General":"General",
                "FireWire Booting":"FireWire Booting",
                "Enable booting macOS from":"Enable booting macOS from",
                "FireWire drives.":"FireWire drives.",
                "XHCI Booting":"XHCI Booting",
                "Enable booting macOS from add-in":"Enable booting macOS from add-in",
                "USB 3.0 expansion cards on systems":"USB 3.0 expansion cards on systems",
                "without native support.":"without native support.",
                "NVMe Booting":"NVMe Booting",
                "Enable booting macOS from NVMe":"Enable booting macOS from NVMe",
                "drives on systems without native":"drives on systems without native",
                "support.":"support.",
                "Note: Requires Firmware support":"Note: Requires Firmware support",
                "for OpenCore to load from NVMe.":"for OpenCore to load from NVMe.",
                "OpenCore Vaulting":"OpenCore Vaulting",
                "Digitally sign OpenCore to prevent":"Digitally sign OpenCore to prevent",
                "tampering or corruption.":"tampering or corruption.",
                "Show OpenCore Boot Picker":"Show OpenCore Boot Picker",
                "When disabled, users can hold ESC to":"When disabled, users can hold ESC to",
                "show picker in the firmware.":"show picker in the firmware.",
                "Boot Picker Timeout":"Boot Picker Timeout",
                "Timeout before boot picker selects default":"Timeout before boot picker selects default",
                "entry in seconds.":"entry in seconds.",
                "Set to 0 for no timeout.":"Set to 0 for no timeout.",
                "MacPro3,1/Xserve2,1 Workaround":"MacPro3,1/Xserve2,1 Workaround",
                "Limits to 4 threads max on these units.":"Limits to 4 threads max on these units.",
                "Required for macOS Sequoia and later.":"Required for macOS Sequoia and later.",
                "Debug":"Debug",
                "Verbose":"Verbose",
                "Verbose output during boot.":"Verbose output during boot.",
                "Kext Debugging":"Kext Debugging",
                "Use DEBUG variants of kexts and":"Use DEBUG variants of kexts and",
                "enables additional kernel logging.":"enables additional kernel logging.",
                "OpenCore Debugging":"OpenCore Debugging",
                "Use DEBUG variant of OpenCore":"Use DEBUG variant of OpenCore",
                "and enables additional logging.":"and enables additional logging.",
                "Extras":"Extras",
                "General (Continued)":"General (Continued)",
                "Wake on WLAN":"Wake on WLAN",
                "Disabled by default due to":"Disabled by default due to",
                "performance degradation":"performance degradation",
                "on some systems from wake.":"on some systems from wake.",
                "Only applies to BCM943224, 331,":"Only applies to BCM943224, 331,",
                "360 and 3602 chipsets.":"360 and 3602 chipsets.",
                "Disable Thunderbolt":"Disable Thunderbolt",
                "For MacBookPro11,x with faulty":"For MacBookPro11,x with faulty",
                "PCHs that may crash sporadically.":"PCHs that may crash sporadically.",
                "Windows GMUX":"Windows GMUX",
                "Allow iGPU to be exposed in Windows":"Allow iGPU to be exposed in Windows",
                "for dGPU-based MacBooks.":"for dGPU-based MacBooks.",
                "Disable CPUFriend":"Disable CPUFriend",
                "Disables power management helper":"Disables power management helper",
                "for unsupported models.":"for unsupported models.",
                "Disable mediaanalysisd service":"Disable mediaanalysisd service",
                "For systems that are the primary iCloud":"For systems that are the primary iCloud",
                "Photo Library host with a 3802-based GPU,":"Photo Library host with a 3802-based GPU,",
                "this may aid in prolonged idle stability.":"this may aid in prolonged idle stability.",
                "Allow AppleALC Audio":"Allow AppleALC Audio",
                "Allow AppleALC to manage audio":"Allow AppleALC to manage audio",
                "if applicable.":"if applicable.",
                "Only disable if your host lacks":"Only disable if your host lacks",
                "a GOP ROM.":"a GOP ROM.",
                "NVRAM WriteFlash":"NVRAM WriteFlash",
                "Allow OpenCore to write to NVRAM.":"Allow OpenCore to write to NVRAM.",
                "Disable on systems with faulty or":"Disable on systems with faulty or",
                "degraded NVRAM.":"degraded NVRAM.",
                "3rd Party NVMe PM":"3rd Party NVMe PM",
                "Enable non-stock NVMe power":"Enable non-stock NVMe power",
                "management in macOS.":"management in macOS.",
                "3rd Party SATA PM":"3rd Party SATA PM",
                "Enable non-stock SATA power":"Enable non-stock SATA power",
                "management in macOS.":"management in macOS.",
                "APFS Trim":"APFS Trim",
                "Recommended for all users, however faulty":"Recommended for all users, however faulty",
                "SSDs may benefit from disabling this.":"SSDs may benefit from disabling this.",
                "Advanced":"Advanced",
                "Miscellaneous":"Miscellaneous",
                "Disable Firmware Throttling":"Disable Firmware Throttling",
                "Disables firmware-based throttling":"Disables firmware-based throttling",
                "caused by missing hardware.":"caused by missing hardware.",
                "Ex. Missing Display, Battery, etc.":"Ex. Missing Display, Battery, etc.",
                "Software DeMUX":"Software DeMUX",
                "Enable software based DeMUX":"Enable software based DeMUX",
                "for MacBookPro8,2 and MacBookPro8,3.":"for MacBookPro8,2 and MacBookPro8,3.",
                "Prevents faulty dGPU from turning on.":"Prevents faulty dGPU from turning on.",
                "Note: Requires associated NVRAM arg:":"Note: Requires associated NVRAM arg:",
                "'gpu-power-prefs'.":"'gpu-power-prefs'.",
                "FeatureUnlock":"FeatureUnlock",
                "Enabled":"Enabled",
                "Partial":"Partial",
                "Disabled":"Disabled",
                "Configure FeatureUnlock level.":"Configure FeatureUnlock level.",
                "Recommend lowering if your system":"Recommend lowering if your system",
                "experiences memory instability.":"experiences memory instability.",
                "Hibernation Work-around":"Hibernation Work-around",
                "Only load minimum EFI drivers":"Only load minimum EFI drivers",
                "to prevent hibernation issues.":"to prevent hibernation issues.",
                "Note: This may break booting from":"Note: This may break booting from",
                "external drives.":"external drives.",
                "Graphics":"Graphics",
                "AMD GOP Injection":"AMD GOP Injection",
                "Inject AMD GOP for boot screen":"Inject AMD GOP for boot screen",
                "support on PC GPUs.":"support on PC GPUs.",
                "Nvidia GOP Injection":"Nvidia GOP Injection",
                "Inject Nvidia Kepler GOP for boot":"Inject Nvidia Kepler GOP for boot",
                "screen support on PC GPUs.":"screen support on PC GPUs.",
                "Graphics Override":"Graphics Override",
                "None":"None",
                "Nvidia Kepler":"Nvidia Kepler",
                "AMD GCN":"AMD GCN",
                "AMD Polaris":"AMD Polaris",
                "AMD Lexa":"AMD Lexa",
                "AMD Navi":"AMD Navi",
                "Override detected/assumed GPU on":"Override detected/assumed GPU on",
                "socketed MXM-based iMacs.":"socketed MXM-based iMacs.",
                "Security":"Security",
                "Kernel Security":"Kernel Security",
                "Disable Library Validation":"Disable Library Validation",
                "Required for loading modified":"Required for loading modified",
                "system files from root patching.":"system files from root patching.",
                "Disable AMFI":"Disable AMFI",
                "Extended version of 'Disable":"Extended version of 'Disable",
                "Library Validation', required":"Library Validation', required",
                "for systems with deeper":"for systems with deeper",
                "root patches.":"root patches.",
                "Secure Boot Model":"Secure Boot Model",
                "Set Apple Secure Boot Model Identifier":"Set Apple Secure Boot Model Identifier",
                "to matching T2 model if spoofing.":"to matching T2 model if spoofing.",
                "Note: Incompatible with Root Patching.":"Note: Incompatible with Root Patching.",
                "System Integrity Protection":"System Integrity Protection",
                "SMBIOS":"SMBIOS",
                "Model Spoofing":"Model Spoofing",
                "SMBIOS Spoof Level":"SMBIOS Spoof Level",
                "None":"None",
                "Minimal":"Minimal",
                "Moderate":"Moderate",
                "Advanced":"Advanced",
                "Supported Levels:":"Supported Levels:",
                "   - None: No spoofing.":"   - None: No spoofing.",
                "   - Minimal: Overrides Board ID.":"   - Minimal: Overrides Board ID.",
                "   - Moderate: Overrides Model.":"   - Moderate: Overrides Model.",
                "   - Advanced: Overrides Model and serial.":"   - Advanced: Overrides Model and serial.",
                "SMBIOS Spoof Model":"SMBIOS Spoof Model",
                "Default":"Default",
                "Set Mac Model to spoof to.":"Set Mac Model to spoof to.",
                "Allow spoofing native Macs":"Allow spoofing native Macs",
                "Allow OpenCore to spoof natively":"Allow OpenCore to spoof natively",
                "supported Macs.":"supported Macs.",
                "Primarily used for enabling":"Primarily used for enabling",
                "Universal Control on unsupported Macs":"Universal Control on unsupported Macs",
                "Serial Spoofing":"Serial Spoofing",
                "Patch":"Patch",
                "Patch-General":"Patch-General",
                "TeraScale 2 Acceleration":"TeraScale 2 Acceleration",
                "Enable AMD TeraScale 2 GPU":"Enable AMD TeraScale 2 GPU",
                "Acceleration on MacBookPro8,2 and":"Acceleration on MacBookPro8,2 and",
                "MacBookPro8,3.":"MacBookPro8,3.",
                "By default this is disabled due to":"By default this is disabled due to",
                "common GPU failures on these models.":"common GPU failures on these models.",
                "Audio Patch choice":"Audio Patch choice",
                "AppleHDA":"AppleHDA",
                "VoodooHDA":"VoodooHDA",
                "   - AppleALC: AppleALC patch on Tahoe.":"   - AppleALC: AppleALC patch on Tahoe.",
                "   - VoodooHDA: VoodooHDA patch ,":"   - VoodooHDA: VoodooHDA patch ,",
                "  on Monterey and newer.":"  on Monterey and newer.",
                "  Not recommended.":"  Not recommended.",
                "Allow Tahoe Modern USB Patch":"Allow Tahoe Modern USB Patch",
                "When enabled, this will patch the Old USB":"When enabled, this will patch the Old USB",
                "extensions on Tahoe.":"extensions on Tahoe.",
                "Allow APFS Patch For Non-T2":"Allow APFS Patch For Non-T2",
                "When enabled, this will patch the apfs.efi":"When enabled, this will patch the apfs.efi",
                "on Tahoe.":"on Tahoe.",
                "AppleHDA.kext Version":"AppleHDA.kext Version",
                "Non-Metal":"Non-Metal",
                "Non-Metal Settings":"Non-Metal Settings",
                "Log out required to apply changes to SkyLight":"Log out required to apply changes to SkyLight",
                "Dark Menu Bar":"Dark Menu Bar",
                "If Beta Menu Bar is enabled,":"If Beta Menu Bar is enabled,",
                "menu bar colour will dynamically":"menu bar colour will dynamically",
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
                "Allow OpenCore to be installed":"Allow OpenCore to be installed",
                "on natively supported Macs.":"on natively supported Macs.",
                "Note this will not allow unsupported":"Note this will not allow unsupported",
                "macOS versions to be installed on":"macOS versions to be installed on",
                "your system.":"your system.",
                "Ignore App Updates":"Ignore App Updates",
                "Github Proxy":"Github Proxy",
                "Default":"Default",
                "SimpleHac":"SimpleHac",
                "gh-proxy":"gh-proxy",
                "ghfast":"ghfast",
                "Default : https://dortania.github.io/":"Default : https://dortania.github.io/",
                "SimpleHac : https://next.oclpapi.simplehac.cn/":"SimpleHac : https://next.oclpapi.simplehac.cn/",
                "gh-proxy : https://gh-proxy.com/":"gh-proxy : https://gh-proxy.com/",
                "ghfast : https://ghfast.top/":"ghfast : https://ghfast.top/",
                "Disable Reporting":"Disable Reporting",
                "When enabled, patcher will not":"When enabled, patcher will not",
                "report any info to Hackdoc.":"report any info to Hackdoc.",
                "Remove Unused KDKs":"Remove Unused KDKs",
                "When enabled, the app will remove":"When enabled, the app will remove",
                "unused Kernel Debug Kits from the system":"unused Kernel Debug Kits from the system",
                "during root patching.":"during root patching.",
                "Manually Download KDKs and\nMetallibs":"Manually Download KDKs and\nMetallibs",
                "When enabled, patcher will allow":"When enabled, patcher will allow",
                "you download KDKs and metallibs manually.":"you download KDKs and metallibs manually.",
                "Misc":"Misc",
                "Choose Download Path":"Choose Download Path",
                "Choose":"Choose",
                "Choose Save Path":"Choose Save Path",
                "Developer":"Developer",
                "Validation":"Validation",
                "Install latest nightly build 🧪":"Install latest nightly build 🧪",
                "If you're already here, I assume you're ok":"If you're already here, I assume you're ok",
                "bricking your system 🧱.":"bricking your system 🧱.",
                "Check CHANGELOG before blindly updating.":"Check CHANGELOG before blindly updating.",
                "Trigger Exception":"Trigger Exception",
                "Export constants":"Export constants",
                "Export constants.py values to a txt file.":"Export constants.py values to a txt file.",
                "Developer Root Volume Patching":"Developer Root Volume Patching",
                "Mount Root Volume":"Mount Root Volume",
                "Life's too short to type 'sudo mount -o":"Life's too short to type 'sudo mount -o",
                "nobrowse -t apfs /dev/diskXsY":"nobrowse -t apfs /dev/diskXsY",
                "/System/Volumes/Update/mnt1' every time.":"/System/Volumes/Update/mnt1' every time.",
                "Save Root Volume":"Save Root Volume",
                "Rebuild kernel cache and bless snapshot 🙏":"Rebuild kernel cache and bless snapshot 🙏",
                "Statistics":"Statistics",
                "Populate Stats":"Populate Stats",
                "Return":"Return",
                "Populate FeatureUnlock Override":"Populate FeatureUnlock Override",
                "Inject Nvidia Kepler GOP for boot screen":"Inject Nvidia Kepler GOP for boot screen",
                "Populate Graphics Override":"Populate Graphics Override",
                "Flip individual bits corresponding to":"Flip individual bits corresponding to",
                "Currently configured SIP:":"Currently configured SIP:",
                "Currently booted SIP:":"Currently booted SIP:",
                "Description:":"Description:",
                "Cannot write to the selected directory.":"Cannot write to the selected directory." ,
                "Read-only directory":"Read-only directory",
                "Choose Path:":"Choose Path:",
                "Custom Serial Number":"Custom Serial Number",
                "Custom Board Serial Number":"Custom Board Serial Number",
                "Generate S/N:":"Generate S/N:",
                """
Application Information:
    Application Version: {0}
    PatcherSupportPkg Version: {1}
    Application Path: {2}
    Application Mount: {3}

Commit Information:
    Branch: {4}
    Date: {5}
    URL: {6}

Booted Information:
    Booted OS: XNU {7} ({8})
    Booted Patcher Version: {9}
    Booted OpenCore Version: {10}
    Booted OpenCore Disk: {11}

Hardware Information:
    {12}
""":"""
Application Information: 
    Application Version: {0} 
    PatcherSupportPkg Version: {1} 
    Application Path: {2} 
    Application Mount: {3} 
 
Commit Information: 
    Branch: {4} 
    Date: {5} 
    URL: {6} 
 
Booted Information: 
    Booted OS: XNU {7} ({8}) 
    Booted Patcher Version: {9} 
    Booted OpenCore Version: {10} 
    Booted OpenCore Disk: {11} 
 
 Hardware Information: 
    {12} 
 """,
                "Enter a custom board serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Board Serial Number\" checkbox is not checked.":"Enter a custom board serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Board Serial Number\" checkbox is not checked.",
                "Please take caution when using serial spoofing. This should only be used on machines that were legally obtained and require reserialization.\n\nNote: new serials are only overlayed through OpenCore and are not permanently installed into ROM.\n\nMisuse of this setting can break power management and other aspects of the OS if the system does not need spoofing\n\nHackdoc does not condone the use of our software on stolen devices.\n\nAre you certain you want to continue?":"Please take caution when using serial spoofing. This should only be used on machines that were legally obtained and require reserialization.\n\nNote: new serials are only overlayed through OpenCore and are not permanently installed into ROM.\n\nMisuse of this setting can break power management and other aspects of the OS if the system does not need spoofing\n\nHackdoc does not condone the use of our software on stolen devices.\n\nAre you certain you want to continue?",
                "Enter a custom serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Serial Number\" checkbox is not checked.":"Enter a custom serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Serial Number\" checkbox is not checked.",
                "This settings requires 'gpu-power-prefs' NVRAM argument to be set to '1'.\n\nIf missing and this option is toggled, the system will not boot\n\nFull command:\nnvram FA4CE28D-B62F-4C99-9CC3-6815686E30F9:gpu-power-prefs=%01%00%00%00":"This settings requires 'gpu-power-prefs' NVRAM argument to be set to '1'.\n\nIf missing and this option is toggled, the system will not boot\n\nFull command:\nnvram FA4CE28D-B62F-4C99-9CC3-6815686E30F9:gpu-power-prefs=%01%00%00%00",
                "Failed to generate serial number:":"Failed to generate serial number:",
                "GUI:custom_serial_number":"GUI:custom_serial_number",
                "GUI:custom_board_serial_number":"GUI:custom_board_serial_number",
                "GUI:fu_status":"GUI:fu_status",
                "Unknown GPU Model":"Unknown GPU Model",
                "Which branch would you like to download?":"Which branch would you like to download?",
                "Branch Selection":"Branch Selection",
                "Save Constants File":"Save Constants File",
                "Updating FU Status: Disabled":"Updating FU Status: Disabled",
                "Updating FU Status: Enabled":"Updating FU Status: Enabled",
                "Updating FU Status: Partial":"Updating FU Status: Partial",
                "Saving constants to {0}":"Saving constants to {0}",
                "Test Exception":"Test Exception",
                "Success":"Success",
                "Error":"Error",
                "Root Volume Mount Failed, check terminal output":"Root Volume Mount Failed, check terminal output",
                "Root Volume saved, please reboot to apply changes":"Root Volume saved, please reboot to apply changes",
                "Root Volume Mounted, remember to fix permissions before saving the Root Volume":"Root Volume Mounted, remember to fix permissions before saving the Root Volume",
                "This option should only be used if your Mac natively supports the OSes you wish to run.\n\nIf you are currently running an unsupported OS, this option will break booting. Only toggle for enabling OS features on a native Mac.\n\nAre you certain you want to continue?":"This option should only be used if your Mac natively supports the OSes you wish to run.\n\nIf you are currently running an unsupported OS, this option will break booting. Only toggle for enabling OS features on a native Mac.\n\nAre you certain you want to continue?",
                "Using Real Model: {model}":"Using Real Model: {model}",
                "Using Custom Model: {selection}":"Using Custom Model: {selection}",
                "Model: {selection}":"Model: {selection}",
                "warning":"warning",
                "Warning":"Warning",
                "Updating Local Setting: {variable} = {value}":"Updating Local Setting: {variable} = {value}",
                "Updating Global Setting: {variable} = {value}":"Updating Global Setting: {variable} = {value}",
                "Initializing Settings Frame":"Initializing Settings Frame",
                "Choose Your Language":"Choose Your Language",
                "Provide English & Chinese Simplified.":"Provide English & Chinese Simplified.",
                "Updating System Defaults: {variable} = {value} ({value_type})":"Updating System Defaults: {variable} = {value} ({value_type})",
                "Updating System Defaults (root): {variable} = {value} ({value_type})":"Updating System Defaults (root): {variable} = {value} ({value_type})",
            }
        elif self.language_point=="简体中文":
            trans={
                "Initializing Settings Frame":"初始化设置框架",
                "Choose Your Language":"选择您的语言",
                "Provide English & Chinese Simplified.":"提供英文和简体中文",
                "Updating System Defaults (root): {variable} = {value} ({value_type})":"更新系统默认值（root）：{variable} = {value} ({value_type})",
                "Updating System Defaults: {variable} = {value} ({value_type})":"更新系统默认值：{variable} = {value} ({value_type})",
                "Updating Global Setting: {variable} = {value}":"更新全局设置：{variable} = {value}",
                "Updating Local Setting: {variable} = {value}":"更新本地设置：{variable} = {value}",
                "Warning":"警告",
                "warning":"警告",
                "Model: {selection}":"机型：{selection}",
                "Using Real Model: {model}":"使用真实机型：{model}",
                "Using Custom Model: {selection}":"使用自定义机型：{selection}",
                "This option should only be used if your Mac natively supports the OSes you wish to run.\n\nIf you are currently running an unsupported OS, this option will break booting. Only toggle for enabling OS features on a native Mac.\n\nAre you certain you want to continue?":"此选项仅在您的 Mac 原生支持您要运行的操作系统时才应使用。\n\n如果您当前正在运行不受支持的操作系统，此选项使Mac无法启动。仅在您的 Mac 原生支持操作系统时才切换以启用操作系统功能。\n\n您确定要继续吗？",
                "Root Volume Mount Failed, check terminal output":"根卷挂载失败，请检查终端输出",
                "Error":"错误",
                "Root Volume saved, please reboot to apply changes":"已保存快照，请重新启动以应用更改",
                "Success":"成功",
                "Root Volume Mounted, remember to fix permissions before saving the Root Volume":"根卷已挂载，请修复权限后再保存根卷",
                "Test Exception":"测试异常",
                "Saving constants to {0}":"保存 Constants 文件到 {0}",
                "Updating FU Status: Partial":"更新功能解锁状态：部分",
                "Updating FU Status: Enabled":"更新功能解锁状态：已启用",
                "Updating FU Status: Disabled":"更新功能解锁状态：已禁用",
                "Save Constants File":"保存Constants文件",
                "Branch Selection":"分支选择",
                "Which branch would you like to download?":"您想下载哪个分支？",
                "Unknown GPU Model":"未知 GPU 型号",
                "GUI:fu_arguments":"GUI:功能解锁参数",
                "GUI:fu_status":"GUI:功能解锁状态",
                "GUI:custom_board_serial_number":"GUI:自定义主板序列号",
                "GUI:custom_serial_number":"GUI:自定义序列号",
                "Failed to generate serial number:":"生成序列号失败:",
                "Please take caution when using serial spoofing. This should only be used on machines that were legally obtained and require reserialization.\n\nNote: new serials are only overlayed through OpenCore and are not permanently installed into ROM.\n\nMisuse of this setting can break power management and other aspects of the OS if the system does not need spoofing\n\nHackdoc does not condone the use of our software on stolen devices.\n\nAre you certain you want to continue?":"请谨慎使用序列号仿冒功能。此功能仅适用于合法获取且需要重新序列化的设备。\n\n注意：新序列号仅通过 OpenCore 覆盖，不会永久写入 ROM。\n\n如果系统不需要序列号仿冒，滥用此设置可能会破坏电源管理以及操作系统的其他功能。\n\nHackdoc,Ghltbm 严厉禁止在被盗设备上使用我们的软件.若发现,将会通过法律和MIT License追究责任.\n\n您确定要继续吗?",
                """
Application Information:
    Application Version: {0}
    PatcherSupportPkg Version: {1}
    Application Path: {2}
    Application Mount: {3}

Commit Information:
    Branch: {4}
    Date: {5}
    URL: {6}

Booted Information:
    Booted OS: XNU {7} ({8})
    Booted Patcher Version: {9}
    Booted OpenCore Version: {10}
    Booted OpenCore Disk: {11}

Hardware Information:
    {12}
""":"""
应用程序信息：
    应用程序版本：{0}
    补丁支持包版本：{1}
    应用程序路径：{2}
    应用程序挂载点：{3}

提交信息：
    分支：{4}
    日期：{5}
    URL：{6}

启动信息：
    启动的操作系统：XNU {7} ({8})
    启动的补丁程序版本：{9}
    启动的 OpenCore 版本：{10}
    启动的 OpenCore 磁盘：{11}

硬件信息：
    {12}
""",
                "Generate S/N:":"生成 S/N:",
                "Enter a custom board serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Board Serial Number\" checkbox is not checked.":"输入自定义主板序列号，将用于 SMBIOS 和 iMessage。\n\n注意：如果未选中 \"使用自定义主板序列号\" 复选框，则此设置将不被使用。",
                "Custom Board Serial Number":"自定义主板序列号",
                "Enter a custom serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Serial Number\" checkbox is not checked.":"输入自定义序列号，将用于 SMBIOS 和 iMessage。\n\n注意：如果未选中 \"使用自定义序列号\" 复选框，则此设置将不被使用。",
                "Custom Serial Number":"自定义序列号",
                "Read-only directory":"只读目录",
                "Choose Path:":"选择路径:",
                "Cannot write to the selected directory.":"无法写入选择的目录。",
                "Description:":"描述:",
                "Currently booted SIP:":"当前启动的 SIP:",
                "Currently configured SIP:":"当前配置的 SIP:",
                "Flip individual bits corresponding to":"翻转对应 XNU csr.h 位",
                "Populate SIP":"填充 SIP",
                "Populate Graphics Override":"填充图形覆盖",
                "Inject Nvidia Kepler GOP for boot screen":"注入 Nvidia Kepler GOP 以启动屏幕",
                "Populate FeatureUnlock Override":"Populate FeatureUnlock Override",
                "Target Model":"目标机型",
                "Host Model":"主机机型",
                "Overrides Mac Model the Patcher will build for.":"覆盖补丁程序将构建的 Mac 机型。",
                "Build":"构建",
                "General":"常规",
                "FireWire Booting":"FireWire 启动",
                "Enable booting macOS from":"启用从",
                "FireWire drives.":"FireWire 驱动器启动 macOS。",
                "XHCI Booting":"XHCI 启动",
                "Enable booting macOS from add-in":"启用从添加的",
                "USB 3.0 expansion cards on systems":"USB 3.0 扩展卡",
                "without native support.":"在没有原生支持的系统上启动 macOS。",
                "NVMe Booting":"NVMe 启动",
                "Enable booting macOS from NVMe":"启用从 NVMe",
                "drives on systems without native":"驱动器",
                "support.":"在没有原生支持的系统上启动 macOS。",
                "Note: Requires Firmware support":"注：需要固件支持",
                "for OpenCore to load from NVMe.":"才能从 NVMe 加载 OpenCore。",
                "OpenCore Vaulting":"OpenCore 加密",
                "Digitally sign OpenCore to prevent":"对 OpenCore 进行数字签名以防止",
                "tampering or corruption.":"篡改或损坏。",
                "Show OpenCore Boot Picker":"显示 OpenCore 启动选择器",
                "When disabled, users can hold ESC to":"禁用时，用户可以按住 ESC 键",
                "show picker in the firmware.":"在固件中显示选择器。",
                "Boot Picker Timeout":"启动选择器超时",
                "Timeout before boot picker selects default":"启动选择器选择默认项前的超时时间",
                "entry in seconds.":"（秒）。",
                "Set to 0 for no timeout.":"设置为 0 表示无超时。",
                "MacPro3,1/Xserve2,1 Workaround":"MacPro3,1/Xserve2,1 解决方法",
                "Limits to 4 threads max on these units.":"在这些设备上限制最多 4 个线程。",
                "Required for macOS Sequoia and later.":"macOS Sequoia 及更高版本需要。",
                "Debug":"调试",
                "Verbose":"详细输出",
                "Verbose output during boot.":"启动期间显示详细输出。",
                "Kext Debugging":"Kext 调试",
                "Use DEBUG variants of kexts and":"使用 kext 的 DEBUG 版本并",
                "enables additional kernel logging.":"启用额外的内核日志记录。",
                "OpenCore Debugging":"OpenCore 调试",
                "Use DEBUG variant of OpenCore":"使用 OpenCore 的 DEBUG 版本",
                "and enables additional logging.":"并启用额外的日志记录。",
                "Extras":"额外",
                "General (Continued)":"常规（续）",
                "Wake on WLAN":"无线局域网唤醒",
                "Disabled by default due to":"默认禁用，因为",
                "performance degradation":"某些系统从唤醒状态",
                "on some systems from wake.":"恢复时性能会下降。",
                "Only applies to BCM943224, 331,":"仅适用于 BCM943224、331、",
                "360 and 3602 chipsets.":"360 和 3602 芯片组。",
                "Disable Thunderbolt":"禁用 Thunderbolt",
                "For MacBookPro11,x with faulty":"适用于带有",
                "PCHs that may crash sporadically.":"可能偶尔崩溃的故障 PCH 的 MacBookPro11,x。",
                "Windows GMUX":"Windows GMUX",
                "Allow iGPU to be exposed in Windows":"允许 iGPU 在 Windows 中暴露，",
                "for dGPU-based MacBooks.":"适用于基于 dGPU 的 MacBook。",
                "Disable CPUFriend":"禁用 CPUFriend",
                "Choose Save Path":"选择保存目录",
                "Disables power management helper":"禁用电源管理助手",
                "for unsupported models.":"对于不支持的机型。",
                "Disable mediaanalysisd service":"禁用 mediaanalysisd 服务",
                "For systems that are the primary iCloud":"对于作为主要 iCloud",
                "Photo Library host with a 3802-based GPU,":"照片库主机且带有 3802 系列 GPU 的系统，",
                "this may aid in prolonged idle stability.":"这可能有助于延长空闲稳定性。",
                "Allow AppleALC Audio":"允许 AppleALC 音频",
                "Allow AppleALC to manage audio":"允许 AppleALC 管理音频",
                "if applicable.":"在适用时。",
                "Only disable if your host lacks":"仅在主机缺少",
                "a GOP ROM.":"GOP ROM 时禁用。",
                "NVRAM WriteFlash":"NVRAM 写入",
                "Allow OpenCore to write to NVRAM.":"允许 OpenCore 写入 NVRAM。",
                "Disable on systems with faulty or":"在 NVRAM",
                "degraded NVRAM.":"故障或降级的系统上禁用。",
                "3rd Party NVMe PM":"第三方 NVMe 电源管理",
                "Enable non-stock NVMe power":"在 macOS 中启用非原厂 NVMe",
                "management in macOS.":"电源管理。",
                "3rd Party SATA PM":"第三方 SATA 电源管理",
                "Enable non-stock SATA power":"在 macOS 中启用非原厂 SATA",
                "management in macOS.":"电源管理。",
                "APFS Trim":"APFS Trim",
                "Recommended for all users, however faulty":"建议所有用户使用，但有故障的",
                "SSDs may benefit from disabling this.":"SSD 可能受益于禁用此功能。",
                "Advanced":"高级",
                "Miscellaneous":"杂项",
                "Disable Firmware Throttling":"禁用固件限制",
                "Disables firmware-based throttling":"禁用基于固件的限制",
                "caused by missing hardware.":"由缺少硬件引起。",
                "Ex. Missing Display, Battery, etc.":"例如：缺少显示器、电池等。",
                "Software DeMUX":"Software DeMUX",
                "Enable software based DeMUX":"启用基于软件的 DeMUX",
                "for MacBookPro8,2 and MacBookPro8,3.":"为 MacBookPro8,2 和 MacBookPro8,3。",
                "Prevents faulty dGPU from turning on.":"防止故障 dGPU 开启。",
                "Note: Requires associated NVRAM arg:":"注：需要关联的 NVRAM 参数：",
                "'gpu-power-prefs'.":"'gpu-power-prefs'。",
                "FeatureUnlock":"FeatureUnlock",
                "Enabled":"已启用",
                "Partial":"部分",
                "Disabled":"已禁用",
                "Configure FeatureUnlock level.":"配置 FeatureUnlock 级别。",
                "Recommend lowering if your system":"如果系统出现",
                "experiences memory instability.":"内存不稳定，建议降低级别。",
                "Hibernation Work-around":"休眠解决方法",
                "Only load minimum EFI drivers":"仅加载最少的 EFI 驱动程序",
                "to prevent hibernation issues.":"以防止休眠问题。",
                "Note: This may break booting from":"注：这可能会破坏从",
                "external drives.":"外部驱动器启动。",
                "Graphics":"图形",
                "AMD GOP Injection":"AMD GOP 注入",
                "Inject AMD GOP for boot screen":"为 PC GPU 注入 AMD GOP",
                "support on PC GPUs.":"以支持启动屏幕。",
                "Nvidia GOP Injection":"Nvidia GOP 注入",
                "Inject Nvidia Kepler GOP for boot":"为 PC GPU 注入 Nvidia Kepler GOP",
                "screen support on PC GPUs.":"以支持启动屏幕。",
                "Graphics Override":"图形覆盖",
                "None":"无",
                "Nvidia Kepler":"Nvidia Kepler",
                "AMD GCN":"AMD GCN",
                "AMD Polaris":"AMD Polaris",
                "AMD Lexa":"AMD Lexa",
                "AMD Navi":"AMD Navi",
                "Override detected/assumed GPU on":"覆盖基于 MXM 插槽的 iMac 上",
                "socketed MXM-based iMacs.":"检测到/假设的 GPU。",
                "Security":"安全",
                "Kernel Security":"内核安全",
                "Disable Library Validation":"禁用库验证",
                "Required for loading modified":"从根补丁加载修改后的",
                "system files from root patching.":"系统文件所需。",
                "Disable AMFI":"禁用 AMFI",
                  "Extended version of 'Disable":"'禁用库验证'的扩展版本，",
                  "Library Validation', required":"具有较深根补丁的系统",
                  "for systems with deeper":"需要。",
                  "root patches.":"",
                "Secure Boot Model":"安全启动机型",
                  "Set Apple Secure Boot Model Identifier":"如果进行仿冒，将 Apple 安全启动机型标识符",
                  "to matching T2 model if spoofing.":"设置为匹配的 T2 机型。",
                  "Note: Incompatible with Root Patching.":"注：与根补丁不兼容。",
                "System Integrity Protection":"系统完整性保护",
                "SMBIOS":"SMBIOS",
                "Model Spoofing":"机型仿冒",
                "SMBIOS Spoof Level":"SMBIOS 仿冒级别",
                "None":"无",
                "Minimal":"最小",
                "Moderate":"适度",
                "Advanced":"高级",
                "Supported Levels:":"支持的级别：",
                  "   - None: No spoofing.":"   - 无：不进行仿冒。",
                  "   - Minimal: Overrides Board ID.":"   - 最小：覆盖 Board ID。",
                  "   - Moderate: Overrides Model.":"   - 适度：覆盖机型。",
                  "   - Advanced: Overrides Model and serial.":"   - 高级：覆盖机型和序列号。",
                "SMBIOS Spoof Model":"SMBIOS 仿冒机型",
                "Default":"默认",
                "Set Mac Model to spoof to.":"设置要仿冒的 Mac 机型。",
                "Allow spoofing native Macs":"允许仿冒原生 Mac",
                "Allow OpenCore to spoof natively":"允许 OpenCore 仿冒原生",
                  "supported Macs.":"支持的 Mac。",
                  "Primarily used for enabling":"主要用于启用",
                  "Universal Control on unsupported Macs":"在不支持的 Mac 上的通用控制。",
                "Serial Spoofing":"序列号仿冒",
                "Patch":"补丁",
                "Patch-General":"补丁-通用",
                "TeraScale 2 Acceleration":"TeraScale 2 加速",
                "Enable AMD TeraScale 2 GPU":"启用 AMD TeraScale 2 GPU",
                  "Acceleration on MacBookPro8,2 and":"在 MacBookPro8,2 和",
                  "MacBookPro8,3.":"MacBookPro8,3 上的加速。",
                  "By default this is disabled due to":"默认禁用，因为",
                  "common GPU failures on these models.":"这些机型常见 GPU 故障。",
                "Audio Patch choice":"音频补丁选择",
                "AppleHDA":"AppleHDA",
                "VoodooHDA":"VoodooHDA",
                "   - AppleALC: AppleALC patch on Tahoe.":"   - AppleALC: Tahoe 上的 AppleALC 补丁。",
                "   - VoodooHDA: VoodooHDA patch ,":"   - VoodooHDA: VoodooHDA 补丁，",
                "  on Monterey and newer.":"  在 Monterey 及更高版本上。",
                "  Not recommended.":"  不推荐。",
                "Allow Tahoe Modern USB Patch":"允许 Tahoe 现代 USB 补丁",
                "When enabled, this will patch the Old USB":"启用时，这将修补旧 USB",
                "extensions on Tahoe.":"在 Tahoe 上的扩展。",
                "Allow APFS Patch For Non-T2":"允许非 T2 设备的 APFS 补丁",
                "When enabled, this will patch the apfs.efi":"启用时，这将修补 apfs.efi",
                "on Tahoe.":"在 Tahoe 上。",
                "AppleHDA.kext Version":"AppleHDA.kext 版本",
                "Non-Metal":"非 Metal",
                "Non-Metal Settings":"非 Metal 设置",
                "Log out required to apply changes to SkyLight":"应用更改到 SkyLight 需要注销",
                "Dark Menu Bar":"深色菜单栏",
                "If Beta Menu Bar is enabled,":"如果启用了测试版菜单栏，",
                "menu bar colour will dynamically":"菜单栏颜色将动态变化",
                "Beta Blur":"测试版模糊",
                "Control window blur behaviour.":"控制窗口模糊行为。",
                "Beach Ball Cursor Workaround":"彩虹球球光标解决方法",
                "Control beach ball cursor behaviour.":"控制彩虹球光标行为。\n注意这会占用更多CPU资源",
                "Beta Menu Bar":"测试版菜单栏",
                "Supports dynamic colour changes.":"支持动态颜色变化。",
                "Disable Beta Rim":"禁用测试版边框",
                "Control Window Rim rendering.":"控制窗口边框渲染。",
                "Disable Color Widgets Enforcement":"禁用颜色小组件强制执行",
                "Control Color Desktop Widgets Enforcement.":"控制彩色桌面小组件强制。",
                "App":"应用",
                "General":"常规",
                "Allow native models":"允许原生机型",
                "Allow OpenCore to be installed":"允许在原生支持的 Mac 上",
                  "on natively supported Macs.":"安装 OpenCore。",
                  "Note this will not allow unsupported":"请注意，这不会允许",
                  "macOS versions to be installed on":"在您的系统上安装",
                  "your system.":"不支持的 macOS 版本。",
                "Ignore App Updates":"忽略应用更新",
                "Github Proxy":"Github 代理",
                "Default":"默认",
                "SimpleHac":"SimpleHac",
                "gh-proxy":"gh-proxy",
                "ghfast":"ghfast",
                "Default : https://dortania.github.io/":"默认 : https://dortania.github.io/",
                  "SimpleHac : https://next.oclpapi.simplehac.cn/":"SimpleHac : https://next.oclpapi.simplehac.cn/",
                  "gh-proxy : https://gh-proxy.com/":"gh-proxy : https://gh-proxy.com/",
                  "ghfast : https://ghfast.top/":"ghfast : https://ghfast.top/",
                  "Default : https://dortania.github.io/":"默认 : https://dortania.github.io/",
                "SimpleHac : https://next.oclpapi.simplehac.cn/":"SimpleHac : https://next.oclpapi.simplehac.cn/",
                "gh-proxy : https://gh-proxy.com/":"gh-proxy : https://gh-proxy.com/",
                "ghfast : https://ghfast.top/":"ghfast : https://ghfast.top/",
                "Disable Reporting":"禁用报告",
                  "When enabled, patcher will not":"启用时，补丁程序不会",
                  "report any info to Hackdoc.":"向 Hackdoc 报告任何信息。",
                  "When enabled, patcher will not":"启用时，补丁程序不会",
                  "report any info to Hackdoc.":"向 Hackdoc 报告任何信息。",
                "Remove Unused KDKs":"移除未使用的 KDK",
                  "When enabled, the app will remove":"启用时，应用程序将在根补丁期间",
                  "unused Kernel Debug Kits from the system":"从系统中移除未使用的",
                  "during root patching.":"内核调试工具包。",
                  "When enabled, the app will remove":"启用时，应用程序将移除",
                  "unused Kernel Debug Kits from the system":"未使用的内核调试工具包",
                  "during root patching.":"在根补丁期间。",
                "Manually Download KDKs and\nMetallibs":"手动下载 KDK 和 Metallib",
                "When enabled, patcher will allow":"启用时，补丁程序将允许",
                "you download KDKs and metallibs manually.":"您手动下载 KDK 和 metallib。",
                "Misc":"杂项",
                "Choose Download Path":"选择下载路径",
                "Choose":"选择",
                "Developer":"开发者",
                "Validation":"验证",
                "Install latest nightly build 🧪":"安装最新的夜间构建 🧪",
                "If you're already here, I assume you're ok":"如果你已经在这里，我假设你愿意",
                "bricking your system 🧱.":"让你的系统变砖 🧱.",
                "Check CHANGELOG before blindly updating.":"在盲目更新前查看 CHANGELOG。",
                "Trigger Exception":"触发异常",
                "Export constants":"导出常量",
                "Export constants.py values to a txt file.":"将 constants.py 值导出到 txt 文件。",
                "Developer Root Volume Patching":"开发者根卷补丁",
                "Mount Root Volume":"挂载根卷",
                "Life's too short to type 'sudo mount -o":"人生苦短，何必每次都输入 'sudo mount -o",
                "nobrowse -t apfs /dev/diskXsY":"nobrowse -t apfs /dev/diskXsY",
                "/System/Volumes/Update/mnt1' every time.":"/System/Volumes/Update/mnt1'.",
                "Save Root Volume":"保存根卷",
                "Rebuild kernel cache and bless snapshot 🙏":"重建内核缓存并祝福快照别寄(bushi~) 🙏",
                "Statistics":"统计信息",
                "Populate Stats":"填充统计信息",
                "Return":"返回",
                "This settings requires 'gpu-power-prefs' NVRAM argument to be set to '1'.\n\nIf missing and this option is toggled, the system will not boot\n\nFull command:\nnvram FA4CE28D-B62F-4C99-9CC3-6815686E30F9:gpu-power-prefs=%01%00%00%00":"此设置需要 'gpu-power-prefs' NVRAM 参数设置为 '1'。\n\n如果缺失且此选项被切换，系统将无法启动\n\n完整命令：\nnvram FA4CE28D-B62F-4C99-9CC3-6815686E30F9:gpu-power-prefs=%01%00%00%00"
            }
        return trans
    
    def gui_support(self):
        if self.language_point=="English":
            trans={
                "&About OCLP-R":"&About OCLP-R",
                "&Reveal Log File":"&Reveal Log File",
                "During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.":"During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.",
                "Internal Error occurred!":"Internal Error occurred!",
                "Reboot to apply?":"Reboot to apply?",
                "Reboot":"Reboot",
                "Ignore":"Ignore",
                "Error while trying to reboot:":"Error while trying to reboot:"
            }
        elif self.language_point=="简体中文":
            trans={
                "&About OCLP-R":"&关于 OCLP-R",
                "&Reveal Log File":"&显示日志文件",
                "During unpacking of our internal files, we seemed to have encountered an error.\n\nIf you keep seeing this error, please try rebooting and redownloading the application.":"在解包我们的内部文件时，我们似乎遇到了错误。\n\n如果您继续看到此错误，请尝试重启并重新下载应用程序。",
                "Internal Error occurred!":"发生内部错误！",
                "Reboot to apply?":"是否重启应用？",
                "Reboot":"重启",
                "Ignore":"忽略",
                "Error while trying to reboot:":"重启时出错："
            }
        return trans
    
    def gui_sys_patch_display(self):
        if self.language_point=="English":
            trans={
                "Built from source, running from socure":"Built from source, running from socure",
                "Checking if new patches are needed":"Checking if new patches are needed",
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
        elif self.language_point=="简体中文":
            trans={
                "Built from source, running from socure":"以源代码运行",
                "Checking if new patches are needed":"检查是否需要新的补丁",
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
        if self.language_point=="English":
            trans={
                "An internal error occurred while running the Root Patcher:\n":"An internal error occurred while running the Root Patcher:\n",
                "Starting root patching":"Starting root patching",
                "Metallib installation complete":"Metallib installation complete",
                "Metallib download complete, installing Metallib PKG":"Metallib download complete, installing Metallib PKG",
                "MetallibSupportPkg missing, generating Metallib download frame":"MetallibSupportPkg missing, generating Metallib download frame",
                "KDK missing, generating KDK download frame":"KDK missing, generating KDK download frame",
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
                "Ignore":"Ignore",
                "Error":"Error",
                "Reverting root patches":"Reverting root patches",
                "KDK download complete, validating with hdiutil":"KDK download complete, validating with hdiutil",
                "KDK download complete":"KDK download complete",
                "Metallib Build ":"Metallib Build ",
                "Unsupported variant:":"Unsupported variant:",
                "Root Patching":"Root Patching",
                "Available patches:":"Available patches:",
                "Checking if new patches are needed":"Checking if new patches are needed",
                "No new patches detected for system":"No new patches detected for system",
                "- Patch {patch} not installed":"- Patch {patch} not installed",
                "Built from source, running from socure":"Built from source, running from socure",
            }
        elif self.language_point=="简体中文":
            trans={
                "Built from source, running from socure":"以源代码运行",
                "- Patch {patch} not installed":"- 补丁 {patch} 未安装",
                "No new patches detected for system":"没有新的系统补丁",
                "Checking if new patches are needed":"检查是否有新的补丁需要应用",
                "An internal error occurred while running the Root Patcher:\n":"运行根卷补丁器时发生内部错误：\n",
                "Starting root patching":"开始根卷补丁",
                "Available patches:":"可用补丁：",
                "Root Patching":"根卷补丁",
                "Unsupported variant:":"不支持的版本:",
                "Metallib installation complete":"Metallib 安装完成",
                "Metallib download complete, installing Metallib PKG":"Metallib 下载完成，正在安装 Metallib PKG",
                "Metallib Build ":"Metallib 构建 ",
                "MetallibSupportPkg missing, generating Metallib download frame":"MetallibSupportPkg 缺失，正在生成 Metallib 下载框架",
                "KDK download complete":"KDK 下载完成",
                "KDK download complete, validating with hdiutil":"KDK 下载完成，正在使用 hdiutil 验证",
                "Error":"错误",
                "KDK missing, generating KDK download frame":"KDK 缺失，正在生成 KDK 下载框架",
                "Downloading Kernel Debug Kit":"正在下载内核调试工具包",
                "Fetching KDK database...":"正在获取 KDK 数据库...",
                "KDK download failed: ":"KDK 下载失败：",
                "Validating KDK: ":"正在验证 KDK: ",
                "Checking if checksum is valid...":"正在检查校验和是否有效...",
                "KDK checksum validation failed: ":"KDK 校验和验证失败：",
                "Downloading Metal Libraries":"正在下载 Metal 库",
                "Fetching MetallibSupportPkg database...":"正在获取 MetallibSupportPkg 数据库...",
                "Metallib download failed: ":"Metallib 下载失败：",
                "Installing Metallib: ":"正在安装 Metallib: ",
                "Installing MetallibSupportPkg PKG...":"正在安装 MetallibSupportPkg 包...",
                "Metallib installation failed: ":"Metallib 安装失败: ",
                "Root Patching":"根卷补丁",
                "Reverting root patches":"还原根补丁",
                "Revert Root Patches":"还原根卷补丁",
                "Root Patching will patch the following:":"根卷补丁将修补以下内容: ",
                "No patches to apply":"没有补丁可应用",
                "Reverting to last sealed snapshot":"正在还原到最后一个密封快照",
                "Return to Main Menu":"返回主菜单",
                "Root Patcher finished successfully!\n\nWould you like to reboot now?":"根卷补丁成功完成！\n\n您现在想要重启吗？",
                "Root Patcher finished successfully!\nIf you were prompted to open System Settings to authorize new kexts, this can be ignored. Your system is ready once restarted.\n\nWould you like to reboot now?":"根卷补丁成功完成！\n如果您被提示打开系统设置以授权新的 kext, 这可以忽略。您的系统重启后即可使用。\n\n您现在想要重启吗?",
                "We just finished installing the patches to your Root Volume!\n\nHowever, Apple requires users to manually approve the kernel extensions installed before they can be used next reboot.\n\nWould you like to open System Preferences?":"我们刚刚完成了对您根卷的补丁安装！\n\n但, Apple 要求用户手动批准安装的内核扩展，然后才能在下次重启时使用它们。\n\n您想要打开系统偏好设置吗?",
                "Open System Preferences?":"打开系统偏好设置？",
                "Open System Preferences":"打开系统偏好设置",
                "Ignore":"忽略"
            }
        return trans
    
    def gui_update(self):
        if self.language_point=="English":
            trans={
                "Failed to install update.":"Failed to install update.",
                "Extracting nightly update":"Extracting nightly update",
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
                " seconds":" seconds",
                "Initializing Update Frame":"Initializing Update Frame",
                "Update URL: {url}":"Update URL: {url}",
                "Update Version: {version_label}":"Update Version: {version_label}",
                "Failed to extract update.":"Failed to extract update.",
                "Failed to extract update. Error: {0}":"Failed to extract update. Error: {0}",
                "Installing update: {0}":"Installing update: {0}",
                "User cancelled update":"User cancelled update",
                "User cancelled":"User cancelled",
                "Update Cancelled":"Update Cancelled",
                "Failed to install update, attempting to open PKG":"Failed to install update, attempting to open PKG",
                "has been installed:":"has been installed:",
                "close_chinese":"",
                "Closing old process in":"Closing old process in",
                "seconds":"seconds",
                "Failed to install update. Please try installing the OCLP-R.pkg manually or download from GitHub":"Failed to install update. Please try installing the OCLP-R.pkg manually or download from GitHub",
            }
        elif self.language_point=="简体中文":
            trans={
                "seconds":"秒",
                "Closing old process in":"此进程将在",
                "close_chinese":"内关闭",
                "has been installed:":"已安装到:",
                "Failed to install update. Please try installing the OCLP-R.pkg manually or download from GitHub":"安装更新失败。请手动安装 OCLP-R.pkg 或从 GitHub 下载。",
                "Failed to install update, attempting to open PKG":"安装更新失败，正在尝试打开 PKG 文件。",
                "Failed to install update.":"安装更新失败。",
                "Update Cancelled":"更新已取消",
                "User cancelled update":"用户取消更新",
                "User cancelled":"用户取消",
                "Installing update: {0}":"正在安装更新: {0}",
                "Failed to extract update. Error: {0}":"提取更新失败。错误：{0}",
                "Failed to extract update.":"提取更新失败。",
                "Extracting nightly update":"提取夜间更新",
                "Update Version: {version_label}":"更新版本: {version_label}",
                "Update URL: {url}":"更新 URL: {url}",
                "Initializing Update Frame":"初始化更新框架",
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
class TranslateLanguage_sys_patch:
    def __init__(self, global_constants = None) -> None:
        self.file_name:              str = ".com.hackdoc.oclp-r.plist"
        self.global_settings_folder: str = "/Users/Shared"
        self.global_settings_plist:  str = f"{self.global_settings_folder}/{self.file_name}"
        try:
            self.plist = load(Path(self.global_settings_plist).open("rb"))
            self.language_point = self.plist["GUI:language_option"]
        except Exception:
            self.language_point = "English"
    def detect(self):
        if self.language_point=="English":
            trans={
                "- Breakdown:":"- Breakdown:",
                "Network connection missing, checking whether network patches are applicable":"Network connection missing, checking whether network patches are applicable",
                "Failed to parse diskutil output.":"Failed to parse diskutil output.",
                "FileVault is Off":"FileVault is Off",
                "Settings: Kernel Debug Kit required":"Settings: Kernel Debug Kit required",
                "Settings: Kernel Debug Kit missing":"Settings: Kernel Debug Kit missing",
                "Settings: MetallibSupportPkg.pkg required":"Settings: MetallibSupportPkg.pkg required",
                "Settings: MetallibSupportPkg.pkg missing":"Settings: MetallibSupportPkg.pkg missing",
                "Validation: Unsupported Host OS":"Validation: Unsupported Host OS",
                "Validation: Missing Network Connection":"Validation: Missing Network Connection",
                "Validation: FileVault is enabled":"Validation: FileVault is enabled",
                "Validation: System Integrity Protection is enabled":"Validation: System Integrity Protection is enabled",
                "Validation: SecureBootModel is enabled":"Validation: SecureBootModel is enabled",
                "Validation: AMFI is enabled":"Validation: AMFI is enabled",
                "Validation: WhateverGreen.kext missing":"Validation: WhateverGreen.kext missing",
                "Validation: Force OpenGL property missing":"Validation: Force OpenGL property missing",
                "Validation: Force compat property missing":"Validation: Force compat property missing",
                "Validation: nvda_drv(_vrl) variable missing":"Validation: nvda_drv(_vrl) variable missing",
                "Validation: Patching not possible":"Validation: Patching not possible",
                "Validation: Unpatching not possible":"Validation: Unpatching not possible",
                "Validation: Root volume dirty":"Validation: Root volume dirty",
                "System volume is tainted, unpatching is required":"System volume is tainted, unpatching is required",
                "Installed patches are from different commit, unpatching is required":"Installed patches are from different commit, unpatching is required",
                "Patch(es) already installed: {0}, unpatching is required":"Patch(es) already installed: {0}, unpatching is required",
                "Network patches are already applied, requiring network connection":"Network patches are already applied, requiring network connection",
                "Network patches are applicable, removing other patches":"Network patches are applicable, removing other patches",
                "Network patches are not applicable, requiring network connection":"Network patches are not applicable, requiring network connection",
            }
        elif self.language_point=="简体中文":
            trans={
                "- Breakdown:":"- 分析",
                "Network patches are applicable, removing other patches":"网络补丁可用，会移除其他补丁",
                "Network patches are not applicable, requiring network connection":"网络补丁不适用，需要网络连接",
                "Network patches are already applied, requiring network connection":"网络补丁已应用，需要网络连接",
                "Network connection missing, checking whether network patches are applicable":"无网络连接，检测网络补丁是否可用",
                "Patch(es) already installed: {0}, unpatching is required":"已安装的补丁：{0}，需要取消修补",
                "Installed patches are from different commit, unpatching is required":"已安装的补丁来自不同的提交，需要取消修补",
                "System volume is tainted, unpatching is required":"系统卷已被修改，需要取消修补",
                "Failed to parse diskutil output.":"解析diskutil输出失败",
                "FileVault is Off":"文件保险箱已关闭",
                "Settings: Kernel Debug Kit required":"Settings: 需要内核调试工具包",
                "Settings: Kernel Debug Kit missing":"Settings: 缺少内核调试工具包",
                "Settings: MetallibSupportPkg.pkg required":"Settings: 需要MetallibSupportPkg.pkg",
                "Settings: MetallibSupportPkg.pkg missing":"Settings: 缺少MetallibSupportPkg.pkg",
                "Validation: Unsupported Host OS":"Validation: 不支持的主机操作系统",
                "Validation: Missing Network Connection":"Validation: 缺少网络连接",
                "Validation: FileVault is enabled":"Validation: 文件保险箱已启用",
                "Validation: System Integrity Protection is enabled":"Validation: 系统完整性保护已启用",
                "Validation: SecureBootModel is enabled":"Validation: SecureBootModel已启用",
                "Validation: AMFI is enabled":"Validation: AMFI已启用",
                "Validation: WhateverGreen.kext missing":"Validation: 缺少WhateverGreen.kext",
                "Validation: Force OpenGL property missing":"Validation: 缺少强制OpenGL属性",
                "Validation: Force compat property missing":"Validation: 缺少强制兼容属性",
                "Validation: nvda_drv(_vrl) variable missing":"Validation: 缺少nvda_drv(_vrl)变量",
                "Validation: Patching not possible":"Validation: 无法修补",
                "Validation: Unpatching not possible":"Validation: 无法取消修补",
                "Validation: Root volume dirty":"Validation: 根卷目录已被修补"
            }
        return trans
    def auto_patcher(self):
        if self.language_point=="English":
            trans={
                "- Skipping Auto Patcher Launch Agent, not supported when running from source":"- Skipping Auto Patcher Launch Agent, not supported when running from source",
                "- Installing {name}":"- Installing {name}",
                "  - {name} checksums match, skipping":"  - {name} checksums match, skipping",
                "  - Existing service found, removing":"  - Existing service found, removing",
                "  - Creating {path} directory":"  - Creating {path} directory",
                "- Checking if RSRMonitor is needed":"- Checking if RSRMonitor is needed",
                "- No OS.dmg, skipping RSRMonitor":"- No OS.dmg, skipping RSRMonitor",
                "  - Failed to check if {name} is a directory: {error}":"  - Failed to check if {name} is a directory: {error}",
                "  - Failed to load plist for {name}: {error}":"  - Failed to load plist for {name}: {error}",
                "  - Found kext with GPUCompanionBundles: {name}":"  - Found kext with GPUCompanionBundles: {name}",
                "- No kexts found with GPUCompanionBundles, skipping RSRMonitor":"- No kexts found with GPUCompanionBundles, skipping RSRMonitor",
                "  - Adding monitor: {path}":"  - Adding monitor: {path}",
                "- Starting Automatic Patching":"- Starting Automatic Patching",
                "- Auto Patch option is not supported on TUI, please use GUI":"- Auto Patch option is not supported on TUI, please use GUI",
                "- Found new version: {version}":"- Found new version: {version}",
                "A new version of OCLP-R is available!":"A new version of OCLP-R is available!",
                "OCLP-R {version} is now available - You have {current_version}. Would you like to update?":"OCLP-R {version} is now available - You have {current_version}. Would you like to update?",
                "Ignore":"Ignore",
                "View on GitHub":"View on GitHub",
                "Download and Install":"Download and Install",
                "- Detected Snapshot seal intact, detecting patches":"- Detected Snapshot seal intact, detecting patches",
                "- Detected applicable patches, determining whether possible to patch":"- Detected applicable patches, determining whether possible to patch",
                "- Cannot run patching":"- Cannot run patching",
                "- Determined patching is possible, checking for OCLP updates":"- Determined patching is possible, checking for OCLP updates",
                "- No new binaries found on Github, proceeding with patching":"- No new binaries found on Github, proceeding with patching",
                "OCLP-R has detected you're running without Root Patches, and would like to install them.\n\nmacOS wipes all root patches during OS installs and updates, so they need to be reinstalled.\n\nFollowing Patches have been detected for your system: \n{patch_string}\nWould you like to apply these patches?{warning_str}":"OCLP-R has detected you're running without Root Patches, and would like to install them.\n\nmacOS wipes all root patches during OS installs and updates, so they need to be reinstalled.\n\nFollowing Patches have been detected for your system: \n{patch_string}\nWould you like to apply these patches?{warning_str}",
                "WARNING: We're unable to verify whether there are any new releases of OCLP-R on Github. Be aware that you may be using an outdated version for this OS. If you're unsure, verify on Github that OCLP-R {version} is the latest official release":"WARNING: We're unable to verify whether there are any new releases of OCLP-R on Github. Be aware that you may be using an outdated version for this OS. If you're unsure, verify on Github that OCLP-R {version} is the latest official release",
                "- No patches detected":"- No patches detected",
                "- Detected Snapshot seal not intact, skipping":"- Detected Snapshot seal not intact, skipping",
                "- Checking booted vs installed OCLP Build":"- Checking booted vs installed OCLP Build",
                "- Booted version not found":"- Booted version not found",
                "- Versions match":"- Versions match",
                "- Special build detected, assuming installed is older":"- Special build detected, assuming installed is older",
                "- Installed version is newer than booted version":"- Installed version is newer than booted version",
                "OCLP-R has detected that you are booting {build_type} OpenCore build\n- Booted: {booted_version}\n- Installed: {installed_version}\n\nWould you like to update the OpenCore bootloader?":"OCLP-R has detected that you are booting {build_type} OpenCore build\n- Booted: {booted_version}\n- Installed: {installed_version}\n\nWould you like to update the OpenCore bootloader?",
                "a different":"a different",
                "an outdated":"an outdated",
                "- Launching GUI's Build/Install menu":"- Launching GUI's Build/Install menu",
                "- Determining if macOS drive matches boot drive":"- Determining if macOS drive matches boot drive",
                "- Skipping due to user preference":"- Skipping due to user preference",
                "- Skipping due to hackintosh":"- Skipping due to hackintosh",
                "- Failed to find disk OpenCore launched from":"- Failed to find disk OpenCore launched from",
                "  - Boot Drive: {boot_disk} ({root_disk})":"  - Boot Drive: {boot_disk} ({root_disk})",
                "  - macOS Drive: {macos_disk}":"  - macOS Drive: {macos_disk}",
                "  - APFS Physical Stores: {physical_stores}":"  - APFS Physical Stores: {physical_stores}",
                "- Boot drive matches macOS drive ({disk})":"- Boot drive matches macOS drive ({disk})",
                "- Boot Drive does not match macOS drive, checking if OpenCore is on a USB drive":"- Boot Drive does not match macOS drive, checking if OpenCore is on a USB drive",
                "- Boot Disk is not removable, skipping prompt":"- Boot Disk is not removable, skipping prompt",
                "- Boot Disk is ejectable, prompting user to install to internal":"- Boot Disk is ejectable, prompting user to install to internal",
                "OCLP-R has detected that you are booting OpenCore from an USB or External drive.\n\nIf you would like to boot your Mac normally without a USB drive plugged in, you can install OpenCore to the internal hard drive.\n\nWould you like to launch OCLP-R and install to disk?":"OCLP-R has detected that you are booting OpenCore from an USB or External drive.\n\nIf you would like to boot your Mac normally without a USB drive plugged in, you can install OpenCore to the internal hard drive.\n\nWould you like to launch OCLP-R and install to disk?",
                "- Unable to determine if boot disk is removable, skipping prompt":"- Unable to determine if boot disk is removable, skipping prompt"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Skipping Auto Patcher Launch Agent, not supported when running from source":"- 跳过自动修补程序启动代理，从源代码运行时不受支持",
                "- Installing {name}":"- 正在安装 {name}",
                "  - {name} checksums match, skipping":"  - {name} 校验和匹配，跳过",
                "  - Existing service found, removing":"  - 找到现有服务，正在删除",
                "  - Creating {path} directory":"  - 正在创建 {path} 目录",
                "- Checking if RSRMonitor is needed":"- 检查是否需要 RSRMonitor",
                "- No OS.dmg, skipping RSRMonitor":"- 没有 OS.dmg，跳过 RSRMonitor",
                "  - Failed to check if {name} is a directory: {error}":"  - 检查 {name} 是否为目录失败: {error}",
                "  - Failed to load plist for {name}: {error}":"  - 加载 {name} 的 plist 失败: {error}",
                "  - Found kext with GPUCompanionBundles: {name}":"  - 找到带有 GPUCompanionBundles 的 kext: {name}",
                "- No kexts found with GPUCompanionBundles, skipping RSRMonitor":"- 未找到带有 GPUCompanionBundles 的 kext，跳过 RSRMonitor",
                "  - Adding monitor: {path}":"  - 正在添加监视器: {path}",
                "- Starting Automatic Patching":"- 开始自动修补",
                "- Auto Patch option is not supported on TUI, please use GUI":"- 自动修补选项在 TUI 中不受支持，请使用 GUI",
                "- Found new version: {version}":"- 找到新版本: {version}",
                "A new version of OCLP-R is available!":"OCLP-R 有新版本可用！",
                "OCLP-R {version} is now available - You have {current_version}. Would you like to update?":"OCLP-R {version} 现已可用 - 您当前使用的是 {current_version}。是否要更新？",
                "Ignore":"忽略",
                "View on GitHub":"在 GitHub 上查看",
                "Download and Install":"下载并安装",
                "- Detected Snapshot seal intact, detecting patches":"- 检测到快照密封完好，正在检测补丁",
                "- Detected applicable patches, determining whether possible to patch":"- 检测到适用的补丁，正在确定是否可以修补",
                "- Cannot run patching":"- 无法运行修补",
                "- Determined patching is possible, checking for OCLP updates":"- 确定可以修补，正在检查 OCLP 更新",
                "- No new binaries found on Github, proceeding with patching":"- 在 Github 上未找到新的二进制文件，继续修补",
                "OCLP-R has detected you're running without Root Patches, and would like to install them.\n\nmacOS wipes all root patches during OS installs and updates, so they need to be reinstalled.\n\nFollowing Patches have been detected for your system: \n{patch_string}\nWould you like to apply these patches?{warning_str}":"OCLP-R 检测到您正在运行没有根补丁的系统，并希望安装它们。\n\nmacOS 在操作系统安装和更新期间会清除所有根补丁，因此需要重新安装。\n\n已为您的系统检测到以下补丁：\n{patch_string}\n是否要应用这些补丁？{warning_str}",
                "WARNING: We're unable to verify whether there are any new releases of OCLP-R on Github. Be aware that you may be using an outdated version for this OS. If you're unsure, verify on Github that OCLP-R {version} is the latest official release":"警告：我们无法验证 Github 上是否有 OCLP-R 的新版本。请注意，您可能正在使用此操作系统的过时版本。如果不确定，请在 Github 上验证 OCLP-R {version} 是否是最新官方版本。",
                "- No patches detected":"- 未检测到补丁",
                "- Detected Snapshot seal not intact, skipping":"- 检测到快照密封不完整，跳过",
                "- Checking booted vs installed OCLP Build":"- 检查启动的与安装的 OCLP 构建",
                "- Booted version not found":"- 未找到启动版本",
                "- Versions match":"- 版本匹配",
                "- Special build detected, assuming installed is older":"- 检测到特殊构建，假设安装的版本较旧",
                "- Installed version is newer than booted version":"- 安装的版本比启动的版本新",
                "OCLP-R has detected that you are booting {build_type} OpenCore build\n- Booted: {booted_version}\n- Installed: {installed_version}\n\nWould you like to update the OpenCore bootloader?":"OCLP-R 检测到您正在启动 {build_type} OpenCore 构建\n- 启动的: {booted_version}\n- 安装的: {installed_version}\n\n是否要更新 OpenCore 引导加载程序？",
                "a different":"不同的",
                "an outdated":"过时的",
                "- Launching GUI's Build/Install menu":"- 启动 GUI 的构建/安装菜单",
                "- Determining if macOS drive matches boot drive":"- 确定 macOS 驱动器是否与启动驱动器匹配",
                "- Skipping due to user preference":"- 由于用户偏好跳过",
                "- Skipping due to hackintosh":"- 由于是黑苹果跳过",
                "- Failed to find disk OpenCore launched from":"- 找不到 OpenCore 启动的磁盘",
                "  - Boot Drive: {boot_disk} ({root_disk})":"  - 启动驱动器: {boot_disk} ({root_disk})",
                "  - macOS Drive: {macos_disk}":"  - macOS 驱动器: {macos_disk}",
                "  - APFS Physical Stores: {physical_stores}":"  - APFS 物理存储: {physical_stores}",
                "- Boot drive matches macOS drive ({disk})":"- 启动驱动器与 macOS 驱动器匹配 ({disk})",
                "- Boot Drive does not match macOS drive, checking if OpenCore is on a USB drive":"- 启动驱动器与 macOS 驱动器不匹配，检查 OpenCore 是否在 USB 驱动器上",
                "- Boot Disk is not removable, skipping prompt":"- 启动磁盘不可移动，跳过提示",
                "- Boot Disk is ejectable, prompting user to install to internal":"- 启动磁盘可弹出，提示用户安装到内部",
                "OCLP-R has detected that you are booting OpenCore from an USB or External drive.\n\nIf you would like to boot your Mac normally without a USB drive plugged in, you can install OpenCore to the internal hard drive.\n\nWould you like to launch OCLP-R and install to disk?":"OCLP-R 检测到您正在从 USB 或外部驱动器启动 OpenCore。\n\n如果您希望在没有插入 USB 驱动器的情况下正常启动 Mac，可以将 OpenCore 安装到内部硬盘。\n\n是否要启动 OCLP-R 并安装到磁盘？",
                "- Unable to determine if boot disk is removable, skipping prompt":"- 无法确定启动磁盘是否可移动，跳过提示"
            }
        return trans

    def kernelcache(self):
        if self.language_point=="English":
            trans={
                "- Syncing Kernel Cache to Preboot":"- Syncing Kernel Cache to Preboot",
                "- Rebuilding Prelinked Kernel":"- Rebuilding Prelinked Kernel",
                "- Rebuilding MKext cache":"- Rebuilding MKext cache",
                "  - {kext_name} requires authentication in System Preferences":"  - {kext_name} requires authentication in System Preferences",
                "  - Adding AuxKC support to {install_file}":"  - Adding AuxKC support to {install_file}",
                "- Cleaning Auxiliary Kernel Collection":"- Cleaning Auxiliary Kernel Collection",
                "  - Removing {file}":"  - Removing {file}",
                "  - Relocating {file_name} kext to {relocation_path}":"  - Relocating {file_name} kext to {relocation_path}",
                "- Rebuilding Boot and System Kernel Collections":"- Rebuilding Boot and System Kernel Collections",
                "- Rebuilding Boot, System and Auxiliary Kernel Collections":"- Rebuilding Boot, System and Auxiliary Kernel Collections",
                "  (You will get a prompt by System Preferences, ignore for now)":"  (You will get a prompt by System Preferences, ignore for now)",
                "- Forcing Auxiliary Kernel Collection usage":"- Forcing Auxiliary Kernel Collection usage",
                "- Unable to kill syspolicyd and kernelmanagerd":"- Unable to kill syspolicyd and kernelmanagerd",
                "- Unable to remove {file}":"- Unable to remove {file}",
                "- Building new Auxiliary Kernel Collection":"- Building new Auxiliary Kernel Collection",
                "- Unable to build Auxiliary Kernel Collection":"- Unable to build Auxiliary Kernel Collection"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Syncing Kernel Cache to Preboot":"- 正在将内核缓存同步到 Preboot",
                "- Rebuilding Prelinked Kernel":"- 正在重建预链接内核",
                "- Rebuilding MKext cache":"- 正在重建 MKext 缓存",
                "  - {kext_name} requires authentication in System Preferences":"  - {kext_name} 需要在系统偏好设置中进行身份验证",
                "  - Adding AuxKC support to {install_file}":"  - 正在为 {install_file} 添加 AuxKC 支持",
                "- Cleaning Auxiliary Kernel Collection":"- 正在清理辅助内核集合",
                "  - Removing {file}":"  - 正在删除 {file}",
                "  - Relocating {file_name} kext to {relocation_path}":"  - 正在将 {file_name} kext 重定位到 {relocation_path}",
                "- Rebuilding Boot and System Kernel Collections":"- 正在重建启动和系统内核集合",
                "- Rebuilding Boot, System and Auxiliary Kernel Collections":"- 正在重建启动、系统和辅助内核集合",
                "  (You will get a prompt by System Preferences, ignore for now)":"  (您将在系统偏好设置中收到提示，暂时忽略)",
                "- Forcing Auxiliary Kernel Collection usage":"- 正在强制使用辅助内核集合",
                "- Unable to kill syspolicyd and kernelmanagerd":"- 无法终止 syspolicyd 和 kernelmanagerd",
                "- Unable to remove {file}":"- 无法删除 {file}",
                "- Building new Auxiliary Kernel Collection":"- 正在构建新的辅助内核集合",
                "- Unable to build Auxiliary Kernel Collection":"- 无法构建辅助内核集合"
            }
        return trans

    def mount(self):
        if self.language_point=="English":
            trans={
                "Failed to parse diskutil output.":"Failed to parse diskutil output.",
                "Failed to mount root volume":"Failed to mount root volume",
                "{root_volume_identifier} has already been unmounted.":"{root_volume_identifier} has already been unmounted.",
                "Attempted to mount root volume, but failed: {result}":"Attempted to mount root volume, but failed: {result}",
                "Failed to unmount root volume":"Failed to unmount root volume",
                "Failed to create APFS snapshot":"Failed to create APFS snapshot",
                "- This is an APFS bug with Monterey and newer! Perform a clean installation to ensure your APFS volume is built correctly":"- This is an APFS bug with Monterey and newer! Perform a clean installation to ensure your APFS volume is built correctly",
                "Failed to revert APFS snapshot":"Failed to revert APFS snapshot"
            }
        elif self.language_point=="简体中文":
            trans={
                "Failed to parse diskutil output.":"解析diskutil输出失败",
                "Failed to mount root volume":"挂载根卷失败",
                "{root_volume_identifier} has already been unmounted.":"{root_volume_identifier} 已经卸载",
                "Attempted to mount root volume, but failed: {result}":"尝试挂载根卷失败: {result}",
                "Failed to unmount root volume":"卸载根卷失败",
                "Failed to create APFS snapshot":"创建APFS快照失败",
                "- This is an APFS bug with Monterey and newer! Perform a clean installation to ensure your APFS volume is built correctly":"- 这是Monterey及更新版本的APFS错误！请执行干净安装以确保您的APFS卷正确构建",
                "Failed to revert APFS snapshot":"恢复APFS快照失败"
            }
        return trans

    def sys_patch(self):
        if self.language_point=="English":
            trans={
                "- Unmounting root volume":"- Unmounting root volume",
                "- Running sanity checks before patching":"- Running sanity checks before patching",
                "- Failed to find SystemVersion.plist on mounted root volume":"- Failed to find SystemVersion.plist on mounted root volume",
                "An update is in progress on your machine and patching cannot continue until it is cancelled or finished":"An update is in progress on your machine and patching cannot continue until it is cancelled or finished",
                "- Failed to parse SystemVersion.plist":"- Failed to parse SystemVersion.plist",
                "- Cleaning LaunchPad Settings":"- Cleaning LaunchPad Settings",
                "- Unpatching complete":"- Unpatching complete",
                "\nPlease reboot the machine for patches to take effect":"\nPlease reboot the machine for patches to take effect",
                "- Patching complete":"- Patching complete",
                "Note: Apple will require you to open System Preferences -> Security to allow the new kernel extensions to be loaded":"Note: Apple will require you to open System Preferences -> Security to allow the new kernel extensions to be loaded",
                "- Rebuilding dyld shared cache":"- Rebuilding dyld shared cache",
                "- Rebuilding preboot kernel cache":"- Rebuilding preboot kernel cache",
                "- Found SkylightPlugins folder, removing old plugins":"- Found SkylightPlugins folder, removing old plugins",
                "- Creating SkylightPlugins folder":"- Creating SkylightPlugins folder",
                "- Removing non-Metal Enforcement Preference: {arg}":"- Removing non-Metal Enforcement Preference: {arg}",
                "- Writing patchset information to Root Volume":"- Writing patchset information to Root Volume",
                "- Running patches for {model}":"- Running patches for {model}",
                "- Installing Patchset: {patch}":"- Installing Patchset: {patch}",
                "- Remove Files at: {remove_patch_directory}":"- Remove Files at: {remove_patch_directory}",
                "- Handling Installs in: {install_patch_directory}":"- Handling Installs in: {install_patch_directory}",
                "- Running Process as Root:\n{process}":"- Running Process as Root:\n{process}",
                "- Running Process:\n{process}":"- Running Process:\n{process}",
                "Failed to find MetalLibSupportPkg: {error_msg}":"Failed to find MetalLibSupportPkg: {error_msg}",
                "Using MetalLibSupportPkg: {metallib_installed_path}":"Using MetalLibSupportPkg: {metallib_installed_path}",
                "Could not download MetalLibSupportPkg: {error_msg}":"Could not download MetalLibSupportPkg: {error_msg}",
                "Failed to install MetalLibSupportPkg":"Failed to install MetalLibSupportPkg",
                "- Running Preflight Checks before patching":"- Running Preflight Checks before patching",
                "- Finished Preflight, starting patching":"- Finished Preflight, starting patching",
                "- Starting Patch Process":"- Starting Patch Process",
                "- Determining Required Patch set for Darwin {detected_os}":"- Determining Required Patch set for Darwin {detected_os}",
                "- No Root Patches required for your machine!":"- No Root Patches required for your machine!",
                "- Verifying whether Root Patching possible":"- Verifying whether Root Patching possible",
                "- Cannot continue with patching!!!":"- Cannot continue with patching!!!",
                "- Patcher is capable of patching":"- Patcher is capable of patching",
                "- Critical resources missing, cannot continue with patching!!!":"- Critical resources missing, cannot continue with patching!!!",
                "- Failed to mount root volume, cannot continue with patching!!!":"- Failed to mount root volume, cannot continue with patching!!!",
                "- Failed sanity checks, cannot continue with patching!!!":"- Failed sanity checks, cannot continue with patching!!!",
                "- Please ensure that you do not have any updates pending":"- Please ensure that you do not have any updates pending",
                "- Starting Unpatch Process":"- Starting Unpatch Process",
                "- Cannot continue with unpatching!!!":"- Cannot continue with unpatching!!!",
                "- Failed to mount root volume, cannot continue with unpatching!!!":"- Failed to mount root volume, cannot continue with unpatching!!!",
                "Failed to find {source_file}":"Failed to find {source_file}",
                "Failed to find MetalLibSupportPkg: {error_msg}":"Failed to find MetalLibSupportPkg: {error_msg}",
                "Could not download MetalLibSupportPkg: {error_msg}":"Could not download MetalLibSupportPkg: {error_msg}",
                "Failed to install MetalLibSupportPkg":"Failed to install MetalLibSupportPkg",
                "Unknown Dynamic Patchset: {variant}":"Unknown Dynamic Patchset: {variant}"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Unmounting root volume":"- 正在卸载根卷",
                "- Running sanity checks before patching":"- 正在运行修补前的完整性检查",
                "- Failed to find SystemVersion.plist on mounted root volume":"- 在挂载的根卷上找不到 SystemVersion.plist",
                "An update is in progress on your machine and patching cannot continue until it is cancelled or finished":"您的机器正在进行更新，修补无法继续，直到更新被取消或完成",
                "- Failed to parse SystemVersion.plist":"- 解析 SystemVersion.plist 失败",
                "- Cleaning LaunchPad Settings":"- 正在清理 LaunchPad 设置",
                "- Unpatching complete":"- 取消修补完成",
                "\nPlease reboot the machine for patches to take effect":"\n请重启机器以使补丁生效",
                "- Patching complete":"- 修补完成",
                "Note: Apple will require you to open System Preferences -> Security to allow the new kernel extensions to be loaded":"注意：Apple 将要求您打开系统偏好设置 -> 安全以允许加载新的内核扩展",
                "- Rebuilding dyld shared cache":"- 正在重建 dyld 共享缓存",
                "- Rebuilding preboot kernel cache":"- 正在重建预启动内核缓存",
                "- Found SkylightPlugins folder, removing old plugins":"- 找到 SkylightPlugins 文件夹，正在删除旧插件",
                "- Creating SkylightPlugins folder":"- 正在创建 SkylightPlugins 文件夹",
                "- Removing non-Metal Enforcement Preference: {arg}":"- 正在删除非 Metal 强制偏好设置: {arg}",
                "- Writing patchset information to Root Volume":"- 正在将补丁集信息写入根卷",
                "- Running patches for {model}":"- 正在为 {model} 运行补丁",
                "- Installing Patchset: {patch}":"- 正在安装补丁集: {patch}",
                "- Remove Files at: {remove_patch_directory}":"- 正在删除文件位置: {remove_patch_directory}",
                "- Handling Installs in: {install_patch_directory}":"- 正在处理安装位置: {install_patch_directory}",
                "- Running Process as Root:\n{process}":"- 正在以 Root 身份运行进程:\n{process}",
                "- Running Process:\n{process}":"- 正在运行进程:\n{process}",
                "Failed to find MetalLibSupportPkg: {error_msg}":"找不到 MetalLibSupportPkg: {error_msg}",
                "Using MetalLibSupportPkg: {metallib_installed_path}":"正在使用 MetalLibSupportPkg: {metallib_installed_path}",
                "Could not download MetalLibSupportPkg: {error_msg}":"无法下载 MetalLibSupportPkg: {error_msg}",
                "Failed to install MetalLibSupportPkg":"安装 MetalLibSupportPkg 失败",
                "- Running Preflight Checks before patching":"- 正在运行修补前的预检检查",
                "- Finished Preflight, starting patching":"- 预检完成，开始修补",
                "- Starting Patch Process":"- 开始修补过程",
                "- Determining Required Patch set for Darwin {detected_os}":"- 正在确定 Darwin {detected_os} 所需的补丁集",
                "- No Root Patches required for your machine!":"- 您的机器不需要根补丁！",
                "- Verifying whether Root Patching possible":"- 正在验证根修补是否可能",
                "- Cannot continue with patching!!!":"- 无法继续修补！！！",
                "- Patcher is capable of patching":"- 修补程序能够进行修补",
                "- Critical resources missing, cannot continue with patching!!!":"- 关键资源缺失，无法继续修补！！！",
                "- Failed to mount root volume, cannot continue with patching!!!":"- 挂载根卷失败，无法继续修补！！！",
                "- Failed sanity checks, cannot continue with patching!!!":"- 完整性检查失败，无法继续修补！！！",
                "- Please ensure that you do not have any updates pending":"- 请确保您没有任何待处理的更新",
                "- Starting Unpatch Process":"- 开始取消修补过程",
                "- Cannot continue with unpatching!!!":"- 无法继续取消修补！！！",
                "- Failed to mount root volume, cannot continue with unpatching!!!":"- 挂载根卷失败，无法继续取消修补！！！",
                "Failed to find {source_file}":"找不到 {source_file}",
                "Failed to find MetalLibSupportPkg: {error_msg}":"找不到 MetalLibSupportPkg: {error_msg}",
                "Could not download MetalLibSupportPkg: {error_msg}":"无法下载 MetalLibSupportPkg: {error_msg}",
                "Failed to install MetalLibSupportPkg":"安装 MetalLibSupportPkg 失败",
                "Unknown Dynamic Patchset: {variant}":"未知的动态补丁集: {variant}"
        }
        return trans

    def sys_patch_helpers(self):
        if self.language_point=="English":
            trans={
                "Found unsupported Board ID {reported_board_id}, performing AppleIntelSNBGraphicsFB bin patching":"Found unsupported Board ID {reported_board_id}, performing AppleIntelSNBGraphicsFB bin patching",
                "Replacing {board_to_patch} with {reported_board_id}":"Replacing {board_to_patch} with {reported_board_id}",
                "Error: Board ID {reported_board_id} is longer than {board_to_patch}":"Error: Board ID {reported_board_id} is longer than {board_to_patch}",
                "Error: Could not find {path}":"Error: Could not find {path}",
                "Disabling WindowServer Caching":"Disabling WindowServer Caching",
                "Installing Kernel Collection syncing utility":"Installing Kernel Collection syncing utility",
                "- Failed to install RSRRepair":"- Failed to install RSRRepair",
                "Merging GPUCompiler.framework libraries to match binary":"Merging GPUCompiler.framework libraries to match binary",
                "Host's Board ID is longer than the kext's Board ID, cannot patch!!!":"Host's Board ID is longer than the kext's Board ID, cannot patch!!!",
                "Failed to find AppleIntelSNBGraphicsFB.kext, cannot patch!!!":"Failed to find AppleIntelSNBGraphicsFB.kext, cannot patch!!!",
                "Failed to find GPUCompiler libraries at {dest_dir}":"Failed to find GPUCompiler libraries at {dest_dir}"
            }
        elif self.language_point=="简体中文":
            trans={
                "Found unsupported Board ID {reported_board_id}, performing AppleIntelSNBGraphicsFB bin patching":"发现不支持的 Board ID {reported_board_id}，正在执行 AppleIntelSNBGraphicsFB 二进制修补",
                "Replacing {board_to_patch} with {reported_board_id}":"正在将 {board_to_patch} 替换为 {reported_board_id}",
                "Error: Board ID {reported_board_id} is longer than {board_to_patch}":"错误：Board ID {reported_board_id} 比 {board_to_patch} 长",
                "Error: Could not find {path}":"错误：找不到 {path}",
                "Disabling WindowServer Caching":"正在禁用 WindowServer 缓存",
                "Installing Kernel Collection syncing utility":"正在安装内核集合同步工具",
                "- Failed to install RSRRepair":"- 安装 RSRRepair 失败",
                "Merging GPUCompiler.framework libraries to match binary":"正在合并 GPUCompiler.framework 库以匹配二进制文件",
                "Host's Board ID is longer than the kext's Board ID, cannot patch!!!":"主机的 Board ID 比 kext 的 Board ID 长，无法修补！！！",
                "Failed to find AppleIntelSNBGraphicsFB.kext, cannot patch!!!":"找不到 AppleIntelSNBGraphicsFB.kext，无法修补！！！",
                "Failed to find GPUCompiler libraries at {dest_dir}":"在 {dest_dir} 找不到 GPUCompiler 库"
            }
        return trans

    def utilities(self):
        if self.language_point=="English":
            trans={
                # dmg_mount.py
                "- PatcherSupportPkg resources missing, Patcher likely corrupted!!!":"- PatcherSupportPkg resources missing, Patcher likely corrupted!!!",
                "- Failed to mount Universal-Binaries.dmg":"- Failed to mount Universal-Binaries.dmg",
                "- Mounted Universal-Binaries.dmg":"- Mounted Universal-Binaries.dmg",
                "- Found HackdocInternal resources, mounting...":"- Found HackdocInternal resources, mounting...",
                "- Failed to mount HackdocInternal resources":"- Failed to mount HackdocInternal resources",
                "- Mounted HackdocInternal resources":"- Mounted HackdocInternal resources",
                "- Failed to merge HackdocInternal resources":"- Failed to merge HackdocInternal resources",
                "- Local PatcherSupportPkg resources available, continuing...":"- Local PatcherSupportPkg resources available, continuing...",
                
                # files.py
                "  - Skipping {file_name}, cannot locate {source_folder}":"  - Skipping {file_name}, cannot locate {source_folder}",
                "  - Installing: {file_name}":"  - Installing: {file_name}",
                "  - Found existing {file_name}, overwriting...":"  - Found existing {file_name}, overwriting...",
                "  - Removing: {file_name}":"  - Removing: {file_name}",
                
                # kdk_merge.py
                "- Matching KDK determined to already be merged, skipping":"- Matching KDK determined to already be merged, skipping",
                "- Backing up IOHIDEventDriver CodeSignature":"- Backing up IOHIDEventDriver CodeSignature",
                "- Restoring IOHIDEventDriver CodeSignature":"- Restoring IOHIDEventDriver CodeSignature",
                "  - CodeSignature folder missing, creating":"  - CodeSignature folder missing, creating",
                "- Merging KDK with Root Volume: {kdk_name}":"- Merging KDK with Root Volume: {kdk_name}",
                "- Failed to merge KDK with Root Volume":"- Failed to merge KDK with Root Volume",
                "- Successfully merged KDK with Root Volume":"- Successfully merged KDK with Root Volume",
                "Failed to install KDK":"Failed to install KDK",
                "Unable to get KDK info: {error_msg}":"Unable to get KDK info: {error_msg}",
                "Could not retrieve KDK: {error_msg}":"Could not retrieve KDK: {error_msg}",
                "Could not download KDK: {error_msg}":"Could not download KDK: {error_msg}",
                "KDK checksum validation failed: {error_msg}":"KDK checksum validation failed: {error_msg}",
                "KDK was not installed, but should have been: {error_msg}":"KDK was not installed, but should have been: {error_msg}",
                "- Unable to find Kernel Debug Kit":"- Unable to find Kernel Debug Kit",
                "- Found KDK at: {kdk_path}":"- Found KDK at: {kdk_path}"
            }
        elif self.language_point=="简体中文":
            trans={
                # dmg_mount.py
                "- PatcherSupportPkg resources missing, Patcher likely corrupted!!!":"- PatcherSupportPkg 资源缺失，修补程序可能已损坏！！！",
                "- Failed to mount Universal-Binaries.dmg":"- 挂载 Universal-Binaries.dmg 失败",
                "- Mounted Universal-Binaries.dmg":"- 已挂载 Universal-Binaries.dmg",
                "- Found HackdocInternal resources, mounting...":"- 找到 HackdocInternal 资源，正在挂载...",
                "- Failed to mount HackdocInternal resources":"- 挂载 HackdocInternal 资源失败",
                "- Mounted HackdocInternal resources":"- 已挂载 HackdocInternal 资源",
                "- Failed to merge HackdocInternal resources":"- 合并 HackdocInternal 资源失败",
                "- Local PatcherSupportPkg resources available, continuing...":"- 本地 PatcherSupportPkg 资源可用，继续...",
                
                # files.py
                "  - Skipping {file_name}, cannot locate {source_folder}":"  - 跳过 {file_name}，无法定位 {source_folder}",
                "  - Installing: {file_name}":"  - 正在安装: {file_name}",
                "  - Found existing {file_name}, overwriting...":"  - 找到现有 {file_name}，正在覆盖...",
                "  - Removing: {file_name}":"  - 正在删除: {file_name}",
                
                # kdk_merge.py
                "- Matching KDK determined to already be merged, skipping":"- 匹配的 KDK 已确定已合并，跳过",
                "- Backing up IOHIDEventDriver CodeSignature":"- 正在备份 IOHIDEventDriver 代码签名",
                "- Restoring IOHIDEventDriver CodeSignature":"- 正在恢复 IOHIDEventDriver 代码签名",
                "  - CodeSignature folder missing, creating":"  - 代码签名文件夹缺失，正在创建",
                "- Merging KDK with Root Volume: {kdk_name}":"- 正在将 KDK 与根卷合并: {kdk_name}",
                "- Failed to merge KDK with Root Volume":"- 将 KDK 与根卷合并失败",
                "- Successfully merged KDK with Root Volume":"- 成功将 KDK 与根卷合并",
                "Failed to install KDK":"安装 KDK 失败",
                "Unable to get KDK info: {error_msg}":"无法获取 KDK 信息: {error_msg}",
                "Could not retrieve KDK: {error_msg}":"无法检索 KDK: {error_msg}",
                "Could not download KDK: {error_msg}":"无法下载 KDK: {error_msg}",
                "KDK checksum validation failed: {error_msg}":"KDK 校验和验证失败: {error_msg}",
                "KDK was not installed, but should have been: {error_msg}":"KDK 未安装，但应该已安装: {error_msg}",
                "- Unable to find Kernel Debug Kit":"- 无法找到内核调试工具包",
                "- Found KDK at: {kdk_path}":"- 在 {kdk_path} 找到 KDK"
            }
        return trans

    def hardware(self):
        if self.language_point=="English":
            trans={
                # Hardware Variants
                "Graphics":"Graphics",
                "Networking":"Networking",
                "Audio":"Audio",
                "Miscellaneous":"Miscellaneous",
                "USB":"USB",
                
                # Audio
                "Legacy Audio":"Legacy Audio",
                "Modern Audio":"Modern Audio",
                "Voodoo Audio":"Voodoo Audio",
                
                # Graphics
                "AMD Legacy GCN":"AMD Legacy GCN",
                "AMD Navi":"AMD Navi",
                "AMD Polaris":"AMD Polaris",
                "AMD TeraScale 1":"AMD TeraScale 1",
                "AMD TeraScale 2":"AMD TeraScale 2",
                "AMD Vega":"AMD Vega",
                "Intel Broadwell":"Intel Broadwell",
                "Intel Haswell":"Intel Haswell",
                "Intel Iron Lake":"Intel Iron Lake",
                "Intel Ivy Bridge":"Intel Ivy Bridge",
                "Intel Sandy Bridge":"Intel Sandy Bridge",
                "Intel Skylake":"Intel Skylake",
                "Nvidia Kepler":"Nvidia Kepler",
                "Nvidia Tesla":"Nvidia Tesla",
                "Nvidia Web Drivers":"Nvidia Web Drivers",
                
                # Miscellaneous
                "FileVault Patch for Non-T2":"FileVault Patch for Non-T2",
                "Legacy CPUs (Lacking AVX)":"Legacy CPUs (Lacking AVX)",
                "Legacy GMUX":"Legacy GMUX",
                "Legacy Keyboard Backlight":"Legacy Keyboard Backlight",
                "PCIe FaceTime Camera":"PCIe FaceTime Camera",
                "T1 Security Chip":"T1 Security Chip",
                "Legacy Backlight Control":"Legacy Backlight Control",
                
                # Networking
                "Legacy Wireless":"Legacy Wireless",
                "Modern Wireless":"Modern Wireless",
                
                # USB
                "Modern USB":"Modern USB",
                "Legacy USB 1.1":"Legacy USB 1.1",
            }
        elif self.language_point=="简体中文":
            trans={
                # Hardware Variants
                "Graphics":"图形",
                "Networking":"网络",
                "Audio":"音频",
                "Miscellaneous":"杂项",
                "USB":"USB",
                
                # Audio
                "Legacy Audio":"传统音频补丁",
                "Modern Audio":"现代音频补丁",
                "Voodoo Audio":"Voodoo 音频补丁",
                
                # Graphics
                "AMD Legacy GCN":"AMD 传统 GCN",
                "AMD Navi":"AMD Navi",
                "AMD Polaris":"AMD Polaris",
                "AMD TeraScale 1":"AMD TeraScale 1",
                "AMD TeraScale 2":"AMD TeraScale 2",
                "AMD Vega":"AMD Vega",
                "Intel Broadwell":"Intel Broadwell (iGPU,5th)",
                "Intel Haswell":"Intel Haswell (iGPU,4th)",
                "Intel Iron Lake":"Intel Iron Lake",
                "Intel Ivy Bridge":"Intel Ivy Bridge (iGPU,3rd)",
                "Intel Sandy Bridge":"Intel Sandy Bridge (iGPU,2nd)",
                "Intel Skylake":"Intel Skylake (iGPU,6th)",
                "Nvidia Kepler":"Nvidia Kepler",
                "Nvidia Tesla":"Nvidia Tesla",
                "Nvidia Web Drivers":"Nvidia Web 驱动程序",
                
                # Miscellaneous
                "FileVault Patch for Non-T2":"非 T2 芯片 的 FileVault 补丁",
                "Legacy CPUs (Lacking AVX)":"传统 CPU（缺少 AVX）的补丁",
                "Legacy GMUX":"传统 GMUX 补丁",
                "Legacy Keyboard Backlight":"传统键盘背光补丁",
                "PCIe FaceTime Camera":"PCIe FaceTime 摄像头补丁",
                "T1 Security Chip":"T1 安全芯片补丁",
                "Legacy Backlight Control":"传统背光控制补丁",
                
                # Networking
                "Legacy Wireless":"传统无线补丁",
                "Modern Wireless":"现代无线补丁",
                
                # USB
                "Modern USB":"现代 USB 补丁",
                "Legacy USB 1.1":"传统 USB 1.1补丁",
            }
        return trans

    def base(self):
        if self.language_point=="English":
            trans={
                "Overwrite System Volume":"Overwrite System Volume",
                "Overwrite Data Volume":"Overwrite Data Volume",
                "Merge System Volume":"Merge System Volume",
                "Merge Data Volume":"Merge Data Volume",
                "Remove System Volume":"Remove System Volume",
                "Remove Data Volume":"Remove Data Volume",
                "Execute":"Execute",
                "MetallibSupportPkg":"MetallibSupportPkg",
            }
        elif self.language_point=="简体中文":
            trans={
                "Overwrite System Volume":"覆盖系统卷",
                "Overwrite Data Volume":"覆盖数据卷",
                "Merge System Volume":"合并系统卷",
                "Merge Data Volume":"合并数据卷",
                "Remove System Volume":"删除系统卷",
                "Remove Data Volume":"删除数据卷",
                "Execute":"执行",
                "MetallibSupportPkg":"MetallibSupportPkg",
            }
        return trans

class TranslateLanguage_efi_builder:
    def __init__(self, global_constants: Constants = None) -> None:
        self.file_name:              str = ".com.hackdoc.oclp-r.plist"
        self.global_settings_folder: str = "/Users/Shared"
        self.global_settings_plist:  str = f"{self.global_settings_folder}/{self.file_name}"
        try:
            self.plist = load(Path(self.global_settings_plist).open("rb"))
            self.language_point = self.plist["GUI:language_option"]
        except Exception:
            self.language_point = "English"
    def bluetooth(self):
        if self.language_point=="English":
            trans={
                "- Fixing Legacy Bluetooth for macOS Monterey":"- Fixing Legacy Bluetooth for macOS Monterey",
                "- Detected 3rd Party Bluetooth Chipset":"- Detected 3rd Party Bluetooth Chipset",
                "- Enabling Bluetooth FeatureFlags":"- Enabling Bluetooth FeatureFlags"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Fixing Legacy Bluetooth for macOS Monterey":"- 修复 macOS Monterey 中的传统蓝牙",
                "- Detected 3rd Party Bluetooth Chipset":"- 检测到第三方蓝牙芯片组",
                "- Enabling Bluetooth FeatureFlags":"- 启用蓝牙功能标志"
            }
        return trans
    def build(self):
        if self.language_point=="English":
            trans={
                "Building Configuration {0} model: {1}":"Building Configuration {0} model: {1}",
                "- Adding bootmgfw.efi BlessOverride":"- Adding bootmgfw.efi BlessOverride",
                "Creating build folder":"Creating build folder",
                "Build folder already present, skipping":"Build folder already present, skipping",
                "Deleting old copy of OpenCore zip":"Deleting old copy of OpenCore zip",
                "Deleting old copy of OpenCore folder":"Deleting old copy of OpenCore folder",
                "- Adding OpenCore v{0} {1}":"- Adding OpenCore v{0} {1}",
                "- Adding config.plist for OpenCore":"- Adding config.plist for OpenCore",
                "Your OpenCore EFI for {0} has been built at:":"Your OpenCore EFI for {0} has been built at:",
                "    {0}":"    {0}"
            }
        elif self.language_point=="简体中文":
            trans={
                "Building Configuration {0} model: {1}":"正在为{1}构建配置{0}",
                "- Adding bootmgfw.efi BlessOverride":"- 添加 bootmgfw.efi BlessOverride",
                "Creating build folder":"创建构建文件夹",
                "Build folder already present, skipping":"构建文件夹已存在，跳过",
                "Deleting old copy of OpenCore zip":"删除旧的 OpenCore zip 副本",
                "Deleting old copy of OpenCore folder":"删除旧的 OpenCore 文件夹副本",
                "- Adding OpenCore v{0} {1}":"- 添加 OpenCore v{0} {1}",
                "- Adding config.plist for OpenCore":"- 为 OpenCore 添加 config.plist",
                "Your OpenCore EFI for {0} has been built at:":"您的{0} OpenCore EFI 已构建完成，路径为：",
                "    {0}":"    {0}"
            }
        return trans
    def firmware(self):
        if self.language_point=="English":
            trans={
                "- Enabling Boot Logo patch":"- Enabling Boot Logo patch",
                "- Enabling legacy power management support":"- Enabling legacy power management support",
                "- Overriding ACPI SMC matching":"- Overriding ACPI SMC matching",
                "- Disabling Firmware Throttling":"- Disabling Firmware Throttling",
                "- Adding SSDT-CPBG.aml":"- Adding SSDT-CPBG.aml",
                "- Enabling Windows 10 UEFI Audio support":"- Enabling Windows 10 UEFI Audio support",
                "- Enabling Rosetta Cryptex support in Ventura":"- Enabling Rosetta Cryptex support in Ventura",
                "- Adding SurPlus Patch for Race Condition":"- Adding SurPlus Patch for Race Condition",
                "- Allowing SurPlus on all newer OSes":"- Allowing SurPlus on all newer OSes",
                "- Adding IOHIDFamily patch":"- Adding IOHIDFamily patch",
                "- Adding CPU Thread Limit Patch":"- Adding CPU Thread Limit Patch",
                "- Enabling macOS 26 FileVault 2 support":"- Enabling macOS 26 FileVault 2 support",
                "- Adding ExFatDxeLegacy.efi":"- Adding ExFatDxeLegacy.efi",
                "- Enabling NVMe boot support":"- Enabling NVMe boot support",
                "- Adding USB 3.0 Controller Patch":"- Adding USB 3.0 Controller Patch",
                "- Adding XhciDxe.efi and UsbBusDxe.efi":"- Adding XhciDxe.efi and UsbBusDxe.efi",
                "- Adding PCIe Link Rate Patch":"- Adding PCIe Link Rate Patch",
                "- Adding PCI Bus Enumeration Patch":"- Adding PCI Bus Enumeration Patch",
                "- Enabling VMM patch":"- Enabling VMM patch",
                "- Enabling VMX Bit for non-macOS OSes":"- Enabling VMX Bit for non-macOS OSes",
                "- Disabling ConnectDrivers":"- Disabling ConnectDrivers",
                "- Disabling Hardware NVRAM Write":"- Disabling Hardware NVRAM Write",
                "- Adding 4K/5K Display Patch":"- Adding 4K/5K Display Patch"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Enabling Boot Logo patch":"- 启用启动徽标补丁",
                "- Enabling legacy power management support":"- 启用传统电源管理支持",
                "- Overriding ACPI SMC matching":"- 覆盖 ACPI SMC 匹配",
                "- Disabling Firmware Throttling":"- 禁用固件节流",
                "- Adding SSDT-CPBG.aml":"- 添加 SSDT-CPBG.aml",
                "- Enabling Windows 10 UEFI Audio support":"- 启用 Windows 10 UEFI 音频支持",
                "- Enabling Rosetta Cryptex support in Ventura":"- 在 Ventura 中启用 Rosetta Cryptex 支持",
                "- Adding SurPlus Patch for Race Condition":"- 添加 SurPlus 竞争条件补丁",
                "- Allowing SurPlus on all newer OSes":"- 允许在所有较新操作系统上使用 SurPlus",
                "- Adding IOHIDFamily patch":"- 添加 IOHIDFamily 补丁",
                "- Adding CPU Thread Limit Patch":"- 添加 CPU 线程限制补丁",
                "- Enabling macOS 26 FileVault 2 support":"- 启用 macOS 26 FileVault 2 支持",
                "- Adding ExFatDxeLegacy.efi":"- 添加 ExFatDxeLegacy.efi",
                "- Enabling NVMe boot support":"- 启用 NVMe 启动支持",
                "- Adding USB 3.0 Controller Patch":"- 添加 USB 3.0 控制器补丁",
                "- Adding XhciDxe.efi and UsbBusDxe.efi":"- 添加 XhciDxe.efi 和 UsbBusDxe.efi",
                "- Adding PCIe Link Rate Patch":"- 添加 PCIe 链路速率补丁",
                "- Adding PCI Bus Enumeration Patch":"- 添加 PCI 总线枚举补丁",
                "- Enabling VMM patch":"- 启用 VMM 补丁",
                "- Enabling VMX Bit for non-macOS OSes":"- 为非 macOS 操作系统启用 VMX 位",
                "- Disabling ConnectDrivers":"- 禁用 ConnectDrivers",
                "- Disabling Hardware NVRAM Write":"- 禁用硬件 NVRAM 写入",
                "- Adding 4K/5K Display Patch":"- 添加 4K/5K 显示补丁"
            }
        return trans
    def graphics_audio(self):
        if self.language_point=="English":
            trans={
                "- Adding Mac Pro, Xserve DRM patches":"- Adding Mac Pro, Xserve DRM patches",
                "- Enabling Nvidia Output Patch":"- Enabling Nvidia Output Patch",
                "- Falling back to boot-args":"- Falling back to boot-args",
                "- No socketed dGPU found":"- No socketed dGPU found",
                "- device path and GFX0 Device path are different":"- device path and GFX0 Device path are different",
                "- Failed to find GFX0 Device path, falling back on known logic":"- Failed to find GFX0 Device path, falling back on known logic",
                "- Adding Nvidia Brightness Control and DRM patches":"- Adding Nvidia Brightness Control and DRM patches",
                "- Disabling unsupported iGPU":"- Disabling unsupported iGPU",
                "- Adding AMD DRM patches":"- Adding AMD DRM patches",
                "- Adding iMac9,1 Brightness Control and DRM patches":"- Adding iMac9,1 Brightness Control and DRM patches",
                "- Adding Legacy GCN Power Gate Patches":"- Adding Legacy GCN Power Gate Patches",
                "- Adding Lexa Spoofing Patches":"- Adding Lexa Spoofing Patches",
                "- Adding Navi Spoofing Patches":"- Adding Navi Spoofing Patches",
                "- Adding UGA to GOP Patch":"- Adding UGA to GOP Patch",
                "- Enabling software demux":"- Enabling software demux",
                "- Allowing GMUX switching in Windows":"- Allowing GMUX switching in Windows",
                "- Forcing GOP Support":"- Forcing GOP Support",
                "- Adding AMDGOP.efi":"- Adding AMDGOP.efi",
                "- Adding NVGOP_GK.efi":"- Adding NVGOP_GK.efi",
                "- Adding AppleMuxControl Override":"- Adding AppleMuxControl Override",
                "- Adding AppleGraphicsPowerManagement Override":"- Adding AppleGraphicsPowerManagement Override",
                "- Adding AppleGraphicsDevicePolicy Override":"- Adding AppleGraphicsDevicePolicy Override",
                "- Adding dual GPU patch":"- Adding dual GPU patch",
                "- Prioritizing DRM support over Intel QuickSync":"- Prioritizing DRM support over Intel QuickSync",
                "- Adding Metal GPU patches on request":"- Adding Metal GPU patches on request",
                "- Failed to find vendor":"- Failed to find vendor",
                "- Detected dGPU: ":"- Detected dGPU: ",
            }
        elif self.language_point=="简体中文":
            trans={
                "- Detected dGPU: ":"- 检测到 dGPU: ",
                "- Adding Mac Pro, Xserve DRM patches":"- 添加 Mac Pro, Xserve DRM 补丁",
                "- Enabling Nvidia Output Patch":"- 启用 Nvidia 输出补丁",
                "- Falling back to boot-args":"- 回退到 boot-args",
                "- No socketed dGPU found":"- 未找到可插拔 dGPU",
                "- device path and GFX0 Device path are different":"- 设备路径与 GFX0 设备路径不同",
                "- Failed to find GFX0 Device path, falling back on known logic":"- 未能找到 GFX0 设备路径，回退到已知逻辑",
                "- Adding Nvidia Brightness Control and DRM patches":"- 添加 Nvidia 亮度控制和 DRM 补丁",
                "- Disabling unsupported iGPU":"- 禁用不支持的 iGPU",
                "- Adding AMD DRM patches":"- 添加 AMD DRM 补丁",
                "- Adding iMac9,1 Brightness Control and DRM patches":"- 添加 iMac9,1 亮度控制和 DRM 补丁",
                "- Adding Legacy GCN Power Gate Patches":"- 添加传统 GCN 电源门控补丁",
                "- Adding Lexa Spoofing Patches":"- 添加 Lexa 仿冒补丁",
                "- Adding Navi Spoofing Patches":"- 添加 Navi 仿冒补丁",
                "- Adding UGA to GOP Patch":"- 添加 UGA 到 GOP 补丁",
                "- Enabling software demux":"- 启用软件解复用",
                "- Allowing GMUX switching in Windows":"- 允许在 Windows 中切换 GMUX",
                "- Forcing GOP Support":"- 强制 GOP 支持",
                "- Adding AMDGOP.efi":"- 添加 AMDGOP.efi",
                "- Adding NVGOP_GK.efi":"- 添加 NVGOP_GK.efi",
                "- Adding AppleMuxControl Override":"- 添加 AppleMuxControl 覆盖",
                "- Adding AppleGraphicsPowerManagement Override":"- 添加 AppleGraphicsPowerManagement 覆盖",
                "- Adding AppleGraphicsDevicePolicy Override":"- 添加 AppleGraphicsDevicePolicy 覆盖",
                "- Adding dual GPU patch":"- 添加双 GPU 补丁",
                "- Prioritizing DRM support over Intel QuickSync":"- 优先支持 DRM 而非 Intel QuickSync",
                "- Adding Metal GPU patches on request":"- 根据请求添加 Metal GPU 补丁",
                "- Failed to find vendor":"- 未能找到供应商"
            }
        return trans
    def misc(self):
        if self.language_point=="English":
            trans={
                "- Disabling memory error reporting":"- Disabling memory error reporting",
                "- Disabling mediaanalysisd":"- Disabling mediaanalysisd",
                "- Fixing CoreGraphics support on Ivy Bridge":"- Fixing CoreGraphics support on Ivy Bridge",
                "- Enabling FireWire Boot Support":"- Enabling FireWire Boot Support",
                "- Enabling SPI-based top case support":"- Enabling SPI-based top case support",
                "- Disabling 2013-2014 laptop Thunderbolt Controller":"- Disabling 2013-2014 laptop Thunderbolt Controller",
                "- Adding USB-Map.kext and USB-Map-Tahoe.kext":"- Adding USB-Map.kext and USB-Map-Tahoe.kext",
                "- Adding UHCI/OHCI USB support":"- Adding UHCI/OHCI USB support",
                "- Enabling Verbose boot":"- Enabling Verbose boot",
                "- Enabling DEBUG Kexts":"- Enabling DEBUG Kexts",
                "- Enabling DEBUG OpenCore":"- Enabling DEBUG OpenCore",
                "- Adding OpenCanopy GUI":"- Adding OpenCanopy GUI",
                "- Hiding OpenCore picker":"- Hiding OpenCore picker",
                "- Setting custom OpenCore picker timeout to {self.constants.oc_timeout} seconds":"- Setting custom OpenCore picker timeout to {self.constants.oc_timeout} seconds",
                "- Setting Vault configuration":"- Setting Vault configuration",
                "- Enabling T1 Security Chip support":"- Enabling T1 Security Chip support",
                "- Adding additional FeatureUnlock args: {}":"- Adding additional FeatureUnlock args: {}",
                "- Setting RestrictEvents block arguments: {}":"- Setting RestrictEvents block arguments: {}",
                "- Setting RestrictEvents patch arguments: {}":"- Setting RestrictEvents patch arguments: {}"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Disabling memory error reporting":"- 禁用内存错误报告",
                "- Disabling mediaanalysisd":"- 禁用 mediaanalysisd",
                "- Fixing CoreGraphics support on Ivy Bridge":"- 修复 Ivy Bridge 上的 CoreGraphics 支持",
                "- Enabling FireWire Boot Support":"- 启用 FireWire 启动支持",
                "- Enabling SPI-based top case support":"- 启用基于 SPI 的顶壳支持",
                "- Disabling 2013-2014 laptop Thunderbolt Controller":"- 禁用 2013-2014 笔记本电脑 Thunderbolt 控制器",
                "- Adding USB-Map.kext and USB-Map-Tahoe.kext":"- 添加 USB-Map.kext 和 USB-Map-Tahoe.kext",
                "- Adding UHCI/OHCI USB support":"- 添加 UHCI/OHCI USB 支持",
                "- Enabling Verbose boot":"- 启用详细启动",
                "- Enabling DEBUG Kexts":"- 启用 DEBUG Kexts",
                "- Enabling DEBUG OpenCore":"- 启用 DEBUG OpenCore",
                "- Adding OpenCanopy GUI":"- 添加 OpenCanopy GUI",
                "- Hiding OpenCore picker":"- 隐藏 OpenCore 选择器",
                "- Setting custom OpenCore picker timeout to {self.constants.oc_timeout} seconds":"- 设置自定义 OpenCore 选择器超时为 {self.constants.oc_timeout} 秒",
                "- Setting Vault configuration":"- 设置 Vault 配置",
                "- Enabling T1 Security Chip support":"- 启用 T1 安全芯片支持",
                "- Adding additional FeatureUnlock args: {}":"- 添加额外的 FeatureUnlock 参数: {}",
                "- Setting RestrictEvents block arguments: {}":"- 设置 RestrictEvents 阻止参数: {}",
                "- Setting RestrictEvents patch arguments: {}":"- 设置 RestrictEvents 补丁参数: {}"
            }
        return trans
    def security(self):
        if self.language_point=="English":
            trans={
                "- Adding ipc_control_port_options=0 to boot-args":"- Adding ipc_control_port_options=0 to boot-args",
                "- Setting SIP value to: {self.constants.custom_sip_value}":"- Setting SIP value to: {self.constants.custom_sip_value}",
                "- Set SIP to allow Root Volume patching":"- Set SIP to allow Root Volume patching",
                "- Allowing FileVault on Root Patched systems":"- Allowing FileVault on Root Patched systems",
                "- Enabling KC UUID mismatch patch":"- Enabling KC UUID mismatch patch",
                "- Disabling AMFI":"- Disabling AMFI",
                "- Disabling Library Validation":"- Disabling Library Validation",
                "- Disabling SecureBootModel":"- Disabling SecureBootModel",
                "- Enabling AMFIPass":"- Enabling AMFIPass"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Adding ipc_control_port_options=0 to boot-args":"- 将 ipc_control_port_options=0 添加到 boot-args",
                "- Setting SIP value to: {self.constants.custom_sip_value}":"- 设置 SIP 值为: {self.constants.custom_sip_value}",
                "- Set SIP to allow Root Volume patching":"- 设置 SIP 以允许根卷修补",
                "- Allowing FileVault on Root Patched systems":"- 允许在根卷修补系统上使用 FileVault",
                "- Enabling KC UUID mismatch patch":"- 启用 KC UUID 不匹配补丁",
                "- Disabling AMFI":"- 禁用 AMFI",
                "- Disabling Library Validation":"- 禁用库验证",
                "- Disabling SecureBootModel":"- 禁用 SecureBootModel",
                "- Enabling AMFIPass":"- 启用 AMFIPass"
            }
        return trans
    def smbios(self):
        if self.language_point=="English":
            trans={
                "- Enabling Board ID exemption patch":"- Enabling Board ID exemption patch",
                "- Enabling SMC exemption patch":"- Enabling SMC exemption patch",
                "- Enabling USB Rename Patches":"- Enabling USB Rename Patches",
                "- Adding -no_compat_check":"- Adding -no_compat_check",
                "- Setting macOS Monterey Supported SMBIOS":"- Setting macOS Monterey Supported SMBIOS",
                "- Using Model ID: {spoofed_model}":"- Using Model ID: {spoofed_model}",
                "- Using Board ID: {spoofed_board}":"- Using Board ID: {spoofed_board}",
                "- Detected UEFI 1.2 or older Mac, updating BoardProduct":"- Detected UEFI 1.2 or older Mac, updating BoardProduct",
                "- Adding custom serial numbers":"- Adding custom serial numbers",
                "- Patching G State for MacBookPro6,2":"- Patching G State for MacBookPro6,2",
                "- Setting Firmware Feature: {fw_feature}":"- Setting Firmware Feature: {fw_feature}",
                "- Using Moderate SMBIOS patching":"- Using Moderate SMBIOS patching",
                "- Using Advanced SMBIOS patching":"- Using Advanced SMBIOS patching",
                "- Using Minimal SMBIOS patching":"- Using Minimal SMBIOS patching"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Enabling Board ID exemption patch":"- 启用 Board ID 仿冒补丁",
                "- Enabling SMC exemption patch":"- 启用 SMC 仿冒补丁",
                "- Enabling USB Rename Patches":"- 启用 USB 重命名补丁",
                "- Adding -no_compat_check":"- 添加 -no_compat_check",
                "- Setting macOS Monterey Supported SMBIOS":"- 设置 macOS Monterey 支持的 SMBIOS",
                "- Using Model ID: {spoofed_model}":"- 使用型号 ID: {spoofed_model}",
                "- Using Board ID: {spoofed_board}":"- 使用主板 ID: {spoofed_board}",
                "- Detected UEFI 1.2 or older Mac, updating BoardProduct":"- 检测到 UEFI 1.2 或更早版本的 Mac，正在更新 BoardProduct",
                "- Adding custom serial numbers":"- 添加自定义序列号",
                "- Patching G State for MacBookPro6,2":"- 为 MacBookPro6,2 修补 G 状态",
                "- Setting Firmware Feature: {fw_feature}":"- 设置固件特性: {fw_feature}",
                "- Using Moderate SMBIOS patching":"- 使用适度的 SMBIOS 修补",
                "- Using Advanced SMBIOS patching":"- 使用高级的 SMBIOS 修补",
                "- Using Minimal SMBIOS patching":"- 使用最小的 SMBIOS 修补"
            }
        return trans
    def storage(self):
        if self.language_point=="English":
            trans={
                "- Enabling AHCI SSD patch":"- Enabling AHCI SSD patch",
                "- Adding SATA Hibernation Patch":"- Adding SATA Hibernation Patch",
                "- Fixing PCIe Storage Controller ({i + 1}) reporting":"- Fixing PCIe Storage Controller ({i + 1}) reporting",
                "- Failed to find Device path for PCIe Storage Controller {i}, falling back to Innie":"- Failed to find Device path for PCIe Storage Controller {i}, falling back to Innie",
                "- Found 3rd Party NVMe SSD ({i + 1}): {utilities.friendly_hex(controller.vendor_id)}:{utilities.friendly_hex(controller.device_id)}":"- Found 3rd Party NVMe SSD ({i + 1}): {utilities.friendly_hex(controller.vendor_id)}:{utilities.friendly_hex(controller.device_id)}",
                "- Found NVMe ({i}) at {controller.pci_path}":"- Found NVMe ({i}) at {controller.pci_path}",
                "- Falling back to -nvmefaspm":"- Falling back to -nvmefaspm",
                "- Disabling APFS TRIM timeout":"- Disabling APFS TRIM timeout"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Enabling AHCI SSD patch":"- 启用 AHCI SSD 补丁",
                "- Adding SATA Hibernation Patch":"- 添加 SATA 休眠补丁",
                "- Fixing PCIe Storage Controller ({i + 1}) reporting":"- 修复 PCIe 存储控制器 ({i + 1}) 报告",
                "- Failed to find Device path for PCIe Storage Controller {i}, falling back to Innie":"- 无法找到 PCIe 存储控制器 {i} 的设备路径，回退到 Innie",
                "- Found 3rd Party NVMe SSD ({i + 1}): {utilities.friendly_hex(controller.vendor_id)}:{utilities.friendly_hex(controller.device_id)}":"- 发现第三方 NVMe SSD ({i + 1}): {utilities.friendly_hex(controller.vendor_id)}:{utilities.friendly_hex(controller.device_id)}",
                "- Found NVMe ({i}) at {controller.pci_path}":"- 在 {controller.pci_path} 发现 NVMe ({i})",
                "- Falling back to -nvmefaspm":"- 回退到 -nvmefaspm",
                "- Disabling APFS TRIM timeout":"- 禁用 APFS TRIM 超时"
            }
        return trans
    def support(self):
        if self.language_point=="English":
            trans={
                "- Could not find kext {bundle_path}!":"- Could not find kext {bundle_path}!",
                "- Could not find {efi_type}: {bundle_name}!":"- Could not find {efi_type}: {bundle_name}!",
                "- Adding {kext_name} {kext_version}":"- Adding {kext_name} {kext_version}",
                "- Vaulting EFI\n=========================================":"- Vaulting EFI\n=========================================",
                "- Validating generated config":"- Validating generated config",
                "- OpenCore config file missing!!!":"- OpenCore config file missing!!!",
                "- Missing ACPI Table: {acpi['Path']}":"- Missing ACPI Table: {acpi['Path']}",
                "- Missing kext: {kext_path}":"- Missing kext: {kext_path}",
                "- Missing {kext}'s binary: {kext_binary_path}":"- Missing {kext}'s binary: {kext_binary_path}",
                "- Missing {kext}'s plist: {kext_plist_path}":"- Missing {kext}'s plist: {kext_plist_path}",
                "- Missing tool: {tool}":"- Missing tool: {tool}",
                "- Missing driver: {driver}":"- Missing driver: {driver}",
                "- Missing tool from config: {tool_files_name}":"- Missing tool from config: {tool_files_name}",
                "- Found extra driver: {driver_file_name}":"- Found extra driver: {driver_file_name}",
                "- Missing executable for {kext_folder_name}: Contents/MacOS/{expected_executable_name}":"- Missing executable for {kext_folder_name}: Contents/MacOS/{expected_executable_name}",
                "- Cleaning up files":"- Cleaning up files",
                "OpenCore config file missing":"OpenCore config file missing",
                "Missing":"Missing",
                " - Unknown plugin found: {plugin_name}":" - Unknown plugin found: {plugin_name}",
            }
        elif self.language_point=="简体中文":
            trans={
                "- Unknown plugin found: {plugin_name}":"- 找到未知插件：{plugin_name}",
                "Missing":"缺失",
                "OpenCore config file missing":"OpenCore 配置文件缺失",
                "- Could not find kext {bundle_path}!":"- 找不到 kext {bundle_path}!",
                "- Could not find {efi_type}: {bundle_name}!":"- 找不到 {efi_type}: {bundle_name}!",
                "- Adding {kext_name} {kext_version}":"- 添加 {kext_name} {kext_version}",
                "- Vaulting EFI\n=========================================":"- 正在加密 EFI\n=========================================",
                "- Validating generated config":"- 正在验证生成的配置",
                "- OpenCore config file missing!!!":"- OpenCore 配置文件缺失！！！",
                "- Missing ACPI Table: {acpi['Path']}":"- 缺失 ACPI 表：{acpi['Path']}",
                "- Missing kext: {kext_path}":"- 缺失 kext：{kext_path}",
                "- Missing {kext}'s binary: {kext_binary_path}":"- 缺失 {kext} 的二进制文件：{kext_binary_path}",
                "- Missing {kext}'s plist: {kext_plist_path}":"- 缺失 {kext} 的 plist：{kext_plist_path}",
                "- Missing tool: {tool}":"- 缺失工具：{tool}",
                "- Missing driver: {driver}":"- 缺失驱动：{driver}",
                "- Missing tool from config: {tool_files_name}":"- 配置中缺失工具：{tool_files_name}",
                "- Found extra driver: {driver_file_name}":"- 发现额外驱动：{driver_file_name}",
                "- Missing executable for {kext_folder_name}: Contents/MacOS/{expected_executable_name}":"- 缺失 {kext_folder_name} 的可执行文件：Contents/MacOS/{expected_executable_name}",
                "- Cleaning up files":"- 正在清理文件"
            }
        return trans

    def wired(self):
        if self.language_point=="English":
            trans={
                "- Detected Ethernet hardware, using on-model detection":"- Detected Ethernet hardware, using on-model detection",
                "- No Ethernet detected, using pre-built assumptions":"- No Ethernet detected, using pre-built assumptions",
                "- Enabling USB ECM dongle support":"- Enabling USB ECM dongle support",
                "- Enabling i210 NIC support":"- Enabling i210 NIC support",
                "- Enabling BCM5701 Ethernet support":"- Enabling BCM5701 Ethernet support",
                "- Enabling Intel I210 Ethernet support":"- Enabling Intel I210 Ethernet support",
                "- Enabling Intel 8254X Ethernet support":"- Enabling Intel 8254X Ethernet support",
                "- Enabling Intel 82574L Ethernet support":"- Enabling Intel 82574L Ethernet support",
                "- Enabling NVIDIA nForce Ethernet support":"- Enabling NVIDIA nForce Ethernet support",
                "- Enabling Marvell Ethernet support":"- Enabling Marvell Ethernet support",
                "- Enabling Aquantia Ethernet support":"- Enabling Aquantia Ethernet support"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Detected Ethernet hardware, using on-model detection":"- 检测到以太网硬件，使用型号检测",
                "- No Ethernet detected, using pre-built assumptions":"- 未检测到以太网，使用预构建假设",
                "- Enabling USB ECM dongle support":"- 启用 USB ECM 加密狗支持",
                "- Enabling i210 NIC support":"- 启用 i210 网卡支持",
                "- Enabling BCM5701 Ethernet support":"- 启用 BCM5701 以太网支持",
                "- Enabling Intel I210 Ethernet support":"- 启用 Intel I210 以太网支持",
                "- Enabling Intel 8254X Ethernet support":"- 启用 Intel 8254X 以太网支持",
                "- Enabling Intel 82574L Ethernet support":"- 启用 Intel 82574L 以太网支持",
                "- Enabling NVIDIA nForce Ethernet support":"- 启用 NVIDIA nForce 以太网支持",
                "- Enabling Marvell Ethernet support":"- 启用 Marvell 以太网支持",
                "- Enabling Aquantia Ethernet support":"- 启用 Aquantia 以太网支持"
            }
        return trans

    def wireless(self):
        if self.language_point=="English":
            trans={
                "- Found Wireless Device {0}:{1}":"- Found Wireless Device {0}:{1}",
                "- Setting Wireless Card's Country Code: {self.computer.wifi.country_code}":"- Setting Wireless Card's Country Code: {self.computer.wifi.country_code}",
                "- Found ARPT device at {arpt_path}":"- Found ARPT device at {arpt_path}",
                "- Enabling Wake on WLAN support":"- Enabling Wake on WLAN support",
                "- Enabling BCM943224 and BCM94331 Networking Support":"- Enabling BCM943224 and BCM94331 Networking Support",
                "- Enabling BCM94328 Networking Support":"- Enabling BCM94328 Networking Support",
                "- Enabling Atheros Networking Support":"- Enabling Atheros Networking Support",
                "No known PCI pathing for this model":"No known PCI pathing for this model",
                "- Using known ARPT Path: {arpt_path}":"- Using known ARPT Path: {arpt_path}",
                "- Applying fake ID for WiFi, setting Country Code: {self.computer.wifi.country_code}":"- Applying fake ID for WiFi, setting Country Code: {self.computer.wifi.country_code}"
            }
        elif self.language_point=="简体中文":
            trans={
                "- Found Wireless Device {0}:{1}":"- 发现无线设备 {0}:{1}",
                "- Setting Wireless Card's Country Code: {self.computer.wifi.country_code}":"- 设置无线网卡的国家代码：{self.computer.wifi.country_code}",
                "- Found ARPT device at {arpt_path}":"- 在 {arpt_path} 发现 ARPT 设备",
                "- Enabling Wake on WLAN support":"- 启用无线局域网唤醒支持",
                "- Enabling BCM943224 and BCM94331 Networking Support":"- 启用 BCM943224 和 BCM94331 网络支持",
                "- Enabling BCM94328 Networking Support":"- 启用 BCM94328 网络支持",
                "- Enabling Atheros Networking Support":"- 启用 Atheros 网络支持",
                "No known PCI pathing for this model":"此型号没有已知的 PCI 路径",
                "- Using known ARPT Path: {arpt_path}":"- 使用已知的 ARPT 路径：{arpt_path}",
                "- Applying fake ID for WiFi, setting Country Code: {self.computer.wifi.country_code}":"- 为 WiFi 应用假 ID，设置国家代码：{self.computer.wifi.country_code}"
            }
        return trans