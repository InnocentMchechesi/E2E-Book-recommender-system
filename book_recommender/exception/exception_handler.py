import sys
from types import ModuleType
from typing import Optional


class AppException(Exception):
    """
    AppException is a custom exception that captures file name and line number
    from the active traceback, along with the original error message.
    """

    def __init__(self, error_message: Exception, error_detail: Optional[ModuleType] = None) -> None:
        """
        error_message: the original Exception object (e.g., from `except Exception as e`)
        error_detail: a module that provides exc_info(); defaults to `sys`
        """
        super().__init__(error_message)
        if error_detail is None:
            error_detail = sys
        self.error_message = self.get_detailed_error_message(
            error_message=error_message, error_detail=error_detail
        )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: ModuleType) -> str:
        """
        Build a detailed message including file name and line number.
        Safe if called when no active exception exists.
        """
        _, _, exc_tb = error_detail.exc_info()
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error in {file_name} at line {line_number}: {error_message}"
        # Fallback when no traceback is available (e.g., raised outside `except`)
        return f"{error_message}"

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        # Standard, unambiguous representation
        return f"{self.__class__.__name__}({self.error_message!r})"
