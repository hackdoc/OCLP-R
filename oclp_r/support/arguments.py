"""
arguments.py: CLI argument handling
"""

import sys
import time
import logging
import plistlib
import threading
import subprocess

from pathlib import Path

from . import subprocess_wrapper

from .. import constants

from ..efi_builder import build
from ..sys_patch import sys_patch

from ..datasets import (
    model_array,
    os_data
)

from . import (
    utilities,
    defaults,
    validation,
    translate_language,
    swift_bridge
)



# Generic building args
class arguments:

    def __init__(self, global_constants: constants.Constants) -> None:
        self.constants: constants.Constants = global_constants
        self.trans = translate_language.TranslateLanguage(self.constants).arguements()

        self.args = utilities.check_cli_args()

        self._parse_arguments()


    def _parse_arguments(self) -> None:
        """
        Parses arguments passed to the patcher
        """
        
            
        if self.args.validate:
            self._validation_handler()
            return

        if self.args.build:
            self._build_handler()
            return

        if self.args.patch_sys_vol:
            self._sys_patch_handler()
            return

        if self.args.unpatch_sys_vol:
            self._sys_unpatch_handler()
            return

        if self.args.prepare_for_update:
            self._prepare_for_update_handler()
            return

        if self.args.cache_os:
            self._cache_os_handler()
            return

        if self.args.auto_patch:
            self._sys_patch_auto_handler()
            return

        if self.args.print_info:
            self._print_info_handler()
            return

        if self.args.print_patches:
            self._print_patches_handler()
            return

        if self.args.set_settings:
            self._set_settings_handler()
            return

        if self.args.list_disks:
            self._list_disks_handler()
            return

        if self.args.list_partitions:
            self._list_partitions_handler()
            return

        if self.args.install_oc:
            self._install_oc_handler()
            return

        if self.args.list_installers:
            self._list_installers_handler()
            return

        if self.args.list_kdk:
            self._list_kdk_handler()
            return

        if self.args.list_metallib:
            self._list_metallib_handler()
            return

        if self.args.list_ipsw:
            self._list_ipsw_handler()
            return

        if self.args.list_local_installers:
            self._list_local_installers_handler()
            return

        if self.args.download:
            self._download_handler()
            return

        if self.args.extract_installer:
            self._extract_installer_handler()
            return

        if self.args.validate_installer:
            self._validate_installer_handler()
            return

        if self.args.verify_sha1:
            self._verify_sha1_handler()
            return

        if self.args.flash_installer:
            self._flash_installer_handler()
            return

        if self.args.check_updates:
            self._check_updates_handler()
            return

        if self.args.install_update:
            self._install_update_handler()
            return

        if self.args.cache_os_headless:
            self._cache_os_headless_handler()
            return




    def _validation_handler(self) -> None:
        """
        Enter validation mode
        """
        logging.info(self.trans["Set Validation Mode"])
        validation.PatcherValidation(self.constants)

    
        

    def _sys_patch_handler(self) -> None:
        """
        Start root volume patching
        """

        logging.info(self.trans["Set System Volume patching"])
        if "Library/InstallerSandboxes/" in str(self.constants.payload_path):
            logging.info(self.trans["- Running from Installer Sandbox, blocking OS updaters"])
            thread = threading.Thread(target=sys_patch.PatchSysVolume(self.constants.custom_model or self.constants.computer.real_model, self.constants, None).start_patch)
            thread.start()
            while thread.is_alive():
                utilities.block_os_updaters()
                time.sleep(1)
        else:
            sys_patch.PatchSysVolume(self.constants.custom_model or self.constants.computer.real_model, self.constants, None).start_patch()


    def _sys_unpatch_handler(self) -> None:
        """
        Start root volume unpatching
        """
        logging.info(self.trans["Set System Volume unpatching"])
        sys_patch.PatchSysVolume(self.constants.custom_model or self.constants.computer.real_model, self.constants, None).start_unpatch()


    def _sys_patch_auto_handler(self) -> None:
        """
        Start root volume auto patching
        """

        logging.info(self.trans["Set Auto patching"])
        from ..sys_patch.auto_patcher import StartAutomaticPatching
        StartAutomaticPatching(self.constants).start_auto_patch()


    def _print_info_handler(self) -> None:
        """
        Emit host info as JSON for the native SwiftUI front-end
        """
        swift_bridge.emit_result(swift_bridge.build_info(self.constants))
        sys.exit(0)


    def _print_patches_handler(self) -> None:
        """
        Emit detected root patches as JSON for the native SwiftUI front-end
        """
        swift_bridge.emit_result(swift_bridge.detect_patches(self.constants))
        sys.exit(0)


    def _set_settings_handler(self) -> None:
        """
        Persist settings from a JSON payload for the native SwiftUI front-end
        """
        import json
        try:
            payload = json.loads(self.args.set_settings)
        except Exception as error:
            swift_bridge.emit_result({"ok": False, "error": f"Invalid JSON: {error}"})
            sys.exit(1)
        result = swift_bridge.apply_settings(self.constants, payload)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _list_disks_handler(self) -> None:
        """
        Emit installable disks as JSON for the native SwiftUI front-end
        """
        swift_bridge.emit_result(swift_bridge.list_disks(self.constants))
        sys.exit(0)


    def _list_partitions_handler(self) -> None:
        """
        Emit installable partitions for a disk as JSON for the native front-end
        """
        result = swift_bridge.list_partitions(self.constants, self.args.list_partitions)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _install_oc_handler(self) -> None:
        """
        Install a previously built OpenCore config to an EFI partition
        """
        result = swift_bridge.install_oc(self.constants, self.args.install_oc)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _list_installers_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.list_installers(self.constants))
        sys.exit(0)


    def _list_kdk_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.list_kdk(self.constants))
        sys.exit(0)


    def _list_metallib_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.list_metallib(self.constants))
        sys.exit(0)


    def _list_ipsw_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.list_ipsw(self.constants))
        sys.exit(0)


    def _list_local_installers_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.list_local_installers(self.constants))
        sys.exit(0)


    def _download_handler(self) -> None:
        import json as _json
        try:
            payload = _json.loads(self.args.download)
        except Exception as error:
            swift_bridge.emit_result({"ok": False, "error": f"Invalid JSON: {error}"})
            sys.exit(1)
        result = swift_bridge.download(
            self.constants,
            payload.get("url"),
            payload.get("path"),
            payload.get("size"),
        )
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _extract_installer_handler(self) -> None:
        result = swift_bridge.extract_installer(self.constants, self.args.extract_installer)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _validate_installer_handler(self) -> None:
        result = swift_bridge.validate_installer(self.constants, self.args.validate_installer)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _verify_sha1_handler(self) -> None:
        import json as _json
        try:
            payload = _json.loads(self.args.verify_sha1)
        except Exception as error:
            swift_bridge.emit_result({"ok": False, "error": f"Invalid JSON: {error}"})
            sys.exit(1)
        result = swift_bridge.verify_sha1(payload.get("path"), payload.get("sha1"))
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _flash_installer_handler(self) -> None:
        import json as _json
        try:
            payload = _json.loads(self.args.flash_installer)
        except Exception as error:
            swift_bridge.emit_result({"ok": False, "error": f"Invalid JSON: {error}"})
            sys.exit(1)
        result = swift_bridge.flash_installer(
            self.constants,
            payload.get("installer_path"),
            payload.get("disk"),
        )
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _check_updates_handler(self) -> None:
        swift_bridge.emit_result(swift_bridge.check_updates(self.constants))
        sys.exit(0)


    def _install_update_handler(self) -> None:
        import json as _json
        try:
            payload = _json.loads(self.args.install_update)
        except Exception as error:
            swift_bridge.emit_result({"ok": False, "error": f"Invalid JSON: {error}"})
            sys.exit(1)
        result = swift_bridge.install_update(self.constants, payload.get("url"), payload.get("version", ""))
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _cache_os_headless_handler(self) -> None:
        result = swift_bridge.cache_os_headless(self.constants)
        swift_bridge.emit_result(result)
        sys.exit(0 if result.get("ok") else 1)


    def _prepare_for_update_handler(self) -> None:
        """
        Prepare host for macOS update
        """
        logging.info(self.trans["Preparing host for macOS update"])

        os_data = utilities.fetch_staged_update(variant="Update")
        if os_data[0] is None:
            logging.info(self.trans["No update staged, skipping"])
            return

        os_version = os_data[0]
        os_build   = os_data[1]

        logging.info(f"{self.trans['Preparing for update to']} {os_version} ({os_build})")

        self._clean_le_handler()


    def _cache_os_handler(self) -> None:
        """
        Fetch KDK for incoming OS
        """
        results = subprocess.run(["/bin/ps", "-ax"], stdout=subprocess.PIPE)
        if results.stdout.decode("utf-8").count("OCLP-R --cache_os") > 1:
            logging.info(self.trans["Another instance of OS caching is running, exiting"])
            return

        from ..wx_gui import gui_entry
        gui_entry.EntryPoint(self.constants).start(entry=gui_entry.SupportedEntryPoints.OS_CACHE)


    def _clean_le_handler(self) -> None:
        """
        Clean /Library/Extensions of problematic kexts
        Note macOS Ventura and older do this automatically
        """

        if self.constants.detected_os < os_data.os_data.sonoma:
            return

        logging.info(self.trans["Cleaning /Library/Extensions"])

        for kext in Path("/Library/Extensions").glob("*.kext"):
            if not Path(f"{kext}/Contents/Info.plist").exists():
                continue
            try:
                kext_plist = plistlib.load(open(f"{kext}/Contents/Info.plist", "rb"))
            except Exception as e:
                logging.info(f"  {self.trans['- Failed to load plist for']} {kext.name}: {e}")
                continue
            if "GPUCompanionBundles" not in kext_plist:
                continue
            logging.info(f"  {self.trans['- Removing']} {kext.name}")
            subprocess_wrapper.run_as_root(["/bin/rm", "-rf", kext])


    def _build_handler(self) -> None:
        """
        Start config building process
        """
        logging.info(self.trans["Set OpenCore Build"])

        if self.args.model:
            if self.args.model:
                logging.info(f"{self.trans['- Using custom model:']} {self.args.model}")
                self.constants.custom_model = self.args.model
                defaults.GenerateDefaults(self.constants.custom_model, False, self.constants)
            elif self.constants.computer.real_model not in model_array.SupportedSMBIOS and self.constants.allow_oc_everywhere is False:
                logging.info(
                    self.trans["""Your model is not supported by this patcher for running unsupported OSes!

If you plan to create the USB for another machine, please select the "Change Model" option in the menu."""]
                )
                sys.exit(1)
            else:
                logging.info(f"{self.trans['- Using detected model:']} {self.constants.computer.real_model}")
                defaults.GenerateDefaults(self.constants.custom_model, True, self.constants)

        if self.args.verbose:
            logging.info(self.trans["- Set verbose configuration"])
            self.constants.verbose_debug = True
        else:
            self.constants.verbose_debug = False  # Override Defaults detected

        
        if self.args.debug_oc:
            logging.info(self.trans["- Set OpenCore DEBUG configuration"])
            self.constants.opencore_debug = True

        if self.args.debug_kext:
            logging.info(self.trans["- Set kext DEBUG configuration"])
            self.constants.kext_debug = True

        if self.args.hide_picker:
            logging.info(self.trans["- Set HidePicker configuration"])
            self.constants.showpicker = False

        if self.args.disable_sip:
            logging.info(self.trans["- Set Disable SIP configuration"])
            self.constants.sip_status = False
        else:
            self.constants.sip_status = True  # Override Defaults detected

        if self.args.disable_smb:
            logging.info(self.trans["- Set Disable SecureBootModel configuration"])
            self.constants.secure_status = False
        else:
            self.constants.secure_status = True  # Override Defaults detected

        if self.args.vault:
            logging.info(self.trans["- Set Vault configuration"])
            self.constants.vault = True

        if self.args.firewire:
            logging.info(self.trans["- Set FireWire Boot configuration"])
            self.constants.firewire_boot = True

        if self.args.nvme:
            logging.info(self.trans["- Set NVMe Boot configuration"])
            self.constants.nvme_boot = True

        if self.args.wlan:
            logging.info(self.trans["- Set Wake on WLAN configuration"])
            self.constants.enable_wake_on_wlan = True

        if self.args.disable_tb:
            logging.info(self.trans["- Set Disable Thunderbolt configuration"])
            self.constants.disable_tb = True

        if self.args.force_surplus:
            logging.info(self.trans["- Forcing SurPlus override configuration"])
            self.constants.force_surplus = True

        if self.args.moderate_smbios:
            logging.info(self.trans["- Set Moderate SMBIOS Patching configuration"])
            self.constants.serial_settings = "Moderate"

        if self.args.smbios_spoof:
            if self.args.smbios_spoof == "Minimal":
                self.constants.serial_settings = "Minimal"
            elif self.args.smbios_spoof == "Moderate":
                self.constants.serial_settings = "Moderate"
            elif self.args.smbios_spoof == "Advanced":
                self.constants.serial_settings = "Advanced"
            else:
                logging.info(f"{self.trans['- Unknown SMBIOS arg passed:']} {self.args.smbios_spoof}")

        if self.args.support_all:
            logging.info(self.trans["- Building for natively supported model"])
            self.constants.allow_oc_everywhere = True
            self.constants.serial_settings = "None"
        


        build.BuildOpenCore(self.constants.custom_model or self.constants.computer.real_model, self.constants)
