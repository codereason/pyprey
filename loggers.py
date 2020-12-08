import logging
from logging.handlers import TimedRotatingFileHandler

from config.config import cf


def build_timed_logger(name: str,filename: str):
    '''
    Returns a logger that creates appends a new log file daily
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    # if not settings.testing:
    log_path = cf.get_configs().get("logger")['log_path']
    path = f"{log_path}/{filename}"
    handler = TimedRotatingFileHandler(path, when="d", interval=1, utc=True)
    logger.addHandler(handler)
    return logger
