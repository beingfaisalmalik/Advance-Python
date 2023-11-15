
import functools

def decoratoreven(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling Even The Function')
        results = func(args[0])*2
        return results
    return wrapper

def decoratorodd(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling Odd The Function')
        results = func(args[0])/3
        print(results)
    return wrapper

@decoratorodd
@decoratoreven
def func(num):
    return num**2


func(2)