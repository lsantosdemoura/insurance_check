import logging
import logging.config

from src import settings

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "correlated": {
            "()": "uvicorn.logging.DefaultFormatter",
            "format": "%(levelprefix)s [%(name)s:%(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "correlated",
        },
    },
    "root": {"level": settings.LOG_LEVEL, "handlers": ["console"]},
}

logging.config.dictConfig(LOGGING_CONFIG)
