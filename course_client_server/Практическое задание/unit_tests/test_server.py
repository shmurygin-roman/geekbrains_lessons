"""Тесты программы-сервера"""

import unittest
from server import process_client_msg
from variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT


class TestServer(unittest.TestCase):
    # тест функции process_client_msg с ответом 200
    def test_process_client_msg_ans_200(self):
        first = process_client_msg({ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}})
        second = {RESPONSE: 200}
        self.assertEqual(first, second)

    # тест функции process_client_msg нет действия
    def test_process_client_msg_no_action(self):
        first = process_client_msg({TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}})
        second = {RESPONSE: 400, ERROR: 'Bad Request'}
        self.assertEqual(first, second)

    # тест функции process_client_msg нет времени
    def test_process_client_msg_no_time(self):
        first = process_client_msg({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}})
        second = {RESPONSE: 400, ERROR: 'Bad Request'}
        self.assertEqual(first, second)

    # тест функции process_client_msg нет юзера
    def test_process_client_msg_no_user(self):
        first = process_client_msg({ACTION: PRESENCE, TIME: 1.0})
        second = {RESPONSE: 400, ERROR: 'Bad Request'}
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
