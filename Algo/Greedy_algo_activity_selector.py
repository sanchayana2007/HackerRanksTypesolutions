def max_activity(S,E):
        print(E)
        print(S)
        d=[(itm,S[indx]) for indx,itm in enumerate(E)]
        Sorted_E= sorted(d,key=lambda x:x[0])
        l=len(d)
        i=0
        print(Sorted_E[i])
        for n in range(1,l):
                if Sorted_E[n][1] >= Sorted_E[i][0]:
                        print(Sorted_E[n])
                        i=n
                else:
                        i=n-1



if __name__=="__main__":
        A=[1,3,0,5,8,5]
        B=[2,4,6,7,9,9]
        max_activity(A,B)

