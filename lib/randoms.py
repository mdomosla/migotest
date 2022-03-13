import random
import string
from lib.logger import Logger

log = Logger()


def random_string(length, upper=True):
    """ Generates random string with only ascii letters
    :param length: string len
    :param upper: default True, set False if you want have string in lowercase format
    :return: string
    """
    if upper:
        word = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    else:
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    log.logger('DEBUG', F'random string {word} generated')
    return word


def random_digits(length):
    """ Generates random string with digits only. If string start with 0, 0 is removed.
    :param length: string length
    :return: string
    """
    word = ''.join(random.choice(string.digits) for _ in range(length))
    log.logger('DEBUG', F'random string digits {word} generated')
    if word.startswith('0'):
        word = word.replace('0', '1')
    return word


def random_chars_digits(length, upper=True):
    """ Generates random string with letters and digits
    :param length: string length
    :param upper: default True, set False if you want have lowercase format
    :return: string
    """
    if upper:
        word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    else:
        word = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    log.logger('DEBUG', F'random string with letters and digits generated: {word}')
    return word


def get_date_without_space():
    """
    Generates string with current date and time in format YearMonthDayHourMinuteSecondsMilliseconds
    :return: string
    """
    data_print = datetime.now()
    data_formatted = str(data_print.strftime('%Y%m%d%H%M%S%f'))
    return data_formatted