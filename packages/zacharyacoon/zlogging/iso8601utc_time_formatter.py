from logging import Formatter
from datetime import datetime
from .default import date_format


class ISO8601UTCTimeFormatter(Formatter):
    def formatTime(self, record, datefmt=None):
        current_time = datetime.fromtimestamp(record.created)
        current_time = current_time.astimezone(datetime.now().astimezone().tzinfo)
        if not datefmt:
            datefmt = date_format
        return current_time.strftime(datefmt)
