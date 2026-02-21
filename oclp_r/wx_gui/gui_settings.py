"""
gui_settings.py: Settings Frame for the GUI
"""

from pdb import Restart
import wx
import wx.adv
import pprint
import logging
import py_sip_xnu
import subprocess

from pathlib import Path

from .. import constants

from ..sys_patch import sys_patch

from ..wx_gui import (
    gui_support,
    gui_update
)
from ..support import (
    global_settings,
    defaults,
    generate_smbios,
    network_handler,
    subprocess_wrapper,
    hackdoc_private,
)
from ..datasets import (
    model_array,
    sip_data,
    smbios_data,
    os_data,
    cpu_data
)
from ..support   import utilities
from ..support.translate_language import TranslateLanguage
import platform
class SettingsFrame(wx.Frame):
    """
    Modal-based Settings Frame
    """

    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants, screen_location: tuple = None):
        self.trans=TranslateLanguage(global_constants).gui_settings()
        logging.info(self.trans["Initializing Settings Frame"])
        hackdoc_private.PRIVATE()
        self.constants: constants.Constants = global_constants
        self.title: str = title
        self.parent: wx.Frame = parent
        self.xnu_major = int(platform.release().split(".")[0])
        self.hyperlink_colour = (25, 179, 231)
        self.settings = self._settings()

        self.frame_modal = wx.Dialog(parent, title=title, size=(600, 720))

        self._generate_elements(self.frame_modal)
        self.frame_modal.ShowWindowModal()
    def condition_exp(self,key:str):
        import json
        try:
            
            developer_path=Path("~/.hackdoc_developer").expanduser()
            if developer_path.exists():
                return True
            
            base_path=Path("~/Library/Logs/Hackdoc/JSON/control.json").expanduser()
            with open(base_path,"r",encoding="utf-8") as file:
                data=json.load(file)
                if data[key]=="1":
                    return True
            return False
        except:
            return False
    
        
    def _generate_elements(self, frame: wx.Frame = None) -> None:
        """
        Generates elements for the Settings Frame
        Uses wx.Notebook to implement a tabbed interface
        and relies on 'self._settings()' for populating
        """

        notebook = wx.Notebook(frame, style=wx.NB_MULTILINE)
        notebook.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        notebook.SetMinSize((-1, 300))
        if hasattr(self, 'frame_modal'):
            current_size = self.frame_modal.GetSize()
            self.frame_modal.SetSize((current_size[0], max(current_size[1], 750)))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(10)

        model_label = wx.StaticText(frame, label=self.trans["Target Model"], pos=(-1, -1))
        model_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
        sizer.Add(model_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        model_choice = wx.Choice(frame, choices=model_array.SupportedSMBIOS + [self.trans["Host Model"]], pos=(-1, -1), size=(150, -1))
        model_choice.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        model_choice.Bind(wx.EVT_CHOICE, lambda event: self.on_model_choice(event, model_choice))
        selection = self.constants.custom_model if self.constants.custom_model else self.trans["Host Model"]
        model_choice.SetSelection(model_choice.FindString(selection))
        sizer.Add(model_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        model_description = wx.StaticText(frame, label=self.trans["Overrides Mac Model the Patcher will build for."], pos=(-1, -1))
        model_description.SetFont(gui_support.font_factory(11, wx.FONTWEIGHT_NORMAL))
        sizer.Add(model_description, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        tabs = list(self.settings.keys())
        if not Path("~/.hackdoc_developer").expanduser().exists():
            tabs.remove(self.trans["Developer"])
        for tab in tabs:
            panel = wx.Panel(notebook)
            notebook.AddPage(panel, tab)

        sizer.Add(notebook, 1, wx.EXPAND | wx.ALL, 10)

        # Add return button
        return_button = wx.Button(frame, label=self.trans["Return"], pos=(-1, -1), size=(100, 30))
        return_button.Bind(wx.EVT_BUTTON, self.on_return)
        return_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        sizer.Add(return_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        frame.SetSizer(sizer)

        horizontal_center = frame.GetSize()[0] / 2
        for tab in tabs:
            if tab not in self.settings:
                continue

            stock_height = 0
            stock_width = 20

            height = stock_height
            width = stock_width

            lowest_height_reached = height
            highest_height_reached = height

            panel = notebook.GetPage(tabs.index(tab))

            for setting, setting_info in self.settings[tab].items():
                if setting_info["type"] == "populate":
                    # execute populate function
                    if setting_info["args"] == wx.Frame:
                        setting_info["function"](panel)
                    else:
                        raise Exception("Invalid populate function")
                    continue

                if setting_info["type"] == "title":
                    stock_height = lowest_height_reached
                    height = stock_height
                    width = stock_width

                    height += 10

                    # Add title
                    title = wx.StaticText(panel, label=setting, pos=(-1, -1))
                    title.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))

                    title.SetPosition((int(horizontal_center) - int(title.GetSize()[0] / 2) - 15, height))
                    highest_height_reached = height + title.GetSize()[1] + 10
                    height += title.GetSize()[1] + 10
                    continue

                if setting_info["type"] == "sub_title":
                    # Add sub-title
                    sub_title = wx.StaticText(panel, label=setting, pos=(-1, -1))
                    sub_title.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))

                    sub_title.SetPosition((int(horizontal_center) - int(sub_title.GetSize()[0] / 2) - 15, height))
                    highest_height_reached = height + sub_title.GetSize()[1] + 10
                    height += sub_title.GetSize()[1] + 10
                    continue

                if setting_info["type"] == "wrap_around":
                    height = highest_height_reached
                    width = 300 if width is stock_width else stock_width
                    continue

                if setting_info["type"] == "checkbox":
                    # Add checkbox, and description underneath
                    checkbox = wx.CheckBox(panel, label=setting, pos=(10 + width, 10 + height), size = (300,-1))

                    value = False
                    if "value" in setting_info:
                        try:
                            value = bool(setting_info["value"])
                        except ValueError:
                            logging.error(f"Invalid value for {setting}, got {setting_info['value']} (type: {type(setting_info['value'])})")
                            value = False

                    checkbox.SetValue(value)
                    checkbox.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
                    event = lambda event, warning=setting_info["warning"] if "warning" in setting_info else "", override=bool(setting_info["override_function"]) if "override_function" in setting_info else False: self.on_checkbox(event, warning, override)
                    checkbox.Bind(wx.EVT_CHECKBOX, event)
                    if "condition" in setting_info:
                        checkbox.Enable(setting_info["condition"])
                        if setting_info["condition"] is False:
                            checkbox.SetValue(False)

                elif setting_info["type"] == "spinctrl":
                    # Add spinctrl, and description underneath
                    spinctrl = wx.SpinCtrl(panel, value=str(setting_info["value"]), pos=(width - 20, 10 + height), min=setting_info["min"], max=setting_info["max"], size = (45,-1))
                    spinctrl.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
                    spinctrl.Bind(wx.EVT_TEXT, lambda event, variable=setting: self.on_spinctrl(event, variable))
                    # Add label next to spinctrl
                    label = wx.StaticText(panel, label=setting, pos=(spinctrl.GetSize()[0] + width - 16, spinctrl.GetPosition()[1]))
                    label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
                elif setting_info["type"] == "choice":
                    # Title
                    title = wx.StaticText(panel, label=setting, pos=(width + 30, 10 + height))
                    title.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
                    height += title.GetSize()[1] + 10

                    # Add combobox, and description underneath
                    choice = wx.Choice(panel, pos=(width + 25, 10 + height), choices=setting_info["choices"], size = (150,-1))
                    choice.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
                    choice.SetSelection(choice.FindString(setting_info["value"]))
                    if "override_function" in setting_info:
                        choice.Bind(wx.EVT_CHOICE, lambda event, variable=setting: self.settings[tab][variable]["override_function"](event))
                    else:
                        choice.Bind(wx.EVT_CHOICE, lambda event, variable=setting: self.on_choice(event, variable))
                    if "condition" in setting_info:
                        choice.Enable(setting_info["condition"])
                        if setting_info["condition"] is False:
                            choice.Disable()
                    height += 10
                elif setting_info["type"] == "button":
                    button = wx.Button(panel, label=setting, pos=(width + 25, 10 + height), size = (200,-1))
                    button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
                    button.Bind(wx.EVT_BUTTON, lambda event, variable=setting: self.settings[tab][variable]["function"](event))
                    height += 10

                else:
                    raise Exception("Invalid setting type")

                lines = '\n'.join(setting_info["description"])
                description = wx.StaticText(panel, label=lines, pos=(30 + width, 10 + height + 20))
                description.SetFont(gui_support.font_factory(11, wx.FONTWEIGHT_NORMAL))
                height += 40
                if "condition" in setting_info:
                    if setting_info["condition"] is False:
                        description.SetForegroundColour((128, 128, 128))

                # Check number of lines in description, and adjust spacer accordingly
                for i, line in enumerate(lines.split('\n')):
                    if line == "":
                        continue
                    if i == 0:
                        height += 11
                    else:
                        height += 13

                if height > lowest_height_reached:
                    lowest_height_reached = height
    def audio_check(self):
        if self.xnu_major<os_data.os_data.tahoe:
            return False
        if utilities.check_kext_loaded("com.apple.driver.AppleHDA") and self.xnu_major>=os_data.os_data.tahoe:
            self.constants.audio_type="AppleHDA"
            return False
        return True
    def _settings(self) -> dict:
        """
        Generates a dictionary of settings to be used in the GUI
        General format:
        {
            "Tab Name": {
                "type": "title" | "checkbox" | "spinctrl" | "populate" | "wrap_around",
                "value": bool | int | str,
                "variable": str,  (Variable name)
                "constants_variable": str, (Constants variable name, if different from "variable")
                "description": [str, str, str], (List of strings)
                "warning": str, (Optional) (Warning message to be displayed when checkbox is checked)
                "override_function": function, (Optional) (Function to be executed when checkbox is checked)
            }
        }
        """

        models = [model for model in smbios_data.smbios_dictionary if "_" not in model and " " not in model and smbios_data.smbios_dictionary[model]["Board ID"] is not None]
        socketed_imac_models = ["iMac9,1", "iMac10,1", "iMac11,1", "iMac11,2", "iMac11,3", "iMac12,1", "iMac12,2"]
        socketed_gpu_models = socketed_imac_models + ["MacPro3,1", "MacPro4,1", "MacPro5,1", "Xserve2,1", "Xserve3,1"]

        settings = {
            self.trans["Build"]: {
                self.trans["General"]: {
                    "type": "title",
                },
                self.trans["FireWire Booting"]: {
                    "type": "checkbox",
                    "value": self.constants.firewire_boot,
                    "variable": "firewire_boot",
                    "description": [
                        self.trans["Enable booting macOS from"],
                        self.trans["FireWire drives."],
                    ],
                    "condition": not (generate_smbios.check_firewire(self.constants.custom_model or self.constants.computer.real_model) is False)
                },
                self.trans["XHCI Booting"]: {
                    "type": "checkbox",
                    "value": self.constants.xhci_boot,
                    "variable": "xhci_boot",
                    "description": [
                        self.trans["Enable booting macOS from add-in"],
                        self.trans["USB 3.0 expansion cards on systems"],
                        self.trans["without native support."],
                    ],
                    "condition": not gui_support.CheckProperties(self.constants).host_has_cpu_gen(cpu_data.CPUGen.ivy_bridge) # Sandy Bridge and older do not natively support XHCI booting
                },
                self.trans["NVMe Booting"]: {
                    "type": "checkbox",
                    "value": self.constants.nvme_boot,
                    "variable": "nvme_boot",
                    "description": [
                        self.trans["Enable booting macOS from NVMe"],
                        self.trans["drives on systems without native"],
                        self.trans["support."],
                        self.trans["Note: Requires Firmware support"],
                        self.trans["for OpenCore to load from NVMe."],
                    ],
                    "condition": not gui_support.CheckProperties(self.constants).host_has_cpu_gen(cpu_data.CPUGen.ivy_bridge) # Sandy Bridge and older do not natively support NVMe booting
                },
                "wrap_around 2": {
                    "type": "wrap_around",
                },
                self.trans["OpenCore Vaulting"]: {
                    "type": "checkbox",
                    "value": self.constants.vault,
                    "variable": "vault",
                    "description": [
                        self.trans["Digitally sign OpenCore to prevent"],
                        self.trans["tampering or corruption."]
                    ],
                },

                self.trans["Show OpenCore Boot Picker"]: {
                    "type": "checkbox",
                    "value": self.constants.showpicker,
                    "variable": "showpicker",
                    "description": [
                        self.trans["When disabled, users can hold ESC to"],
                        self.trans["show picker in the firmware."],
                    ],
                },
                self.trans["Boot Picker Timeout"]: {
                    "type": "spinctrl",
                    "value": self.constants.oc_timeout,
                    "variable": "oc_timeout",
                    "description": [
                        self.trans["Timeout before boot picker selects default"],
                        self.trans["entry in seconds."],
                        self.trans["Set to 0 for no timeout."],
                    ],

                    "min": 0,
                    "max": 60,
                },
                self.trans["MacPro3,1/Xserve2,1 Workaround"]: {
                    "type": "checkbox",
                    "value": self.constants.force_quad_thread,
                    "variable": "force_quad_thread",
                    "description": [
                        self.trans["Limits to 4 threads max on these units."],
                        self.trans["Required for macOS Sequoia and later."],
                    ],
                    "condition": (self.constants.custom_model and self.constants.custom_model in ["MacPro3,1", "Xserve2,1"]) or self.constants.computer.real_model in ["MacPro3,1", "Xserve2,1"]
                },
                self.trans["Debug"]: {
                    "type": "title",
                },

                self.trans["Verbose"]: {
                    "type": "checkbox",
                    "value": self.constants.verbose_debug,
                    "variable": "verbose_debug",
                    "description": [
                        self.trans["Verbose output during boot."],
                    ],

                },
                self.trans["Kext Debugging"]: {
                    "type": "checkbox",
                    "value": self.constants.kext_debug,
                    "variable": "kext_debug",
                    "description": [
                        self.trans["Use DEBUG variants of kexts and"],
                        self.trans["enables additional kernel logging."],
                    ],
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["OpenCore Debugging"]: {
                    "type": "checkbox",
                    "value": self.constants.opencore_debug,
                    "variable": "opencore_debug",
                    "description": [
                        self.trans["Use DEBUG variant of OpenCore"],
                        self.trans["and enables additional logging."],
                    ],
                },
            },
            self.trans["Extras"]: {
                self.trans["General (Continued)"]: {
                    "type": "title",
                },
                self.trans["Wake on WLAN"]: {
                    "type": "checkbox",
                    "value": self.constants.enable_wake_on_wlan,
                    "variable": "enable_wake_on_wlan",
                    "description": [
                        self.trans["Disabled by default due to"],
                        self.trans["performance degradation"],
                        self.trans["on some systems from wake."],
                        self.trans["Only applies to BCM943224, 331,"],
                        self.trans["360 and 3602 chipsets."],
                    ],
                },
                self.trans["Disable Thunderbolt"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_tb,
                    "variable": "disable_tb",
                    "description": [
                        self.trans["For MacBookPro11,x with faulty"],
                        self.trans["PCHs that may crash sporadically."],    
                    ],
                    "condition": (self.constants.custom_model and self.constants.custom_model in ["MacBookPro11,1", "MacBookPro11,2", "MacBookPro11,3"]) or self.constants.computer.real_model in ["MacBookPro11,1", "MacBookPro11,2", "MacBookPro11,3"]
                },
                self.trans["Windows GMUX"]: {
                    "type": "checkbox",
                    "value": self.constants.dGPU_switch,
                    "variable": "dGPU_switch",
                    "description": [
                        self.trans["Allow iGPU to be exposed in Windows"],
                        self.trans["for dGPU-based MacBooks."],
                    ],
                },
                self.trans["Disable CPUFriend"]: {
                    "type": "checkbox",
                    "value": self.constants.disallow_cpufriend,
                    "variable": "disallow_cpufriend",
                    "description": [
                        self.trans["Disables power management helper"],
                        self.trans["for unsupported models."],
                    ],
                },
                self.trans["Disable mediaanalysisd service"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_mediaanalysisd,
                    "variable": "disable_mediaanalysisd",
                    "description": [
                        self.trans["For systems that are the primary iCloud"],
                        self.trans["Photo Library host with a 3802-based GPU,"],
                        self.trans["this may aid in prolonged idle stability."],    
                    ],
                    "condition": gui_support.CheckProperties(self.constants).host_has_3802_gpu()
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["Allow AppleALC Audio"]: {
                    "type": "checkbox",
                    "value": self.constants.set_alc_usage,
                    "variable": "set_alc_usage",
                    "description": [
                        self.trans["Allow AppleALC to manage audio"],
                        self.trans["if applicable."],
                        self.trans["Only disable if your host lacks"],
                        self.trans["a GOP ROM."],
                    ],
                },
                self.trans["NVRAM WriteFlash"]: {
                    "type": "checkbox",
                    "value": self.constants.nvram_write,
                    "variable": "nvram_write",
                    "description": [
                        self.trans["Allow OpenCore to write to NVRAM."],
                        self.trans["Disable on systems with faulty or"],
                        self.trans["degraded NVRAM."],
                    ],
                },
                self.trans["3rd Party NVMe PM"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_nvme_fixing,
                    "variable": "allow_nvme_fixing",
                    "description": [
                        self.trans["Enable non-stock NVMe power"],
                        self.trans["management in macOS."],
                    ],
                },
                self.trans["3rd Party SATA PM"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_3rd_party_drives,
                    "variable": "allow_3rd_party_drives",
                    "description": [
                        self.trans["Enable non-stock SATA power"],
                        self.trans["management in macOS."],
                    ],
                    "condition": not bool(self.constants.computer.third_party_sata_ssd is False and not self.constants.custom_model)
                },
                self.trans["APFS Trim"]: {
                    "type": "checkbox",
                    "value": self.constants.apfs_trim_timeout,
                    "variable": "apfs_trim_timeout",
                    "description": [
                        self.trans["Recommended for all users, however faulty"],
                        self.trans["SSDs may benefit from disabling this."],
                    ],
                },
            },
            self.trans["Advanced"]: {
                self.trans["Miscellaneous"]: {
                    "type": "title",
                },
                self.trans["Disable Firmware Throttling"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_fw_throttle,
                    "variable": "disable_fw_throttle",
                    "description": [
                        self.trans["Disables firmware-based throttling"],
                        self.trans["caused by missing hardware."],
                        self.trans["Ex. Missing Display, Battery, etc."],
                    ],
                },
                self.trans["Software DeMUX"]: {
                    "type": "checkbox",
                    "value": self.constants.software_demux,
                    "variable": "software_demux",
                    "description": [
                        self.trans["Enable software based DeMUX"],
                        self.trans["for MacBookPro8,2 and MacBookPro8,3."],
                        self.trans["Prevents faulty dGPU from turning on."],
                        self.trans["Note: Requires associated NVRAM arg:"],
                        self.trans["'gpu-power-prefs'."],
                    ],
                    "warning": self.trans["This settings requires 'gpu-power-prefs' NVRAM argument to be set to '1'.\n\nIf missing and this option is toggled, the system will not boot\n\nFull command:\nnvram FA4CE28D-B62F-4C99-9CC3-6815686E30F9:gpu-power-prefs=%01%00%00%00"],
                    "condition": not bool((not self.constants.custom_model and self.constants.computer.real_model not in ["MacBookPro8,2", "MacBookPro8,3"]) or (self.constants.custom_model and self.constants.custom_model not in ["MacBookPro8,2", "MacBookPro8,3"]))
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["FeatureUnlock"]: {
                    "type": "choice",
                    "choices": [
                        "Enabled",
                        "Partial",
                        "Disabled",
                    ],
                    "value": "Enabled",
                    "variable": "",
                    "description": [
                        self.trans["Configure FeatureUnlock level."],
                        self.trans["Recommend lowering if your system"],
                        self.trans["experiences memory instability."],
                    ],
                },
                self.trans["Populate FeatureUnlock Override"]: {
                    "type": "populate",
                    "function": self._populate_fu_override,
                    "args": wx.Frame,
                },
                self.trans["Hibernation Work-around"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_connectdrivers,
                    "variable": "disable_connectdrivers",
                    "description": [
                        self.trans["Only load minimum EFI drivers"],
                        self.trans["to prevent hibernation issues."],
                        self.trans["Note: This may break booting from"],    
                        self.trans["external drives."],
                    ],
                },
                self.trans["Graphics"]: {
                    "type": "title",
                },
                self.trans["AMD GOP Injection"]: {
                    "type": "checkbox",
                    "value": self.constants.amd_gop_injection,
                    "variable": "amd_gop_injection",
                    "description": [
                        self.trans["Inject AMD GOP for boot screen"],
                        self.trans["support on PC GPUs."],
                    ],
                    "condition": not bool((not self.constants.custom_model and self.constants.computer.real_model not in socketed_gpu_models) or (self.constants.custom_model and self.constants.custom_model not in socketed_gpu_models))
                },
                self.trans["Nvidia GOP Injection"]: {
                    "type": "checkbox",
                    "value": self.constants.nvidia_kepler_gop_injection,
                    "variable": "nvidia_kepler_gop_injection",
                    "description": [
                        self.trans["Inject Nvidia Kepler GOP for boot screen"],
                        self.trans["support on PC GPUs."],
                    ],
                    "condition": not bool((not self.constants.custom_model and self.constants.computer.real_model not in socketed_gpu_models) or (self.constants.custom_model and self.constants.custom_model not in socketed_gpu_models))
                },
                "wrap_around 2": {
                    "type": "wrap_around",
                },
                self.trans["Graphics Override"]: {
                    "type": "choice",
                    "choices": [
                        "None",
                        "Nvidia Kepler",
                        "AMD GCN",
                        "AMD Polaris",
                        "AMD Lexa",
                        "AMD Navi",
                    ],
                    "value": "None",
                    "variable": "",
                    "description": [
                        self.trans["Override detected/assumed GPU on"],
                        self.trans["socketed MXM-based iMacs."],
                    ],
                    "condition": bool((not self.constants.custom_model and self.constants.computer.real_model in socketed_imac_models) or (self.constants.custom_model and self.constants.custom_model in socketed_imac_models))
                },
                "Populate Graphics Override": {
                    "type": "populate",
                    "function": self._populate_graphics_override,
                    "args": wx.Frame,
                },

            },
            self.trans["Security"]: {
                self.trans["Kernel Security"]: {
                    "type": "title",
                },
                self.trans["Disable Library Validation"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_cs_lv,
                    "variable": "disable_cs_lv",
                    "description": [
                        self.trans["Required for loading modified"],
                        self.trans["system files from root patching."],
                    ],
                },
                self.trans["Disable AMFI"]: {
                    "type": "checkbox",
                    "value": self.constants.disable_amfi,
                    "variable": "disable_amfi",
                    "description": [
                        self.trans["Extended version of 'Disable"],
                        self.trans["Library Validation', required"],
                        self.trans["for systems with deeper"],
                        self.trans["root patches."],
                    ],
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["Secure Boot Model"]: {
                    "type": "checkbox",
                    "value": self.constants.secure_status,
                    "variable": "secure_status",
                    "description": [
                        self.trans["Set Apple Secure Boot Model Identifier"],
                        self.trans["to matching T2 model if spoofing."],
                        self.trans["Note: Incompatible with Root Patching."],
                    ],
                },
                self.trans["System Integrity Protection"]: {
                    "type": "title",
                },
                "Populate SIP": {
                    "type": "populate",
                    "function": self._populate_sip_settings,
                    "args": wx.Frame,
                },
            },
            self.trans["SMBIOS"]: {
                self.trans["Model Spoofing"]: {
                    "type": "title",
                },
                self.trans["SMBIOS Spoof Level"]: {
                    "type": "choice",
                    "choices": [
                        "None",
                        "Minimal",
                        "Moderate",
                        "Advanced",
                    ],
                    "value": self.constants.serial_settings,
                    "variable": "serial_settings",
                    "description": [
                        self.trans["Supported Levels:"],
                        self.trans["   - None: No spoofing."],
                        self.trans["   - Minimal: Overrides Board ID."],
                        self.trans["   - Moderate: Overrides Model."],
                        self.trans["   - Advanced: Overrides Model and serial."],
                    ],
                },
                self.trans["SMBIOS Spoof Model"]: {
                    "type": "choice",
                    "choices": models + ["Default"],
                    "value": self.constants.override_smbios,
                    "variable": "override_smbios",
                    "description": [
                        self.trans["Set Mac Model to spoof to."],
                    ],

                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["Allow spoofing native Macs"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_native_spoofs,
                    "variable": "allow_native_spoofs",
                    "description": [
                        self.trans["Allow OpenCore to spoof natively"],
                        self.trans["supported Macs."],
                        self.trans["Primarily used for enabling"],
                        self.trans["Universal Control on unsupported Macs"],
                    ],
                },
                self.trans["Serial Spoofing"]: {
                    "type": "title",
                },
                "Populate Serial Spoofing": {
                    "type": "populate",
                    "function": self._populate_serial_spoofing_settings,
                    "args": wx.Frame,
                },
            },
            self.trans["Patch"]: {
                self.trans["Patch-General"]: {
                    "type": "title",
                },
                self.trans["TeraScale 2 Acceleration"]: {
                    "type": "checkbox",
                    "value": global_settings.GlobalEnviromentSettings().read_property("MacBookPro_TeraScale_2_Accel") or self.constants.allow_ts2_accel,
                    "variable": "MacBookPro_TeraScale_2_Accel",
                    "constants_variable": "allow_ts2_accel",
                    "description": [
                        self.trans["Enable AMD TeraScale 2 GPU"],
                        self.trans["Acceleration on MacBookPro8,2 and"],
                        self.trans["MacBookPro8,3."],
                        self.trans["By default this is disabled due to"],
                        self.trans["common GPU failures on these models."],
                    ],
                    "override_function": self._update_global_settings,
                    "condition": not bool(self.constants.computer.real_model not in ["MacBookPro8,2", "MacBookPro8,3"])
                },
                self.trans["Audio Patch choice"]: {
                    "type": "choice",
                    "choices": [
                        "AppleHDA",
                        "VoodooHDA"
                    ],
                    "value": self.constants.audio_type,
                    "variable": "audio_type",
                    "constants_variable": "audio_type",
                    "description": [
                        self.trans["   - AppleALC: AppleALC patch on Tahoe."],
                        self.trans["   - VoodooHDA: VoodooHDA patch ,"],
                        self.trans["  on Monterey and newer."],
                        self.trans["  Not recommended."],
                    ],
                    "condition":self.audio_check()
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["Allow Tahoe Modern USB Patch"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_usb_patch,
                    "variable": "allow_usb_patch",
                    "constants_variable": "allow_usb_patch",
                    "description": [
                        self.trans["When enabled, this will patch the Old USB"],
                        self.trans["extensions on Tahoe."],
                    ],
                    "condition":self.condition_exp("USB")
                },     
                self.trans["Allow APFS Patch For Non-T2"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_apfs_aligned_patch,
                    "variable": "allow_apfs_aligned_patch",
                    "constants_variable": "allow_apfs_aligned_patch",
                    "description": [
                        self.trans["When enabled, this will patch the apfs.efi"],
                        self.trans["on Tahoe."],
                    ],
                },     
                self.trans["AppleHDA.kext Version"]: {
                    "type": "choice",
                    "choices": [
                        "15.6",
                        "26.0 Beta 1"
                    ],
                    "value": self.constants.applehda_version,
                    "variable": "applehda_version",
                    "constants_variable": "applehda_version",
                    "description": [
                        "",
                    ],
                },         
            },
            self.trans["Non-Metal"]:{
                self.trans["Non-Metal Settings"]: {
                    "type": "title",
                },
                self.trans["Log out required to apply changes to SkyLight"]: {
                    "type": "sub_title",
                },
                self.trans["Dark Menu Bar"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Moraea_DarkMenuBar"),
                    "variable": "Moraea_DarkMenuBar",
                    "description": [
                        self.trans["If Beta Menu Bar is enabled,"],
                        self.trans["menu bar colour will dynamically"],
                    ],
                    "override_function": self._update_system_defaults,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)
                },
                self.trans["Beta Blur"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Moraea_BlurBeta"),
                    "variable": "Moraea_BlurBeta",
                    "description": [
                        self.trans["Control window blur behaviour."],
                    ],
                    "override_function": self._update_system_defaults,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)

                },
                self.trans["Beach Ball Cursor Workaround"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Moraea.EnableSpinHack"),
                    "variable": "Moraea.EnableSpinHack",
                    "description": [
                        self.trans["Control beach ball cursor behaviour."],
                    ],
                    "override_function": self._update_system_defaults_root,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)
                },
                "wrap_around 2": {
                    "type": "wrap_around",
                },
                self.trans["Beta Menu Bar"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Amy.MenuBar2Beta"),
                    "variable": "Amy.MenuBar2Beta",
                    "description": [
                        self.trans["Supports dynamic colour changes."],
                    ],
                    "override_function": self._update_system_defaults,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)
                },
                self.trans["Disable Beta Rim"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Moraea_RimBetaDisabled"),
                    "variable": "Moraea_RimBetaDisabled",
                    "description": [
                        self.trans["Control Window Rim rendering."],
                    ],
                    "override_function": self._update_system_defaults,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)
                },
                self.trans["Disable Color Widgets Enforcement"]: {
                    "type": "checkbox",
                    "value": self._get_system_settings("Moraea_ColorWidgetDisabled"),
                    "variable": "Moraea_ColorWidgetDisabled",
                    "description": [
                        self.trans["Control Color Desktop Widgets Enforcement."],
                    ],
                    "override_function": self._update_system_defaults,
                    "condition": gui_support.CheckProperties(self.constants).host_is_non_metal(general_check=True)
                },
            },
            self.trans["App"]: {
                self.trans["General"]: {
                    "type": "title",
                },
                self.trans["Allow native models"]: {
                    "type": "checkbox",
                    "value": self.constants.allow_oc_everywhere,
                    "variable": "allow_oc_everywhere",
                    "description": [
                        self.trans["Allow OpenCore to be installed"],
                        self.trans["on natively supported Macs."],
                        self.trans["Note this will not allow unsupported"],
                        self.trans["macOS versions to be installed on"],
                        self.trans["your system."],
                    ],
                    "warning": self.trans["This option should only be used if your Mac natively supports the OSes you wish to run.\n\nIf you are currently running an unsupported OS, this option will break booting. Only toggle for enabling OS features on a native Mac.\n\nAre you certain you want to continue?"],
                },
                self.trans["Ignore App Updates"]: {
                    "type": "checkbox",
                    "value": global_settings.GlobalEnviromentSettings().read_property("IgnoreAppUpdates") or self.constants.ignore_updates,
                    "variable": "IgnoreAppUpdates",
                    "constants_variable": "ignore_updates",
                    "description": [
                        # "Ignore app updates",
                    ],
                    "override_function": self._update_global_settings,
                },                
                self.trans["Github Proxy"]: {
                    "type": "choice",
                    "choices": [
                        "Default",
                        "SimpleHac",
                        "gh-proxy",
                        "ghfast",
                        "ghllkk",
                    ],
                    "value": self.constants.github_proxy_link,
                    "variable": "github_proxy_link",
                    "constants_variable": "github_proxy_link",
                    "description": [
                        self.trans["Default : https://dortania.github.io/"],
                        self.trans["SimpleHac : https://next.oclpapi.simplehac.cn/"],
                        self.trans["gh-proxy : https://gh-proxy.com/"],
                        self.trans["ghfast : https://ghfast.top/"],
                        self.trans["ghllkk : https://gh.llkk.cc/"],
                    ],
                },
                
                "wrap_around 1": {
                    "type": "wrap_around",
                },                
                self.trans["Disable Reporting"]: {
                    "type": "checkbox",
                    "value": global_settings.GlobalEnviromentSettings().read_property("DisableCrashAndAnalyticsReporting"),
                    "variable": "DisableCrashAndAnalyticsReporting",
                    "description": [
                        self.trans["When enabled, patcher will not"],
                        self.trans["report any info to Hackdoc."],
                    ],
                    "override_function": self._update_global_settings,
                },
                self.trans["Remove Unused KDKs"]: {
                    "type": "checkbox",
                    "value": global_settings.GlobalEnviromentSettings().read_property("ShouldNukeKDKs") or self.constants.should_nuke_kdks,
                    "variable": "ShouldNukeKDKs",
                    "constants_variable": "should_nuke_kdks",
                    "description": [
                        self.trans["When enabled, the app will remove"],
                        self.trans["unused Kernel Debug Kits from the system"],
                        self.trans["during root patching."],
                    ],
                    "override_function": self._update_global_settings,
                },               
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                #manually_download_kdk
                self.trans["Manually Download KDKs and\nMetallibs"]: {
                    "type": "checkbox",
                    "value": self.constants.manually_download_kdk,
                    "variable": "manually_download_kdk",
                    "constants_variable": "manually_download_kdk",
                    "description": [
                        "",
                        self.trans["When enabled, patcher will allow"],
                        self.trans["you download KDKs and metallibs manually."],
                    ],
                },
                self.trans["Choose Your Language"]:{
                    "type": "choice",
                    "choices": self.constants.language_key,
                    "value": self.constants.language_option,
                    "variable": "language_option",
                    "constants_variable": "language_option",
                    "description": [
                        self.trans["Provide English & Chinese Simplified."],
                    ],
                    #"override_function": self.close,
                },
                
                self.trans["Misc"]: {
                    "type": "title",
                },
                "Choose Download Path": {
                    "type": "populate",
                    "function": self._change_download_path,
                    "args": wx.Frame,
                },
            },
            self.trans["Developer"]: {
                "Validation": {
                    "type": "title",
                },
                self.trans["Install latest nightly build 🧪"]: {
                    "type": "button",
                    "function": self.on_nightly,
                    "description": [
                        self.trans["If you're already here, I assume you're ok"],
                        self.trans["bricking your system 🧱."],
                        self.trans["Check CHANGELOG before blindly updating."],
                    ],
                },
                self.trans["Trigger Exception"]: {
                    "type": "button",
                    "function": self.on_test_exception,
                    "description": [
                    ],
                },
                "wrap_around 1": {
                    "type": "wrap_around",
                },
                self.trans["Export constants"]: {
                    "type": "button",
                    "function": self.on_export_constants,
                    "description": [
                        self.trans["Export constants.py values to a txt file."],
                    ],
                },

                self.trans["Developer Root Volume Patching"]: {
                    "type": "title",
                },
                self.trans["Mount Root Volume"]: {
                    "type": "button",
                    "function": self.on_mount_root_vol,
                    "description": [
                        self.trans["Life's too short to type 'sudo mount -o"],
                        self.trans["nobrowse -t apfs /dev/diskXsY"],
                        self.trans["/System/Volumes/Update/mnt1' every time."],
                    ],
                },
                "wrap_around 2": {
                    "type": "wrap_around",
                },
                self.trans["Save Root Volume"]: {
                    "type": "button",
                    "function": self.on_bless_root_vol,
                    "description": [
                        self.trans["Rebuild kernel cache and bless snapshot 🙏"],
                    ],
                },
                self.trans["Statistics"]: {
                    "type": "title",
                },
                "Populate Stats": {
                    "type": "populate",
                    "function": self._populate_app_stats,
                    "args": wx.Frame,
                },
            },
        }

        return settings


    def on_model_choice(self, event: wx.Event, model_choice: wx.Choice) -> None:
        """
        Sets model to use for patching.
        """

        selection = model_choice.GetStringSelection()
        if selection == self.trans["Host Model"]:
            selection = self.constants.computer.real_model
            self.constants.custom_model = None
            logging.info(self.trans["Using Real Model: {model}"].format(model=self.constants.computer.real_model))
            defaults.GenerateDefaults(self.constants.computer.real_model, True, self.constants)
        else:
            logging.info(self.trans["Using Custom Model: {selection}"].format(selection=selection))
            self.constants.custom_model = selection
            defaults.GenerateDefaults(self.constants.custom_model, False, self.constants)
            self.parent.build_button.Enable()



        self.parent.model_label.SetLabel(self.trans["Model: {selection}"].format(selection=selection))
        self.parent.model_label.Centre(wx.HORIZONTAL)

        self.frame_modal.Destroy()
        SettingsFrame(
            parent=self.parent,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.parent.GetPosition()
        )


    def _populate_sip_settings(self, panel: wx.Frame) -> None:

        horizontal_spacer = 250

        # Look for title on frame
        sip_title: wx.StaticText = None
        for child in panel.GetChildren():
            if child.GetLabel() == self.trans["System Integrity Protection"]:
                sip_title = child
                break


        # Label: Flip individual bits corresponding to XNU's csr.h
        # If you're unfamiliar with how SIP works, do not touch this menu
        sip_label = wx.StaticText(panel, label=self.trans["Flip individual bits corresponding to"], pos=(sip_title.GetPosition()[0] - 20, sip_title.GetPosition()[1] + 30))
        sip_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))

        # Hyperlink: csr.h
        spacer = 1 if self.constants.detected_os >= os_data.os_data.big_sur else 3
        sip_csr_h = wx.adv.HyperlinkCtrl(panel, id=wx.ID_ANY, label="XNU's csr.h", url="https://github.com/apple-oss-distributions/xnu/blob/xnu-8020.101.4/bsd/sys/csr.h", pos=(sip_label.GetPosition()[0] + sip_label.GetSize()[0] + 4, sip_label.GetPosition()[1] + spacer))
        sip_csr_h.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        sip_csr_h.SetHoverColour(self.hyperlink_colour)
        sip_csr_h.SetNormalColour(self.hyperlink_colour)
        sip_csr_h.SetVisitedColour(self.hyperlink_colour)

        # Label: SIP Status
        if self.constants.custom_sip_value is not None:
            self.sip_value = int(self.constants.custom_sip_value, 16)
        elif self.constants.sip_status is True:
            self.sip_value = 0x00
        else:
            self.sip_value = 0x803
        sip_configured_label = wx.StaticText(panel, label=f"{self.trans['Currently configured SIP:']} {hex(self.sip_value)}", pos=(sip_label.GetPosition()[0] + 35, sip_label.GetPosition()[1] + 20))
        sip_configured_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
        self.sip_configured_label = sip_configured_label

        # Label: SIP Status
        sip_booted_label = wx.StaticText(panel, label=f"{self.trans['Currently booted SIP:']} {hex(py_sip_xnu.SipXnu().get_sip_status().value)}", pos=(sip_configured_label.GetPosition()[0], sip_configured_label.GetPosition()[1] + 20))
        sip_booted_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))


        # SIP toggles
        entries_per_row = len(sip_data.system_integrity_protection.csr_values) // 2
        horizontal_spacer = 15
        vertical_spacer = 25
        index = 1
        for sip_bit in sip_data.system_integrity_protection.csr_values_extended:
            self.sip_checkbox = wx.CheckBox(panel, label=sip_data.system_integrity_protection.csr_values_extended[sip_bit]["name"].split("CSR_")[1], pos = (vertical_spacer, sip_booted_label.GetPosition()[1] + 20 + horizontal_spacer))
            self.sip_checkbox.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
            self.sip_checkbox.SetToolTip(f'{self.trans["Description:"]} {sip_data.system_integrity_protection.csr_values_extended[sip_bit]["description"]}\nValue: {hex(sip_data.system_integrity_protection.csr_values_extended[sip_bit]["value"])}\nIntroduced in: macOS {sip_data.system_integrity_protection.csr_values_extended[sip_bit]["introduced_friendly"]}')

            if self.sip_value & sip_data.system_integrity_protection.csr_values_extended[sip_bit]["value"] == sip_data.system_integrity_protection.csr_values_extended[sip_bit]["value"]:
                self.sip_checkbox.SetValue(True)

            horizontal_spacer += 20
            if index == entries_per_row:
                horizontal_spacer = 15
                vertical_spacer += 250

            index += 1
            self.sip_checkbox.Bind(wx.EVT_CHECKBOX, self.on_sip_value)
    def on_text_change(self, event:wx.Event):
        self.constants.user_download_file = event.GetEventObject().GetValue()
        logging.info(f"{self.trans['user_download_file:']} {self.constants.user_download_file}")
    def _change_download_path(self,panel:wx.Frame) -> None:
        def is_dir_writable(dirpath):
            import os
            return os.access(dirpath, os.W_OK | os.X_OK)
        if not is_dir_writable(self.constants.user_download_file):
            import getpass
            self.constants.user_download_file=f"/Users/{getpass.getuser()}/Downloads"
        title: wx.StaticText = None
        for child in panel.GetChildren():
            if child.GetLabel() == self.trans["Misc"]:
                title = child
                break
        self.custom_download_label = wx.StaticText(panel, label=self.trans["Choose Download Path"], pos=(title.GetPosition()[0] - 150, title.GetPosition()[1] + 30))
        self.custom_download_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))
        self.custom_download_textctrl=wx.TextCtrl(panel,pos=(self.custom_download_label.GetPosition()[0] - 77, self.custom_download_label.GetPosition()[1] + 20), size=(300, 25))
        self.custom_download_textctrl.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.custom_download_textctrl.SetValue(self.constants.user_download_file)
        self.custom_download_textctrl.Bind(wx.EVT_TEXT,self.on_text_change)
        self.choose_path_button = wx.Button(panel, label=self.trans["Choose"], pos=(title.GetPosition()[0] +100, self.custom_download_label.GetPosition()[1]+20), size=(100, 25))
        self.choose_path_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.choose_path_button.Bind(wx.EVT_BUTTON, self.on_choose_directory)
    def on_choose_directory(self, event):
        with wx.DirDialog(self.frame_modal, self.trans["Choose Save Path"], 
                        style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_OK:
                backup=self.constants.user_download_file
                self.constants.user_download_file = dirDialog.GetPath()
                def is_dir_writable(dirpath):
                    import os
                    return os.access(dirpath, os.W_OK | os.X_OK)
                if not is_dir_writable(self.constants.user_download_file):
                    wx.MessageBox(
                        self.trans["Cannot write to the selected directory."], 
                        self.trans["Read-only directory"], 
                        wx.OK | wx.ICON_WARNING
                    )  
                    self.constants.user_download_file=backup
                else:
                    logging.info(f"{self.trans['Choose Path:']} {self.constants.user_download_file}")     
                    self.custom_download_textctrl.SetValue(self.constants.user_download_file)
    def _populate_serial_spoofing_settings(self, panel: wx.Frame) -> None:
        title: wx.StaticText = None
        for child in panel.GetChildren():
            if child.GetLabel() == self.trans["Serial Spoofing"]:
                title = child
                break

        # Label: Custom Serial Number
        custom_serial_number_label = wx.StaticText(panel, label=self.trans["Custom Serial Number"], pos=(title.GetPosition()[0] - 150, title.GetPosition()[1] + 30))
        custom_serial_number_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))

        # Textbox: Custom Serial Number
        custom_serial_number_textbox = wx.TextCtrl(panel, pos=(custom_serial_number_label.GetPosition()[0] - 27, custom_serial_number_label.GetPosition()[1] + 20), size=(200, 25))
        custom_serial_number_textbox.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        custom_serial_number_textbox.SetToolTip(self.trans["Enter a custom serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Serial Number\" checkbox is not checked."])
        custom_serial_number_textbox.Bind(wx.EVT_TEXT, self.on_custom_serial_number_textbox)
        custom_serial_number_textbox.SetValue(self.constants.custom_serial_number)
        self.custom_serial_number_textbox = custom_serial_number_textbox

        # Label: Custom Board Serial Number
        custom_board_serial_number_label = wx.StaticText(panel, label=self.trans["Custom Board Serial Number"], pos=(title.GetPosition()[0] + 120, custom_serial_number_label.GetPosition()[1]))
        custom_board_serial_number_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_BOLD))

        # Textbox: Custom Board Serial Number
        custom_board_serial_number_textbox = wx.TextCtrl(panel, pos=(custom_board_serial_number_label.GetPosition()[0] - 5, custom_serial_number_textbox.GetPosition()[1]), size=(200, 25))
        custom_board_serial_number_textbox.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        custom_board_serial_number_textbox.SetToolTip(self.trans["Enter a custom board serial number here. This will be used for the SMBIOS and iMessage.\n\nNote: This will not be used if the \"Use Custom Board Serial Number\" checkbox is not checked."])
        custom_board_serial_number_textbox.Bind(wx.EVT_TEXT, self.on_custom_board_serial_number_textbox)
        custom_board_serial_number_textbox.SetValue(self.constants.custom_board_serial_number)
        self.custom_board_serial_number_textbox = custom_board_serial_number_textbox

        # Button: Generate Serial Number (below)
        generate_serial_number_button = wx.Button(panel, label=f"{self.trans['Generate S/N:']} {self.constants.custom_model or self.constants.computer.real_model}", pos=(title.GetPosition()[0] - 30, custom_board_serial_number_label.GetPosition()[1] + 60), size=(200, 25))
        generate_serial_number_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        generate_serial_number_button.Bind(wx.EVT_BUTTON, self.on_generate_serial_number)


    def _populate_app_stats(self, panel: wx.Frame) -> None:
        title: wx.StaticText = None
        for child in panel.GetChildren():
            if child.GetLabel() == self.trans["Statistics"]:
                title = child
                break

        lines = self.trans["""
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
"""].format(
            self.constants.patcher_version,
            self.constants.patcher_support_pkg_version,
            self.constants.launcher_binary,
            self.constants.payload_path,
            self.constants.commit_info[0],
            self.constants.commit_info[1],
            self.constants.commit_info[2] if self.constants.commit_info[2] != "" else "N/A",
            self.constants.detected_os,
            self.constants.detected_os_version,
            self.constants.computer.oclp_version,
            self.constants.computer.opencore_version,
            self.constants.booted_oc_disk,
            pprint.pformat(self.constants.computer, indent=4),
        )
        # TextCtrl: properties
        self.app_stats = wx.TextCtrl(panel, value=lines, pos=(-1, title.GetPosition()[1] + 30), size=(600, 240), style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH2)
        self.app_stats.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))


    def on_checkbox(self, event: wx.Event, warning_pop: str = "", override_function: bool = False) -> None:
        """
        """
        label = event.GetEventObject().GetLabel()
        value = event.GetEventObject().GetValue()
        if warning_pop != "" and value is True:
            warning = wx.MessageDialog(self.frame_modal, warning_pop, f"{self.trans['Warning']}: {label}", wx.YES_NO | wx.ICON_WARNING | wx.NO_DEFAULT)
            if warning.ShowModal() == wx.ID_NO:
                event.GetEventObject().SetValue(not event.GetEventObject().GetValue())
                return
            if label == self.trans["Allow native models"]:
                if self.constants.computer.real_model in smbios_data.smbios_dictionary:
                    if self.constants.detected_os > smbios_data.smbios_dictionary[self.constants.computer.real_model]["Max OS Supported"]:
                        chassis_type = "aluminum"
                        if self.constants.computer.real_model in ["MacBook5,2", "MacBook6,1", "MacBook7,1"]:
                            chassis_type = "plastic"
                        dlg = wx.MessageDialog(self.frame_modal, f"This model, {self.constants.computer.real_model}, does not natively support macOS {os_data.os_conversion.kernel_to_os(self.constants.detected_os)}, {os_data.os_conversion.convert_kernel_to_marketing_name(self.constants.detected_os)}. The last native OS was macOS {os_data.os_conversion.kernel_to_os(smbios_data.smbios_dictionary[self.constants.computer.real_model]['Max OS Supported'])}, {os_data.os_conversion.convert_kernel_to_marketing_name(smbios_data.smbios_dictionary[self.constants.computer.real_model]['Max OS Supported'])}\n\nToggling this option will break booting on this OS. Are you absolutely certain this is desired?\n\nYou may end up with a nice {chassis_type} brick 🧱", "Are you certain?", wx.YES_NO | wx.ICON_WARNING | wx.NO_DEFAULT)
                        if dlg.ShowModal() == wx.ID_NO:
                            event.GetEventObject().SetValue(not event.GetEventObject().GetValue())
                            return
        if override_function is True:
            self.settings[self._find_parent_for_key(label)][label]["override_function"](self.settings[self._find_parent_for_key(label)][label]["variable"], value, self.settings[self._find_parent_for_key(label)][label]["constants_variable"] if "constants_variable" in self.settings[self._find_parent_for_key(label)][label] else None)
            return

        self._update_setting(self.settings[self._find_parent_for_key(label)][label]["variable"], value)
        if label == self.trans["Allow native models"]:
            if gui_support.CheckProperties(self.constants).host_can_build() is True:
                self.parent.build_button.Enable()
            else:
                self.parent.build_button.Disable()


    def on_spinctrl(self, event: wx.Event, label: str) -> None:
        """
        """
        value = event.GetEventObject().GetValue()
        self._update_setting(self.settings[self._find_parent_for_key(label)][label]["variable"], value)


    def _update_setting(self, variable, value):
        logging.info(self.trans["Updating Local Setting: {variable} = {value}"].format(variable=variable, value=value))
        setattr(self.constants, variable, value)
        tmp_value = value
        if tmp_value is None:
            tmp_value = "PYTHON_NONE_VALUE"
        global_settings.GlobalEnviromentSettings().write_property(f"GUI:{variable}", tmp_value)


    def _update_global_settings(self, variable, value, global_setting = None):
        logging.info(self.trans["Updating Global Setting: {variable} = {value}"].format(variable=variable, value=value))
        tmp_value = value
        if tmp_value is None:
            tmp_value = "PYTHON_NONE_VALUE"
        global_settings.GlobalEnviromentSettings().write_property(variable, tmp_value)
        if global_setting is not None:
            self._update_setting(global_setting, value)

    def close(self):
        exit(0)

    def _update_system_defaults(self, variable, value, global_setting = None):
        value_type = type(value)
        if value_type is str:
            value_type = "-string"
        elif value_type is int:
            value_type = "-int"
        elif value_type is bool:
            value_type = "-bool"

        logging.info(self.trans["Updating System Defaults: {variable} = {value} ({value_type})"].format(variable=variable, value=value, value_type=value_type))
        subprocess.run(["/usr/bin/defaults", "write", "-globalDomain", variable, value_type, str(value)])


    def _update_system_defaults_root(self, variable, value, global_setting = None):
        value_type = type(value)
        if value_type is str:
            value_type = "-string"
        elif value_type is int:
            value_type = "-int"
        elif value_type is bool:
            value_type = "-bool"

        logging.info(self.trans["Updating System Defaults (root): {variable} = {value} ({value_type})"].format(variable=variable, value=value, value_type=value_type))
        subprocess_wrapper.run_as_root(["/usr/bin/defaults", "write", "/Library/Preferences/.GlobalPreferences.plist", variable, value_type, str(value)])


    def _find_parent_for_key(self, key: str) -> str:
        for parent in self.settings:
            if key in self.settings[parent]:
                return parent


    def on_sip_value(self, event: wx.Event) -> None:
        """
        """
        dict = sip_data.system_integrity_protection.csr_values_extended[f"CSR_{event.GetEventObject().GetLabel()}"]

        if event.GetEventObject().GetValue() is True:
            self.sip_value = self.sip_value + dict["value"]
        else:
            self.sip_value = self.sip_value - dict["value"]

        if hex(self.sip_value) == "0x0":
            self.constants.custom_sip_value = None
            self.constants.sip_status = True
            global_settings.GlobalEnviromentSettings().write_property("GUI:custom_sip_value", "PYTHON_NONE_VALUE")
            global_settings.GlobalEnviromentSettings().write_property("GUI:sip_status", True)
        elif hex(self.sip_value) == "0x803":
            self.constants.custom_sip_value = None
            self.constants.sip_status = False
            global_settings.GlobalEnviromentSettings().write_property("GUI:custom_sip_value", "PYTHON_NONE_VALUE")
            global_settings.GlobalEnviromentSettings().write_property("GUI:sip_status", False)
        else:
            self.constants.custom_sip_value = hex(self.sip_value)
            global_settings.GlobalEnviromentSettings().write_property("GUI:custom_sip_value", hex(self.sip_value))

        self.sip_configured_label.SetLabel(f"{self.trans['Currently configured SIP:']} {hex(self.sip_value)}")

    def on_choice(self, event: wx.Event, label: str) -> None:
        """
        """
        value = event.GetString()
        self._update_setting(self.settings[self._find_parent_for_key(label)][label]["variable"], value)


    def on_generate_serial_number(self, event: wx.Event) -> None:
        dlg = wx.MessageDialog(self.frame_modal, self.trans["Please take caution when using serial spoofing. This should only be used on machines that were legally obtained and require reserialization.\n\nNote: new serials are only overlayed through OpenCore and are not permanently installed into ROM.\n\nMisuse of this setting can break power management and other aspects of the OS if the system does not need spoofing\n\nHackdoc does not condone the use of our software on stolen devices.\n\nAre you certain you want to continue?"], self.trans["Warning"], wx.YES_NO | wx.ICON_WARNING | wx.NO_DEFAULT)
        if dlg.ShowModal() != wx.ID_YES:
            return

        macserial_output = subprocess.run([self.constants.macserial_path, "--generate", "--model", self.constants.custom_model or self.constants.computer.real_model, "--num", "1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        macserial_output = macserial_output.stdout.decode().strip().split(" | ")
        if len(macserial_output) == 2:
            self.custom_serial_number_textbox.SetValue(macserial_output[0])
            self.custom_board_serial_number_textbox.SetValue(macserial_output[1])
        else:
            wx.MessageBox(f"{self.trans['Failed to generate serial number:']}\n\n{macserial_output}", "Error", wx.OK | wx.ICON_ERROR)


    def on_custom_serial_number_textbox(self, event: wx.Event) -> None:
        self.constants.custom_serial_number = event.GetEventObject().GetValue()
        global_settings.GlobalEnviromentSettings().write_property(self.trans["GUI:custom_serial_number"], self.constants.custom_serial_number)


    def on_custom_board_serial_number_textbox(self, event: wx.Event) -> None:
        self.constants.custom_board_serial_number = event.GetEventObject().GetValue()
        global_settings.GlobalEnviromentSettings().write_property(self.trans["GUI:custom_board_serial_number"], self.constants.custom_board_serial_number)


    def _populate_fu_override(self, panel: wx.Panel) -> None:
        gpu_combo_box: wx.Choice = None
        for child in panel.GetChildren():
            if isinstance(child, wx.Choice):
                gpu_combo_box = child
                break

        gpu_combo_box.Bind(wx.EVT_CHOICE, self.fu_selection_click)
        if self.constants.fu_status is False:
            gpu_combo_box.SetStringSelection("Disabled")
        elif self.constants.fu_arguments is None or self.constants.fu_arguments == "":
            gpu_combo_box.SetStringSelection("Enabled")
        else:
            gpu_combo_box.SetStringSelection("Partial")


    def fu_selection_click(self, event: wx.Event) -> None:
        value = event.GetEventObject().GetStringSelection()
        if value == "Enabled":
            logging.info(self.trans["Updating FU Status: Enabled"])
            self.constants.fu_status = True
            self.constants.fu_arguments = None
            global_settings.GlobalEnviromentSettings().write_property("GUI:fu_status", True)
            global_settings.GlobalEnviromentSettings().write_property("GUI:fu_arguments", "PYTHON_NONE_VALUE")
            return

        if value == "Partial":
            logging.info(self.trans["Updating FU Status: Partial"])
            self.constants.fu_status = True
            self.constants.fu_arguments = " -disable_sidecar_mac"
            global_settings.GlobalEnviromentSettings().write_property("GUI:fu_status", True)
            global_settings.GlobalEnviromentSettings().write_property("GUI:fu_arguments", " -disable_sidecar_mac")
            return

        logging.info(self.trans["Updating FU Status: Disabled"])
        self.constants.fu_status = False
        self.constants.fu_arguments = None
        global_settings.GlobalEnviromentSettings().write_property("GUI:fu_status", False)
        global_settings.GlobalEnviromentSettings().write_property("GUI:fu_arguments", "PYTHON_NONE_VALUE")


    def _populate_graphics_override(self, panel: wx.Panel) -> None:
        gpu_combo_box: wx.Choice = None
        index = 0
        for child in panel.GetChildren():
            if isinstance(child, wx.Choice):
                if index == 0:
                    index = index + 1
                    continue
                gpu_combo_box = child
                break

        gpu_combo_box.Bind(wx.EVT_CHOICE, self.gpu_selection_click)
        gpu_combo_box.SetStringSelection(f"{self.constants.imac_vendor} {self.constants.imac_model}")

        socketed_gpu_models = ["iMac9,1", "iMac10,1", "iMac11,1", "iMac11,2", "iMac11,3", "iMac12,1", "iMac12,2"]
        if ((not self.constants.custom_model and self.constants.computer.real_model not in socketed_gpu_models) or (self.constants.custom_model and self.constants.custom_model not in socketed_gpu_models)):
            gpu_combo_box.Disable()
            return


    def gpu_selection_click(self, event: wx.Event) -> None:
        gpu_choice = event.GetEventObject().GetStringSelection()

        logging.info(self.trans["Updating GPU Selection: {gpu_choice}".format(gpu_choice)])
        if "AMD" in gpu_choice:
            self.constants.imac_vendor = "AMD"
            self.constants.metal_build = True
            if "Polaris" in gpu_choice:
                self.constants.imac_model = "Polaris"
            elif "GCN" in gpu_choice:
                self.constants.imac_model = "GCN"
            elif "Lexa" in gpu_choice:
                self.constants.imac_model = "Lexa"
            elif "Navi" in gpu_choice:
                self.constants.imac_model = "Navi"
            else:
                raise Exception(self.trans["Unknown GPU Model"])
            global_settings.GlobalEnviromentSettings().write_property("GUI:imac_vendor", "AMD")
            global_settings.GlobalEnviromentSettings().write_property("GUI:metal_build", True)
            global_settings.GlobalEnviromentSettings().write_property("GUI:imac_model", self.constants.imac_model)
        elif "Nvidia" in gpu_choice:
            self.constants.imac_vendor = "Nvidia"
            self.constants.metal_build = True
            if "Kepler" in gpu_choice:
                self.constants.imac_model = "Kepler"
            elif "GT" in gpu_choice:
                self.constants.imac_model = "GT"
            else:
                raise Exception(self.trans["Unknown GPU Model"])
            global_settings.GlobalEnviromentSettings().write_property("GUI:imac_vendor", "Nvidia")
            global_settings.GlobalEnviromentSettings().write_property("GUI:metal_build", True)
            global_settings.GlobalEnviromentSettings().write_property("GUI:imac_model", self.constants.imac_model)
        else:
            self.constants.imac_vendor = "None"
            self.constants.metal_build = False
            global_settings.GlobalEnviromentSettings().write_property("GUI:imac_vendor", "None")
            global_settings.GlobalEnviromentSettings().write_property("GUI:metal_build", False)


    def _get_system_settings(self, variable) -> bool:
        result = subprocess.run(["/usr/bin/defaults", "read", "-globalDomain", variable], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode == 0:
            try:
                return bool(int(result.stdout.decode().strip()))
            except:
                return False
        return False


    def on_return(self, event):
        self.frame_modal.Destroy()


    def on_nightly(self, event: wx.Event) -> None:
        # Ask prompt for which branch
        branches = ["main"]
        if self.constants.commit_info[0] not in ["Running from source", "Built from source"]:
            branches = [self.constants.commit_info[0].split("/")[-1]]
        result = network_handler.NetworkUtilities().get("https://api.github.com/repos/hackdoc/OCLP-R/branches")
        if result is not None:
            result = result.json()
            for branch in result:
                if branch["name"] == "gh-pages":
                    continue
                if branch["name"] not in branches:
                    branches.append(branch["name"])

            with wx.SingleChoiceDialog(self.parent, self.trans["Which branch would you like to download?"], self.trans["Branch Selection"], branches) as dialog:
                if dialog.ShowModal() == wx.ID_CANCEL:
                    return

                branch = dialog.GetStringSelection()
        else:
            branch = "main"

        gui_update.UpdateFrame(
            parent=self.parent,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.parent.GetPosition(),
            url=f"https://nightly.link/hackdoc/OCLP-R/workflows/build-app-wxpython/{branch}/OCLP-R.pkg.zip",
            version_label="(Nightly)"
        )


    def on_export_constants(self, event: wx.Event) -> None:
        # Throw pop up to get save location
        with wx.FileDialog(self.parent, self.trans["Save Constants File"], wildcard="JSON files (*.txt)|*.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, defaultFile=f"constants-{self.constants.patcher_version}.txt") as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            # Save the current contents in the file
            pathname = fileDialog.GetPath()
            logging.info(self.trans["Saving constants to {0}"].format(pathname))
            with open(pathname, 'w') as file:
                file.write(pprint.pformat(vars(self.constants), indent=4))


    def on_test_exception(self, event: wx.Event) -> None:
        raise Exception(self.trans["Test Exception"])


    def on_mount_root_vol(self, event: wx.Event) -> None:
        #Don't need to pass model as we're bypassing all logic
        if sys_patch.PatchSysVolume("",self.constants)._mount_root_vol() == True:
            wx.MessageDialog(self.parent, self.trans["Root Volume Mounted, remember to fix permissions before saving the Root Volume"], self.trans["Success"], wx.OK | wx.ICON_INFORMATION).ShowModal()
        else:
            wx.MessageDialog(self.parent, self.trans["Root Volume Mount Failed, check terminal output"], self.trans["Error"], wx.OK | wx.ICON_ERROR).ShowModal()


    def on_bless_root_vol(self, event: wx.Event) -> None:
        #Don't need to pass model as we're bypassing all logic
        if sys_patch.PatchSysVolume("",self.constants)._rebuild_root_volume() == True:
            wx.MessageDialog(self.parent, self.trans["Root Volume saved, please reboot to apply changes"], self.trans["Success"], wx.OK | wx.ICON_INFORMATION).ShowModal()
        else:
            wx.MessageDialog(self.parent, self.trans["Root Volume update Failed, check terminal output"], self.trans["Error"], wx.OK | wx.ICON_ERROR).ShowModal()
