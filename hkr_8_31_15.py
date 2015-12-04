__author__ = 'Sanchayan'
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
# coding: iso-8859-1
'''Given two strings a and b of equal length, whats the longest string (S) that can be constructed such that it is a child of both?
A string x is said to be a child of a string y if x can be formed by deleting 0 or more characters from y.'''

   def lcs(S,T):

    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set


def hr_8_30_15():
	# test 1
	ret = lcs('academy', 'abracadabra')
	for s in ret:
		print s
	python_solutions.php
	# test 2
	ret = lcs('ababc', 'abcdaba')
	for s in ret:
		print s



if  __name__ == '__main__':
    #hr_8_31_15()
    print(hr_8_30_15())
    print(long_substr())
