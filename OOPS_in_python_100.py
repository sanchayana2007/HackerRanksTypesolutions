__author__ = 'Sanchayan'
import sys
from abc import ABCMeta,abstractmethod

#private Implementation
#1>
import inspect
import re

def private_check_deco(functional_arg):
    print(functional_arg)
    def _private_check_deco():
        try:
            # func_call = inspect.getargvalues(inspect.currentframe())
            #matched = re.match('self',func_call)
            arg_func = inspect.getargspec(functional_arg).args[0]
            print(arg_func)
            matched = re.match('self',arg_func)
            #print(matched)
            if matched :
                print('This is a privite function ')
                return AttributeError
            else:
                functional_arg()

        except Exception as e :
            print(e.__doc__)
        # print(e.message)
    return _private_check_deco()


class Priv_test():


    @private_check_deco
    def func(self):
        print('I am a Private function')

    def non_public(self):
        print('Public Function')
        self.func()


# 1> MRO

#2> Interface , abstarct Method implementation virtual keyword

class AbstractEntity(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def func1(self):
        return 1

    @classmethod
    def __subclasshook__(cls, subclass):
        print('detded')
        if cls is Hand:
            if any('func1' in B.__dict__ for B in subclass.__mro__):
                return True

            return NotImplemented


class Entity(AbstractEntity):
    def __init__(self):
        pass
    def test(self):
        pass
    def func1(self,t):
        print('derived')


# 3> Functions as classes = Callables
'''this Functional class will Sum of first n numbers '''
import collections.abc
class SumofN(collections.abc.Callable):
    def __call__(self, n):
        if n > 0:
            return n * (n+1)//2
        else:
            return 0




#RTTIional Classes as Callables



#Multiargument Polymorphism

#Immutable objects (consts)
class Mutable(object):
    def __init__(self,*args):
        self.l = args[0]
        self.val=args[1]
class Immutabe(Mutable):
    def __init__(self,*args):

        if len(args) ==1 or isinstance(args[0],Mutable):
            self.l = args[0].l
        else:
            super().__init__(*args)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    ''''
    def __hash__(self):
        h=0
        for c in self.l:
            h = h + hash(c)
        return h
    '''''
#Static Methods and atributes


if __name__=='__main__':
    #print('hash',sys.hash_info)


    # Private function checks
    p = Priv_test()
    p.func()
    p.non_public()


    #Immutable and Mutable checks
    a = Mutable([1,2,3,4],2)
    b = Immutabe(a)
    d = {a:1}
    e = {b:2}

    #Abstarct Method Checks
    #a = Entity()
    #a.func1(3)

    #Callabales checks
    func = SumofN()
    print(func(5))

