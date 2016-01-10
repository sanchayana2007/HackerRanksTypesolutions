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