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
	def __len__(self):
		return len(self.item)	
	def pop(self):
		pop_item=self.item[:1]
		l=len(self.item)
		self.item=self.item[1:]
		return pop_item	
	 
class HCT:
	def __init__(self,items,Freq):
		self.pq=PQ(items,Freq)
		print("deded")	

	def makehct(self):
		while len(self.pq):
			p1=self.pq.pop()
			p2=self.pq.pop()
			print(len(self.pq),p1,p2)
					
			node=Minheapnode('int_node',p1+p2,p1,p2)
			self.pq.add_node(node)
			
			
	

if __name__=="__main__":
	p=HCT(['c','b','a','h'],[3,2,1,6])
	p.makehct()
	
x
