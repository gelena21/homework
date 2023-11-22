import re
from collections import Counter
from typing import Dict, List


def filter_by_description(
    operations: List[Dict[str, str]], search_string: str
) -> List[Dict[str, str]]:
    """
    Фильтрует список операций по описанию.

    Параметры:
    - operations (List[Dict[str, str]]): Список словарей с данными о банковских операциях.
    - search_string (str): Строка для поиска в описании операций.

    Возвращает:
    - List[Dict[str, str]]: Отфильтрованный список операций.
    """
    filtered_operations = [
        operation
        for operation in operations
        if re.search(search_string, operation.get("description", ""), re.IGNORECASE)
    ]
    return filtered_operations


def count_operations_by_category(
    operations: List[Dict[str, str]], categories: Dict[str, str]
) -> Counter:
    """
    Создает Counter с количеством операций в каждой категории.

    Параметры:
    - operations (List[Dict[str, str]]): Список словарей с данными о банковских операциях.
    - categories (Dict[str, str]): Словарь категорий операций.

    Возвращает:
    - Counter: Counter с количеством операций в каждой категории.
    """
    category_counts = Counter(
        operation.get("category", "")
        for operation in operations
        if operation.get("category", "") in categories
    )
    return category_counts
