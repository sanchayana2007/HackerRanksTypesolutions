from functools import  reduce
## fibonnaci 1
def fibonacci():
	a, b = 1, 1
	while True:
		yield b
		a, b = b, a + b

def fibonaci2(n):
	a, b = 0, 1
	l = []
	for i in range(n):
		a,b = b,a+b
		l.append(b)
	return  l
## palendrome


## prime number
def prime_numbers(n):
	if 0 in  [0 if n%i==0 else 1 for i in range(2,n-1)]:
		return  False
	else:
		return  True

# if N is a power of 2 or not
def power2(N):

    while N%2==0 and N > 1:
        N=N/2
    return N==1

def power2_new(n):
	return n & n-1 ==0

# Nearest Power of 2 Number
def Power2_lesserN(N):
	num = N
	while(num>1):
		num = num -1
		if not (num & num-1):
			print('Closet pow 2',num)
		return num

# Nearest power of 2 without Loops
def getClosestSmaller(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x |= x >> 32
    x = x + 1
    x = x >> 1
    return x
## patterns in String Search 

def factorial_1(n):
	if n == 1:
		return  1
	else:
		return  n * factorial_1(n-1)

def factorial_2(n):
	return reduce(lambda a,b: a*b, range(1,n+1))

if __name__=='__main__':
	#fib = fibonacci()
	#[print(fib.__next__()) for i in range(10)]
	#print(fibonaci2(10))
	#print(prime_numbers(10))
	#print(power2_new(8))
	print(factorial_1(4))
	print(factorial_2(4))

