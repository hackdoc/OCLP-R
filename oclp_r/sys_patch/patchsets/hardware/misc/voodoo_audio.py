"""
voodoo_audio.py: Modern Audio patch set for macOS 12+26(VoodooHDA)
"""
from ..base import BaseHardware, HardwareVariant
from ...base import PatchType
from .....constants import Constants
from .....datasets.os_data import os_data
from .....support   import utilities
class VoodooAudio(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)


    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: Voodoo Audio"


    def present(self) -> bool:
        return self._constants.audio_type=="VoodooHDA" and utilities.check_kext_loaded("as.vit9696.AppleALC") =="" and utilities.check_kext_loaded("org.voodoo.driver.VoodooHDA")==""


    def native_os(self) -> bool:
        if self._xnu_major < os_data.monterey.value:
            return True
        return False


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.MISCELLANEOUS


    def _voodoo_audio_patches(self) -> dict:
        """
        Patches for Modern Audio
        """
        if self._xnu_major >= os_data.tahoe and self._os_build != "25A5279m":
            return {
                "Voodoo Audio": {
                    PatchType.OVERWRITE_SYSTEM_VOLUME: {
                        "/Library/Extensions": {
                            "VoodooHDA.kext":"11.3",
                        },
                        "/Library/PreferencePanes":{
                            "VoodooHDA.prefPane":"11.3",
                        },
                    },
                },
            }
        else:
            return {
                "Voodoo Audio": {
                    PatchType.OVERWRITE_SYSTEM_VOLUME: {
                        "/Library/Extensions": {
                            "VoodooHDA.kext":"11.3",
                            "AppleHDADisabler.kext": "11.3" ,
                        },
                        "/Library/PreferencePanes":{
                            "VoodooHDA.prefPane":"11.3",
                        },
                    },
                },
            }

    def patches(self) -> dict:
        """
        Patches for voodoo audio
        """
        if self.native_os() is True:
            return {}

        return self._voodoo_audio_patches()