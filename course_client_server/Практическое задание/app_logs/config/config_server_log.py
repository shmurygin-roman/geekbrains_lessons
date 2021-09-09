"""Конфиг логгера для сервера"""

import logging.handlers
import os
from pathlib import Path

FORMATTER = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s ")

FULL_PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(str(Path(FULL_PATH).parents[0]), 'logs\server.log')

FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='midnight')
FILE_HANDLER.setFormatter(FORMATTER)


LOG = logging.getLogger('server')
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
    LOG.warning('Предупреждение')
    LOG.critical('Критическое общение')
    LOG.error('Ошибка')
