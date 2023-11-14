import json
import os
import unittest
from src.utils import load_transactions, convert_to_rubles


class TestUtilsFunctions(unittest.TestCase):

    def test_load_transactions(self):
        test_data = [{'amount': 100.0, 'currency': 'RUB'}, {'amount': 50.0, 'currency': 'USD'}]
        test_file_path = 'test_operations.json'

        with open(test_file_path, 'w', encoding='utf-8') as test_file:
            json.dump(test_data, test_file)

        transactions = load_transactions(test_file_path)
        self.assertEqual(transactions, test_data)

        os.remove(test_file_path)

    def test_convert_to_rubles(self):
        transaction_rub = {'amount': 100.0, 'currency': 'RUB'}
        result_rub = convert_to_rubles(transaction_rub)
        self.assertEqual(result_rub, 100.0)
        transaction_usd = {'amount': 50.0, 'currency': 'USD'}
        with self.assertRaises(ValueError):
            convert_to_rubles(transaction_usd)
