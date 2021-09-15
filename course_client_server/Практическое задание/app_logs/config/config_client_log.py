"""Конфиг логгера для клиента"""

import logging.handlers
import os
from pathlib import Path

FORMATTER = logging.Formatter("%(asctime)s - %(levelname)-8s - %(filename)s - %(message)s ")

FULL_PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(str(Path(FULL_PATH).parents[0]), 'logs\client.log')

FILE_HANDLER = logging.FileHandler(PATH, encoding='utf8')
FILE_HANDLER.setFormatter(FORMATTER)


LOG = logging.getLogger('client')
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
    LOG.warning('Предупреждение')
    LOG.critical('Критическое общение')
    LOG.error('Ошибка')
