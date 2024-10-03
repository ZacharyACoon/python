from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable
from .iso8601utc_time_formatter import ISO8601UTCTimeFormatter
from .configure_loggers import configure_loggers
from .log_file_handlers import generate_log_file_handlers
from .stdout_stderr_handlers import generate_stdout_stderr_handlers


date_format = "%Y%m%dT%H%M%S.%f%z"
log_format = "%(name)s, %(asctime)s, %(levelname)s, %(filename)s:%(lineno)s, %(message)s"
formatter = ISO8601UTCTimeFormatter(fmt=log_format, datefmt=date_format)
