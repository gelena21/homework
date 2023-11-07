import datetime
from functools import wraps


def log(filename="log.txt"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                status = "ok"
            except Exception as e:
                result = f"error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                status = "error"
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} {func.__name__} {status}"
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


result = my_function(1, 2)
