from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable

import logging


date_format = "%Y%m%dT%H%M%S.%f%z"
log_format = "%(name)s, %(asctime)s, %(levelname)s, %(filename)s:%(lineno)s, %(message)s"


def configure_loggers(
    logger_names: Iterable[str],
    handlers: Iterable[logging.Handler],
    log_level: int = logging.INFO,
):
    for logger_name in logger_names:
        logger = logging.getLogger(logger_name)
        logger.handlers = handlers
        logger.propagate = False
        logger.setLevel(log_level)
