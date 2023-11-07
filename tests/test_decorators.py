import datetime

import pytest
from src.decorators import log


@pytest.fixture
def log_file(tmp_path):
    return tmp_path / "test_log.txt"


def test_log_error(log_file):
    @log(filename=log_file)
    def unsafe_operation():
        return 1 / 0

    result = unsafe_operation()
    assert result == "error: ZeroDivisionError. Inputs: (), {}"
    with open(log_file, "r") as file:
        log_content = file.read()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_log = "{} unsafe_operation error\n".format(timestamp)
    assert log_content.startswith(expected_log)
