"""Тесты программы-клиента"""

import unittest
from client import create_presence, process_ans
from variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR


class TestClient(unittest.TestCase):
    # тест функции create_presence
    def test_create_presence(self):
        first = create_presence()
        first[TIME] = 1.0
        second = {ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(first, second)

    # тест функции process_ans с ответом 200
    def test_process_ans_200(self):
        first = process_ans({RESPONSE: 200})
        second = '200 : OK'
        self.assertEqual(first, second)

    # тест функции process_ans с ответом 400
    def test_process_ans_400(self):
        first = process_ans({RESPONSE: 400, ERROR: 'Error'})
        second = '400 : Error'
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
