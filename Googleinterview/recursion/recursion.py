import datetime
def memoize_factorial(f):
    memory = {}
  
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:         
            memory[num] = f(num)
        return memory[num]
  
    return inner



@memoize_factorial
def fib(n):
	if n == 1:
		return n 
	else:
		return fib(n) * fib(n-1)  \
	

def gritraveller(m,n):
	if m == 1 and n ==1 : 
		return 1
	else:
		m == 1 or n ==1 :
		return 1
	
	return gritraveller(m -1 , m )  * 


# Function to find a pair in an array with a given sum using hashing
if __name__=="__main__":
	start = datetime.datetime.now()
	print(fib(6))
	end =  datetime.datetime.now()
	print(end - start)