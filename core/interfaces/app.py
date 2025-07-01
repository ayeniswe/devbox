"""Module containing the abstract base class for app providers."""

from abc import abstractmethod

from core.enums import Result
from core.interfaces.base import Provider
import requests
import logging

logger = logging.getLogger(__name__)


class AppProvider(Provider):
    """Abstract base class for app providers."""

    def _download(self, url: str) -> Result:
        """Download artifact from url"""
        try:
            logger.info(f"Starting download of {self.name} from {url}")
            with requests.get(url, stream=True) as stream:
                stream.raise_for_status()
                with open(f"{self.name}", "wb") as f:
                    for chunk in stream.iter_content(1024):
                        if chunk:
                            f.write(chunk)
                            logger.debug("Received a chunk of size %d bytes",
                                         len(chunk))
            logger.info(f"{self.name} download complete.")
        except Exception as e:
            logger.error(f"Download failed: {e}")

    @abstractmethod
    def install(self) -> Result:
        """
        Install or set up the app.

        Returns:
            Result: The result of the installation process.
        """
        ...

    @abstractmethod
    def start(self) -> None:
        """
        Start or launch the app.
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Stop or shut down the app.
        """
        ...
