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

    non_existing_file_path = 'non_existing_file.json'
    transactions_non_existing = load_transactions(non_existing_file_path)
    assert transactions_non_existing == []

    invalid_data_file_path = 'invalid_data_file.json'
    with open(invalid_data_file_path, 'w', encoding='utf-8') as invalid_data_file:
        invalid_data_file.write("Not a JSON array")

    transactions_invalid_data = load_transactions(invalid_data_file_path)
    assert transactions_invalid_data == []
    os.remove(invalid_data_file_path)


def test_convert_to_rubles():
    transaction_rub = {'amount': 100.0, 'currency': 'RUB'}
    result_rub = convert_to_rubles(transaction_rub)
    assert result_rub == 100.0

    transaction_usd = {'amount': 50.0, 'currency': 'USD'}
    with pytest.raises(ValueError, match="Транзакция выполнена не в рублях. Укажите транзакцию в рублях"):
        convert_to_rubles(transaction_usd)

    transaction_no_amount = {'currency': 'RUB'}
    with pytest.raises(ValueError, match="Транзакция не содержит 'amount'"):
        convert_to_rubles(transaction_no_amount)

    transaction_no_currency = {'amount': 50.0}
    with pytest.raises(ValueError, match="Транзакция выполнена не в рублях. Укажите транзакцию в рублях"):
        convert_to_rubles(transaction_no_currency)

    transaction_no_keys = {}
    with pytest.raises(ValueError, match="Транзакция не содержит 'amount'"):
        convert_to_rubles(transaction_no_keys)


