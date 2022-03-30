#Stack yusing List 
class List_stack:
    def __init__(self) -> None:
        self.stack=[]

    def push(self,ele):
        self.stack.append(ele)

    #Last inserted element 
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()    
        else:
            print("No element")
    def display(self):
        print(self.stack)

if __name__=="__main__":
        L=List_stack()
        L.push(1)
        L.push(2)
        L.push(3)
        L.display()
        L.pop()
        L.display()
        L.pop()
        L.pop()
        L.display()
        L.pop()
