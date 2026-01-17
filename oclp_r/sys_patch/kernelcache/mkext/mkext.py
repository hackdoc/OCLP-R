"""
mkext.py: MKext cache management
"""

import logging
import subprocess

from ..base.cache import BaseKernelCache
from ....support  import subprocess_wrapper
from ....support import translate_language


class MKext(BaseKernelCache):

    def __init__(self, mount_location: str, global_constants=None) -> None:
        self.mount_location = mount_location
        self.global_constants = global_constants
        if global_constants:
            self.trans = translate_language.TranslateLanguage_sys_patch(global_constants).kernelcache()
        else:
            self.trans = None


    def _mkext_arguments(self) -> list[str]:
        args = ["/usr/bin/touch", f"{self.mount_location}/System/Library/Extensions"]
        return args


    def rebuild(self) -> None:
        if self.trans:
            logging.info(self.trans["- Rebuilding MKext cache"])
        else:
            logging.info("- Rebuilding MKext cache")
        result = subprocess_wrapper.run_as_root(self._mkext_arguments(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        if result.returncode != 0:
            subprocess_wrapper.log(result)
            return False

        return True