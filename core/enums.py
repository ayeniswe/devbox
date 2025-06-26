"""This module contains enumeration classes used throughout the DevBox system
to standardize"""

from enum import Enum

class Result(Enum):
    """Enumeration for arbitrary results."""
    SUCCESS = 0
    WARNING = 1
    FAILURE = 2
