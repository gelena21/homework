import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler("masks.log", mode="w", encoding="utf-8")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты пользователя"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Функция для маскировки номера счета пользователя"""
    account_number = account_number.replace("Счет", "").replace(" ", "")
    masked_number = f"**{account_number[-4:]}"
    return masked_number
