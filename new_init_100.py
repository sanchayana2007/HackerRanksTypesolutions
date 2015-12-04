__author__ = 'Sanchayan'


class myclass(object):
    #def __new__(cls, *args, **kwargs):
     #   print('Inside the new Mthd', cls, args, kwargs)

    def __init__(self):
        print('Inside init mthd')


if __name__ == '__main__':
    t = myclass()
