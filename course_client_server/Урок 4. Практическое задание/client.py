"""Программа-клиент"""
import sys
import json
import time
from socket import socket, AF_INET, SOCK_STREAM
from utils import get_msg, send_msg
from variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT


def create_presence(account_name='Guest'):
    """
    Генерирует запрос о присутствии клиента
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(msg):
    """
    Разбирает ответ сервера
    """
    if RESPONSE in msg:
        if msg[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {msg[ERROR]}'
    raise ValueError


def main():
    """
    Загружаем параметы коммандной строки
    """
    try:
        address = sys.argv[1]
        port = int(sys.argv[2])
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        address = DEFAULT_IP_ADDRESS
        port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCK.connect((address, port))
    msg_to_server = create_presence()
    send_msg(CLIENT_SOCK, msg_to_server)
    try:
        answer = process_ans(get_msg(CLIENT_SOCK))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
