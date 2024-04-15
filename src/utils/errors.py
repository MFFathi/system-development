# Author: Mohamed Elafifi (22066939)
"""Module with all exceptions in."""


class HorizonError(Exception):
    """Base class for all horizon restaurant errors."""

    def __init__(self, message: str) -> None:
        """Create error message."""
        self.message = message


class AlreadyExistsError(HorizonError):
    """Error for when a unique item already exists in the database."""


class AuthenticationError(HorizonError):
    """Error for when a user dosen't have permission to do something."""


class AuthorizationError(HorizonError):
    """Error for when a user has incorrect credentials to login."""


class InputError(HorizonError):
    """
    Error for when an invalid input is provided.

    E.g. it dosen't fit validation rules
    """