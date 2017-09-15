class Minheapnode():

        def __init__(self,data,freq,left=None,right=None,top=None):
                self.data=data
                self.freq=freq
                self.left=left
                self.right=right
                self.top=top

        def __str__(self):
                return "Data: {0} and freq: {1}".format(self.data,self.freq)


#Piority Queue baed on Min frequency the Items are arranaged 

class PQ():
        def __init__(self,items,freq):
                ln=len(items)
                item=sorted([(items[count],freq[count]) for count in range(ln)],key=lambda x:x[1])
                self.item=[(itm[0],itm[1]) for indx,itm in enumerate(item)]

                print(self.item)
        def __str__(self):
                return "\n".join(" Item: {0} freq: {1}".format(itm[0],itm[1]) for itm in self.item)

        def add_node(self,int_node):
                self.item.append((str(int_node),int_node))
                ln=len(self.item)
                self.item=sorted([(self.item[count],self.item[count]) for count in range(ln)],key=lambda x:x[1])


        def pop(self):
                pop_item=self.item[:1]
                l=len(self.item)
                self.item=self.item[1:]
                return pop_item



if __name__=="__main__":
        p=PQ(['c','b','a','h'],[3,2,1,6])
