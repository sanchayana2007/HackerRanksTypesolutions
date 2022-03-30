

class Solution:
    def can_assign(self, A, B, val):
        #print("V",val,"B",B)
        if B > len(A):
            return False
        sum_pages = 0
        for num in A:
            #print(val,B)
            if B == 0:
                return False
            if sum_pages + num <= val:
                sum_pages += num
            elif num <= val:
                sum_pages = num
                B -= 1
            else:
                return False
        return B > 0 and sum_pages <= val
    
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        # edge cases
        if B == 0 and len(A) == 0:
            return 0
        if B == 0 and len(A) > 0:
            return -1
        
        # binary search
        left = 0
        right = sum(A)
        while left <= right:
            mid = (left + right) // 2
            if self.can_assign(A, B, mid):
                right = mid - 1
            else:
                left = mid + 1
            print("R",right,"M", mid,"L",left)        
        if self.can_assign(A, B, left):
            return left
        return -1
 
A = [1,2,3,4]
B = 2
s = Solution()
print(s.books(A,B))