__author__ = 'Sanchayan'

if __name__ == "__main__":
    a = [1,1,2,2,2,2,7,7]
    a = [1,1,2,2,2,2,2,2,2,2,7,7,7,7,7,7]
    l =[]
    max = 0
    n = 1
    for i,val in enumerate(a):
        if i < len(a)-1:

            if a[i+1] == a[i]:
               # print(i , a[i+1], a[i])
                n = n+ 1
            else:
               # print('Non matching',i,a[i],n)
                l.append((i,a[i],n))
                if n >max:
                    max = n
                n = 1
        else:
            if n >max:
                    max = n
            l.append((i,a[i],n))
            #print(i,n,a[i])

    print(max)
    print(l)
