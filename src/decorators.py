import datetime
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызовов функций и результатов их работы.

    Args:
        filename (str, optional): Имя файла, в который будут записываться логи.
            Если не передано, логи будут выводиться в консоль. По умолчанию None.

    Returns:
        function: Обернутая функция с функциональностью логирования.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Внутренняя функция-обертка, логирующая вызовы функций и результаты их работы.
            """
            try:
                result = func(*args, **kwargs)
                status = "ok"
            except Exception as e:
                result = None
                status = f"error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} {status}")
                raise e
            if filename:
                with open(filename, "a") as file:
                    file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} {status}\n")
            else:
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} {status}")
            return result

        return wrapper

    return decorator
