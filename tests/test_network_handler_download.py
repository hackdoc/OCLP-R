import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from oclp_r.support.network_handler import DownloadObject, DownloadStatus


class DownloadObjectStatusTests(unittest.TestCase):
    def test_multipart_download_marks_status_complete(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "demo.bin"

            with patch("oclp_r.support.network_handler.NetworkUtilities.verify_network_connection", return_value=True), \
                 patch.object(DownloadObject, "_populate_file_size", lambda self: setattr(self, "total_file_size", 1024)), \
                 patch("oclp_r.support.network_handler.utilities.disable_sleep_while_running", lambda: None), \
                 patch("oclp_r.support.network_handler.utilities.enable_sleep_after_running", lambda: None):
                download = DownloadObject("https://example.com/demo.bin", str(target))
                download._prepare_working_directory = lambda path: True
                download._should_use_multipart_download = lambda: True

                def fake_multipart_download():
                    download.download_complete = True

                download._download_multipart = fake_multipart_download

                download.download(spawn_thread=False)

            self.assertTrue(download.download_complete)
            self.assertEqual(download.status, DownloadStatus.COMPLETE)
            self.assertFalse(download.is_active())


if __name__ == "__main__":
    unittest.main()
