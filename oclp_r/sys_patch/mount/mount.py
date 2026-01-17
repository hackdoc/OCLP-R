"""
mount.py: Handling macOS root volume mounting and unmounting
"""

import logging
import plistlib
import subprocess

from pathlib import Path

from .snapshot import APFSSnapshot

from ...datasets import os_data
from ...support  import subprocess_wrapper
from ...support import translate_language


class RootVolumeMount:

    def __init__(self, xnu_major: int, global_constants=None) -> None:
        self.xnu_major = xnu_major
        self.root_volume_identifier = self._fetch_root_volume_identifier()
        self.global_constants = global_constants
        
        if global_constants:
            self.trans = translate_language.TranslateLanguage_sys_patch(global_constants).mount()
        else:
            self.trans = None

        self.mount_path = None


    def _fetch_root_volume_identifier(self) -> str:
        """
        Resolve path to disk identifier

        ex. / -> disk1s1
        """
        try:
            content = plistlib.loads(subprocess.run(["/usr/sbin/diskutil", "info", "-plist", "/"], capture_output=True).stdout)
        except plistlib.InvalidFileException:
            if self.trans:
                raise RuntimeError(self.trans["Failed to parse diskutil output."])
            else:
                raise RuntimeError("Failed to parse diskutil output.")

        disk = content["DeviceIdentifier"]

        if "APFSSnapshot" in content and content["APFSSnapshot"] is True:
            # Remove snapshot suffix (last 2 characters)
            # ex. disk1s1s1 -> disk1s1
            disk = disk[:-2]

        return disk


    def _mount_root_volume(self) -> str | None:
        """
        Mount the root volume.

        Returns the path to the root volume.
        """
        # Root volume same as data volume
        if self.xnu_major < os_data.os_data.catalina.value:
            return "/"

        # Catalina implemented a read-only root volume
        if self.xnu_major == os_data.os_data.catalina.value:
            result = subprocess_wrapper.run_as_root(["/sbin/mount", "-uw", "/"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode != 0:
                if self.trans:
                    logging.error(self.trans["Failed to mount root volume"])
                else:
                    logging.error("Failed to mount root volume")
                subprocess_wrapper.log(result)
                return None
            return "/"

        # Big Sur and newer implemented APFS snapshots for the root volume
        if self.xnu_major >= os_data.os_data.big_sur.value:
            if Path("/System/Volumes/Update/mnt1/System/Library/CoreServices/SystemVersion.plist").exists():
                return "/System/Volumes/Update/mnt1"
            
            result_unmount = subprocess_wrapper.run_as_root(["/usr/sbin/diskutil", "unmount", f"/dev/{self.root_volume_identifier}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)            
            if result_unmount.returncode != 0:
                if self.trans:
                    logging.info(self.trans["{root_volume_identifier} has already been unmounted."].format(root_volume_identifier=self.root_volume_identifier))
                else:
                    logging.info(f"{self.root_volume_identifier} has already been unmounted.")

            result = subprocess_wrapper.run_as_root(["/sbin/mount", "-o", "nobrowse", "-t", "apfs", f"/dev/{self.root_volume_identifier}", "/System/Volumes/Update/mnt1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode != 0:
                if self.trans:
                    logging.error(self.trans["Failed to mount root volume"])
                else:
                    logging.error("Failed to mount root volume")
                subprocess_wrapper.log(result)
                return None
            return "/System/Volumes/Update/mnt1"
        return None


    def _unmount_root_volume(self, ignore_errors: bool = True) -> bool:
        """
        Unmount the root volume.
        """
        if self.xnu_major < os_data.os_data.catalina.value:
            return True

        args = ["/sbin/umount"]

        if self.xnu_major == os_data.os_data.catalina.value:
            args += ["-uw", self.mount_path]

        if self.xnu_major >= os_data.os_data.big_sur.value:
            args += [self.mount_path]

        result = subprocess_wrapper.run_as_root(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            if ignore_errors is False:
                if self.trans:
                    logging.error(self.trans["Failed to unmount root volume"])
                else:
                    logging.error("Failed to unmount root volume")
                subprocess_wrapper.log(result)
            return False

        return True


    def mount(self) -> str | None:
        """
        Mount the root volume.

        Returns the path to the root volume.

        If none, failed to mount.
        """
        result = self._mount_root_volume()
        if result is None:
            if self.trans:
                logging.error(self.trans["Failed to mount root volume"])
            else:
                logging.error("Failed to mount root volume")
            return None
        if not Path(result).exists():
            if self.trans:
                logging.error(self.trans["Attempted to mount root volume, but failed: {result}"].format(result=result))
            else:
                logging.error(f"Attempted to mount root volume, but failed: {result}")
            return None

        self.mount_path = result

        return result


    def unmount(self, ignore_errors: bool = True) -> bool:
        """
        Unmount the root volume.

        Returns True if successful, False otherwise.

        Note for Big Sur and newer, a snapshot is created before unmounting.
        And that unmounting is not critical to the process.
        """
        return self._unmount_root_volume(ignore_errors=ignore_errors)


    def create_snapshot(self) -> bool:
        """
        Create APFS snapshot of the root volume.
        """
        if self.mount_path is None:
            return False
        return APFSSnapshot(self.xnu_major, self.mount_path, self.global_constants).create_snapshot()


    def revert_snapshot(self) -> bool:
        """
        Revert APFS snapshot of the root volume.
        """
        if self.mount_path is None:
            return False
        return APFSSnapshot(self.xnu_major, self.mount_path, self.global_constants).revert_snapshot()