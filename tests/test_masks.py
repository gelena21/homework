import pytest
from src.masks import mask_card_number, mask_account_number


@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654")
    ]


@pytest.fixture
def account_numbers():
    return [
        ("1234567890", "**90"),
        ("9876543210", "**10")
    ]


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("9876543210987654", "9876 54** **** 7654")
])
def test_mask_card_number(card_number, expected):
    masked_number = mask_card_number(card_number)
    assert masked_number == expected


@pytest.mark.parametrize("account_number, expected", [
    ("1234567890", "**7890"),
    ("9876543210", "**3210")
])
def test_mask_account_number(account_number, expected):
    masked_number = mask_account_number(account_number)
    assert masked_number == expected
