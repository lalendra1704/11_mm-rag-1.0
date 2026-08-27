"""Project-specific exception types."""

from __future__ import annotations

from typing import Optional


class DocumentPortalException(Exception):
    """Wrap an underlying error raised while processing a document."""

    def __init__(self, message: str, error: Optional[Exception] = None) -> None:
        self.message = message
        self.error = error
        super().__init__(message if error is None else f"{message}: {error}")
