import os

import loguru


def get_logger() -> loguru.logger:
    """
    Get the loguru logger for the application.

    Returns:
        logger: The loguru logger for the application.
    """
    loguru.logger.add("logs/app.log", rotation="500 MB")
    loguru.logger.info(f"Environment: {os.getenv('ENV', 'dev')}")
    return loguru.logger


logger = get_logger()
