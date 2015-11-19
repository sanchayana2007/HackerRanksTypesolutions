__author__ = 'Sanchayan'

class MagicMtdscomposed(object):
    def __repr__(self):
        return "{__class__.__name__}".format(__class__=self.__class__)


class MagicMtds(object):
    def __init__(self,atr1=0,*list_val):
        self.val = atr1
        self.val_list = list_val[0]
        self.fixed_val=12
    def display_val(self):
        print('Priting Values')
        print('val',self.val)
        print('val_list',self.val_list)
        print('fixed_val',self.fixed_val)
#bject dispaly <__main__.MagicMtds object at 0x00354930>
    def __repr__(self):
        return "{__class__.__name__}({  atr1!r },{ _val_list})".format(__class__=self.__class__,_val_list=",".join(map(str,self.val_list)))
        #return "{__class__.__name__}".format(__class__=self.__class__)
    def __str__(self):
        return ",".join(map(str,self.val_list))
##------------Hash Immutable
class HashMthdOveride(object):
     def __init__(self,*list_val):
         self.mem_tuple= list_val[0]
         self.mem_frz_set = list_val[1]

     def __eq__(self, other):
         print('eq mthd')
         return self.mem_frz_set == other.mem_frz_set and self.mem_tuple == other.mem_tuple
     def __hash__(self):
         return hash(self.mem_tuple) ^ hash(self.mem_frz_set)

##------------Hash mutable
class HashMutMthdOveride(object):
     def __init__(self,*list_val):
         self.mem_list= list_val[0]
         self.mem_frz_set = list_val[1]

     def __eq__(self, other):
         print('eq mthd')
         return self.mem_frz_set == other.mem_frz_set and self.mem_tuple == other.mem_tuple
     __hash__ = None ## Defining hash for list will result in type error


if __name__=='__main__':
    a = MagicMtds(MagicMtdscomposed(),[1,2,3,4,5])
    a.display_val()
    print('Object dispaly',a)
    print('Class dispaly',MagicMtds)

    #-------Hash Immutable Overide-------#
    a= HashMthdOveride(('ama','ami'),frozenset([1,2,3,4]))
    b= HashMthdOveride(('ama','ami'),frozenset([1,2,3,4]))
    c= HashMthdOveride(('bma','bami'),frozenset([1,2,3,4]))
    print(id(a),id(b),id(c))# Every object has  a distinct ID
    print(hash(a),hash(b),hash(c))  # Equal objects have same hash
    if a == b:
        print('equal')
    if a is b:
        print('not equal')
    #-------Hash Mutable Overide-------#
    a= HashMutMthdOveride(['ama','ami'],frozenset([1,2,3,4]))
    b= HashMutMthdOveride(['ama','ami'],frozenset([1,2,3,4]))

    #c= HashMthdOveride(('bma','bami'),frozenset([1,2,3,4]))
    print(id(a),id(b))# Every object has  a distinct ID
    print(hash(a),hash(b))  # UNhashable will be a type eror
    if a == b:
        print('equal')
    if a is b:
        print('not equal')
    # the Set(a,b) is also not allowed as they are