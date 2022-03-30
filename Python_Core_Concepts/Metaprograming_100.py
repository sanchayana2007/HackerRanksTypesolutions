__author__ = 'Sanchayan'

#Creating classes Dyamically by using the return type a basic Metaclass
class MetaOne(type):
    def __new__(cls, *args, **kwargs):
        print('......new......',cls,*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

##It can only intilaise the classs variables not the object variables
    def __init__(Class, classname, supers, classdict):
        print('...init class Object',Class)

        print('classname',classname)
        print('classdict',classdict)



class Foo:
    pass

class Myclass(Foo,metaclass=MetaOne):
    class_var = 78

# Cant be changed in meta init bacause des is forms after the class forms
    def __init__(self):
        self.var1= 12

    def mthd(self):
        print('My class Method ')

        return self.data


#Using a Function as Metaclass

def MetaFunc(classname, supers, classdict):
	print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
	return type(classname, supers, classdict)
class Eggs:
	pass
	print('making class')
class Spam(Eggs, metaclass=MetaFunc): # Run simple function at end
    data = 1 # Function returns class

    def meth(self, arg):
        return self.data + arg





if __name__=="__main__":

    # basic Metaclase
    #X = Myclass()

    #Metaclass on the Function
    print('making instance')
    X = Spam()
    print('data:', X.data, X.meth(2))


