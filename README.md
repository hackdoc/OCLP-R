<div align="center">
             <img src="docs/images/OC-Patcher.png" alt="OpenCore Patcher Logo" width="256" />
             <h1>OCLP-R</h1>
</div>

A Python-based project revolving around [Acidanthera's OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) and [Lilu](https://github.com/acidanthera/Lilu) for both running and unlocking features in macOS on supported and unsupported Macs.

Our project's main goal is to breathe new life into Macs no longer supported by Apple, allowing for the installation and usage of macOS Big Sur and newer on machines as old as 2007.

----------
![GitHub all releases](https://img.shields.io/github/release/hackdoc/OCLP-R)
![GitHub all releases](https://img.shields.io/github/downloads/hackdoc/OCLP-R/total?color=white&style=plastic) ![GitHub top language](https://img.shields.io/github/languages/top/hackdoc/OCLP-R?color=4B8BBE&style=plastic)

----------

Noteworthy features of OCLP-R:

* Support for macOS Big Sur, Monterey, Ventura, Sonoma and Sequoia
* Native Over the Air (OTA) System Updates
* Supports Penryn and newer Macs
* Full support for WPA Wi-Fi and Personal Hotspot on BCM943224 and newer wireless chipsets
* System Integrity Protection, FileVault 2, .im4m Secure Boot and Vaulting
* Recovery OS, Safe Mode and Single-user Mode booting on non-native OSes
* Unlocks features such as Sidecar and AirPlay to Mac even on native Macs
* Enables enhanced SATA and NVMe power management on non-Apple storage devices
* Zero firmware patching required (ie. APFS ROM patching)
* Graphics acceleration for both Metal and non-Metal GPUs

----------

Note: Only clean-installs and upgrades are supported. macOS Big Sur installs already patched with other patchers, such as [Patched Sur](https://github.com/BenSova/Patched-Sur) or [bigmac](https://github.com/StarPlayrX/bigmac), cannot be used due to broken file integrity with APFS snapshots and SIP.

* You can, however, reinstall macOS with this patcher and retain your original data

Note 2: Currently, OCLP-R officially supports patching to run macOS Big Sur through Sonoma installs. For older OSes, OpenCore may function; however, support is currently not provided from Dortania.

* For macOS Mojave and Catalina support, we recommend the use of [dosdude1's patchers](http://dosdude1.com)

## Getting Started

To start using the project, please see our in-depth guide:

* [OCLP-R Guide](https://dortania.github.io/OpenCore-Legacy-Patcher/)


## Running from source

To run the project from source, see here: [Build and run from source](./SOURCE.md)

## Credits

* [Acidanthera](https://github.com/Acidanthera)
  * OpenCorePkg, as well as many of the core kexts and tools
* [Hackdoc](https://github.com/hackdoc)
  * Main co-author
* [vit9696](https://github.com/vit9696)
  * Endless amount of help troubleshooting, determining fixes and writing patches
