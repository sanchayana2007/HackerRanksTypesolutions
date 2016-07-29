## 1
## Use of Global Variable :
## if Any variable is declared at a Global Scope it only keeps the global Value
var_global=1
var_global1=1

def global_change():
  var_global=10
  
  global var_global1
  var_global1=1
 
def global_print():
  print(var_global) ## prints 1 although changed
  print(var_global1)## prints 10
  
  
##Reason : In python the variable is var_global as intantiated inside the function  Python creates
## a local variable that shadows the global variable of the same name That local goes out of scope
## and is garbage-collected when global_change() returns; meanwhile, global_print() can never see anything other than 
## the (unmodified) var_global but as soon global is with var_global1 the global varibale is used .
  
  
if __name__=="__main__":
  global_change()
  global_print()
