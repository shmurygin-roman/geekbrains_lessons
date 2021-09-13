"""Декораторы"""

import sys
import logging
import traceback
import inspect
from config import config_client_log, config_server_log


if sys.argv[0].find('client.py') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        LOGGER.debug(f'Вызвана функция {func.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func.__module__}. '
                     f'Ver.1.Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Ver.2.Вызов из функции {inspect.stack()[1][3]}.', stacklevel=2)
        return return_value
    return wrapper
