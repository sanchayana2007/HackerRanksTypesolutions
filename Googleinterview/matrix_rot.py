class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
       print(len(A))
       print(zip(*A[::-1]))
       print ([[A[j][i] for j in range(len(A))] for i in range(len(A[0])-1,-1,-1)])

if __name__=="__main__":
        L=Solution()
        L.rotate([[1,2,3],[4,5,6],[7,8,9]])

