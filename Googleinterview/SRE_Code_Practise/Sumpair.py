def sumpair(arr,val):
    d = {}
    com= {}
    foundlist=[]
    for ind,i in enumerate(arr):
        
        d[val - i] = (i,ind)
        if i in d:
            print("Found")
            if d[i][1] < ind:
                foundlist.append(((i,ind) ,d[i]))
    print(foundlist)
    if len(foundlist) == 0 : 
        print("Not Found")

if __name__ == "__main__":
    a= [1,2,3,5]
    sumpair(a,8)
    a= [1,2,4,4]
    sumpair(a,8)    