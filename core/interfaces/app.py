"""Module containing the abstract base class for app providers."""

from abc import abstractmethod

from core.enums import Result
from core.interfaces import Provider


class AppProvider(Provider):
    """Abstract base class for app providers."""

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
