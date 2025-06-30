"""
App Name: VSCode

Description:
Visual Studio Code (VSCode) is a powerful, extensible code editor developed by Microsoft.
This app module is responsible for automating the deployment and lifecycle management
(install, start, stop) of VSCode within the DevBox environment.
"""

import requests

from core.enums import Result
from core.interfaces import AppProvider


class VSCode(AppProvider):

    def install(self, offline=False) -> Result:
        if not offline:
            requests.get()
        return

    def start(self) -> None:
        ...

    def stop(self) -> None:
        """
        Stop or shut down the app.
        """
        ...
