#Stack using List 

def swp(arr,k):
    sum =0 
    maxsum=0
    L = []
    for i in range(len(arr)-2):
        for j in range(i,i+3):
            sum+=arr[j]
            #print(k,i)
            L.append(arr[j])
            if maxsum <= sum:
                maxsum = sum
                print(L)
        sum = 0
                
        L.clear()
            
    return maxsum    


if __name__=="__main__":
        
        arr = [64, 34, 25, 12, 22, 12, 90]
        print(swp(arr,3))
        
        