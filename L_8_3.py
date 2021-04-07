def type_logger(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for i in args:
            print(f'{func.__name__}({i}: {type(i)}')
        print('Тип результата:', type(func(*args, **kwargs)))
    return wrapper

@type_logger
def calc_cube(x, y):
    return x ** 3 + y

a = calc_cube(5.5, 10.8)

