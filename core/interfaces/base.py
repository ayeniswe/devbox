"""Defines the abstract base Provider interface used by all provider types in the DevBox system.

This module provides the foundational abstract base class, `Provider`, which specifies the
interface that all provider implementations must adhere to within the DevBox system.
"""
from abc import ABC, abstractmethod

class Provider(ABC):
    """
    Abstract base class for providers.

    Defines the interface that all provider implementations must follow.
    """

    def __init__(self, name=None):
        """
        Initialize the provider with an optional name or identifier.

        Args:
            name (str, optional): Name or identifier for the provider.
        """
        self.name = name

    @abstractmethod
    def exists(self) -> bool:
        """
        Check if the provider exists.

        Returns:
            bool: True if the provider exists, False otherwise.
        """
        ...