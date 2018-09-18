from collections import OrderedDict 

class Limit_Order_Book():
	def __init__(self):
		self.Buy_dict={}
		self.Sell_dict={}

	def add_to_book(self,order):
		print(order)
		if order[1]=="Buy":
			#Check in Sell
			quantity = self.Sell_Check(order[0],order[4],order[2])
			if quantity:
				self.Buy_dict[order[0]]=(order[4],quantity)
		elif order[1]=="Sell":
			#Check in Buy 
			quantity = self.Buy_Check(order[0],order[4],order[2])
			if quantity:
				 self.Sell_dict[order[0]]=(order[4],quantity)
		elif order[1]=="Cancel":
			#Check in Buy
			self.cancel_order(order[0]) 


	def Sell_Check(self,ID,price,quantity):
		allfilled=[]
		prev_quantity =quantity
		for item in self.Sell_dict.items():
			if item[1][0] <=price:
				#As the price is same or less
				leftitem = item[1][1]-quantity
				if leftitem > 0:
					self.Sell_dict[item[0]]=(item[1][0],leftitem)
					print("Fully matched with ",item[0],"(",quantity,"@",item[1][0],")")
					quantity=0
				elif leftitem <0:
					quantity=abs(leftitem)
					print("Partially matched with ",item[0],"(",item[1][1],"@",item[1][0],")")
					allfilled.append(item[0])
				else:
						
					print("Fully matched with ",item[0],"(",item[1][1],"@",item[1][0],")")
					allfilled.append(item[0])
					quantity=0
		for i in allfilled:
			del self.Sell_dict[i]
		if prev_quantity ==quantity:
			print("OK")
		return quantity	


	def Buy_Check(self,ID,price,quantity):
		allfilled=[]
		prev_quantity =quantity
		#print("*****Buy dict", self.Buy_dict)
		# Make priority to Best Buying Price
		sorted_by_value =OrderedDict(sorted( self.Buy_dict.items(), key=lambda t: t[1][1],reverse=True))
		for item in sorted_by_value.items():
			if item[1][0] >=price:
				#As the price is same or more
				leftitem = item[1][1]-quantity
				if leftitem > 0:
					self.Buy_dict[item[0]]=(item[1][0],leftitem)
					print("Fully matched with ",item[0],"(",quantity,"@",item[1][0],")")
					quantity=0
				elif leftitem <0:
					quantity=abs(leftitem)
					print("Partially matched with ",item[0],"(",item[1][1],"@",item[1][0],")")
					allfilled.append(item[0])
				else:
						
					print("Fully matched with ",item[0],"(",item[1][1],"@",item[1][0],")")
					allfilled.append(item[0])
					quantity=0
		for i in allfilled:
			del self.Buy_dict[i]
		if prev_quantity ==quantity:
			print("OK")
		return quantity	

	def cancel_order(self,id):
		if id in self.Buy_dict:
			del self.Buy_dict[id]
			print('OK')
		elif id in self.Sell_dict:
			del self.Sell_dict[id]
			print('OK')
		else:
			print("No Such Active Item")
			
if __name__=="__main__":
	a = Limit_Order_Book()
	c=["AAA","Buy",10,"@",10]
	a.add_to_book(c)
	c=["BBB","Buy",12,"@",12]
	a.add_to_book(c)
	c=["CCC","Buy",14,"@",14]
	a.add_to_book(c)
	c=["CCC","Cancel"]
	a.add_to_book(c)
	c=["DDD","Sell",10,"@",15]
	a.add_to_book(c)
	c=["EEE","Sell",2,"@",12]
	a.add_to_book(c)
	c=["FFF","Sell",4,"@",12]
	a.add_to_book(c)
	c=["GGG","Sell",10,"@",12]
	a.add_to_book(c)
	c=["BBB","Cancel"]
	a.add_to_book(c)
	c=["HHH","Buy",14,"@",12]
	a.add_to_book(c)
	c=["KKK","Sell",20,"@",10]
	a.add_to_book(c)
	c=["DDD","Cancel"]
	a.add_to_book(c)
	c=["DDD","Cancel"]
	a.add_to_book(c)
	 	
