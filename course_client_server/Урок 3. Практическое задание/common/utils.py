"""Утилиты"""

import json
from variables import MAX_PACKAGE_LENGTH, ENCODING


def get_msg(client):
    """
    Приём и декодирование сообщения
    принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_msg(sock, msg):
    """
    Кодирование и отправка сообщения
    принимает словарь и отправляет его
    """
    json_msg = json.dumps(msg)
    encoded_msg = json_msg.encode(ENCODING)
    sock.send(encoded_msg)
