from typing import Any, Optional


def filter_by_state(
    data: list[dict[str, str]], state: Optional[str] = "EXECUTED"
) -> list[dict[str, str]]:
    """
    Функция для фильтрации списка словарей по значению ключа 'state'.
     Args:
        data (list[dict[str, str]]): Список словарей, который нужно отфильтровать.
        state (Optional[str], optional): Значение ключа 'state', по которому нужно выполнить фильтрацию.
                                        По умолчанию установлено значение "EXECUTED".

    Returns:
        list[dict[str, str]]: Отфильтрованный список словарей.

    """
    filtered_data = list(filter(lambda x: x.get("state") == state, data))
    return filtered_data


def sort_by_date(data: Any, reverse: bool = True) -> list[dict[str, str]]:
    """
    Функция для сортировки списка словарей по значению ключа 'date'.
    Args:
        data (Any): Список словарей, который нужно отсортировать.
        reverse (bool, optional): Указывает, следует ли сортировать в обратном порядке (по убыванию).
                                  По умолчанию установлено значение True.

    Returns:
        list[dict[str, str]]: Отсортированный список словарей.

    """
    sorted_data = sorted(data, key=lambda x: x.get("date"), reverse=reverse)
    return sorted_data
