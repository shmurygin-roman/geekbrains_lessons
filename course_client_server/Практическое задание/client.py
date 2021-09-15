"""Программа-клиент"""
import sys
import json
import logging
from time import time
from socket import socket, AF_INET, SOCK_STREAM
from argparse import ArgumentParser
from utils import get_msg, send_msg
import config.config_client_log
from decor import log
from variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, \
                      MESSAGE, MESSAGE_TEXT, SENDER

LOGGER = logging.getLogger('client')


@log
def create_presence(account_name='Guest'):
    """
    Генерирует запрос о присутствии клиента
    """
    out = {
        ACTION: PRESENCE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def process_ans(msg):
    """
    Разбирает ответ сервера
    """
    LOGGER.debug(f'Разбор сообщения от сервера: {msg}')
    if RESPONSE in msg:
        if msg[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {msg[ERROR]}'
    raise ValueError


@log
def msg_from_server(msg):
    """
    Обработчик сообщений других пользователей, поступающих с сервера
    """
    if ACTION in msg and msg[ACTION] == MESSAGE and SENDER in msg and MESSAGE_TEXT in msg:
        print(f'Получено сообщение от пользователя {msg[SENDER]}:\n{msg[MESSAGE_TEXT]}')
        LOGGER.info(f'Получено сообщение от пользователя {msg[SENDER]}: {msg[MESSAGE_TEXT]}')
    else:
        LOGGER.error(f'Получено некорректное сообщение с сервера: {msg}')


@log
def create_msg(sock, account_name='Guest'):
    """
    Ввод данных и завершение работы
    """
    msg = input('Введите сообщение для отправки или \'!!!\' для завершения работы: ')
    if msg == '!!!':
        sock.close()
        print('Завершение работы по команде пользователя.')
        LOGGER.info('Завершение работы по команде пользователя.')
        sys.exit(0)
    msg_dict = {
        ACTION: MESSAGE,
        TIME: time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: msg
    }
    LOGGER.debug(f'Сформировано сообщение: {msg_dict}')
    return msg_dict


@log
def arg_parser():
    """
    Парсер аргументов коммандной строки
    """
    parser = ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-m', '--mode', default='listen', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    address = namespace.addr
    port = namespace.port
    mode = namespace.mode
    # Проверим подходящий номер порта
    if not 1023 < port < 65536:
        LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {port}. '
            f'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    # Проверим допустим ли выбранный режим работы клиента
    if mode not in ('listen', 'send'):
        LOGGER.critical(f'Указан недопустимый режим работы {mode}, допустимые режимы: listen, send')
        sys.exit(1)
    return address, port, mode


@log
def main():
    # Загружаем параметы коммандной строки
    address, port, mode = arg_parser()
    LOGGER.info(f'Запущен клиент с парамертами: адрес сервера: {address}, порт: {port}')
    # Инициализация сокета и обмен
    try:
        CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
        CLIENT_SOCK.connect((address, port))
        msg_to_server = create_presence()
        send_msg(CLIENT_SOCK, msg_to_server)
        answer = process_ans(get_msg(CLIENT_SOCK))
        LOGGER.info(f'Установлено соединение с сервером. Ответ сервера: {answer}')
        print(f'Установлено соединение с сервером.')
    except (ValueError, json.JSONDecodeError):
        LOGGER.error('Не удалось декодировать полученную Json строку.')
    else:
        # Обмен с сервером, согласно требуемому режиму.
        if mode == 'send':
            print('Режим работы - отправка сообщений.')
        else:
            print('Режим работы - приём сообщений.')
        while True:
            # Режим работы - отправка
            if mode == 'send':
                try:
                    send_msg(CLIENT_SOCK, create_msg(CLIENT_SOCK))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    LOGGER.error(f'Соединение с сервером {address} было потеряно.')
                    sys.exit(1)
            # Режим работы - приём
            if mode == 'listen':
                try:
                    msg_from_server(get_msg(CLIENT_SOCK))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    LOGGER.error(f'Соединение с сервером {address} было потеряно.')
                    sys.exit(1)


if __name__ == '__main__':
    main()
