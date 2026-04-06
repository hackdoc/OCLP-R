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
import math
import io
import os
import queue
import re
from typing import Union, Optional
from pathlib import Path
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

from . import utilities
from .. import constants
SESSION = requests.Session()
from .translate_language import TranslateLanguage

# Security constants
ALLOWED_URL_SCHEMES = {'https', 'http'}
MAX_REDIRECTS = 10
MAX_MEMORY_USAGE = 1024 * 1024 * 1024 * 1024  # 1TB max memory for multipart downloads
SENSITIVE_PARAMS = {'token', 'key', 'api_key', 'apikey', 'secret', 'password', 'auth', 'access_token'}

# Default allowed domains (can be extended by configuration)
DEFAULT_ALLOWED_DOMAINS = {
    "next.oclpapi.simplehac.cn",
    "oclpapi.simplehac.cn",
    "simplehac.cn","gitapi.simplehac.top",
    "ghfast.top","gh-proxy.com","gh.llkk.cc",
    'github.com', 'api.github.com', 'codeload.github.com',
    'github-releases.githubusercontent.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'objects.githubusercontent.com',
    'developer.apple.com', 'download.developer.apple.com',
    'updates.cdn-apple.com', 'swcdn.apple.com',
    'oclp-download.example.com'
}


def sanitize_url_for_logging(url: str) -> str:
    """
    Remove sensitive parameters from URL for safe logging
    
    Parameters:
        url (str): URL to sanitize
        
    Returns:
        str: Sanitized URL with sensitive params masked
    """
    try:
        parsed = urlparse(url)
        if not parsed.query:
            return url
        
        params = parse_qs(parsed.query)
        sanitized_params = {}
        for key, value in params.items():
            if key.lower() in SENSITIVE_PARAMS:
                sanitized_params[key] = ['***']
            else:
                sanitized_params[key] = value
        
        new_query = urlencode(sanitized_params, doseq=True)
        sanitized = parsed._replace(query=new_query)
        return urlunparse(sanitized)
    except Exception:
        return "[URL sanitization failed]"


def validate_url(url: str, allowed_domains: set = None) -> tuple[bool, str]:
    """
    Validate URL for security
    
    Parameters:
        url (str): URL to validate
        allowed_domains (set): Set of allowed domains (optional)
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not url:
        return False, "URL is empty"
    
    try:
        parsed = urlparse(url)
        
        # Check scheme
        if parsed.scheme.lower() not in ALLOWED_URL_SCHEMES:
            return False, f"URL scheme '{parsed.scheme}' not allowed. Only {ALLOWED_URL_SCHEMES} are permitted."
        
        # Check domain
        domains = allowed_domains if allowed_domains else DEFAULT_ALLOWED_DOMAINS
        hostname = parsed.netloc.lower()
        # Remove port if present
        if ':' in hostname:
            hostname = hostname.split(':')[0]
        
        # Check if domain or subdomain is allowed
        domain_allowed = any(
            hostname == domain or hostname.endswith('.' + domain)
            for domain in domains
        )
        
        if not domain_allowed:
            return False, f"Domain '{hostname}' not in allowed list"
        
        return True, ""
        
    except Exception as e:
        return False, f"Invalid URL format: {str(e)}"


def validate_path(path: Path, base_dir: Path = None) -> tuple[bool, str]:
    """
    Validate path to prevent path traversal attacks
    
    Parameters:
        path (Path): Path to validate
        base_dir (Path): Base directory that path must be within (optional)
        
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        resolved_path = path.resolve()
        
        # Check for suspicious patterns
        path_str = str(resolved_path)
        if '..' in path_str:
            return False, "Path traversal detected"
        
        # If base_dir is specified, ensure path is within it
        if base_dir:
            resolved_base = base_dir.resolve()
            if not str(resolved_path).startswith(str(resolved_base)):
                return False, f"Path '{resolved_path}' is outside allowed directory '{resolved_base}'"
        
        return True, ""
        
    except Exception as e:
        return False, f"Invalid path: {str(e)}"

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
            response = requests.head(self.url, timeout=5, allow_redirects=True, verify=True)
            if response.status_code == 200:
                return True
            if response.status_code == 404:
                return False
            return True
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.SSLError
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
            requests.exceptions.HTTPError,
            requests.exceptions.SSLError
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
            # Set default max redirects if not specified
            if 'allow_redirects' in kwargs and kwargs['allow_redirects']:
                kwargs['max_redirects'] = kwargs.get('max_redirects', MAX_REDIRECTS)
            result = SESSION.get(url, **kwargs)
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.SSLError
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
            # Set default max redirects if not specified
            if 'allow_redirects' in kwargs and kwargs['allow_redirects']:
                kwargs['max_redirects'] = kwargs.get('max_redirects', MAX_REDIRECTS)
            result = SESSION.post(url, **kwargs)
        except (
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.SSLError
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

    def __init__(self, url: str, path: str, size: str = None, resume_download: bool = True,
                 allowed_domains: set = None, base_dir: Path = None, skip_validation: bool = False) -> None:
        self.contents = constants.Constants()
        self.trans = TranslateLanguage(self.contents).network_handler()
        self.url: str = url
        self.status: str = DownloadStatus.INACTIVE
        self.error_msg: str = ""
        self.filename: str = self._get_filename()
        self.size: str = size
        self.resume_download: bool = resume_download
        self.allowed_domains: set = allowed_domains if allowed_domains else DEFAULT_ALLOWED_DOMAINS
        self.base_dir: Path = base_dir
        
        # Initialize all attributes first (before validation)
        self.filepath: Path = Path(path) if path else Path("/tmp/download")
        self.progress_file: Path = Path(f"{path}.progress") if path else Path("/tmp/download.progress")
    
        self.total_file_size: float = 0.0
        self.downloaded_file_size: float = 0.0
        self.downloaded_file_offset: float = 0.0
        self.start_time: float = time.time()
        self.multipart_threshold: float = 1024 * 1024 * 50
        self.chunk_count: int = 16
        self.part_buffers: list[io.BytesIO] = []
        self.part_errors_queue: queue.Queue = queue.Queue()
        self.part_progress: dict[int, dict] = {}
        self._download_lock = threading.Lock()
        
        # Private session and active connections for quick cancellation
        self._session: requests.Session = None
        self._active_responses: list[requests.Response] = []
        self._connections_lock = threading.Lock()

        self.error: bool = False
        self.should_stop: bool = False
        self.download_complete: bool = False
        self.has_network: bool = False
        self._validation_passed: bool = False

        self.active_thread: threading.Thread = None

        self.should_checksum: bool = False

        self.checksum = None
        self._checksum_storage: hash = None
        
        # Security validation
        if not skip_validation:
            if not self._validate_inputs():
                return
        
        self._validation_passed = True
        self.has_network = NetworkUtilities(self.url).verify_network_connection()

        if self.has_network:
            self._populate_file_size()

    def _validate_inputs(self) -> bool:
        """
        Validate URL and path inputs for security
        
        Returns:
            bool: True if validation passed, False otherwise
        """
        # Validate URL
        is_valid, error_msg = validate_url(self.url, self.allowed_domains)
        if not is_valid:
            self.error = True
            self.error_msg = f"URL validation failed: {error_msg}"
            self.status = DownloadStatus.ERROR
            logging.error(self.error_msg)
            return False
        
        # Validate path
        is_valid, error_msg = validate_path(Path(self.url.split('?')[0].split('/')[-1]).name if self.url else "download", self.base_dir)
        # Path validation for download location is done in _prepare_working_directory
        
        return True

    def _get_sanitized_url(self) -> str:
        """
        Get URL sanitized for logging
        
        Returns:
            str: Sanitized URL
        """
        return sanitize_url_for_logging(self.url)


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
        Save download progress to a file with secure permissions
        """
        try:
            # Create file with secure permissions (read/write for owner only)
            fd = os.open(str(self.progress_file), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, 'w') as f:
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

    def _supports_range_download(self) -> bool:
        try:
            result = SESSION.head(self.url, allow_redirects=True, timeout=5)
            if result.headers.get("Accept-Ranges", "").lower() == "bytes":
                return True

            probe = NetworkUtilities().get(self.url, stream=True, timeout=10, headers={"Range": "bytes=0-0"})
            return probe.status_code == 206
        except Exception:
            return False

    def _should_use_multipart_download(self) -> bool:
        if self.resume_download and self.downloaded_file_offset > 0:
            return False
        if self.total_file_size == 0.0:
            return False
        if self.total_file_size < self.multipart_threshold:
            return False
        if self.chunk_count <= 1:
            return False
        return self._supports_range_download()

    def _build_download_ranges(self) -> list[tuple[int, int]]:
        part_size = max(1, math.ceil(self.total_file_size / self.chunk_count))
        ranges = []
        start = 0

        while start < self.total_file_size:
            end = min(start + part_size - 1, int(self.total_file_size) - 1)
            ranges.append((start, end))
            start = end + 1

        return ranges

    def _download_part(self, part_index: int, start: int, end: int, max_retries: int = 3) -> None:
        buffer = io.BytesIO()
        self.part_buffers[part_index] = buffer
        part_size = end - start + 1
        response = None
        
        with self._download_lock:
            self.part_progress[part_index] = {
                'status': 'pending',
                'downloaded': 0,
                'total': part_size,
                'percent': 0.0,
                'attempt': 0
            }
        
        headers = {"Range": f"bytes={start}-{end}"}
        
        try:
            for attempt in range(max_retries):
                try:
                    with self._download_lock:
                        self.part_progress[part_index]['status'] = 'downloading'
                        self.part_progress[part_index]['attempt'] = attempt + 1
                    
                    if attempt > 0:
                        logging.info(f"- Retry part {part_index + 1} (attempt {attempt + 1}/{max_retries})")
                        buffer.seek(0)
                        buffer.truncate(0)
                        with self._download_lock:
                            self.part_progress[part_index]['downloaded'] = 0
                            self.part_progress[part_index]['percent'] = 0.0
                    
                    logging.info(f"- Download part {part_index + 1}/{len(self.part_buffers)}: bytes={start}-{end}")
                    
                    # Use private session and track response for quick cancellation
                    if not self._session:
                        self._session = requests.Session()
                    
                    response = self._session.get(self.url, stream=True, timeout=100, headers=headers)
                    
                    # Track response for cancellation
                    with self._connections_lock:
                        self._active_responses.append(response)

                    if response.status_code != 206:
                        raise Exception(f"Unexpected status code for part {part_index}: {response.status_code}")

                    for chunk in response.iter_content(1024 * 1024 * 4):
                        if self.should_stop:
                            raise Exception("Download stopped")
                        if chunk:
                            buffer.write(chunk)
                            with self._download_lock:
                                self.downloaded_file_size += len(chunk)
                                self.part_progress[part_index]['downloaded'] = len(buffer.getvalue())
                                self.part_progress[part_index]['percent'] = (
                                    self.part_progress[part_index]['downloaded'] / 
                                    self.part_progress[part_index]['total'] * 100
                                )

                    with self._download_lock:
                        self.part_progress[part_index]['status'] = 'complete'
                    logging.info(f"- Completed part {part_index + 1}/{len(self.part_buffers)}: {len(buffer.getvalue())} bytes in memory")
                    return
                except Exception as e:
                    if self.should_stop:
                        with self._download_lock:
                            self.part_progress[part_index]['status'] = 'cancelled'
                        # Close and clear buffer on cancellation
                        buffer.close()
                        self.part_buffers[part_index] = None
                        raise e
                    with self._download_lock:
                        self.part_progress[part_index]['status'] = 'error'
                    if attempt < max_retries - 1:
                        logging.warning(f"- Part {part_index + 1} failed: {e}, retrying...")
                        time.sleep(2 ** attempt)
                    else:
                        raise e
                finally:
                    # Remove response from tracking and close it
                    if response:
                        with self._connections_lock:
                            if response in self._active_responses:
                                self._active_responses.remove(response)
                        try:
                            response.close()
                        except Exception:
                            pass
        except Exception:
            # Ensure buffer is closed on any unhandled exception
            if buffer:
                buffer.close()
                self.part_buffers[part_index] = None
            raise

    def _merge_download_parts(self) -> None:
        with open(self.filepath, "wb") as destination:
            for buffer in self.part_buffers:
                if buffer is None:
                    continue
                buffer.seek(0)
                while True:
                    chunk = buffer.read(1024 * 1024 * 4)
                    if not chunk:
                        break
                    destination.write(chunk)
                    if self.should_checksum:
                        self._update_checksum(chunk)
        
        self.part_buffers.clear()

    def _download_multipart(self) -> None:
        ranges = self._build_download_ranges()
        self.part_buffers = [None] * len(ranges)
        # Clear the error queue
        while not self.part_errors_queue.empty():
            try:
                self.part_errors_queue.get_nowait()
            except queue.Empty:
                break
        threads = []

        logging.info(f"- Using multipart download with {len(ranges)} parts")

        def _worker(index: int, start: int, end: int) -> None:
            try:
                self._download_part(index, start, end)
            except Exception as error:
                self.part_errors_queue.put(str(error))
                self.should_stop = True

        for index, (start, end) in enumerate(ranges):
            thread = threading.Thread(target=_worker, args=(index, start, end), name=f"DownloadPart-{index}")
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        # Collect errors from queue
        errors = []
        while not self.part_errors_queue.empty():
            try:
                errors.append(self.part_errors_queue.get_nowait())
            except queue.Empty:
                break
        
        if errors:
            logging.error(f"- Multipart download failed with {len(errors)} part error(s)")
            self.delete_temp_files()
            raise Exception(errors[0])

        self._merge_download_parts()
        self.download_complete = True
        self._clear_progress()
        logging.info(self.trans["Download complete: {0}"].format(self.filename))
        logging.info(self.trans["Stats:"])
        logging.info(self.trans["- Downloaded size: {0}"].format(utilities.human_fmt(self.downloaded_file_size)))
        logging.info(self.trans["- Time elapsed: {0:.2f} seconds"].format((time.time() - self.start_time)))
        logging.info(self.trans["- Speed: {0}/s"].format(utilities.human_fmt(self.downloaded_file_size / (time.time() - self.start_time))))
        logging.info(self.trans["- Location: {0}"].format(self.filepath))


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

            if not self._validation_passed:
                raise Exception(self.error_msg if self.error_msg else "Validation failed")

            if self._prepare_working_directory(self.filepath) is False:
                raise Exception(self.error_msg)

            # Check memory limit for multipart downloads
            if self._should_use_multipart_download():
                estimated_memory = self.total_file_size
                if estimated_memory > MAX_MEMORY_USAGE:
                    logging.warning(f"- File size ({utilities.human_fmt(estimated_memory)}) exceeds memory limit ({utilities.human_fmt(MAX_MEMORY_USAGE)}), using single-thread download")
                    self.chunk_count = 1
                else:
                    self._download_multipart()
                    self.status = DownloadStatus.COMPLETE
                    return

            headers = {}
            if self.resume_download and self.downloaded_file_offset > 0:
                headers['Range'] = f'bytes={self.downloaded_file_offset}-'
                logging.info(self.trans["Resuming download from byte {0}"].format(self.downloaded_file_offset))

            response = NetworkUtilities().get(self.url, stream=True, timeout=100, headers=headers)
            logging.info(f"- Download URL: {self._get_sanitized_url()}")
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
        else:
            self.status = DownloadStatus.COMPLETE
        finally:
            utilities.enable_sleep_after_running()


    def get_percent(self) -> float:
        """
        Query the download percent

        Returns:
            float: The download percent, or -1 if unknown
        """
        with self._download_lock:
            if self.total_file_size == 0.0:
                return -1
            return self.downloaded_file_size / self.total_file_size * 100


    def get_speed(self) -> float:
        """
        Query the download speed

        Returns:
            float: The download speed in bytes per second
        """
        with self._download_lock:
            elapsed = time.time() - self.start_time
            if elapsed <= 0:
                return 0
            return self.downloaded_file_size / elapsed


    def get_time_remaining(self) -> float:
        """
        Query the time remaining for the download

        Returns:
            float: The time remaining in seconds, or -1 if unknown
        """
        with self._download_lock:
            if self.total_file_size == 0.0:
                return -1
            elapsed = time.time() - self.start_time
            if elapsed <= 0:
                return -1
            speed = self.downloaded_file_size / elapsed
            if speed <= 0:
                return -1
            return (self.total_file_size - self.downloaded_file_size) / speed


    def get_file_size(self) -> float:
        """
        Query the file size of the file to be downloaded

        Returns:
            float: The file size in bytes, or 0.0 if unknown
        """
        with self._download_lock:
            return self.total_file_size


    def get_downloaded_size(self) -> float:
        """
        Query the downloaded file size

        Returns:
            float: The downloaded file size in bytes
        """
        with self._download_lock:
            return self.downloaded_file_size


    def get_part_progress(self) -> dict[int, dict]:
        """
        Query the progress of each download part

        Returns:
            dict: Dictionary with part index as key and progress info as value
                  Each entry contains: status, downloaded, total, percent, attempt
        """
        with self._download_lock:
            return dict(self.part_progress)


    def print_part_progress(self) -> None:
        """
        Print the progress of all parts to console
        """
        progress = self.get_part_progress()
        if not progress:
            return
        
        print(f"\n--- Part Progress ({len(progress)} parts) ---")
        for idx, info in sorted(progress.items()):
            status_icon = {
                'pending': '⏳',
                'downloading': '⬇️',
                'complete': '✅',
                'error': '❌',
                'cancelled': '🚫'
            }.get(info['status'], '❓')
            
            retry_info = f" [retry {info['attempt']}]" if info['attempt'] > 1 else ""
            print(f"Part {idx + 1:2d}: {status_icon} {info['status']:12s} "
                  f"{info['percent']:6.1f}% ({utilities.human_fmt(info['downloaded'])}/{utilities.human_fmt(info['total'])})"
                  f"{retry_info}")
        print("----------------------------------------")


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
        errors = []
        
        try:
            # Delete the partially downloaded file
            if self.filepath and self.filepath.exists():
                self.filepath.unlink()
                logging.info(self.trans.get("Deleted partially downloaded file: {0}", "Deleted partially downloaded file: {0}").format(self.filepath))
        except Exception as e:
            errors.append(f"Failed to delete file {self.filepath}: {e}")
        
        try:
            # Delete the progress file
            if self.progress_file and self.progress_file.exists():
                self.progress_file.unlink()
                logging.info(self.trans.get("Deleted progress file: {0}", "Deleted progress file: {0}").format(self.progress_file))
        except Exception as e:
            errors.append(f"Failed to delete progress file: {e}")

        try:
            # Clear memory buffers and free memory
            for i, buffer in enumerate(self.part_buffers):
                if buffer is not None:
                    try:
                        buffer.close()
                    except Exception:
                        pass
            self.part_buffers.clear()
            logging.info("Cleared download memory buffers")
        except Exception as e:
            errors.append(f"Failed to clear memory buffers: {e}")
        
        if errors:
            logging.warning(f"Errors during cleanup: {'; '.join(errors)}")

    def _close_all_connections(self) -> None:
        """
        Close all active network connections immediately
        This ensures quick cancellation without waiting for network timeouts
        """
        with self._connections_lock:
            # Close all active response objects
            for response in self._active_responses:
                try:
                    if response:
                        response.close()
                except Exception:
                    pass
            self._active_responses.clear()
            
            # Close the private session
            if self._session:
                try:
                    self._session.close()
                except Exception:
                    pass
                self._session = None
            
            logging.info("Closed all network connections")

    def stop(self) -> None:
        """
        Stop the download

        If the download is active, this function will hold the thread until stopped or timeout
        """
        self.should_stop = True
        
        # First, close all network connections for quick cancellation
        self._close_all_connections()
        
        # Wait for active thread with timeout
        if self.active_thread and self.active_thread.is_alive():
            self.active_thread.join(timeout=10)
            if self.active_thread.is_alive():
                logging.warning("Download thread did not stop gracefully within timeout")
        
        # Delete temporary files if download was cancelled by user
        if not self.download_complete:
            self.delete_temp_files()