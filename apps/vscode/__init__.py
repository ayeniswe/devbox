"""
App Name: VSCode

Description:
Visual Studio Code (VSCode) is a powerful, extensible code editor developed by Microsoft.
This app module is responsible for automating the deployment and lifecycle management
(install, start, stop) of VSCode within the DevBox environment.
"""

from common.mac.path import APPLICATIONS_PATH
from core.context import Os
from core.enums import Result
from core.interfaces import AppProvider
import logging

logger = logging.getLogger(__name__)


class VSCode(AppProvider):

    def __init__(self, ctx):
        super().__init__(ctx, __class__.__name__)

    def install(self) -> Result:
        import zipfile
        if self.ctx.online:
            os = self.ctx.platform.os
            url = f"https://code.visualstudio.com/sha/download?build=stable&os={os}-{self.ctx.platform.arch}"
            self._download(url)
            match os:
                case Os.WINDOWS:
                    # TODO add support Windows
                    ...
                case Os.MAC:
                    with zipfile.ZipFile(__class__.__name__, "r") as f:
                        f.extractall(APPLICATIONS_PATH)
                case Os.LINUX:
                    # TODO add support Linux
                    ...
        else:
            logger.error("No support for offline install")

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    def exists(self):
        ...


__all__ = ['VSCode']
