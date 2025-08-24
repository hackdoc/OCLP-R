"""
Control.py: Control Center patch set for macOS 26 B6+
DO NOT USE ON MACOS SEQUOIA
"""

from ..base import BaseHardware, HardwareVariant

from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support   import utilities


class ModernControl(BaseHardware):

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
        return False
    def native_os(self) -> bool:
        """
        - Everything before macOS Tahoe 26 is considered native
        """
        if self._xnu_major < os_data.tahoe.value:
            return True
        if self._os_build == "25A5279m" or self._os_build == "25A5295e" or self._os_build == "25A5306g" or self._os_build == "25A5316i" or self._os_build == "25A5327h":
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
            "Control Center": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/CoreServices": {
                        "ControlCenter.app":      f"26.0 Beta 5",
                    },
                },
                PatchType.MERGE_SYSTEM_VOLUME:{
                    "/System/Library/PrivateFrameworks":{
                        "ControlCenter.framework": "26.0 Beta 5",
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