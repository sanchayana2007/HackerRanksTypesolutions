from audioop import reverse
def reverse(tree):
        if not tree :
            return
        
        current = tree
        left  = current.left     
        right  = current.right

        current.left = right
        current.right  = left

        reverse(current.left)   
        reverse(current.right) 
    

class Bst:
    def __init__(self,val= None) -> None:
        self.left = None 
        self.right = None
        self.val = val
        self.nodecouount= 0 
        self.vals = []

    def insertR(self, val):
        if not val:
            return 
        #This is the 1st entry in the tree 
        if not self.val:
            self.val = val
            return 
        
        if val < self.val:
            if self.left :
                self.left.insertR(val)
                
            else:
                self.left = Bst(val)
                self.nodecouount += 1

        elif val > self.val:
            if self.right :
                self.right.insertR(val)
            else:
                self.right = Bst(val)
                self.nodecouount += 1
        else:
            return 0 


        
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

        
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

if __name__ == "__main__":
    a= [1,27,32,43,58]
    
    t=Bst()
    for i in a:
        t.insertR(i)
    print(t.get_min())
    print(t.get_max())
    reverse(t)
    print(t.get_min())
    