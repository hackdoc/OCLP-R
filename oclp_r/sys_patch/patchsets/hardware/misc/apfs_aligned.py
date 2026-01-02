"""
modern_audio.py: Modern Audio patch set for macOS 26
"""

from ..base import BaseHardware, HardwareVariant
from .....detections.amfi_detect import AmfiConfigDetectLevel
from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support   import utilities


class APFSP(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)

    def required_amfi_level(self) -> AmfiConfigDetectLevel:
        """
        What level of AMFI configuration is required for this patch set
        Currently defaulted to AMFI needing to be disabled
        """
        return AmfiConfigDetectLevel.NO_CHECK
    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: FileVault Patch for Non-T2"


    def present(self) -> bool:
        """
        AppleHDA was outright removed in macOS 26, so this patch set is always present if OS requires it
        """
        return self._constants.allow_apfs_aligned_patch
        
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

        

        return False


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.MISCELLANEOUS


    def _apfs_patches(self) -> dict:
        """
        Patches for APFS-Patch For Non-T2
        """
        return {
            "APFS-Patch For Non-T2": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/usr/standalone/i386": {
                        "apfs.efi":      "15.6",
                        "apfs_aligned.efi":      "15.6",
                    },
                },
            },
        }


    def patches(self) -> dict:
        """
        Patches for APFS-Patch For Non-T2
        """
        if self.native_os() is True:
            return {}

        return self._apfs_patches()