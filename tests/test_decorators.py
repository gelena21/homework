import datetime
import os.path

from src.decorators import log


@log()
def test_console() -> None:
    def my_function(x: int, y: int) -> float:
        return x / y

    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    assert my_function(10, 0) == f'{now}, Возникла ошибка:division by zero. my_function, Inputs: (10, 0)'
    assert my_function(10, 5) == f'{now}, my_function, ok\n'


def test_log_to_file() -> None:
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def my_function(x: int, y: int) -> float:
        return x + y

    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    my_function(10, 2)

    with open(filename, 'r') as file:
        log_mess = file.read().strip()

    expected_logs = f"{now}, my_function ok"
    assert log_mess == expected_logs
