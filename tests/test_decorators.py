import datetime

from src.decorators import log


@log()
def test_console() -> None:
    def my_function(x: int, y: int) -> float:
        return x / y

    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    assert my_function(10, 0) == f'{now}, Возникла ошибка:division by zero. my_function, Inputs: (10, 0)'
    assert my_function(10, 5) == f'{now}, my_function, ok\n'


def test_log_to_file() -> None:
    filename = "test_logs.txt"

    @log(filename="test_logs.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(10, 2)

    with open(filename, 'r') as file:
        logs = file.read()
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    expected_logs = f"{now}, my_function, ok\n"
    assert logs == expected_logs
