__author__ = 'Sanchayan'

class API(object):
    def print_values(self,obj):
        def _print_values(mtdname):
            # Rejects all the  __XX__  mthds
            if mtdname.startswith('_'):
                return ''
            val = getattr(obj,mtdname)
            doc = val.__doc__
         #   print(doc)
            return '%s:%s'%(mtdname,doc)
        res = [_print_values(ent) for ent in dir(obj)]
        #print(res)
        return '\n'.join([ent for ent in res if ent != ''])

    def __get__(self, instance, owner):
        #Get gets the call from API
        if instance is not None:
            print('instnce')
            self.print_values(instance)
        else:
            print(self.print_values(owner))



class Myclass(object):
    # doc set as object of API
    __doc__ = API()

    def __init__(self):
        self.a =2

    def addby1(self):
        """Method is add by 1"""
        return self.a +1
    def addby2(self):
        """Method is add by 2"""
        return self.a +2

if __name__ == '__main__':
    #Lets call the Doc of the class
    Myclass.__doc__

    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
        print(i)

    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
       print(i)
