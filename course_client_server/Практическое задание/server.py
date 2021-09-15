"""Программа-сервер"""
import sys
import json
import logging
from time import time
from socket import socket, AF_INET, SOCK_STREAM
from argparse import ArgumentParser
from select import select
from utils import get_msg, send_msg
from config import config_server_log
from decor import log
from variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, \
                      MESSAGE, MESSAGE_TEXT, SENDER

LOGGER = logging.getLogger('server')


@log
def process_client_msg(msg, msg_list, client):
    """
    Обработчик сообщений от клиентов, принимает словарь-сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента
    """
    LOGGER.debug(f'Разбор сообщения от клиента : {msg}')
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg and USER in msg and msg[USER][ACCOUNT_NAME] == 'Guest':
        send_msg(client, {RESPONSE: 200})
        return
    elif ACTION in msg and msg[ACTION] == MESSAGE and TIME in msg and MESSAGE_TEXT in msg:
        msg_list.append((msg[ACCOUNT_NAME], msg[MESSAGE_TEXT]))
        return
    else:
        send_msg(client, {RESPONSE: 400, ERROR: 'Bad Request'})
        return


@log
def arg_parser():
    """
    Парсер аргументов коммандной строки
    """
    parser = ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    address = namespace.a
    port = namespace.p
    # Проверим подходящий номер порта
    if not 1023 < port < 65536:
        LOGGER.critical(f'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    return address, port


@log
def main():
    # Загрузка параметров командной строки
    address, port = arg_parser()
    LOGGER.info(f'Запущен сервер, порт для подключений: {port}, адрес с которого принимаются подключения: {address}.')
    # Готовим сокет
    SERV_SOCK = socket(AF_INET, SOCK_STREAM)
    SERV_SOCK.bind((address, port))
    SERV_SOCK.settimeout(0.5)
    # Список клиентов
    clients = []
    # Очередь сообщений
    messages = []
    # Слушаем порт
    SERV_SOCK.listen(MAX_CONNECTIONS)

    while True:
        try:
            CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        except OSError:
            pass
        else:
            LOGGER.info(f'Установлено соедение с ПК {ADDR}')
            clients.append(CLIENT_SOCK)
        # Список клиентов от которых получаем сообщения
        clients_read = []
        # Список клиентов которым отправляем сообщения
        clients_write = []

        try:
            if clients:
                clients_read, clients_write, errors = select(clients, clients, [], 0)
        except OSError:
            pass
        # Принимаем сообщения
        if clients_read:
            for client in clients_read:
                try:
                    process_client_msg(get_msg(client), messages, client)
                except:
                    LOGGER.info(f'Клиент {client.getpeername()} отключился от сервера.')
                    clients.remove(client)
        # Отправляем сообщения
        if messages and clients_write:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for client in clients_write:
                try:
                    send_msg(client, message)
                except:
                    LOGGER.info(f'Клиент {client.getpeername()} отключился от сервера.')
                    clients.remove(client)


if __name__ == '__main__':
    main()
