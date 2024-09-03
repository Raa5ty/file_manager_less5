def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("***" * 10)
        result = func(*args, **kwargs)
        print("***" * 10)
        return result
    return wrapper