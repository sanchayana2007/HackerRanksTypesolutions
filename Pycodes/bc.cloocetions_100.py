
__author__ = 'Sanchayan'
from collections.abc import Set as ColSet
import inspect

class ListBasedSet(ColSet):
    def __init__(self,val):
        self.elements = []
        if val is  not None:
            [self.elements.append(x) for x in val if not x in self.elements ]
    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, item):
        return item in self.elements
    def __len__(self):
        return len(self.elements)









if __name__ == '__main__':

    s1 = ListBasedSet('dedefftys')
    s2 = ListBasedSet('deddsdff')
#    [print(i) for i in s1 & s2]
    for z in (i for i in inspect.getmembers(list())):
        print(z)


 --------------------Atribute_getting_100.py-----------------------------
__author__ = 'Sanchayan'

class A:
    def __init__(self,t):
        self.test=t
    '''
    def __getattribute__(self, item):
        print('x y z')
        return item
    '''
    def __getattr__(self, item):
        print('jkl')
        return item

if __name__ == '__main__':
    a = A(45)

    print(a.test)
    print(a.nf)

