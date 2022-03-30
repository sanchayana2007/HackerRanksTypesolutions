__author__ = 'Sanchayan'

'''This is a class that writes documents and print the values from the docstrng'''


class DocWriter():

    def _print_docs(self,obj):
            print(obj)
            for mtd in dir(obj):
                if not mtd.startswith('_') and mtd:

                    print(mtd,getattr(obj,mtd).__doc__)


    def __get__(self, instance, owner):
        if instance is not None:
            self._print_docs(instance)
        else:

            print(self._print_docs(owner))


class AClass():
    __doc__ = DocWriter()

    def __init__(self):
        self.a =2

    def method1(self):
        """ kjkjkj"""
        pass
    def method2(self):
        """ kjkjkj2"""
        pass


if __name__ =="__main__":
    AClass.__doc__
    a = AClass()


