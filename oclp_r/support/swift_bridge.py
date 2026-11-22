"""
swift_bridge.py: JSON bridge for the native SwiftUI front-end

The SwiftUI shell runs the patcher as a subprocess and parses a small,
sentinel-delimited JSON payload written to stdout. Everything here is additive:
it reuses the existing backend (install.tui_disk_installation, model_array,
device probe results already populated on ``constants``) and does not alter
any patcher logic.

Output contract
---------------
Commands emit, after any log lines, a single result envelope::

    @@OCLPR_RESULT_BEGIN@@
    {json}
    @@OCLPR_RESULT_END@@

The front-end extracts the JSON between the two markers.
"""

import json
import logging
import sys

from ..datasets import model_array
from ..support import install


RESULT_BEGIN = "@@OCLPR_RESULT_BEGIN@@"
RESULT_END = "@@OCLPR_RESULT_END@@"

# Settings that map 1:1 to a `constants` attribute and are persisted as
# "GUI:<attribute>" in the shared global settings plist (same convention as
# the wxPython GUI, so both front-ends share one settings store).
SETTINGS_KEYS = [
    "showpicker", "oc_timeout", "verbose_debug", "kext_debug", "opencore_debug",
    "firewire_boot", "xhci_boot", "nvme_boot", "vault",
    "enable_wake_on_wlan", "disable_tb", "dGPU_switch", "disallow_cpufriend",
    "disable_mediaanalysisd", "nvram_write", "allow_nvme_fixing",
    "allow_3rd_party_drives", "apfs_trim_timeout", "disable_fw_throttle",
    "software_demux", "disable_connectdrivers", "amd_gop_injection",
    "nvidia_kepler_gop_injection", "sip_status", "secure_status",
    "disable_cs_lv", "disable_amfi", "serial_settings", "override_smbios",
    "allow_native_spoofs", "set_alc_usage", "allow_usb_patch",
    "allow_intel_wifi_patch", "applehda_version", "force_surplus",
    "allow_oc_everywhere", "manually_download_kdk",
]

# Global (non-"GUI:") keys used by the App tab.
GLOBAL_SETTINGS_KEYS = [
    "IgnoreAppUpdates",
    "DisableCrashAndAnalyticsReporting",
    "ShouldNukeKDKs",
]


def _silence_stdout_logging() -> None:
    """
    Stop log records from being written to stdout so the result envelope is the
    only thing the front-end sees on that stream. Logging to file is preserved.
    """
    root = logging.getLogger()
    for handler in list(root.handlers):
        if isinstance(handler, logging.StreamHandler) and getattr(handler.stream, "name", None) == "<stdout>":
            root.removeHandler(handler)


def emit_result(payload) -> None:
    """
    Write a JSON result envelope to stdout.
    """
    _silence_stdout_logging()
    sys.stdout.write(RESULT_BEGIN + "\n")
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    sys.stdout.write(RESULT_END + "\n")
    sys.stdout.flush()


def host_can_build(constants) -> bool:
    """
    Mirror of gui_support.CheckProperties.host_can_build(), kept wx-free so the
    info command does not need to initialise a wx.App.
    """
    if constants.custom_model:
        return True
    if constants.host_is_hackintosh is True:
        return False
    if constants.allow_oc_everywhere is True:
        return True
    if constants.computer.real_model in model_array.SupportedSMBIOS:
        return True
    return False


def _json_safe(value):
    """
    Coerce a constants/plist value into a JSON-serialisable scalar.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        return value
    return None


def read_settings(constants) -> dict:
    """
    Return the effective settings (after defaults/global settings were applied).
    Keys whose value is not a JSON scalar are omitted.
    """
    settings = {}
    for key in SETTINGS_KEYS:
        if not hasattr(constants, key):
            continue
        value = _json_safe(getattr(constants, key))
        if value is not None:
            settings[key] = value
    return settings


def read_global_settings() -> dict:
    """
    Return the App-tab global settings stored outside the "GUI:" namespace.
    Unset keys are omitted (never emitted as null).
    """
    from . import global_settings
    store = global_settings.GlobalEnviromentSettings()
    result = {}
    for key in GLOBAL_SETTINGS_KEYS:
        value = _json_safe(store.read_property(key))
        if value is not None:
            result[key] = value
    return result


def build_info(constants) -> dict:
    """
    Summarise host state for the main menu / settings screens.
    """
    return {
        "patcher_name": constants.patcher_name,
        "patcher_version": constants.patcher_version,
        "detected_os": int(constants.detected_os),
        "detected_os_version": constants.detected_os_version,
        "detected_os_build": constants.detected_os_build,
        "host_model": constants.computer.real_model,
        "host_is_hackintosh": bool(constants.host_is_hackintosh),
        "host_can_build": host_can_build(constants),
        "booted_oc_disk": constants.booted_oc_disk,
        "voodoo_patch_already": bool(constants.voodoo_patch_already),
        "hdau_patch_already": bool(constants.hdau_patch_already),
        "supported_models": list(model_array.SupportedSMBIOS),
        "settings": read_settings(constants),
        "global_settings": read_global_settings(),
        "copyright": getattr(constants, "copyright_date", ""),
        "guide_link": getattr(constants, "guide_link", ""),
        "discord_link": getattr(constants, "discord_link", ""),
        "repo_link": getattr(constants, "repo_link", ""),
    }


def list_disks(constants) -> dict:
    """
    Return installable disks (those containing a FAT32/EFI partition).
    """
    disks = install.tui_disk_installation(constants).list_disks()

    # Match the wx GUI: hide disk images / virtual / read-only devices.
    ignore = ("disk image", "read-only", "virtual")
    filtered = {}
    for identifier, info in disks.items():
        if any(token in str(info.get("name", "")).lower() for token in ignore):
            continue
        filtered[identifier] = info

    return {"ok": True, "disks": filtered}


def list_partitions(constants, disk_identifier: str) -> dict:
    """
    Return FAT32/EFI partitions on the requested disk.
    """
    disks = install.tui_disk_installation(constants).list_disks()
    if disk_identifier not in disks:
        return {"ok": False, "error": f"Unknown disk: {disk_identifier}"}

    partitions = install.tui_disk_installation(constants).list_partitions(disk_identifier, disks)
    return {"ok": True, "disk": disk_identifier, "partitions": partitions}


def install_oc(constants, partition_identifier: str) -> dict:
    """
    Install a previously built OpenCore config onto the requested EFI partition.
    """
    result = install.tui_disk_installation(constants).install_opencore(partition_identifier)
    return {"ok": result is True, "partition": partition_identifier}


def detect_patches(constants) -> dict:
    """
    Detect which root-volume patches apply to this host.

    Mirrors the wx Root Patcher's pre-patch detection step (which shows a
    loading gauge) and returns the list of patch names that would be applied.
    """
    # The KDK/Metallib handlers read these links directly; make sure they are
    # populated even if the background api_link thread has not run yet.
    if not constants.kdk_api_link:
        constants.kdk_api_link = "https://dortania.github.io/KdkSupportPkg/manifest.json"
    if not constants.metallib_api_link:
        constants.metallib_api_link = "https://dortania.github.io/MetallibSupportPkg/manifest.json"

    try:
        from ..sys_patch.patchsets import HardwarePatchsetDetection, HardwarePatchsetValidation
        detection = HardwarePatchsetDetection(constants=constants)
    except Exception as error:  # pragma: no cover - defensive
        return {"ok": False, "error": str(error)}

    properties = detection.device_properties or {}
    patches = sorted(
        name for name, enabled in properties.items()
        if enabled is True and not name.startswith(("Settings", "Validation"))
    )

    # Reasons patching is blocked (mirrors the wx "Cannot patch due to..." list).
    blockers = []
    for name, enabled in properties.items():
        if enabled is not True or not name.startswith("Validation"):
            continue
        if name in (HardwarePatchsetValidation.PATCHING_NOT_POSSIBLE,
                    HardwarePatchsetValidation.UNPATCHING_NOT_POSSIBLE):
            continue
        blockers.append(name.split("Validation: ", 1)[-1])

    # Last patched version/date, if present.
    last_patched = None
    computer = getattr(constants, "computer", None)
    if computer is not None:
        version = getattr(computer, "oclp_sys_version", None)
        date = getattr(computer, "oclp_sys_date", None)
        if version and date:
            last_patched = {"version": version, "date": date.split(" @")[0]}

    return {
        "ok": True,
        "can_patch": bool(detection.can_patch),
        "can_unpatch": bool(detection.can_unpatch),
        "patches": patches,
        "blockers": blockers,
        "last_patched": last_patched,
    }


def _coerce(value, expected_type):
    """
    Validate/normalise a JSON value against the type of a constants attribute.
    Returns (ok, normalised_value).
    """
    if expected_type is bool:
        if isinstance(value, bool):
            return True, value
        return False, None
    if expected_type is int:
        if isinstance(value, bool):
            return False, None
        if isinstance(value, int):
            return True, value
        if isinstance(value, float) and value.is_integer():
            return True, int(value)
        return False, None
    if expected_type is str:
        if isinstance(value, str):
            return True, value
        return False, None
    if value is None:
        return True, None
    return isinstance(value, expected_type), value


def apply_settings(constants, payload: dict) -> dict:
    """
    Persist settings to the shared global settings plist and apply them to the
    running constants object.

    ``payload`` shape::

        {"gui": {"showpicker": False, ...}, "global": {"ShouldNukeKDKs": True}}
    """
    from . import global_settings

    store = global_settings.GlobalEnviromentSettings()
    applied, errors = [], {}

    for attribute, value in (payload.get("gui") or {}).items():
        if attribute not in SETTINGS_KEYS or not hasattr(constants, attribute):
            errors[attribute] = "unknown setting"
            continue
        ok, normalised = _coerce(value, type(getattr(constants, attribute)))
        if not ok:
            errors[attribute] = f"invalid type, expected {type(getattr(constants, attribute)).__name__}"
            continue
        store.write_property(f"GUI:{attribute}", "PYTHON_NONE_VALUE" if normalised is None else normalised)
        setattr(constants, attribute, normalised)
        applied.append(f"GUI:{attribute}")

    for key, value in (payload.get("global") or {}).items():
        if key not in GLOBAL_SETTINGS_KEYS:
            errors[key] = "unknown setting"
            continue
        if not isinstance(value, (bool, int, str)):
            errors[key] = "invalid type"
            continue
        store.write_property(key, value)
        applied.append(key)

    return {"ok": not errors, "applied": applied, "errors": errors}


# ============================ Downloads ============================

PROGRESS_PREFIX = "@@P@@ "

DEFAULT_KDK_LINK = "https://dortania.github.io/KdkSupportPkg/manifest.json"
DEFAULT_METALLIB_LINK = "https://dortania.github.io/MetallibSupportPkg/manifest.json"


def _seed_name(seed) -> str:
    if seed is None:
        return None
    return getattr(seed, "name", str(seed))


def list_installers(constants) -> dict:
    """
    macOS InstallAssistant catalog from Apple's Software Update Catalog.
    Each entry includes compatibility problems for the target model.
    """
    from .. import sucatalog
    from ..datasets import smbios_data, cpu_data, os_data

    try:
        catalog = sucatalog.CatalogURL(seed=sucatalog.SeedType.DeveloperSeed).url_contents
        if catalog is None:
            return {"ok": False, "error": "Failed to download installer catalog from Apple"}
        products = sucatalog.CatalogProducts(catalog).latest_products
    except Exception as error:
        return {"ok": False, "error": str(error)}

    model = constants.custom_model or constants.computer.real_model

    installers = []
    for product in products:
        ia = product.get("InstallAssistant") or {}
        xnu_major = ia.get("XNUMajor")

        problems = []
        if model in smbios_data.smbios_dictionary and xnu_major is not None:
            if xnu_major >= os_data.os_data.ventura:
                cpu_gen = smbios_data.smbios_dictionary[model].get("CPU Generation", 999)
                if cpu_gen <= cpu_data.CPUGen.penryn or model in ["MacPro4,1", "MacPro5,1", "Xserve3,1"]:
                    if model.startswith("MacBook"):
                        problems.append("Lack of internal Keyboard/Trackpad in macOS installer.")
                    else:
                        problems.append("Lack of internal Keyboard/Mouse in macOS installer.")

        installers.append({
            "title": product.get("Title"),
            "version": product.get("Version"),
            "build": product.get("Build"),
            "catalog": _seed_name(product.get("Catalog")),
            "url": ia.get("URL"),
            "size": ia.get("Size"),
            "integrity_url": ia.get("IntegrityDataURL"),
            "integrity_size": ia.get("IntegrityDataSize"),
            "xnu_major": xnu_major,
            "problems": problems,
        })
    return {"ok": True, "installers": installers}


def _fetch_manifest(link: str, user_agent: str) -> list:
    from ..support import network_handler
    try:
        results = network_handler.NetworkUtilities().get(link, headers={"User-Agent": user_agent}, timeout=10)
    except Exception:
        return None
    if results is None or results.status_code != 200:
        return None
    data = results.json()
    if isinstance(data, dict):
        for key in ("kdks", "metallibs", "assets", "items"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    return data if isinstance(data, list) else None


def _manifest_entry(item: dict) -> dict:
    return {
        "name": item.get("name"),
        "version": item.get("version"),
        "build": item.get("build"),
        "date": item.get("date"),
        "url": item.get("url"),
        "size": item.get("fileSize") or item.get("size") or item.get("filesize"),
        "sha256": item.get("sha256sum"),
        "md5": item.get("md5sum"),
    }


def list_kdk(constants) -> dict:
    link = constants.kdk_api_link or DEFAULT_KDK_LINK
    data = _fetch_manifest(link, f"OCLP/{constants.patcher_version}")
    if data is None:
        return {"ok": False, "error": "Could not fetch KDK list"}
    return {"ok": True, "items": [_manifest_entry(item) for item in data if isinstance(item, dict)]}


def list_metallib(constants) -> dict:
    link = constants.metallib_api_link or DEFAULT_METALLIB_LINK
    data = _fetch_manifest(link, f"OCLP/{constants.patcher_version}")
    if data is None:
        return {"ok": False, "error": "Could not fetch Metallib list"}
    return {"ok": True, "items": [_manifest_entry(item) for item in data if isinstance(item, dict)]}


def _parse_apple_ipsw_catalog(contents: bytes) -> list:
    import plistlib
    ipsws = []
    by_url = {}
    try:
        catalog = plistlib.loads(contents)
        devices = catalog.get("MobileDeviceSoftwareVersionsByVersion", {}).get("1", {}).get("MobileDeviceSoftwareVersions", {})
    except Exception:
        return ipsws
    if not isinstance(devices, dict):
        return ipsws
    for identifier, builds in devices.items():
        if not identifier.startswith(("Mac", "iMac", "VirtualMac")):
            continue
        if not isinstance(builds, dict):
            continue
        for build, entry in builds.items():
            if not isinstance(entry, dict):
                continue
            restore = entry.get("Restore") or entry.get("Universal", {}).get("Restore", {})
            url = restore.get("FirmwareURL")
            if not url:
                continue
            sha1sum = restore.get("FirmwareSHA1", "")
            if url in by_url:
                if not by_url[url]["sha1sum"] and sha1sum:
                    by_url[url]["sha1sum"] = sha1sum
                continue
            record = {
                "version": restore.get("ProductVersion", ""),
                "buildid": restore.get("BuildVersion", build),
                "url": url,
                "filesize": 0,
                "releasedate": "",
                "signed": True,
                "sha1sum": sha1sum,
            }
            by_url[url] = record
            ipsws.append(record)
    return ipsws


def list_ipsw(constants) -> dict:
    import requests
    ipsws = []
    try:
        response = requests.get(constants.ipsw_api_link, timeout=60)
        response.raise_for_status()
        firmwares = response.json().get("firmwares", [])
        if isinstance(firmwares, list):
            ipsws = [fw for fw in firmwares if isinstance(fw, dict) and fw.get("url")]
    except Exception:
        ipsws = []

    if not ipsws:
        try:
            response = requests.get(constants.ipsw_apple_api_link, timeout=60)
            response.raise_for_status()
            ipsws = _parse_apple_ipsw_catalog(response.content)
        except Exception as error:
            return {"ok": False, "error": str(error)}

    items = []
    for fw in ipsws:
        items.append({
            "version": fw.get("version", ""),
            "build": fw.get("buildid", ""),
            "url": fw.get("url", ""),
            "size": fw.get("filesize", 0),
            "releasedate": fw.get("releasedate", ""),
            "signed": bool(fw.get("signed", False)),
            "sha1": fw.get("sha1sum", "") or fw.get("sha1", "") or "",
        })

    def _sort_key(item):
        return item.get("version", "")
    items.sort(key=_sort_key, reverse=True)
    return {"ok": True, "items": items}


def _emit_progress(percent, speed, downloaded, total) -> None:
    sys.stdout.write(PROGRESS_PREFIX + json.dumps({
        "percent": round(float(percent or 0), 1),
        "speed": round(float(speed or 0)),
        "downloaded": int(downloaded or 0),
        "total": int(total or 0),
    }) + "\n")
    sys.stdout.flush()


def download(constants, url: str, path: str, size) -> dict:
    """
    Download a file via the backend DownloadObject, streaming progress lines.
    """
    import time
    from ..support import network_handler

    size_arg = None
    if size:
        try:
            size_arg = int(size)
        except (TypeError, ValueError):
            size_arg = str(size)

    try:
        obj = network_handler.DownloadObject(url, path, size_arg, skip_validation=True)
        obj.download(spawn_thread=True)
    except Exception as error:
        return {"ok": False, "error": str(error)}

    last_percent = -1
    while obj.is_active():
        percent = obj.get_percent() or 0
        if int(percent) != last_percent:
            last_percent = int(percent)
            _emit_progress(percent, obj.get_speed(), obj.get_downloaded_size(), obj.get_file_size())
        time.sleep(0.4)

    _emit_progress(100.0 if obj.download_complete else (obj.get_percent() or 0),
                   obj.get_speed(), obj.get_downloaded_size(), obj.get_file_size())
    return {"ok": bool(obj.download_complete), "path": path, "error": obj.error_msg if not obj.download_complete else None}


def list_local_installers(constants) -> dict:
    import glob
    from pathlib import Path
    apps = []
    for pattern in ("/Applications/Install macOS*.app", "/Applications/Install OS X*.app"):
        for path in sorted(glob.glob(pattern)):
            if Path(path).is_dir():
                apps.append({"path": path, "name": Path(path).name})
    return {"ok": True, "installers": apps}


def extract_installer(constants, pkg_path: str) -> dict:
    from ..support import macos_installer_handler
    ok = macos_installer_handler.InstallerCreation(constants).install_macOS_installer(pkg_path)
    return {"ok": bool(ok)}


def validate_installer(constants, integrity_url: str) -> dict:
    """
    Validate the downloaded InstallAssistant.pkg against Apple's chunklist.
    """
    import time
    from pathlib import Path
    from ..support import network_handler, integrity_verification, utilities

    pkg_path = constants.payload_path / Path("InstallAssistant.pkg")
    if not pkg_path.exists():
        return {"ok": False, "error": "InstallAssistant.pkg not found"}

    try:
        chunklist = network_handler.NetworkUtilities().get(integrity_url).content
    except Exception as error:
        return {"ok": False, "error": f"Failed to download chunklist: {error}"}
    if not chunklist:
        return {"ok": False, "error": "Failed to download chunklist"}

    utilities.disable_sleep_while_running()
    chunk_obj = integrity_verification.ChunklistVerification(pkg_path, chunklist, constants)
    if not chunk_obj.chunks:
        return {"ok": False, "error": "Failed to parse chunklist"}

    chunk_obj.validate()
    while chunk_obj.status == integrity_verification.ChunklistStatus.IN_PROGRESS:
        if chunk_obj.total_chunks:
            _emit_progress(float(chunk_obj.current_chunk) / float(chunk_obj.total_chunks) * 100.0,
                           0, chunk_obj.current_chunk, chunk_obj.total_chunks)
        time.sleep(0.3)

    ok = chunk_obj.status == integrity_verification.ChunklistStatus.SUCCESS
    return {"ok": ok, "error": getattr(chunk_obj, "error_msg", "") if not ok else None}


def verify_sha1(path: str, expected_sha1: str) -> dict:
    import hashlib
    from pathlib import Path
    if not expected_sha1:
        return {"ok": True, "skipped": True}
    file_path = Path(path)
    if not file_path.exists():
        return {"ok": False, "error": f"File not found: {path}"}
    sha1 = hashlib.sha1()
    size = file_path.stat().st_size
    done = 0
    with file_path.open("rb") as f:
        while True:
            chunk = f.read(8 * 1024 * 1024)
            if not chunk:
                break
            sha1.update(chunk)
            done += len(chunk)
            if size:
                _emit_progress(float(done) / float(size) * 100.0, 0, done, size)
    computed = sha1.hexdigest()
    ok = computed.lower() == expected_sha1.lower()
    return {"ok": ok, "error": None if ok else f"SHA1 mismatch: {computed}"}


def _download_autopkg_assets(constants) -> None:
    import subprocess
    from pathlib import Path
    from ..support import network_handler, utilities

    link = constants.installer_pkg_url
    if network_handler.NetworkUtilities(link).validate_link() is False:
        logging.info("Stock Install.pkg missing on GitHub, falling back to nightly")
        link = constants.installer_pkg_url_nightly

    path = constants.installer_pkg_zip_path if link.endswith(".zip") else constants.installer_pkg_path

    autopkg_download = network_handler.DownloadObject(link, path, skip_validation=True)
    autopkg_download.download(spawn_thread=False)

    if autopkg_download.download_complete is False:
        logging.warning("Failed to download Install.pkg")
        return

    utilities.disable_sleep_while_running()
    if not str(path).endswith(".zip"):
        return
    if Path(constants.installer_pkg_path).exists():
        subprocess.run(["/bin/rm", str(constants.installer_pkg_path)])
    subprocess.run(["/usr/bin/ditto", "-V", "-x", "-k", "--sequesterRsrc", "--rsrc",
                    str(constants.installer_pkg_zip_path), str(constants.payload_path)])


def _chainload_kdk(constants, build: str, version: str, download_dir) -> None:
    import subprocess
    import tempfile
    from pathlib import Path
    from ..support import kdk_handler, subprocess_wrapper, utilities
    from ..volume import generate_copy_arguments

    download_dir = Path(download_dir)
    kdk_dmg_path = download_dir / "KDK.dmg"
    kdk_pkg_path = download_dir / "KDK.pkg"
    for p in (kdk_dmg_path, kdk_pkg_path):
        if p.exists():
            p.unlink()

    kdk_obj = kdk_handler.KernelDebugKitObject(constants, build, version, ignore_installed=True)
    if kdk_obj.success is False:
        logging.info("Failed to retrieve KDK for chainload")
        return

    kdk_download_obj = kdk_obj.retrieve_download(override_path=str(kdk_dmg_path))
    if kdk_download_obj is None:
        logging.info("Failed to retrieve KDK")
        return

    space = utilities.get_free_space(str(download_dir))
    if space < (kdk_obj.kdk_url_expected_size * 2):
        logging.info("Not enough disk space to download and install KDK")
        if space < kdk_obj.kdk_url_expected_size:
            return
        kdk_dmg_path = constants.kdk_download_path

    kdk_download_obj.download(spawn_thread=False)
    if kdk_download_obj.download_complete is False:
        logging.info("Failed to download KDK")
        return

    if not Path(kdk_dmg_path).exists():
        return

    with tempfile.TemporaryDirectory() as mount_point:
        result = subprocess.run(["/usr/bin/hdiutil", "attach", str(kdk_dmg_path), "-mountpoint", mount_point, "-nobrowse"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            logging.info("Failed to mount KDK")
            return
        subprocess.run(generate_copy_arguments(f"{mount_point}/KernelDebugKit.pkg", str(kdk_pkg_path)))
        subprocess.run(["/usr/bin/hdiutil", "detach", mount_point], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if Path(kdk_dmg_path).exists():
        Path(kdk_dmg_path).unlink()


def _chainload_metallib(constants, build: str, version: str, download_dir) -> None:
    from pathlib import Path
    from ..support import metallib_handler, utilities

    download_dir = Path(download_dir)
    metallib_pkg_path = download_dir / "MetallibSupportPkg.pkg"
    if metallib_pkg_path.exists():
        metallib_pkg_path.unlink()

    metallib_obj = metallib_handler.MetalLibraryObject(constants, build, version, ignore_installed=True)
    if metallib_obj.success is False:
        logging.info("Failed to retrieve Metallib for chainload")
        return

    metallib_download_obj = metallib_obj.retrieve_download(override_path=str(metallib_pkg_path))
    if metallib_download_obj is None:
        logging.info("Failed to retrieve Metallib")
        return

    space = utilities.get_free_space(str(download_dir))
    if space < (100 * 1024 * 1024):
        logging.info("Not enough disk space to download Metallib")
        return

    metallib_download_obj.download(spawn_thread=False)
    if metallib_download_obj.download_complete is False:
        logging.info("Failed to download Metallib")
        return


def _install_installer_pkg(constants, disk: str) -> None:
    import plistlib
    import subprocess
    from pathlib import Path
    from ..support import utilities
    from ..volume import generate_copy_arguments
    from ..datasets import os_data

    disk = disk + "s2"
    if not Path(constants.installer_pkg_path).exists():
        return

    mount = utilities.grab_mount_point_from_disk(disk)
    if not Path(mount + "/System/Library/CoreServices/SystemVersion.plist").exists():
        return

    os_version = plistlib.load(Path(mount + "/System/Library/CoreServices/SystemVersion.plist").open("rb"))
    kernel_version = os_data.os_conversion.os_to_kernel(os_version["ProductVersion"])
    if int(kernel_version) < os_data.os_data.big_sur:
        logging.info("Installer unsupported, requires Big Sur or newer")
        return

    subprocess.run(["/bin/mkdir", "-p", f"{mount}/Library/Packages/"])
    subprocess.run(generate_copy_arguments(str(constants.installer_pkg_path), f"{mount}/Library/Packages/"))

    _chainload_metallib(constants, os_version["ProductBuildVersion"], os_version["ProductVersion"], Path(mount + "/Library/Packages/"))
    _chainload_kdk(constants, os_version["ProductBuildVersion"], os_version["ProductVersion"], Path(mount + "/Library/Packages/"))


def flash_installer(constants, installer_path: str, disk: str) -> dict:
    """
    Full macOS installer flash, matching the wx GUI:

    1. Generate + run createinstallmedia script (erases the disk).
    2. Download AutoPkg-Assets.pkg and install the patcher onto the drive.
    3. Chainload the matching KDK and MetallibSupportPkg onto the drive.
    """
    from ..support import macos_installer_handler, subprocess_wrapper, utilities

    creator = macos_installer_handler.InstallerCreation(constants)
    if not creator.generate_installer_creation_script(str(constants.payload_path), installer_path, disk):
        return {"ok": False, "error": "Failed to generate installer script"}

    utilities.disable_sleep_while_running()

    _download_autopkg_assets(constants)

    with open(constants.installer_sh_path, "r") as f:
        logging.info(f"installer.sh contents:\n{f.read()}")

    result = subprocess_wrapper.run_as_root(["/bin/sh", str(constants.installer_sh_path)], capture_output=True, text=True)
    output = result.stdout or ""
    if "Install media now available at" not in output:
        return {"ok": False, "error": output[-2000:]}

    _install_installer_pkg(constants, disk)

    utilities.enable_sleep_after_running()
    return {"ok": True}



# ==================== Update / OS cache ====================

def check_updates(constants) -> dict:
    """
    Check for a newer OCLP-R binary via GitHub releases.
    """
    from ..support import updates
    result = updates.CheckBinaryUpdates(constants).check_binary_updates()
    if not result:
        return {"ok": True, "update_available": False}
    return {
        "ok": True,
        "update_available": True,
        "version": result.get("Version"),
        "link": result.get("Link"),
        "github_link": result.get("Github Link"),
    }


def install_update(constants, url: str, version: str) -> dict:
    """
    Download, extract (if zip), install and relaunch an OCLP-R update.
    """
    import subprocess
    from pathlib import Path
    from ..support import network_handler, subprocess_wrapper

    file_name = "OCLP-R.pkg.zip" if url.endswith(".zip") else "OCLP-R.pkg"
    pkg_path = constants.payload_path / "OCLP-R.pkg"

    download_obj = network_handler.DownloadObject(url, constants.payload_path / file_name, skip_validation=True)
    download_obj.download(spawn_thread=False)
    if download_obj.download_complete is False:
        return {"ok": False, "error": "Failed to download update"}

    if url.endswith(".zip"):
        if Path(pkg_path).exists():
            subprocess.run(["/bin/rm", "-rf", str(pkg_path)])
        result = subprocess.run(["/usr/bin/ditto", "-xk", str(constants.payload_path / file_name), str(constants.payload_path)], capture_output=True)
        if result.returncode != 0:
            return {"ok": False, "error": "Failed to extract update"}

    result = subprocess_wrapper.run_as_root(["/usr/sbin/installer", "-pkg", str(pkg_path), "-target", "/"], capture_output=True)
    if result.returncode != 0:
        return {"ok": False, "error": "Failed to install update"}

    subprocess.Popen(["/Library/Application Support/Hackdoc/OCLP-R.app/Contents/MacOS/OCLP-R", "--update_installed"])
    return {"ok": True, "version": version}


def cache_os_headless(constants) -> dict:
    """
    Cache the KDK (and MetallibSupportPkg) for a staged macOS update, matching
    the wx "Cache OS Update" flow.
    """
    from ..support import kdk_handler, metallib_handler, utilities

    os_data = utilities.fetch_staged_update(variant="Preflight")
    if not os_data or os_data[0] is None:
        return {"ok": False, "error": "No staged update found"}
    version, build = os_data[0], os_data[1]

    messages = []

    kdk_obj = kdk_handler.KernelDebugKitObject(constants, build, version, passive=True, check_backups_only=True)
    if kdk_obj is not None and kdk_obj.success is True:
        download_obj = kdk_obj.retrieve_download()
        if download_obj is not None:
            download_obj.download(spawn_thread=False)
            if download_obj.download_complete and kdk_obj.validate_kdk_checksum():
                kdk_handler.KernelDebugKitUtilities().install_kdk_dmg(constants.kdk_download_path, only_install_backup=True)
                messages.append(f"KDK cached for {build}")
            else:
                messages.append("KDK download/validation failed")
        else:
            messages.append("KDK already installed")
    else:
        messages.append("No KDK required")

    metallib_obj = metallib_handler.MetalLibraryObject(constants, build, version, passive=True)
    if metallib_obj is not None and metallib_obj.success is True:
        download_obj = metallib_obj.retrieve_download()
        if download_obj is not None:
            download_obj.download(spawn_thread=False)
            if download_obj.download_complete:
                metallib_obj.install_metallib()
                messages.append(f"Metallib cached for {build}")
        else:
            messages.append("Metallib already installed")

    return {"ok": True, "build": build, "version": version, "messages": messages}
