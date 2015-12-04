
class OnlyOne(object):
    class __OnlyOne:
         def __init__(self, arg):
             print('_only one init')
             self.val = arg
         def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):

        if not OnlyOne.instance:
            print('1st time')
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        print("test")
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print (z)
