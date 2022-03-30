from os import read

#Declare 
d={}
file = open("log.txt")
s = None
with file as f:
    s= f.read()
    #print(s)

for i in s.split("\n"):
    #print("Line",i)
    List_items = i.split(" ")
    if len(List_items) > 1:
        #print(List_items)
        if List_items[2] not in d :
            g= {}
            
            g[List_items[0]]=1 
            d[List_items[2]]= g
        else:
            if List_items[0] in  d[List_items[2]]:
                d[List_items[2]][List_items[0]]= d[List_items[2]][List_items[0]] + 1
            else:
                 d[List_items[2]][List_items[0]]=  1
                


f = {}
for i,v in d.items():
    #print(i,v)
    for j,k in v.items():
        print(i,j,k)   

