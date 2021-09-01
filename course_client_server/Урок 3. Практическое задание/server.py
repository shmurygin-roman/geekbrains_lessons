"""Программа-сервер"""
import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from utils import get_msg, send_msg
from variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT


def process_client_msg(msg):
    """
    Обработчик сообщений от клиентов, принимает словарь-сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента
    """
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg and USER in msg and msg[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    """

    # Обрабатываем порт
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEFAULT_PORT
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Обрабатываем адрес
    try:
        if '-a' in sys.argv:
            address = sys.argv[sys.argv.index('-a') + 1]
        else:
            address = ''
    except IndexError:
        print('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет
    SERV_SOCK = socket(AF_INET, SOCK_STREAM)
    SERV_SOCK.bind((address, port))

    # Слушаем порт
    SERV_SOCK.listen(MAX_CONNECTIONS)

    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        try:
            msg_from_client = get_msg(CLIENT_SOCK)
            print(msg_from_client)
            response = process_client_msg(msg_from_client)
            send_msg(CLIENT_SOCK, response)
            CLIENT_SOCK.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            CLIENT_SOCK.close()


if __name__ == '__main__':
    main()
