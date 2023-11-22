from typing import Dict, Iterator, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Функция фильтрует транзакции по заданной валюте.

    Args:
        transactions (List[Dict]): Список словарей с транзакциями.
        currency (str): Код валюты для фильтрации.

    Yields:
        Dict: Транзакция с заданной валютой.
    """
    for transaction in transactions:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        if currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Функция возвращает описание каждой операции.

    Args:
        transactions (List[Dict]): Список словарей с транзакциями.

    Yields:
        str: Описание операции.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт.

    Args:
        start (int): Начальное значение для генерации номеров карт.
        end (int): Конечное значение для генерации номеров карт.

    Yields:
        str: Номер банковской карты в формате "XXXX XXXX XXXX XXXX".

    """
    for num in range(start, end + 1):
        yield "{:04} {:04} {:04} {:04}".format(
            num // 1000000000000,
            (num // 10000000000) % 10000,
            (num // 100000000) % 10000,
            num % 100000000,
        )


usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(transactions)
card_numbers = card_number_generator(1, 5)
