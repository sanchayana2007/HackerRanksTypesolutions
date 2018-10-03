from collections import deque
class Graph:
	def __init__(self):
		self.Nodes={}
		self.root=None

	def add(self,node1,node2,wht):
		if not self.root:
			self.root=node1
		if node1 not in self.Nodes:
			l=[(node2,wht)]
			self.Nodes[node1]=l

		else:
			self.Nodes[node1].append((node2,wht))

	def display(self):
		print(self.Nodes)
	#You can always enter a search element and return from the function 
	#  Time: Space >  O(V + E) : O(V + E)   V= vertexes E = Edges 
	def bfs(self,node):
		print("BFS")
		temp=self.root
		d=deque(temp)
		count=1
		while d:
			s=d.pop()
			if s in self.Nodes:
				for n in self.Nodes[s]:
					print("In level",count,"parent",s,"member",n[0])
					if node==n[0]:
						print("FOUND")
					d.appendleft(n[0])
				count+=1

	#  Time: Space >  O(V + E) : O(V + E)   V= vertexes E = Edges 
	def dfs(self,node):
		print("DFS")
		temp=self.root
		d=deque(temp)
		count=1
		while d:
			s=d.popleft()
			print("In Depth",count,"memebr",s)
			if node ==s:
				print("FOUND")
			if s in self.Nodes:
				for n in self.Nodes[s]:
					d.appendleft(n[0])
				count+=1
			else:
				count-=1


a=Graph()
a.add('a','b',1)
a.add('a','c',1)
a.add('a','a1',1)
a.add('b','b1',1)
a.add('b','b2',1)
a.add('b','b3',1)
a.add('c','c1',1)
a.add('c','c2',1)
a.add('c2','c3',1)
a.add('c3','c4',1)
a.add('c','c3',1)
a.display()
a.bfs('c2')
a.dfs('c4')
# Bfs : Use in Distributions of an amount in a hierchy 
# Water in connected tanks pipelined 

