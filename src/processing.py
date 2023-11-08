from typing import Dict, List, Optional
from datetime import datetime


def filter_dicts_by_state(dicts: List[Dict[str, str]], state: Optional[str] = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Функция для фильтрации списка словарей по значению ключа 'state'.
     Args:
        state (Optional[str], optional): Значение ключа 'state', по которому нужно выполнить фильтрацию.
                                        По умолчанию установлено значение "EXECUTED".

    Returns:
        list[dict[str, str]]: Отфильтрованный список словарей.

    """
    filtered_dicts = [d for d in dicts if d.get('state') == state]
    return filtered_dicts


def sort_dicts_by_date(data: List[dict], reverse: Optional[bool] = True) -> List[dict]:
    """
    Сортирует список словарей по убыванию или возрастанию даты.

    Args:
        data (List[dict]): Список словарей, каждый из которых содержит ключ 'date' с датой в формате '%Y-%m-%dT%H:%M:%S.%f'.
        reverse (Optional[bool]): Флаг сортировки по убыванию. По умолчанию True (сортировка по убыванию).

    Returns:
        List[dict]: Отсортированный список словарей.
    """
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)
    return sorted_data
