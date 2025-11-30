"""
modern_wireless.py: Modern Wireless detection
"""

from ..base import BaseHardware, HardwareVariant

from ...base import PatchType

from .....constants  import Constants
from .....detections import device_probe

from .....datasets.os_data import os_data


class IntelWireless(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)

    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: Intel Wireless"


    def present(self) -> bool:
        """
        Targeting Intel Wireless
        """
        if self._xnu_major<os_data.tahoe.value:
            return False
        if not self._constants.intel_wireless_tahoe:
            return False
        return isinstance(self._computer.wifi, device_probe.IntelWirelessCard)and(
            self._computer.wifi.chipset in [
                device_probe.IntelWirelessCard.Chipsets.IntelWirelessIDs,
            ]
        )    


    def native_os(self) -> bool:
        """
        Only support with macOS 26, Tahoe
        """
        return  self._xnu_major < os_data.tahoe.value


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.NETWORKING


    def patches(self) -> dict:
        """
        Patches for Intel Wireless
        """
        if self.native_os() is True:
            return {}
        return {
            "Intel Wireless": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/usr/libexec": {
                        "airportd": "14.7.7",
                        "wifip2pd": "14.7.7",
                    },
                    "/System/Library/CoreServices": {
                        "WiFiAgent.app": "14.7.7" ,
                    },
                },
                PatchType.MERGE_SYSTEM_VOLUME: {
                    "/System/Library/Frameworks": {
                        "CoreWLAN.framework": "14.7.7",
                    },
                    "/System/Library/PrivateFrameworks": {
                        "CoreWiFi.framework":       "14.7.7",
                        "IO80211.framework":        "14.7.7",
                        "WiFiPeerToPeer.framework": "14.7.7",
                    },
                }
            },
        }
