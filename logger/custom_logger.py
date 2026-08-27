"""Logging helper used throughout the document-processing pipeline."""

import json
import logging
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIRECTORY = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIRECTORY / "document_portal.log"


class StructuredLogger:
    """Expose an event-and-context logging interface backed by ``logging``."""

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def _log(self, level: int, event: str, **context: Any) -> None:
        message = event
        if context:
            message = f"{event} | {json.dumps(context, default=str)}"
        self._logger.log(level, message)

    def info(self, event: str, **context: Any) -> None:
        self._log(logging.INFO, event, **context)

    def warning(self, event: str, **context: Any) -> None:
        self._log(logging.WARNING, event, **context)

    def exception(self, event: str, **context: Any) -> None:
        message = event
        if context:
            message = f"{event} | {json.dumps(context, default=str)}"
        self._logger.exception(message)


class CustomLogger:
    """Create configured loggers compatible with structured parser events."""

    def get_logger(self, name: str) -> StructuredLogger:
        logger = logging.getLogger(name)

        if not logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            logger.setLevel(logging.INFO)
            logger.propagate = False

        return StructuredLogger(logger)
