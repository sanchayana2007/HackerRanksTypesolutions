
## fibonnaci 1
def fibonacci():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a + b
fib = fibonacci()
[fib.next() for i in range(10)]



## palendrome


## 
## patterns in String Search 


if __name__=='__main__':
  fibonacci()
