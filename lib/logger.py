import logging
import inspect
import sys


class Logger(object):
    def __init__(self):
        self.FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
        self.config = logging.basicConfig(
            filename=None,
            level=logging.INFO,
            format=self.FORMAT)

    @staticmethod
    def logger(level, *msg):
        """
        :param level: logs level - string - can be: 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
        :param msg: your logs
        """
        if len(msg) == 1:
            msg = msg[0]
        level = level.upper()
        if level == 'INFO':
            logging.info(msg)
        elif level == 'DEBUG':
            logging.debug(msg)
        elif level == 'WARNING':
            logging.warning(msg)
        elif level == 'ERROR':
            logging.error(msg)
        elif level == 'CRITICAL':
            logging.critical(msg)
        else:
            raise ValueError(F'Unknown log level {msg}, available: INFO, WARNING, DEBUG, ERROR, CRITICAL')


def whoami():
    """
    prints current function name in runtime
    """
    name = inspect.stack()[1][3]
    print('-' * 42 + '-' * len(name), file=sys.stderr)
    print('*' * 20, name, '*' * 20, file=sys.stderr)
    print('-' * 42 + '-' * len(name), file=sys.stderr)
    Logger.logger('INFO', name)
