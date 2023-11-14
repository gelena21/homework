import os
import json
import pytest
from src.utils import load_transactions, convert_to_rubles


@pytest.fixture
def test_file_path():
    test_data = [{'amount': 100.0, 'currency': 'RUB'}, {'amount': 50.0, 'currency': 'USD'}]
    test_file_path = 'test_operations.json'

    with open(test_file_path, 'w', encoding='utf-8') as test_file:
        json.dump(test_data, test_file)

    yield test_file_path
    os.remove(test_file_path)


def test_load_transactions(test_file_path):
    transactions = load_transactions(test_file_path)
    assert transactions == [{'amount': 100.0, 'currency': 'RUB'}, {'amount': 50.0, 'currency': 'USD'}]


def test_convert_to_rubles():
    transaction_rub = {'amount': 100.0, 'currency': 'RUB'}
    result_rub = convert_to_rubles(transaction_rub)
    assert result_rub == 100.0

    transaction_usd = {'amount': 50.0, 'currency': 'USD'}
    with pytest.raises(ValueError):
        convert_to_rubles(transaction_usd)
