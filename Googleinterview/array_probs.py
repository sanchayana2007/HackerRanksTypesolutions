#Stack yusing List 
def sum_pair_N2(arr,sum):
    for i in range(len(arr)-1):
        for j in (i+1,len(arr)-1):

            s=arr[i] + arr[j] 
            #  print(s)
            if sum == s:
                print(arr[i],arr[j])
                print("found")
                return s   
    return 0                      

def sum_pair_NLogN(arr,sum):
    d = {}
    
    for i in range(len(arr)):
        
        s= sum - arr[i]
        
        d[arr[i]]= i
        
        if s in d:
            print(s, arr[i] )
            return 
        print(s,d,i,len(arr)-1)    
            
            
if __name__=="__main__":
        arr = [640, 34, 25, 12, 22, 90, 80]
        print(sum_pair_N2(arr,170))
        
        print(sum_pair_NLogN(arr,170))
        