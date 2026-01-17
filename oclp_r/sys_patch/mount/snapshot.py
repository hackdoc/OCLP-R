"""
snapshot.py: Handling APFS snapshots
"""

import logging
import platform
import subprocess

from ...datasets import os_data
from ...support  import subprocess_wrapper
from ...support import translate_language


class APFSSnapshot:

    def __init__(self, xnu_major: int, mount_path: str, global_constants=None):
        self.xnu_major = xnu_major
        self.mount_path = mount_path
        self.global_constants = global_constants
        
        if global_constants:
            self.trans = translate_language.TranslateLanguage_sys_patch(global_constants).mount()
        else:
            self.trans = None


    def _rosetta_status(self) -> bool:
        """
        Check if currently running inside of Rosetta
        """
        result = subprocess_wrapper.run(["/usr/sbin/sysctl", "-n", "sysctl.proc_translated"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            return False

        return True if result.stdout.decode().strip() == "1" else False


    def create_snapshot(self) -> bool:
        """
        Create APFS snapshot of the root volume.
        """
        if self.xnu_major < os_data.os_data.big_sur.value:
            return True

        args = ["/usr/sbin/bless"]
        if platform.machine() == "arm64" or self._rosetta_status() is True:
            args += ["--mount", self.mount_path, "--create-snapshot"]
        else:
            args += ["--folder", f"{self.mount_path}/System/Library/CoreServices", "--bootefi", "--create-snapshot"]

        result = subprocess_wrapper.run_as_root(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            if self.trans:
                logging.error(self.trans["Failed to create APFS snapshot"])
            else:
                logging.error("Failed to create APFS snapshot")
            subprocess_wrapper.log(result)
            if "Can't use last-sealed-snapshot or create-snapshot on non system volume" in result.stdout.decode():
                if self.trans:
                    logging.info(self.trans["- This is an APFS bug with Monterey and newer! Perform a clean installation to ensure your APFS volume is built correctly"])
                else:
                    logging.info("- This is an APFS bug with Monterey and newer! Perform a clean installation to ensure your APFS volume is built correctly")

            return False

        return True


    def revert_snapshot(self) -> bool:
        """
        Revert APFS snapshot of the root volume.
        """
        if self.xnu_major < os_data.os_data.big_sur.value:
            return True

        result = subprocess_wrapper.run_as_root(["/usr/sbin/bless", "--mount", self.mount_path, "--bootefi", "--last-sealed-snapshot"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            if self.trans:
                logging.error(self.trans["Failed to revert APFS snapshot"])
            else:
                logging.error("Failed to revert APFS snapshot")
            subprocess_wrapper.log(result)
            return False

        return True