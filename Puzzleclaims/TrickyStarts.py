import sys

## 1
## Use of Global Variable :
## if Any variable is declared at a Global Scope it only keeps the global Value
var_global=1
var_global1=1

def global_change():
  var_global=10
  
  global var_global1
  var_global1=10
 
def global_print():
  print(var_global) ## prints 1 although changed
  print(var_global1)## prints 10
  
  
##Reason : In python the variable is var_global as intantiated inside the function  Python creates
## a local variable that shadows the global variable of the same name That local goes out of scope
## and is garbage-collected when global_change() returns; meanwhile, global_print() can never see anything other than 
## the (unmodified) var_global but as soon global is with var_global1 the global varibale is used .


##2
## Defajlt Argumnt keeping as Static
## Also note that def is an executable statement in Python, and that default arguments are evaluated in
## the def statements environment. If you execute def multiple times  it ll create a new function
## object (with freshly calculated default values)
## each time


def default_list(a=[]):
  if a is None:
      a=[]
  a.append(6)
  return  a
## To get the Desired o/P
def default_list_fixed(a= None):
  if a is None:
      a=[]
  a.append(6)
  return  a


#3
## Nested Loop Issue it
def Loop():
  for i in range(10):
    def callback():
      print ("clicked button", i)
    print("button %s" % i, callback)

## 3
## he same object is modified in the function.
def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))

if __name__=="__main__":
  global_change()
  global_print()

  a=default_list()
  print(a)
  b=default_list()
  print(b)

  Loop()

