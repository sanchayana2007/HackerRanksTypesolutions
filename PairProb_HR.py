# coding: iso-8859-1
#Given N integers, count the number of pairs of integers whose difference is K.
def hr_8_31_15():
    '''Complexity:
        time complexity is O(N*log(N))
        space complexity is O(N)
    '''
    a = [1.2,3,4.5,5,6]
    b = map(int,a)
    #Actually this steps make tghe search as logn time as of tree
    c= set(b)
    print (b)# At this point Map object b which a Iterator which comes from generators is exhausted
    for i in b:
        print(i)
    print(pairs(c,2))

def pairs(a,k):
    answer =0
    for v in a:
        # here the search in the Tree takes palce so N.LogN time
        if v+k in a:
            answer+=1
    return answer
