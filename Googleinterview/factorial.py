#Stack yusing List 
def factorial(n):
    #print(n)
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def factorial1(n):
    #print(n)
    if n ==  1:
        return n 
    else:
        n = n *  factorial(n-1)
        return n


def factorialwr(n):
    fact = 1
    for num in range(2, n + 1):
        #print(num)
        fact *= num
    return fact



if __name__=="__main__":
    print(factorial(4))
    print(factorialwr(4))
    print(factorial1(4))