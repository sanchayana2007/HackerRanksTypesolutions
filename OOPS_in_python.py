__author__ = 'Sanchayan'
import sys
from abc import ABCMeta,abstractmethod
#private Implementation


#MRO

#Interface , abstarct Method implementation virtual keyword

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


















#RTTI

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
    a = Mutable([1,2,3,4],2)
    b = Immutabe(a)
    d = {a:1}
    e = {b:2}

    a = Entity()

    a.func1(3)