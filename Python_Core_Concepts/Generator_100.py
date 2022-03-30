__author__ = 'Sanchayan'
import timing

## Basic Generator
def Basic_gen(N):
    x = 0
    while N:
        x = x +1
        yield x
        N = N -1

#Generator of a List Comprehension Pretty useless although
def f():
    y = [ (yield x) for x in range(1,28)]
    print(y)

# making Yeild to Receivee a value
def yield_rcv_val():
    ''' Needed a Send mthd'''
    while True:
        item = yield
        print('Got this item',item)

# Making a yeild and a Return in same function
def yield_return():
    yield 'yield value'
    return 'return Value'

# Yield from to delegate the value of the generator to Another
def yield_from():
    yield 'yield value'
    return 'return Value'

# Chain Functionality in Yield from
def chain(x,y):
    yield from x
    yield from y

if __name__ == "__main__":
## Basic Generator
    '''
    w =  (i for i in Basic_gen(3))
    print('Basic Gen',Basic_gen(3),'Generator Exprsion',w)
    # Generators can be used as Comprehensions or using Next
    print([i for i in w])
    iter = Basic_gen(3)
    print(next(iter))
    print(next(iter))
    '''

# making Yeild to Receivee a value
    v = yield_rcv_val()
    next(v)
    v.send(80)

# Making a yield and a Return in same functn
    v = yield_return()


# Yield from to delegate the value
    def yldfromchck ():
        v = yield from yield_return()
        print(v)
    yldfromchck()

# Multi Yields for Chanining two lists together and finding the value
    for n in chain([1,2,3,],[4,5,6]):
        print(n)