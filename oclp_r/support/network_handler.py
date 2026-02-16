"""
network_handler.py: Library dedicated to Network Handling tasks including downloading files

Primarily based around the DownloadObject class, which provides a simple
object for libraries to query download progress and status
"""

import time
import requests
import threading
import logging
import enum
import hashlib
import atexit
import json
from typing import Union
from pathlib import Path

from urllib3 import response

from . import utilities
from .. import constants
SESSION = requests.Session()
from .translate_language import TranslateLanguage

class DownloadStatus(enum.Enum):
    """
    Enum for download status
    """
    contents=constants.Constants()
    trans=TranslateLanguage(contents).network_handler()
    INACTIVE:    str = trans["Inactive"]
    DOWNLOADING: str = trans["Downloading"]
    ERROR:       str = trans["Error"]
    COMPLETE:    str = trans["Complete"]


class NetworkUtilities:
    """
    Utilities for network related tasks, primarily used for downloading files
    """

    def __init__(self, url: str = None) -> None:
        self.url: str = url
        self.contents=constants.Constants()
        self.trans=TranslateLanguage(self.contents).network_handler()
        if self.contents.github_proxy_link=="Default":
            self.url="https://www.github.com/"
        else:
            self.url = "https://baidu.com/"



    def verify_network_connection(self) -> bool:
        """
        Verifies that the network is available

        Returns:
            bool: True if network is available, False otherwise
        """

        try:
            response=requests.head(self.url, timeout=5, allow_redirects=True,verify=False)
            if response.status_code == 200:
                return True
            if response.status_code == 404:
                return False
            return True
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError
        ):
            return False

    def validate_link(self) -> bool:
        """
        Check for 404 error

        Returns:
            bool: True if link is valid, False otherwise
        """
        try:
            response = SESSION.head(self.url, timeout=5, allow_redirects=True)
            if response.status_code == 404:
                return False
            else:
                return True
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError
        ):
            return False


    def get(self, url: str, **kwargs) -> requests.Response:
        """
        Wrapper for requests's get method
        Implement additional error handling

        Parameters:
            url (str): URL to get
            **kwargs: Additional parameters for requests.get

        Returns:
            requests.Response: Response object from requests.get
        """

        result: requests.Response = None

        try:
            result = SESSION.get(url, **kwargs)
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError
        ) as error:
            logging.warning(f"{self.trans['Error calling requests.get']}: {error}")
            # Return empty response object
            return requests.Response()

        return result

    def post(self, url: str, **kwargs) -> requests.Response:
        """
        Wrapper for requests's post method
        Implement additional error handling

        Parameters:
            url (str): URL to post
            **kwargs: Additional parameters for requests.post

        Returns:
            requests.Response: Response object from requests.post
        """

        result: requests.Response = None

        try:
            result = SESSION.post(url, **kwargs)
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError
        ) as error:
            logging.warning(f"{self.trans['Error calling requests.post']}: {error}")
            # Return empty response object
            return requests.Response()

        return result


class DownloadObject:
    """
    Object for downloading files from the network

    Usage:
        >>> download_object = DownloadObject(url, path)
        >>> download_object.download(display_progress=True)

        >>> if download_object.is_active():
        >>>     print(download_object.get_percent())

        >>> if not download_object.download_complete:
        >>>     print("Download failed")

        >>> print("Download complete"")

    """

    def __init__(self, url: str, path: str, size:str=None, resume_download: bool = True) -> None:
        self.url:       str = url
        self.status:    str = DownloadStatus.INACTIVE
        self.error_msg: str = ""
        self.filename:  str = self._get_filename()
        self.size:      str = size
        self.resume_download: bool = resume_download
        
        self.filepath:  Path = Path(path)
        self.progress_file: Path = Path(f"{path}.progress")
    
        self.total_file_size:      float = 0.0
        self.downloaded_file_size: float = 0.0
        self.downloaded_file_offset: float = 0.0
        self.start_time:           float = time.time()

        self.error:             bool = False
        self.should_stop:       bool = False
        self.download_complete: bool = False
        self.has_network:       bool = NetworkUtilities(self.url).verify_network_connection()

        self.active_thread: threading.Thread = None

        self.should_checksum: bool = False

        self.checksum = None
        self._checksum_storage: hash = None
        
        self.contents=constants.Constants()
        self.trans=TranslateLanguage(self.contents).network_handler()

        if self.has_network:
            self._populate_file_size()


    def __del__(self) -> None:
        self.stop()


    def download(self, display_progress: bool = False, spawn_thread: bool = True, verify_checksum: bool = False) -> None:
        """
        Download the file

        Spawns a thread to download the file, so that the main thread can continue
        Note sleep is disabled while the download is active

        Parameters:
            display_progress (bool): Display progress in console
            spawn_thread (bool): Spawn a thread to download the file, otherwise download in the current thread
            verify_checksum (bool): Calculate checksum of downloaded file if True

        """
        self.status = DownloadStatus.DOWNLOADING
        logging.info(self.trans["Starting download: {0}"].format(self.filename))
        if spawn_thread:
            if self.active_thread:
                logging.error(self.trans["Download already in progress"])
                return
            self.should_checksum = verify_checksum
            self.active_thread = threading.Thread(target=self._download, args=(display_progress,))
            self.active_thread.start()
            return

        self.should_checksum = verify_checksum
        self._download(display_progress)


    def download_simple(self, verify_checksum: bool = False) -> Union[str, bool]:
        """
        Alternative to download(), mimics  utilities.py's old download_file() function

        Parameters:
            verify_checksum (bool): Return checksum of downloaded file if True

        Returns:
            If verify_checksum is True, returns the checksum of the downloaded file
            Otherwise, returns True if download was successful, False otherwise
        """

        if verify_checksum:
            self.should_checksum = True
            self.checksum = hashlib.sha256()

        self.download(spawn_thread=False)

        if not self.download_complete:
            return False

        return self.checksum.hexdigest() if self.checksum else True


    def _get_filename(self) -> str:
        """
        Get the filename from the URL

        Returns:
            str: Filename
        """

        return Path(self.url).name

    def convert_size(self, size_str):
        if isinstance(size_str, float):
            return float(size_str)
        if isinstance(size_str, int):
            return float(size_str)

        units = {'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
        for unit, factor in units.items():
            if unit in size_str:
               return float(size_str.replace(unit, '')) * factor
        return float(size_str)
    def _populate_file_size(self) -> None:
        """
        Get the file size of the file to be downloaded

        If unable to get file size, set to zero
        """

        try:
            result = SESSION.head(self.url, allow_redirects=True, timeout=5)
            if 'Content-Length' in result.headers:
                self.total_file_size = float(result.headers['Content-Length'])
                if self.size != None:
                    self.total_file_size = self.convert_size(self.size)
            else:
                raise Exception(self.trans["Content-Length missing from headers"])
        except Exception as e:
            logging.error(self.trans["Error determining file size {0}: {1}"].format(self.url, str(e)))
            logging.error(self.trans["Assuming file size is 0"])
            self.total_file_size = 0.0


    def _update_checksum(self, chunk: bytes) -> None:
        """
        Update checksum with new chunk

        Parameters:
            chunk (bytes): Chunk to update checksum with
        """
        self._checksum_storage.update(chunk)


    def _prepare_working_directory(self, path: Path) -> bool:
        """
        Validates working enviroment, including free space and handling existing files

        Parameters:
            path (str): Path to the file

        Returns:
            bool: True if successful, False if not
        """

        try:
            if Path(path).exists():
                if self.resume_download:
                    # For resumable download, keep the existing file
                    self.downloaded_file_offset = Path(path).stat().st_size
                    logging.info(self.trans["Resuming download from {0}: {1}"].format(utilities.human_fmt(self.downloaded_file_offset), path))
                else:
                    logging.info(self.trans["Deleting existing file: {0}"].format(path))
                    Path(path).unlink()
                return True

            if not Path(path).parent.exists():
                logging.info(self.trans["Creating directory: {0}"].format(Path(path).parent))
                Path(path).parent.mkdir(parents=True, exist_ok=True)

            available_space = utilities.get_free_space(Path(path).parent)
            if self.total_file_size > available_space:
                msg = self.trans["Not enough free space to download {0}, need {1}, have {2}"].format(self.filename, utilities.human_fmt(self.total_file_size), utilities.human_fmt(available_space))
                logging.error(msg)
                raise Exception(msg)

        except Exception as e:
            self.error = True
            self.error_msg = str(e)
            self.status = DownloadStatus.ERROR
            logging.error(self.trans["Error preparing working directory {0}: {1}"].format(path, self.error_msg))
            return False

        logging.info(self.trans["- Directory ready: {0}"].format(path))
        return True

    def _save_progress(self) -> None:
        """
        Save download progress to a file
        """
        try:
            with open(self.progress_file, 'w') as f:
                json.dump({
                    'downloaded': self.downloaded_file_size,
                    'total': self.total_file_size,
                    'offset': self.downloaded_file_offset
                }, f)
        except Exception as e:
            logging.warning(self.trans["Failed to save download progress: {0}"].format(str(e)))

    def _load_progress(self) -> bool:
        """
        Load download progress from file

        Returns:
            bool: True if progress was loaded, False otherwise
        """
        if not self.progress_file.exists():
            return False

        try:
            with open(self.progress_file, 'r') as f:
                progress = json.load(f)
                self.downloaded_file_size = progress.get('downloaded', 0)
                self.total_file_size = progress.get('total', 0)
                self.downloaded_file_offset = progress.get('offset', 0)
            return True
        except Exception as e:
            logging.warning(self.trans["Failed to load download progress: {0}"].format(str(e)))
            return False

    def _clear_progress(self) -> None:
        """
        Clear download progress file
        """
        try:
            if self.progress_file.exists():
                self.progress_file.unlink()
        except Exception as e:
            logging.warning(self.trans["Failed to clear progress file: {0}"].format(str(e)))


    def _download(self, display_progress: bool = False) -> None:
        """
        Download the file with resumable support

        Libraries should invoke download() instead of this method

        Parameters:
            display_progress (bool): Display progress in console
        """

        utilities.disable_sleep_while_running()

        try:
            if not self.has_network:
                raise Exception(self.trans["No network connection"])

            if self._prepare_working_directory(self.filepath) is False:
                raise Exception(self.error_msg)

            headers = {}
            if self.resume_download and self.downloaded_file_offset > 0:
                headers['Range'] = f'bytes={self.downloaded_file_offset}-'
                logging.info(self.trans["Resuming download from byte {0}"].format(self.downloaded_file_offset))

            response = NetworkUtilities().get(self.url, stream=True, timeout=100, headers=headers)

            mode = 'ab' if self.resume_download and self.downloaded_file_offset > 0 else 'wb'
            with open(self.filepath, mode) as file:
                atexit.register(self.stop)
                for i, chunk in enumerate(response.iter_content(1024 * 1024 * 4)):
                    if self.should_stop:
                        self._save_progress()
                        raise Exception(self.trans["Download stopped"])
                    
                    if chunk:
                        file.write(chunk)
                        self.downloaded_file_size += len(chunk)
                        if self.should_checksum:
                            self._update_checksum(chunk)
                        if display_progress and i % 100:
                            # Don't use logging here, as we'll be spamming the log file
                            if self.total_file_size == 0.0:
                                print(self.trans["Downloaded {0} of {1}"].format(utilities.human_fmt(self.downloaded_file_size), self.filename))
                            else:
                                print(self.trans["Downloaded {0:.2f}% of {1} ({2}/s) ({3:.2f} seconds remaining)"].format(self.get_percent(), self.filename, utilities.human_fmt(self.get_speed()), self.get_time_remaining()))
                
                if response.status_code == 206:  # Partial Content
                    self._save_progress()
                else:
                    self.download_complete = True
                    self._clear_progress()
                    logging.info(self.trans["Download complete: {0}"].format(self.filename))
                    logging.info(self.trans["Stats:"])
                    logging.info(self.trans["- Downloaded size: {0}"].format(utilities.human_fmt(self.downloaded_file_size)))
                    logging.info(self.trans["- Time elapsed: {0:.2f} seconds"].format((time.time() - self.start_time)))
                    logging.info(self.trans["- Speed: {0}/s"].format(utilities.human_fmt(self.downloaded_file_size / (time.time() - self.start_time))))
                    logging.info(self.trans["- Location: {0}"].format(self.filepath))
        except Exception as e:
            self._save_progress()
            self.error = True
            self.error_msg = str(e)
            self.status = DownloadStatus.ERROR
            logging.error(self.trans["Error downloading {0}: {1}"].format(self.url, self.error_msg))

        self.status = DownloadStatus.COMPLETE
        utilities.enable_sleep_after_running()


    def get_percent(self) -> float:
        """
        Query the download percent

        Returns:
            float: The download percent, or -1 if unknown
        """

        if self.total_file_size == 0.0:
            return -1
        return self.downloaded_file_size / self.total_file_size * 100


    def get_speed(self) -> float:
        """
        Query the download speed

        Returns:
            float: The download speed in bytes per second
        """

        return self.downloaded_file_size / (time.time() - self.start_time)


    def get_time_remaining(self) -> float:
        """
        Query the time remaining for the download

        Returns:
            float: The time remaining in seconds, or -1 if unknown
        """

        if self.total_file_size == 0.0:
            return -1
        speed = self.get_speed()
        if speed <= 0:
            return -1
        return (self.total_file_size - self.downloaded_file_size) / speed


    def get_file_size(self) -> float:
        """
        Query the file size of the file to be downloaded

        Returns:
            float: The file size in bytes, or 0.0 if unknown
        """
        return self.total_file_size


    def is_active(self) -> bool:
        """
        Query if the download is active

        Returns:
            boolean: True if active, False if completed, failed, stopped, or inactive
        """

        if self.status == DownloadStatus.DOWNLOADING:
            return True
        return False

    def delete_temp_files(self) -> None:
        """
        Delete temporary files created during download
        """
        try:
            # Delete the partially downloaded file
            if self.filepath.exists():
                self.filepath.unlink()
                logging.info(self.trans["Deleted partially downloaded file: {0}"].format(self.filepath))
            
            # Delete the progress file
            if self.progress_file.exists():
                self.progress_file.unlink()
                logging.info(self.trans["Deleted progress file: {0}"].format(self.progress_file))
        except Exception as e:
            logging.warning(self.trans["Failed to delete temporary files: {0}"].format(str(e))) 

    def stop(self) -> None:
        """
        Stop the download

        If the download is active, this function will hold the thread until stopped or timeout
        """

        self.should_stop = True
        if self.active_thread and self.active_thread.is_alive():
            self.active_thread.join(timeout=10)
        
        # Delete temporary files if download was cancelled by user
        if not self.download_complete:
            self.delete_temp_files()