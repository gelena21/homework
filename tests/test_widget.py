import pytest
from src.widget import type_card, format_date


@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_type_card(input_data, expected_output):
    assert type_card(input_data) == expected_output


@pytest.mark.parametrize("input_date, expected_output", [
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ("2018-06-30T02:08:58.425572", "30.06.2018")
])
def test_format_date(input_date, expected_output):
    formatted_date = format_date(input_date)
    assert formatted_date == expected_output
