def check_count(c):
        l=[]
        count=1
        su=0
        res=0
        for ind,itm in enumerate(c):
                for i in range(ind,count):
                        l.append(c[i])
                        count+=1
                #print(l)
                for j in l:
                        su= j | su
                #print(su)
                res=res+su
        return res


if __name__=="__main__":
        c=[1,2,3,4,5]
        #n=input()
        
        #j=input()
        #l=list(map(int, j.split()))
	l=c
	n=5
        su =0
        for i in range(int(n)):
                su = su + check_count(l[i:])

        print(su)
