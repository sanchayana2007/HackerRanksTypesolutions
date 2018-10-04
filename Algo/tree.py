#This tree stores the value per index
def createnode(node,key,val):
	if node is None: 
	
		return Node(key,val)
	elif key <= node.key:
		node.lft=createnode(node.lft,key,val)
	else:
		node.rht=createnode(node.rht,key,val)
	return node

def search(node,key):
	if node is None: return KeyError
	if key == node.key: return node.val
	elif key <= node.key:
		
		return search(node.lft,key)
	else:
		return search(node.rht,key)

class Node:
	lft=None
	rht=None

	def __init__(self,key,val):
		self.key =key
		self.value=val

class tree:
	def __init__(self):
		self.root =None
		self.count=0

	def add(self,key,val):
		self.count+=1
		self.root=createnode(self.root,key,val)


	#To avoid a seperate outside function one from call 
	# from object and other to pass root 

	def _print_tree(self,node):
		if node.key: print(node.key)
		if node.lft:
			print("Left",node.lft.key)
			return self._print_tree(node.lft)
		if node.rht:
			print("Right",node.rht.key)
			return self._print_tree(node.rht)


	def print_tree(self):
		self._print_tree(self.root)

	def count_nodes(self):
		return self.count 

	# InOrder Left > center > right 
	def _inorder(self,node):
		if not node.key: return 
		if node.lft:
			self._inorder(node.lft)
		print(node.key,node.value)
		if node.rht:
			self._inorder(node.rht)


	def inorder(self):
		print("IN ORDER")
		self._inorder(self.root)

	# Post Order Left > right > center 
	
	def _postorder(self,node):
		if not node.key: return 
		if node.lft:
			self._postorder(node.lft)
		
		if node.rht:
			self._postorder(node.rht)
		print(node.key,node.value)

	def postorder(self):
		print("POST ORDER")
		self._postorder(self.root)


def yes(ques):
	ans=input(ques).lower()
	return ans[0]=='y'


def decsion_tree(t):
	m=tree()
	counter =2
	for i in t :
		if yes(i):
			counter+=1
			m.add(counter,i)
		else:
			counter-=1
			m.add(counter,"Something else")
	m.inorder()


s=tree()
s.add(2,'a')
s.add(4,'a')
s.add(3,'a')
s.print_tree()
s.inorder()
s.postorder()
