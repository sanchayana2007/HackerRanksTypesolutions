class LRUCache:
    

    # @param capacity, an integer
    def __init__(self, capacity):
        
        self.mx=capacity
        self.cur_cap=0
        self.store={}
        self.linked={}
        self.head=None
        self.tail=None
    
    # @return an integer
    def get(self, key):
        if self.mx==0:
            return -1
        if key not in self.store:
            return -1
        #get the double LL prev and next val from the Node(key) 
        l=self.linked
        bef=l[key]['prev']
        aft=l[key]['next']
        #This key is not the First in List 
        #Cut the Node as we need to put that in front 
        
        if bef!=None:
            l[bef]['next']=aft
            if aft!=None:
                l[aft]['prev']=bef
            else:
                self.tail=bef
            head=self.head
            # current Key  next is set has head 
            # Current key is new head 
            l[key]={'next':head,'prev':None}
            l[head]['prev']=key
            
            self.head=key
        return self.store[key]
    
    
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.mx!=0:
            #if the key is not prsent   
            if key not in self.store:
                # handle the first elment creation 
                if self.cur_cap==0 or self.mx==1:
                    self.linked={}
                    self.store={}
                    self.linked[key]={'next':None,'prev':None}
                    self.store[key]=value
                    self.cur_cap=1
                    self.head=key
                    self.tail=key
                #handle teh 2nd and more element creation 
                elif self.cur_cap<self.mx:
                    self.store[key]=value
                    head=self.head
                    l=self.linked
                    l[head]['prev']=key
                    l[key]={'next':head,'prev':None}
                    self.head=key
                    self.cur_cap+=1
               #the List is full now and we have to create space
               # Pop the item from Hash and Tail next as None
               # Set the Head as a new entry and keep it that 
                else:
                    tail=self.tail
                    l=self.linked
                    pn=l[tail]['prev']
                    if tail in self.store:
                        self.store.pop(tail)
                    l.pop(tail)
                    l[pn]['next']=None
                    head=self.head
                    l[head]['prev']=key
                    l[key]={'next':head,'prev':None}
                    self.store[key]=value
                    self.head=key
                    self.tail=pn

            #If the key is found in hash update the key with new value in hash
            # if mx capacity is more then 1 then 
            # remove the item from teh linked list 
            #Set the LL as the new node 

            else:
                self.store[key]=value
                if self.mx!=1:
                    l=self.linked
                    bef=l[key]['prev']
                    aft=l[key]['next']
                    if bef!=None:
                        l[bef]['next']=aft
                        if aft!=None:
                            l[aft]['prev']=bef
                        else:
                            self.tail=bef
                        head=self.head
                        l[key]={'next':head,'prev':None}
                        l[head]['prev']=key
                        self.head=key


if __name__ == '__main__':
    #unittest.main()
    b = LRUCache(3)
    print(b.set(3,"3"))
    print(b.set(2,"2"))
    print(b.set(1,"1"))
    print(b.get(3))
    print(b.get(2))
    print(b.get(1))
    print(b.set(4,"4"))
    print(b.get(3))

