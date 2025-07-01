"""This module defines the interface for hook providers."""

from abc import abstractmethod

from core.enums import Result
from core.interfaces.base import Provider


class HookProvider(Provider):
    """Abstract base class for hook providers."""

    @abstractmethod
    def execute(self) -> Result:
        """Execute any custom or one-off task such as setup, configuration,
        validation, or other actions defined by the specific hook implementation.

        Returns:
            Result: The result of the execution.
        """
        ...
