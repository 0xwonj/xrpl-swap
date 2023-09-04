from loguru import logger


def get_logger(env: str) -> logger:
    logger.add("logs/app.log", rotation="500 MB")
    logger.info(f"Environment: {env}")
    return logger
