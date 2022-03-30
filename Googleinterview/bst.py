#Stack yusing List 
class Bst:
    def __init__(self,array,val):
        print("BST only works on sorted List  OLog(n)")
        self.array=array
        print(array ,"val of", val)
        self.val= val
        self.s= 0 
        self.end= len(array)
        self.search(0, self.end,val)

    def search(self, s, e, val):
        m = s + int((e - s) /2)

        if e >=s:      

            if self.array[m] == val:
                print(m +1)
                return m 
            elif val > self.array[m]:
                self.search(m+1,e,val)
            elif val < self.array[m]:
                self.search(s,m-1,val)
        else :
            return -1

        
if __name__=="__main__":
    # Test array
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    a= Bst(arr,x )
