"""
hda_universal_audio.py: Audio patch set for macOS 26
"""
from .....detections.amfi_detect import AmfiConfigDetectLevel
from ..base import BaseHardware, HardwareVariant
from ...base import PatchType
from .....constants import Constants
from .....datasets.os_data import os_data
from .....support   import utilities
class HDAU(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)


    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self._trans.get(self.hardware_variant(), self.hardware_variant())}: HDAUniversal"

    def required_amfi_level(self) -> AmfiConfigDetectLevel:
        """
        What level of AMFI configuration is required for this patch set
        Currently defaulted to AMFI needing to be disabled
        """
        return AmfiConfigDetectLevel.NO_CHECK

    def present(self) -> bool:
        return self._constants.audio_type=="HDAUniversal" and not self._constants.hdau_patch_already and not self._computer.t2_chip

    
    def native_os(self) -> bool:
        if self._xnu_major < os_data.tahoe.value:
            return True
        return False


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.AUDIO


    def _hdau_audio_patches(self) -> dict:
        """
        Patches for Modern Audio
        """

        return {
            "HDAUniversal": {
                # On macOS 26+ /Library is a firmlink to the Data volume, so
                # /Library/Extensions and /Library/PreferencePanes no longer exist
                # on the System volume. Install to the Data volume instead.
                PatchType.OVERWRITE_DATA_VOLUME: {
                    "/Library/Extensions": {
                        "HDAUniversal.kext":"HDAUniversal",
                    },
                },
                PatchType.REMOVE_DATA_VOLUME:{
                    "/Library/Extensions":[
                        "VoodooHDA.kext",
                        "AppleHDADisabler.kext",
                    ],
                    "/Library/PreferencePanes":[
                        'VoodooHDA.prefPane',
                    ]
                },
            },
        }
    def patches(self) -> dict:
        """
        Patches for HDAUniversal
        """
        if self.native_os() is True:
            return {}

        return self._hdau_audio_patches()