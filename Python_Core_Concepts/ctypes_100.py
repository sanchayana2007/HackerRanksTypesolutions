__author__ = 'Sanchayan'

import ctypes

_libfibb = ctypes.CDLL('fib.so')

def c_types_fibo(a):
    return _libfibb.fib(ctypes.c_int(a))



if __name__=='__main__':
    c_types_fibo(4)
