"""Centralized logging configuration for NetworkGPT."""

import sys

from loguru import logger

logger.remove()

#custom console logger

logger.add(
    sys.stdout,
    level="INFO",
    format = "{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
    colorize = "true"
)