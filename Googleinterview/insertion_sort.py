#Stack yusing List 
class Insertion:
    def __init__(self,arr):
        self.arr= arr
        self.len = len(arr)
    def sort(self):
           # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j >=0 and key < self.arr[j] :
                    print(i,j)
                    self.arr[j+1] = self.arr[j]
                    
                    self.arr[j] = key
                    j -= 1
            print(self.arr)

if __name__=="__main__":
        arr = [64, 34, 25, 12, 22, 11, 90]
        L= Insertion(arr)
        print(L.sort())
        