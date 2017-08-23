
class Node:
	
	def __init__(self,data,pointer=None):
		self.data=data
		self.pointer=pointer

	
class Linkedlist:
	def __init__(self,node=None):
		self.root=node
		
	def append(self,data):
		new_node=Node(data)
		new_node.pointer=None
		if self.root== None:
			
			self.root= new_node
		else:
			temp=self.root
			while temp.pointer != None:
				temp=temp.pointer
			temp.pointer=new_node
	def 


	def dispaly(self):
		temp=self.root
		while temp != None:
			print(temp.data)
			temp=temp.pointer
	
if __name__=="__main__":
	L=Linkedlist()
	L.append(1)
	L.append(2)
	L.append(3)
	L.dispaly()
