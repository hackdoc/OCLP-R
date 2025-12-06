"""
modern_audio.py: Modern Audio patch set for macOS 26
"""

from ..base import BaseHardware, HardwareVariant
from .....detections.amfi_detect import AmfiConfigDetectLevel
from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support import utilities


class ModernAudio(BaseHardware):

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
        return f"{self.hardware_variant()}: Modern Audio"

    def present(self) -> bool:
        """
        AppleHDA was outright removed in macOS 26, so this patch set is always present if OS requires it
        """
        if utilities.check_kext_loaded("org.voodoo.driver.VoodooHDA") != "" and self._constants.audio_type != "AppleHDA":
            self._constants.audio_type = "AppleHDA"
        return self._constants.audio_type == "AppleHDA" and utilities.check_kext_loaded("as.vit9696.AppleALC") != ""

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

        # Technically, macOS Tahoe Beta 1 is also native, so return True
        if self._os_build == "25A5279m" and self._constants.applehda_version == "26.0 Beta 1":
            return True

        return False

    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.AUDIO

    def _modern_audio_patches(self) -> dict:
        """
        Patches for Modern Audio
        """
        return {
            "Modern Audio": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/Extensions": {
                        "AppleHDA.kext":      f"{self._constants.applehda_version}",
                    },
                },

                PatchType.REMOVE_SYSTEM_VOLUME: {
                    "/Library/Extensions": [
                        "AppleHDADisabler.kext" ,
                        "VoodooHDA.kext",
                    ],
                    "/Library/PreferencePanes" : [
                        "VoodooHDA.prefPane",
                    ],
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