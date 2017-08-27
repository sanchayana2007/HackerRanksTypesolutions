def printActivities(s,f):
        n=len(f)
        f_sorted=sorted(f)
        i=0
        for ind,itm in enumerate(s):
                if f_sorted[i] <= s[ind] or ind==0:
                        i=ind
                        print(f_sorted[i])


# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printActivities(s , f)
