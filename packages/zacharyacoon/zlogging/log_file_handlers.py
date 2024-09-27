from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Union, Generator
    from pathlib import Path

import logging.handlers


def generate_log_file_handlers(
    formatter: logging.Formatter,
    log_file_path: Union[Path, str],
    log_retention_days: Union[int, None] = None,
) -> Generator[logging.Handler]:
    """
    Generate handlers to log to files in the log directory.
    If log_retention_days, the file is rotated at midnight and that many days is kept.

    :param formatter: The log formatter to apply.
    :param log_file_path: The path and name to keep logs.
    :param log_retention_days: The number of days to keep logs
    :returns handlers: An iterable of
    """

    if log_file_path:
        log_file_path = Path(log_file_path)
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        if log_retention_days:
            daily_log_file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=log_file_path,
                when="midnight",
                backupCount=log_retention_days,
            )
            daily_log_file_handler.formatter = formatter
            yield daily_log_file_handler

        else:
            file_handler = logging.handlers.WatchedFileHandler(filename=log_file_path)
            file_handler.formatter = formatter
            yield file_handler
