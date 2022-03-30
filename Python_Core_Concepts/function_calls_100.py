__author__ = 'Sanchayan'


def fun(i='abc',L=[]):
    L.append(i)
    return L

def manyArgs(i,*arg):
    print('Fixed argu',i)
    print ("I was called with", len(arg), "arguments:", arg)


if __name__== "__main__":
    print(fun())
    print(fun(89))
    manyArgs(1,2,34,4343,'3232323')