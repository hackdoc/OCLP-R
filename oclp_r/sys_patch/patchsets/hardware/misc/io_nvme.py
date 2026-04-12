"""
io_nvme.py: Modern Audio patch set for macOS 11-13
"""

from ..base import BaseHardware, HardwareVariant
from .....detections.amfi_detect import AmfiConfigDetectLevel
from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data

from .....support import utilities


class IONvme(BaseHardware):

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
        return f"{self._trans.get(self.hardware_variant(), self.hardware_variant())}: {self._trans.get("IONvme Patch", "IONvme Patch")}"

    def present(self) -> bool:
        """
        Requires constants to be set
        """
        return self._constants.allow_ionvme_patch==True

    def requires_kernel_debug_kit(self) -> bool:
        """
        Apple no longer provides standalone kexts in the base OS
        """
        return True

    def native_os(self) -> bool:
        """
        macOS 14+ is native
        """

        if self._xnu_major < os_data.sonoma.value:
            return False
        
        return False

    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.MISCELLANEOUS

    def _ionvme_patches(self) -> dict:
        """
        Patches for Modern Audio
        """
        return {
            "Modern Audio": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/Extensions": {
                        "IONvmeFamily.kext":      "26.4",
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

        return self._ionvme_patches()