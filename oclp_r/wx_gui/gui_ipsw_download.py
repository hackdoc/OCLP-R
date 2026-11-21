"""
gui_ipsw_download.py: macOS IPSW Download Frame

Downloads UniversalMac restore images for Apple Silicon Macs.
Files are saved to the download path configured in Settings.
"""

import wx
import os
import re
import locale
import getpass
import hashlib
import logging
import plistlib
import threading
import requests

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from .. import constants

from ..wx_gui import (
    gui_main_menu,
    gui_support,
    gui_download,
)

from ..support import (
    utilities,
    network_handler,
)

from ..support.translate_language import TranslateLanguage


class IPSWDownloadFrame(wx.Frame):
    """
    Create a frame for downloading macOS IPSW restore images
    Files are saved to constants.user_download_file so the
    download path chosen in Settings is respected.
    """
    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants, screen_location: tuple = None):
        self.trans = TranslateLanguage(global_constants).gui_ipsw_download()
        logging.info(self.trans["Initializing IPSW Download Frame"])
        self.constants: constants.Constants = global_constants
        self.title: str = title
        self.parent: wx.Frame = parent
        self.frame_modal: wx.Dialog = None
        self.ipsws: list = []
        self.ipsws_latest: list = []
        self.list: wx.ListCtrl = None
        self.select_button: wx.Button = None
        self.copy_button: wx.Button = None
        self.showolderversions_checkbox: wx.CheckBox = None
        self._closing_for_download: bool = False
        self._busy: bool = False

        super(IPSWDownloadFrame, self).__init__(None, title=title, size=(300, 200), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        gui_support.GenerateMenubar(self, self.constants).generate()
        self.Centre()
        if screen_location:
            self.SetPosition(screen_location)

        self.icons = [[self._icon_to_bitmap(i), self._icon_to_bitmap(i, (64, 64))] for i in self.constants.icons_path]

        # Window close is vetoed while a blocking operation owns this frame
        self._busy = True
        self.Bind(wx.EVT_CLOSE, self.on_frame_close)
        self.Show()
        self._generate_catalog_frame()

    def on_frame_close(self, event: wx.CloseEvent) -> None:
        """
        Prevent the frame from being destroyed while the catalog is loading
        """
        if self._busy:
            return
        self.on_return_to_main_menu()

    def _icon_to_bitmap(self, icon: str, size: tuple = (32, 32)) -> wx.Bitmap:
        """
        Convert icon to bitmap
        """
        return wx.Bitmap(wx.Bitmap(icon, wx.BITMAP_TYPE_ICON).ConvertToImage().Rescale(size[0], size[1], wx.IMAGE_QUALITY_HIGH))

    def _macos_version_to_icon(self, build_version: int) -> int:
        """
        Convert a Darwin build major version to a macOS icon index
        """
        index = build_version - 19
        if 0 <= index < len(self.constants.icons_path):
            return index
        return 0

    def _build_to_icon(self, build: str) -> int:
        try:
            return self._macos_version_to_icon(int(build[:2]))
        except (ValueError, TypeError):
            return 0

    def _generate_catalog_frame(self) -> None:
        """
        Fetch the IPSW catalog and display available versions
        """
        title_label = wx.StaticText(self, label=self.trans["Finding Available IPSW"], pos=(-1, 5))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        title_label.Centre(wx.HORIZONTAL)

        progress_bar = wx.Gauge(self, range=100, pos=(-1, title_label.GetPosition()[1] + title_label.GetSize()[1] + 5), size=(250, 30))
        progress_bar.Centre(wx.HORIZONTAL)
        progress_bar_animation = gui_support.GaugePulseCallback(self.constants, progress_bar)
        progress_bar_animation.start_pulse()

        self.SetSize((-1, progress_bar.GetPosition()[1] + progress_bar.GetSize()[1] + 50))

        fetch_error = None

        def _fetch_ipsws():
            nonlocal fetch_error
            try:
                response = requests.get(self.constants.ipsw_api_link, timeout=60)
                response.raise_for_status()
                firmwares = response.json().get("firmwares", [])
                if isinstance(firmwares, list):
                    self.ipsws = [fw for fw in firmwares if isinstance(fw, dict) and fw.get("url")]
                if self.ipsws:
                    return
            except Exception as e:
                logging.warning(f"ipsw.me catalog unavailable: {e}")

            # Fall back to Apple's own catalog, which only exposes the currently signed IPSWs
            try:
                response = requests.get(self.constants.ipsw_apple_api_link, timeout=60)
                response.raise_for_status()
                self.ipsws = self._parse_apple_catalog(response.content)
            except Exception as e:
                fetch_error = str(e)

        thread = threading.Thread(target=_fetch_ipsws)
        thread.start()
        gui_support.wait_for_thread(thread)
        self._busy = False

        progress_bar_animation.stop_pulse()
        for child in self.GetChildren():
            child.Destroy()

        if fetch_error or not self.ipsws:
            logging.error(f"{self.trans['Failed to download IPSW catalog']}: {fetch_error}")
            wx.MessageBox(self.trans["Failed to download IPSW catalog"], self.trans["Error"], wx.OK | wx.ICON_ERROR)
            self.on_return_to_main_menu()
            return

        self._sort_ipsws()
        self._display_available_ipsws()

    def _parse_apple_catalog(self, contents: bytes) -> list:
        """
        Parse Apple's com_apple_macOSIPSW catalog into the same shape as the ipsw.me API
        """
        ipsws = []
        by_url = {}

        try:
            catalog = plistlib.loads(contents)
            devices = catalog.get("MobileDeviceSoftwareVersionsByVersion", {}).get("1", {}).get("MobileDeviceSoftwareVersions", {})
        except Exception as e:
            logging.error(f"Failed to parse Apple IPSW catalog: {e}")
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
                    # Some device entries (such as VirtualMac) omit the checksum,
                    # so merge it in from later entries for the same image
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

        # Apple's catalog does not publish file sizes, so query them for the
        # entries we are about to display
        for ipsw in ipsws:
            try:
                response = requests.head(ipsw["url"], allow_redirects=True, timeout=30)
                if response.status_code != 200:
                    raise Exception(f"HTTP {response.status_code}")
                ipsw["filesize"] = int(response.headers.get("Content-Length") or 0)
            except Exception as e:
                logging.warning(f"Failed to get IPSW size for {ipsw['url']}: {e}")

        return ipsws

    @staticmethod
    def _build_sort_key(build: str) -> tuple:
        """
        Split a build string such as 20G165 into numeric components so that
        20G165 sorts above 20G95
        """
        match = re.match(r"^(\d+)([A-Za-z]+)(\d+)$", str(build))
        if match:
            return int(match.group(1)), match.group(2), int(match.group(3))
        return 0, str(build), 0

    def _sort_ipsws(self) -> None:
        """
        Sort IPSWs newest first and keep the latest entry of each major version
        """
        self.ipsws = sorted(
            self.ipsws,
            key=lambda item: (
                str(item.get("releasedate") or ""),
                self._build_sort_key(item.get("buildid") or "")
            ),
            reverse=True
        )

        latest = {}
        for item in self.ipsws:
            major_version = str(item.get("version", "0")).split(".")[0]
            if major_version not in latest:
                latest[major_version] = item
        self.ipsws_latest = list(latest.values())

    @staticmethod
    def _version_to_name(version: str) -> str:
        """
        Map a macOS major version to its marketing name
        """
        names = {
            "27": "Golden Gate",
            "26": "Tahoe",
            "15": "Sequoia",
            "14": "Sonoma",
            "13": "Ventura",
            "12": "Monterey",
            "11": "Big Sur",
        }
        return names.get(str(version).split(".")[0], str(version))

    @staticmethod
    def _format_release_date(releasedate: str) -> str:
        """
        Format the catalog release date in the user's locale
        """
        date_part = str(releasedate or "").split("T")[0]
        try:
            return datetime.strptime(date_part, "%Y-%m-%d").strftime("%x")
        except ValueError:
            return date_part or "-"

    def _display_available_ipsws(self, event: wx.Event = None, show_full: bool = False) -> None:
        """
        Display available IPSWs in a modal dialog
        """
        if self.frame_modal:
            try:
                self.frame_modal.Destroy()
            except RuntimeError:
                # Already destroyed by a previous close event
                pass
            self.frame_modal = None

        self.frame_modal = wx.Dialog(self, title=self.trans["Select macOS IPSW"], size=(490, 600))
        bundles = [wx.BitmapBundle.FromBitmaps(icon) for icon in self.icons]

        title_label = wx.StaticText(self.frame_modal, label=self.trans["Select macOS IPSW"], pos=(-1, -1))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))

        id = wx.NewIdRef()
        self.list = wx.ListCtrl(self.frame_modal, id, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER | wx.BORDER_SUNKEN)
        self.list.SetSmallImages(bundles)
        self.list.InsertColumn(0, "Title",        width=160)
        self.list.InsertColumn(1, "Version",      width=50)
        self.list.InsertColumn(2, "Build",        width=70)
        self.list.InsertColumn(3, "Size",         width=70)
        self.list.InsertColumn(4, "Release Date", width=90)

        ipsws = self.ipsws if show_full is True else self.ipsws_latest
        if show_full is False:
            self.frame_modal.SetSize((490, 390))

        locale.setlocale(locale.LC_TIME, '')
        logging.info(f"{self.trans['Available IPSWs']} ({self.trans['All entries'] if show_full else self.trans['Latest only']}):")
        for item in ipsws:
            version = str(item.get("version", ""))
            build = str(item.get("buildid", ""))
            size = item.get("filesize") or 0
            size_str = utilities.human_fmt(size) if size else "-"
            index = self.list.InsertItem(self.list.GetItemCount(), f"macOS {self._version_to_name(version)}")
            self.list.SetItemImage(index, self._build_to_icon(build))
            self.list.SetItem(index, 1, version)
            self.list.SetItem(index, 2, build)
            self.list.SetItem(index, 3, size_str)
            self.list.SetItem(index, 4, self._format_release_date(item.get("releasedate", "")))
            logging.info(f"- macOS {version} ({build}):\n  - Size: {size_str}\n  - Link: {item.get('url', '')}\n")

        self.list.Select(-1)
        self.list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_select_list)
        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select_list)

        self.select_button = wx.Button(self.frame_modal, label=self.trans["Download"], pos=(-1, -1), size=(150, -1))
        self.select_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.select_button.Bind(wx.EVT_BUTTON, lambda event, ipsws=ipsws: self.on_download_ipsw(ipsws))
        self.select_button.SetToolTip(self.trans["Download the selected IPSW."])
        self.select_button.SetDefault()
        if show_full is True:
            self.select_button.Disable()

        self.copy_button = wx.Button(self.frame_modal, label=self.trans["Copy Link"], pos=(-1, -1), size=(80, -1))
        self.copy_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.copy_button.Bind(wx.EVT_BUTTON, lambda event, ipsws=ipsws: self.on_copy_link(ipsws))
        self.copy_button.SetToolTip(self.trans["Copy the download link of the selected IPSW."])
        if show_full is True:
            self.copy_button.Disable()

        return_button = wx.Button(self.frame_modal, label=self.trans["Return to Main Menu"], pos=(-1, -1), size=(150, -1))
        return_button.Bind(wx.EVT_BUTTON, self.on_return_to_main_menu)
        return_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))

        self.showolderversions_checkbox = wx.CheckBox(self.frame_modal, label=self.trans["Show Older/Beta Versions"], pos=(-1, -1))
        if show_full is True:
            self.showolderversions_checkbox.SetValue(True)
        self.showolderversions_checkbox.Bind(wx.EVT_CHECKBOX, lambda event: self._display_available_ipsws(event, self.showolderversions_checkbox.GetValue()))

        rectbox = wx.StaticBox(self.frame_modal, -1)
        rectsizer = wx.StaticBoxSizer(rectbox, wx.HORIZONTAL)
        rectsizer.Add(self.copy_button, 0, wx.EXPAND | wx.RIGHT, 5)
        rectsizer.Add(self.select_button, 0, wx.EXPAND | wx.LEFT, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(10)
        sizer.Add(title_label, 0, wx.ALIGN_CENTRE | wx.ALL, 0)
        sizer.Add(self.list, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(rectsizer, 0, wx.ALIGN_CENTRE | wx.ALL, 0)
        sizer.AddSpacer(8)
        sizer.Add(self.showolderversions_checkbox, 0, wx.ALIGN_CENTRE | wx.ALL, 15)
        sizer.Add(return_button, 0, wx.ALIGN_CENTRE | wx.BOTTOM, 15)

        self.frame_modal.SetSizer(sizer)
        self.frame_modal.Bind(wx.EVT_CLOSE, self.on_modal_close)
        self.frame_modal.ShowWindowModal()

    def on_modal_close(self, event: wx.CloseEvent) -> None:
        """
        Distinguish the window close button from closing to start a download
        """
        if self._closing_for_download:
            self._closing_for_download = False
            event.Skip()
            return
        self.on_return_to_main_menu()

    def on_select_list(self, event: wx.Event) -> None:
        if self.list.GetSelectedItemCount() > 0:
            self.select_button.Enable()
            self.copy_button.Enable()
        else:
            self.select_button.Disable()
            self.copy_button.Disable()

    def on_copy_link(self, ipsws: list) -> None:
        selected_item = self.list.GetFirstSelected()
        if selected_item != -1:
            clipboard = wx.Clipboard.Get()
            if not clipboard.IsOpened():
                clipboard.Open()
            clipboard.SetData(wx.TextDataObject(ipsws[selected_item].get("url", "")))
            clipboard.Close()
            wx.MessageDialog(self.frame_modal, self.trans["Download link copied to clipboard"], "", wx.OK | wx.ICON_INFORMATION).ShowModal()

    def _configured_download_path(self) -> str:
        return self.constants.user_download_file or f"/Users/{getpass.getuser()}/Downloads"

    def _get_download_directory(self) -> Path:
        """
        Resolve the configured download path, falling back to ~/Downloads if it is not writable
        """
        download_dir = Path(self._configured_download_path()).expanduser()
        try:
            download_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

        if download_dir.is_dir() and os.access(download_dir, os.W_OK | os.X_OK):
            return download_dir

        fallback = Path(f"/Users/{getpass.getuser()}/Downloads")
        try:
            fallback.mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

        if not (fallback.is_dir() and os.access(fallback, os.W_OK | os.X_OK)):
            wx.MessageBox(self.trans["Cannot write to the selected directory."], self.trans["Error"], wx.OK | wx.ICON_ERROR)
            return None

        self.constants.user_download_file = str(fallback)
        message = self.trans["Cannot write to the download path, falling back to {path}"].format(path=fallback)
        logging.warning(message)
        wx.MessageBox(message, self.trans["Error"], wx.OK | wx.ICON_WARNING)
        return fallback

    def _ipsw_file_name(self, ipsw: dict) -> str:
        """
        Use the file name published by Apple, otherwise generate one
        """
        file_name = Path(urlparse(ipsw.get("url", "")).path).name
        if file_name.lower().endswith(".ipsw"):
            return file_name
        return f"UniversalMac_{ipsw.get('version', '')}_{ipsw.get('buildid', '')}_Restore.ipsw"

    def on_download_ipsw(self, ipsws: list) -> None:
        """
        Download the selected IPSW to the configured download path
        """
        selected_item = self.list.GetFirstSelected()
        if selected_item == -1:
            return

        selected_ipsw = ipsws[selected_item]
        download_dir = self._get_download_directory()
        if download_dir is None:
            return

        target_path = download_dir / self._ipsw_file_name(selected_ipsw)
        try:
            expected_size = int(selected_ipsw.get("filesize", 0))
        except (TypeError, ValueError):
            expected_size = 0

        if expected_size:
            existing_size = target_path.stat().st_size if target_path.exists() else 0
            # An incomplete file is resumed, so only the remaining bytes are required;
            # a complete file is deleted before downloading again, freeing its space
            needed_space = max(0, expected_size - existing_size)
            free_space = utilities.get_free_space(download_dir)
            if free_space < needed_space:
                message = self.trans["Insufficient space to download this IPSW: {0} available vs {1} required"].format(
                    utilities.human_fmt(free_space), utilities.human_fmt(needed_space)
                )
                logging.error(message)
                wx.MessageBox(message, self.trans["Insufficient Space"], wx.OK | wx.ICON_WARNING)
                return

        if target_path.exists() and (not expected_size or target_path.stat().st_size >= expected_size):
            # A .progress file means an interrupted download that can be resumed
            if not Path(f"{target_path}.progress").exists():
                if wx.MessageBox(
                    self.trans["IPSW already exists: {path}\n\nDownload it again?"].format(path=target_path),
                    self.trans["IPSW Download"],
                    wx.YES_NO | wx.ICON_QUESTION | wx.NO_DEFAULT
                ) != wx.YES:
                    return

        logging.info(f"{self.trans['Selected IPSW']}: macOS {selected_ipsw.get('version', '')} ({selected_ipsw.get('buildid', '')})")
        self._closing_for_download = True
        self.frame_modal.Close()
        self.frame_modal = None
        self._closing_for_download = False

        download_obj = network_handler.DownloadObject(
            selected_ipsw["url"],
            str(target_path),
            expected_size if expected_size else None
        )
        # IPSWs are 15-30 GB and the multipart downloader buffers parts in memory,
        # so stream to disk on a single connection instead
        download_obj.chunk_count = 1
        gui_download.DownloadFrame(
            self,
            title=self.title,
            global_constants=self.constants,
            download_obj=download_obj,
            item_name=f"macOS IPSW {selected_ipsw.get('version', '')} ({selected_ipsw.get('buildid', '')})",
            download_icon=self.constants.icons_path[self._build_to_icon(str(selected_ipsw.get("buildid", "")))]
        )

        if download_obj.download_complete is False:
            self.on_return_to_main_menu()
            return

        validation_error, delete_file = self._validate_ipsw(
            target_path, expected_size or int(download_obj.total_file_size or 0)
        )
        if validation_error:
            logging.error(f"IPSW validation failed for {target_path}: {validation_error}")
            if delete_file:
                try:
                    target_path.unlink()
                except OSError as e:
                    logging.warning(f"Failed to remove invalid download {target_path}: {e}")
            wx.MessageBox(validation_error, self.trans["Error"], wx.OK | wx.ICON_ERROR)
            self.on_return_to_main_menu()
            return

        checksum_error, delete_corrupt = self._verify_ipsw_checksum(target_path, selected_ipsw)
        if checksum_error:
            logging.error(f"IPSW checksum verification failed for {target_path}: {checksum_error}")
            if delete_corrupt:
                try:
                    target_path.unlink()
                except OSError as e:
                    logging.warning(f"Failed to remove corrupt download {target_path}: {e}")
            wx.MessageBox(checksum_error, self.trans["Verification Failed"], wx.OK | wx.ICON_ERROR)
            self.on_return_to_main_menu()
            return

        wx.MessageBox(
            self.trans["IPSW downloaded to:\n{path}"].format(path=target_path),
            self.trans["Download Complete"],
            wx.OK | wx.ICON_INFORMATION
        )
        self.on_return_to_main_menu()

    def _validate_ipsw(self, path: Path, expected_size: int) -> tuple:
        """
        Validate a finished download before reporting success
        Returns (error_message, should_delete); an empty message means the file is valid
        """
        if not path.exists():
            return self.trans["Downloaded file is missing."], False

        size = path.stat().st_size
        if size == 0:
            return self.trans["Downloaded file is empty."], True

        try:
            with path.open("rb") as file:
                magic = file.read(4)
        except OSError as e:
            return str(e), False

        # IPSWs are zip archives; an HTML/XML error page is not
        if magic != b"PK\x03\x04":
            return self.trans["Downloaded file is not a valid IPSW."], True

        if expected_size and size != expected_size:
            return self.trans["Incomplete download: {0} of {1}"].format(
                utilities.human_fmt(size), utilities.human_fmt(expected_size)
            ), False

        return "", False

    def _verify_ipsw_checksum(self, path: Path, ipsw: dict) -> tuple:
        """
        Verify the downloaded file against the catalog checksum
        Returns (error_message, should_delete); an empty message means the file is valid
        """
        algorithm = ""
        expected = ""
        if ipsw.get("sha256sum"):
            algorithm, expected = "sha256", str(ipsw["sha256sum"]).lower()
        elif ipsw.get("sha1sum"):
            algorithm, expected = "sha1", str(ipsw["sha1sum"]).lower()

        if not expected:
            return "", False

        logging.info(f"Verifying {algorithm} checksum for {path}")

        self._busy = True
        self.Disable()
        dialog = wx.Dialog(self, title=self.trans["Verifying IPSW"], size=(400, 150))
        label = wx.StaticText(dialog, label=self.trans["Verifying the downloaded IPSW..."], pos=(-1, 10))
        label.Centre(wx.HORIZONTAL)
        gauge = wx.Gauge(dialog, range=100, pos=(-1, label.GetPosition()[1] + label.GetSize()[1] + 10), size=(250, 30))
        gauge.Centre(wx.HORIZONTAL)
        animation = gui_support.GaugePulseCallback(self.constants, gauge)
        animation.start_pulse()
        dialog.SetSize((-1, gauge.GetPosition()[1] + gauge.GetSize()[1] + 40))
        dialog.Centre()
        # The dialog must stay alive until hashing finishes
        dialog.Bind(wx.EVT_CLOSE, lambda event: None)
        dialog.Show()

        result = {"digest": "", "error": ""}

        def _hash_file():
            try:
                digest = hashlib.new(algorithm)
                with path.open("rb") as file:
                    for chunk in iter(lambda: file.read(8 * 1024 * 1024), b""):
                        digest.update(chunk)
                result["digest"] = digest.hexdigest()
            except Exception as e:
                result["error"] = str(e)

        thread = threading.Thread(target=_hash_file)
        try:
            thread.start()
            gui_support.wait_for_thread(thread)
        finally:
            animation.stop_pulse()
            try:
                dialog.Destroy()
            except RuntimeError:
                pass
            self.Enable()
            self._busy = False

        if result["error"]:
            return result["error"], False

        if result["digest"] != expected:
            return self.trans["IPSW checksum mismatch."], True

        logging.info("IPSW checksum verified")
        return "", False

    def on_return_to_main_menu(self, event: wx.Event = None) -> None:
        """
        Return to main menu
        """
        if self.frame_modal:
            try:
                self.frame_modal.Hide()
            except RuntimeError:
                pass
        main_menu_frame = gui_main_menu.MainFrame(
            None,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.GetScreenPosition()
        )
        main_menu_frame.Show()
        if self.frame_modal:
            try:
                self.frame_modal.Destroy()
            except RuntimeError:
                pass
            self.frame_modal = None
        self.Destroy()
