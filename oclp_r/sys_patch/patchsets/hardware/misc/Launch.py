"""
launch.py: LaunchPad patch set for macOS 26
Not Recommend for using
"""

from ..base import BaseHardware, HardwareVariant

from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support   import utilities


class LaunchPad(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)


    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: LaunchPad ({self._constants.launchpad_version})"


    def present(self) -> bool:
        return self._constants.change_launchpad
    def requires_kernel_debug_kit(self) -> bool:
        """
        Apple no longer provides standalone kexts in the base OS
        """
        return True
    def native_os(self) -> bool:
        """
        - Everything before macOS Tahoe 26 is considered native
        """
        if self._xnu_major < os_data.tahoe.value:
            return True

        return False


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.MISCELLANEOUS


    def _modern_audio_patches(self) -> dict:
        """
        Patches for Modern Audio
        """
        if self._constants.launchpad_version != "26.0 Beta 4" and self._constants.launchpad_version != "26.0 Beta 2":
            self._constants.launchpad_version = "26.0 Beta 4"
        return {
            "LuanchPad": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/CoreServices": {
                        "Dock.app":      f"{self._constants.launchpad_version}",
                        "Spotlight.app":      f"{self._constants.launchpad_version}",
                    },
                    "/System/Applications": {
                        "Apps.app":      f"{self._constants.launchpad_version}",
                        **({"Launchpad.app": f"{self._constants.launchpad_version}"} if f"{self._constants.launchpad_version}" != "26.0 Beta 4" else {}),
                    },
                },
            },
        }


    def patches(self) -> dict:
        """
        Patches for modern audio
        """
        if self.native_os() is True:
            return {}

        return self._modern_audio_patches()