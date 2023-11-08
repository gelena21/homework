import datetime
import pytest
from src.decorators import log

log_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
expected_log = f"{log_timestamp} unsafe_operation error: ZeroDivisionError. Inputs: (), {{}}"


def test_log_error_to_file(capsys):
    log_file = "test_log.txt"

    @log(filename=log_file)
    def unsafe_operation():
        return 1 / 0

    unsafe_operation()

    captured = capsys.readouterr()
    log_output = captured.out.strip()

    assert log_output == expected_log
