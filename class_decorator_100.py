__author__ = 'Sanchayan'


def debug(func):
    msg =func.__name__
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


#functions as class Decorator

def classdeco(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls





@classdeco
class Myclass:


    def add(self):
        print('Add functions')


    def sub(self):
        print('Sub functions')


    def mul(self):
        print('Mul functions')


if __name__=="__main__":

    # basic Metaclase
    X = Myclass()
    X.add()
    X.sub()
    X.mul()


