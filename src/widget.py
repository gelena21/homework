from src.masks import mask_account_number, mask_card_number


def type_card(data: str) -> str:
    """
    Функция для маскировки номера  карты или счета пользователя
    Args:
        data (str): Номер карты или счета в формате "Тип карты Номер".

    Returns:
        str: Маскированный номер карты или счета в формате "Тип карты *******
    """
    data_split = data.split(" ")
    if "Счет" in data_split:
        masked_acc_number = mask_account_number(data_split[-1])
        return f"{data_split[0]} {masked_acc_number}"
    else:
        name = " ".join(data_split[:-1])
        masked_card_number = mask_card_number(data_split[-1])
        return f"{name} {masked_card_number}"


def format_date(input_date: str) -> str:
    """
    Форматирование даты
    """
    formatted_date = input_date.split("T")[0]
    year, month, day = formatted_date.split("-")
    return f"{day}.{month}.{year}"
