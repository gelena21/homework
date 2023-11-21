import csv

import pandas as pd


def read_csv(file_path):
    """
    Читает данные о финансовых операциях из CSV-файла.

    Параметры:
    - file_path (str): Путь к CSV-файлу.

    Возвращает:
    - list: Список словарей, представляющих финансовые операции.
    """
    transactions = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def read_xlsx(file_path):
    """
    Читает данные о финансовых операциях из XLSX-файла.

    Параметры:
    - file_path (str): Путь к XLSX-файлу.

    Возвращает:
    - list: Список словарей, представляющих финансовые операции.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict("records")
    return transactions
