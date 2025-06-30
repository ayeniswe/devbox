"""
This module defines the abstract base class for service providers.
"""
from abc import abstractmethod

from core.enums import Result
from core.interfaces.base import Provider


class ServiceProvider(Provider):

    @abstractmethod
    def setup(self) -> Result:
        """
        Perform the setup of the service.

        Returns:
            Result: The result of the setup operation.
        """
        ...

    @abstractmethod
    def start(self) -> Result:
        """
        Start the service.

        Returns:
            Result: The result of the start operation.
        """
        ...
