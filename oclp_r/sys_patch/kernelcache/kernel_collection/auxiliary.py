"""
auxiliary.py: Auxiliary Kernel Collection management
"""

import logging
import subprocess

from ..base.cache import BaseKernelCache
from ....support  import subprocess_wrapper
from ....support import translate_language


class AuxiliaryKernelCollection(BaseKernelCache):

    def __init__(self, mount_location: str, global_constants=None) -> None:
        self.mount_location = mount_location
        self.global_constants = global_constants
        if global_constants:
            self.trans = translate_language.TranslateLanguage_sys_patch(global_constants).kernelcache()
        else:
            self.trans = None


    def _kmutil_arguments(self) -> list[str]:
        args = ["/usr/bin/kmutil", "create", "--allow-missing-kdk"]

        args.append("--new")
        args.append("aux")

        args.append("--boot-path")
        args.append(f"{self.mount_location}/System/Library/KernelCollections/BootKernelExtensions.kc")

        args.append("--system-path")
        args.append(f"{self.mount_location}/System/Library/KernelCollections/SystemKernelExtensions.kc")

        return args


    def _force_auxiliary_usage(self) -> bool:
        """
        Force the auxiliary kernel collection to be used.

        This is required as Apple doesn't offer a public way
        to rebuild the auxiliary kernel collection. Instead deleting
        necessary files and directories will force the newly built
        collection to be used.
        """

        if self.trans:
            logging.info(self.trans["- Forcing Auxiliary Kernel Collection usage"])
        else:
            logging.info("- Forcing Auxiliary Kernel Collection usage")
        result = subprocess_wrapper.run_as_root(["/usr/bin/killall", "syspolicyd", "kernelmanagerd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            if self.trans:
                logging.info(self.trans["- Unable to kill syspolicyd and kernelmanagerd"])
            else:
                logging.info("- Unable to kill syspolicyd and kernelmanagerd")
            subprocess_wrapper.log(result)
            return False

        for file in ["KextPolicy", "KextPolicy-shm", "KextPolicy-wal"]:
            result = subprocess_wrapper.run_as_root(["/bin/rm", f"/private/var/db/SystemPolicyConfiguration/{file}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode != 0:
                if self.trans:
                    logging.info(self.trans["- Unable to remove {file}"].format(file=file))
                else:
                    logging.info(f"- Unable to remove {file}")
                subprocess_wrapper.log(result)
                return False

        return True


    def rebuild(self) -> None:
        if self.trans:
            logging.info(self.trans["- Building new Auxiliary Kernel Collection"])
        else:
            logging.info("- Building new Auxiliary Kernel Collection")
        result = subprocess_wrapper.run_as_root(self._kmutil_arguments(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            if self.trans:
                logging.info(self.trans["- Unable to build Auxiliary Kernel Collection"])
            else:
                logging.info("- Unable to build Auxiliary Kernel Collection")
            subprocess_wrapper.log(result)
            return False

        if self._force_auxiliary_usage() is False:
            return False

        return True

