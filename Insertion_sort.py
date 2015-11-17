__author__ = 'Sanchayan'

'Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can ' \
'calculate the number of times Insertion Sort shifts each elements when sorting an array?' \
'If ki is the number of elements over which the ith element of the array has to shift, then the total number of shifts' \
' will be k1 +k2 +…+kN.'

class BIT(object):
    def __init__(self):
        self.sz = sz
        self.tree= [0]*sz
    def update(self,idx,val):
        while idx <= self.sz:
            self.tree[idx]+=val
            idx+=idx & -idx
    def read(self,idx):
        sum =0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum
    if __name__='main':
        l = [32,323,324,545,55,545,77]
        for _ in l:
            cnt = 0
            bit = BIT(10**5+1)
