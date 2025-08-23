"""
control_center.py: Control Center patch set for macOS 26
Not Recommend for using
"""

from ..base import BaseHardware, HardwareVariant

from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support   import utilities


class ControlCenter(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)


    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: Control Center"


    def present(self) -> bool:
        return self._constants.change_control_center
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
        return {
            "LuanchPad": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/CoreServices": {
                        "ControlCenter.app":      f"26.0 Beta 5",
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