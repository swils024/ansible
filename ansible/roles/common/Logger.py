'''
Custom logger class

The Logger class is initialized with several parameters:
1. filename: The name of the log file where the logs will be saved.
2. level: The logging level, which determines the severity of the messages to be logged (e.g., 'debug', 'info', 'warning', 'error', 'crit').
3. when: The interval at which the log files should be rotated (e.g., 'S' for seconds, 'M' for minutes, 'H' for hours, 'D' for days, 'W' for weeks).
4. backCount: The number of backup log files to retain.
5. fmt: The format of the log messages, which includes the time, file path, line number, log level, and the log message itself.

Usage example

from Logger import Logger

log = Logger('log\\all.log', level='debug')
log_error = Logger('log\\all.log', level='debug')
log.logger.info("This is an info message)")
log_error.info("This is an error message")

'''
import logging
from logging import handlers

class Logger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "crit": logging.CRITICAL
    }  # relationship mapping

    def __init__(self, filename, level='info', when='m', backCount=1,
                 fmt='%(asctime)s.%(msecs)03d [%(module)s] %(levelname)s: %(message)s',datefmt="%Y-%m-%d %H:%M:%S"):
        self.logger = logging.getLogger(filename)

        # Setting the log format
        format_str = logging.Formatter(fmt,datefmt)

        # Setting the log level
        self.logger.setLevel(self.level_relations.get(level))

        # on-screen output
        console_handler = logging.StreamHandler()

        # Setting the format
        console_handler.setFormatter(format_str)

        # automatically generates the file at specified intervals
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,encoding="utf-8")

         # Setting the format
        th.setFormatter(format_str)

        # Add the object to the logger
        self.logger.addHandler(th)
