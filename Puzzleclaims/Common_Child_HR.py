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

	# test 2
	ret = lcs('ababc', 'abcdaba')
	for s in ret:
		print s

if  __name__ == '__main__':
    #hr_8_31_15()
    print(hr_8_30_15())
