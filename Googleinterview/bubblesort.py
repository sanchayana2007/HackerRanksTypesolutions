#Stack yusing List 
class Bubble:
    def __init__(self,arr):
        self.array= arr
        self.len = len(arr)
    def sort(self):
        # we can be happy with l -1 as j reaches j+1 = max length when i =0 
        for i in range(self.len -1):
            #print("i",i)
            for j in range(self.len- i -1 ):
                #print("J",j)
                #print(self.array)
                if self.array[j] >  self.array[j +1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1] 
                    self.array[j +1] = temp
        return self.array

    def sort1(self):
            # we can be happy with l -1 as j reaches j+1 = max length when i =0 
            for i in range(self.len -1):
                #print("i",i)
                for j in range(i+1, self.len -1 ):
                    #print("J",j)
                    #print(self.array)
                    if self.array[i] >  self.array[j]:
                        temp = self.array[j]
                        self.array[j] = self.array[i] 
                        self.array[i] = temp
            return self.array

            

    
if __name__=="__main__":
        arr = [640, 34, 25, 12, 22, 90, 80]
        
        L=Bubble(arr)
        print(L.sort())
        print(L.sort1())
        