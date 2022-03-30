
class Solution:
    # @param A : integer
    # @return a list of integers

    def solve(self, A, B):
        
        s = 0 
        for i in range(B):
            
            s += A[len(A)-1 -i]
          
        max_sum = s
        
        #Getthe 1st element form the list
        for idx in range(B):
            s = s - A[len(A)-1 -idx] + A[idx]
            
            if s > max_sum:
                max_sum = s
        print(max_sum)
    

if __name__ == "__main__":
    A= Solution()
    A.solve([3,4,1,2,6],2)

