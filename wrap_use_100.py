__author__ = 'Sanchayan'

from functools import  wraps,partial

def func_deco_nowraps(func):
    msg =func.__qualname__
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


def func_deco(func):
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


def func_deco_partial(func= None,*,prefix=''):
    if func is None:
        return partial(func_deco_partial,prefix=prefix)
    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper



class Myclass:

    @func_deco_nowraps
    def add(self):
        print('Add functions')

    @func_deco
    def sub(self):
        print('Sub functions')

    @func_deco_partial(prefix='*******')
    def mul(self):
        print('Mul functions')


if __name__=="__main__":

    # basic Metaclase
    X = Myclass()
    X.add()
    X.sub()
    X.mul()

