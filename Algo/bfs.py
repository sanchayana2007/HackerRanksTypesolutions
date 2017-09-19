class queue:
	def __init__(self):	
		self.data=[]

	def pop(self):
		l=len(self.data)
		pop_data=self.data[l-1]
		self.data=self.data[:l-1]
		return pop_data

	def push(self,item):
		self.data.insert(0,item)
	def __len__(self):
		return len(self.data)
	def __str__(self):
		return " ".join("{0}->".format(itm) for itm in self.data)


def rotten_check(rotten_it):
	i=j=0
	rotQ=queue()
	for itm in rotten_it:
		for subitm in itm:
			if subitm ==2:
				print("2",i,j)
			j+=1
		i+=1

if __name__=="__main__":
	rotten_it=[[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
	rotten_check(rotten_indx)
