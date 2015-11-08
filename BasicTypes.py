
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
## patterns in String Search 


if __name__=='__main__':
	fib = fibonacci()
	#[print(fib.__next__()) for i in range(10)]
	#print(fibonaci2(10))
	print(prime_numbers(10))
	print(power2_new(8))