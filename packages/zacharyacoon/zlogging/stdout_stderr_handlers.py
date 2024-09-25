import logging
from sys import stdout, stderr


class ExceptionTracebackSquasherFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formatException(self, ei):
        return ''


class StdOutErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.WARNING


def generate_stdout_stderr_handlers(
    formatter: logging.Formatter,
):
    stdout_handler = logging.StreamHandler(stdout)
    stdout_handler.setFormatter(formatter)
    # supress errors to stdout, as they'll go to stderr
    stdout_handler.addFilter(StdOutErrorFilter())

    stderr_handler = logging.StreamHandler(stderr)
    stderr_handler.setFormatter(formatter)
    stderr_handler.setLevel(logging.ERROR)

    return stdout_handler, stderr_handler
