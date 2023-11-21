from unittest.mock import patch

import pandas as pd
import pytest
from src.read_data import read_csv, read_xlsx


def test_read_csv_with_mock():
    with patch("src.read_data.csv.DictReader") as mock_csv_reader:
        mock_csv_reader.return_value = [{"id": "1", "name": "Test"}]
        result = read_csv("data/transactions.csv")
    assert result == [{"id": "1", "name": "Test"}]


def test_read_xlsx_with_patch():
    with patch("src.read_data.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({"id": [1], "name": ["Test"]})
        result = read_xlsx("data/transactions_excel.xlsx")
    assert result == [{"id": 1, "name": "Test"}]


if __name__ == "__main__":
    pytest.main()
