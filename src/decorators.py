from functools import wraps
from typing import Callable, Any
import datetime


def log(filename=None) -> Any:
    """
    Декоратор log
    принимает один необязательный аргумент filename, определяет имя файла, в который будут записываться логи. Если
    filename
    не задан, то логи будут выводиться в консоль
    :param filename: filename = None
    """
    def wrapped(function: Callable) -> Any:
        @wraps(function)
        def inner(*args, **kwargs) -> Any:
            try:
                result = function(*args, **kwargs)
                message = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, {function.__name__} ok\n"
            except Exception as e:
                result = None
                message = (f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {function.__name__} "
                           f"error: {str ( e )} Inputs: {args}, {kwargs}\n.")

            if filename:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(message)
            else:
                print(message)

            return result
        return inner

    return wrapped
