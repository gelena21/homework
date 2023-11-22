from datetime import datetime
from typing import Dict, List, Optional


def filter_dicts_by_state(
    dicts: List[Dict[str, str]], state: Optional[str] = "EXECUTED"
) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        dicts (List[Dict[str, str]]): Список словарей.
        state (Optional[str]): Значение ключа 'state', по которому нужно выполнить фильтрацию.
                               По умолчанию установлено значение "EXECUTED".

    Returns:
        List[Dict[str, str]]: Отфильтрованный список словарей.
    """
    filtered_dicts = [d for d in dicts if d.get("state") == state]
    return filtered_dicts


def sort_dicts_by_date(data: List[dict], reverse: Optional[bool] = True) -> List[dict]:
    """
    Сортирует список словарей по убыванию или возрастанию даты.

    Args:
        data (List[dict]): Список словарей, каждый из которых содержит ключ 'date'
        с датой в формате '%Y-%m-%dT%H:%M:%S.%f'.
        reverse (Optional[bool]): Флаг сортировки по убыванию. По умолчанию True (сортировка по убыванию).

    Returns:
        List[dict]: Отсортированный список словарей.
    """
    sorted_data = sorted(
        data,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse if reverse is not None else True,  # noqa: E501
    )
    return sorted_data
