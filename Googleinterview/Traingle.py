class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, n):

        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            new_row = [1]
            result = self.getRow(n-1)
            #This last row forms the new row after operations
            last_row = result[-1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
            print("N", n, "result" , result, result[-1] ,"new_row",new_row)
            result.append(new_row)
        return result
 

class Ai:
    def tri(self, n, actualn=0 ):
        if n == 0:
            return [] 
        elif n == 1:
            return [[1]] 
        elif n < actualn:
            new = [1]
            res = self.tri(n-1,n)
            lr = res[-1]
            for i in range(len(lr) -1):
                new.append(lr[i ] + lr[i+1])
            new += [1]
            res.append(new)
            return res
        else:
            new = [1]
            res = self.tri(n-1,n)
            lr = res[-1]
            for i in range(len(lr) -1):
                new.append(lr[i ] + lr[i+1])
            new += [1]
            return new
           



if __name__ == "__main__":
    A= Solution()
    A.getRow(7)

    B= Ai()
    print(B.tri(7))
