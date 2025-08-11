"""
modern_usb.py: Legacy USB patch set for macOS 26+
"""

from ..base import BaseHardware, HardwareVariant

from ...base import PatchType

from .....constants import Constants

from .....datasets.os_data import os_data


class LegacyUSBHost(BaseHardware):

    def __init__(self, xnu_major, xnu_minor, os_build, global_constants: Constants) -> None:
        super().__init__(xnu_major, xnu_minor, os_build, global_constants)


    def name(self) -> str:
        """
        Display name for end users
        """
        return f"{self.hardware_variant()}: Modern USB"

    def requires_kernel_debug_kit(self) -> bool:
        """
        Disable KDK requirement as we're only replacing existing kexts
        """
        return self._xnu_major >= os_data.tahoe.value
    def present(self) -> bool:
        return self._constants.allow_usb_patch


    def native_os(self) -> bool:
        return self._xnu_major < os_data.tahoe.value


    def hardware_variant(self) -> HardwareVariant:
        """
        Type of hardware variant
        """
        return HardwareVariant.MISCELLANEOUS


    def _legacy_usb_patches(self) -> dict:
        """
        Patches for USB
        Including:
        - IOUSBMassStorageDriver.kext (USB)
        - IOUSBDeviceFamily.kext (USB)
        - IOUSBFamily.kext (USB)
        - IOUSBHostFamily.kext (USB)
        """
        return {
            "Modern USB": {
                PatchType.OVERWRITE_SYSTEM_VOLUME: {
                    "/System/Library/Extensions": {
                        "AppleUSBACM.kext": "14.7.6",  
                        "AppleUSBAudio.kext": "14.7.6",  
                        "AppleUSBCDC.kext": "14.7.6",  
                        "AppleUSBCommon.kext": "14.7.6",  
                        "AppleUSBDeviceMux.kext": "14.7.6",  
                        "AppleUSBDeviceNCM.kext": "14.7.6",  
                        "AppleUSBDisplays.kext": "14.7.6",  
                        "AppleUSBDMM.kext": "14.7.6",  
                        "AppleUSBECM.kext": "14.7.6",  
                        "AppleUSBEEM.kext": "14.7.6",  
                        "AppleUSBEthernet.kext": "14.7.6",  
                        "AppleUSBEthernetHost.kext": "14.7.6",  
                        "AppleUSBHostS5L8930X.kext": "14.7.6",  
                        "AppleUSBHostS5L8960X.kext": "14.7.6",  
                        "AppleUSBHostT7000.kext": "14.7.6",  
                        "AppleUSBHostT8002.kext": "14.7.6",  
                        "AppleUSBHostT8011.kext": "14.7.6",  
                        "AppleUSBHostT8020.kext": "14.7.6",  
                        "AppleUSBHSIC.kext": "14.7.6",  
                        "AppleUSBiBridge.kext": "14.7.6",  
                        "AppleUSBLightningAdapter.kext": "14.7.6",  
                        "AppleUSBMike.kext": "14.7.6",  
                        "AppleUSBNCM.kext": "14.7.6",  
                        "AppleUSBNetworking.kext": "14.7.6",  
                        "AppleUSBRealtek8153Patcher.kext": "14.7.6",  
                        "AppleUSBSerial.kext": "14.7.6",  
                        "AppleUSBWCM.kext": "14.7.6",  
                        "IOUSBDeviceFamily.kext": "14.7.6",  
                        "IOUSBFamily.kext": "14.7.6",  
                        "IOUSBHostFamily.kext": "14.7.6",  
                        "IOUSBMassStorageDriver.kext": "14.7.6",
                        "IOAccessoryManager.kext": "14.7.6",
                        "IOAccessoryPortUSB.kext": "14.7.6",
                    },
                },
                PatchType.MERGE_SYSTEM_VOLUME: {
                    "/System/Library/Frameworks": {
                        "IOUSBHost.framework": "14.6.1",
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
        return self._legacy_usb_patches()
            
        
            
        