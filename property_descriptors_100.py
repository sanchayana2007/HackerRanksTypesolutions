__author__ = 'Sanchayan'

class ProprtyDescriptor:
#Put a class atribute to used as a property
    _x=0

    def __init__(self):
        print('Initilising the Atribute')
        self._x ='intilised'


    @property
    def x(self):
        print("I am in Getter Property")

        return self._x

    @x.setter
    def x(self,value):
        print("Inside the Setter")
        self._x = value

    @x.deleter
    def x(self):
        print('Inside Deleter')
        del self._x

testProperty = ProprtyDescriptor()
testProperty.x = 'Set'
testProperty.x

del testProperty.x




