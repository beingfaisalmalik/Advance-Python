import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling The Function')
        print(args[0])
        results = func(args[0])
        print(f'The Square Of The Number Is {results}')
        print('Called The Function')
    return wrapper

@decorator
def func(num):
    return num**2


func(10)