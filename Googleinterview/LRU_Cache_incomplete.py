class Node:
	def __init__(self,key,prev,next):
		
		self.prev = prev
		self.next = next
		self.key = key		
		
		
class LRUCache:

	def __init__(self,capacity):
		self.mx = capacity
		self.head = None
		self.tail = None
		self.cur = 0 
		self.store = {}
		self.link =  {}

	def get(self):
		print(self.store)
		print(self.link)

		
	def set(self,key,value):
		#If the Max is not 0 
		if self.mx > 0 :
			if self.cur == 0:
				n = Node(key,None,None)
				self.head = n
				self.tail = n
				self.store[key]= value
				self.link[key]=n
				self.cur +=1
				self.mx -=1
			else:
				if key not in self.store:
					pn = self.tail 
					n= Node(key,pn,None)
					pn.next = n 

					self.tail = n
					self.store[key]= value
					self.link[key]=n
					self.cur +=1
					self.mx -=1
				else:
					print("key is found replace the value ")
					return -1

		elif self.mx ==0 :
			k=self.head.key 
			hn = self.head.next
			n = Node(key,None,hn)
			self.head = n
			self.store.pop(k)
			self.link.pop(k)
			self.store[key]= value
			self.link[key]=n
			self.cur +=1
		

if __name__ == '__main__':
    #unittest.main()
    b = LRUCache(3)
    print(b.set(3,"3"))
    print(b.set(2,"2"))
    print(b.set(1,"1"))
    b.get()
    '''
    print(b.get(3))
    print(b.get(2))
    print(b.get(1))
    print(b.set(4,"4"))
    print(b.get(3))
	'''