__author__ = 'Sanchayan'
import pickle

#basic functions for Reading , Writing data by pickel
		
		
class table(object):
	def __init__(self,name):
		self.P={}
		self.name = name
		self.Populate_Server_passwords()
	
	
	def Populate_Server_passwords(self):
		try :
			filename=self.name + '.p'
			with open(filename,"rb") as source:
				servers_present= pickle.load(source)
				
				#for server in servers_present:
				#	P[server.Servername]=Password_Store(server.Servername,server.password_list)
				self.P=	servers_present
				#print('Populate_Server_passwords',P)
			
		except IOError:
					print('Table is created:',self.name)
	
	
	def add_data(self,rowid,data):
		#Write_Server_info(rowid,data,self.name,self.P)
		filename= self.name + '.p'

		if len(self.P) != 0:
			
			if rowid in self.P :
				print('rowid file is present',rowid)
				if data not in self.P[rowid]:
					self.P[rowid].append(data)
					#print("password not Present")
				else: 
				
					print("data  Present")
			else:
				print('rowid is new entry ',rowid)
				self.P[rowid]=[data,]
		else:	
			self.P[rowid]=[data,]
	
		with open(filename,'wb') as target:
			pickle.dump(self.P,target)
		
	def read_data(self):
		print('table ',self.name,self.P)


	
if __name__== '__main__':
	t=table("Passwords")
	
	t.add_data('1.com','113')
	t.add_data('1.com','112')
	t.add_data('2.com','131')
	t.add_data('3.com','114')
	t.add_data('3.com','114')
	t.read_data()
	
	t1=table("Passwords1")
	
	t1.add_data('1.com','113')
	t1.add_data('1.com','112')
	t1.add_data('2.com','131')
	t1.add_data('3.com','114')
	t1.read_data()
	
	t2=table("Food")
	
	t2.add_data('veg','Allo')
	t2.add_data('NonVeg','chicken')
	t2.add_data('veg','patal')
	t2.add_data('veg','achar')
	t2.add_data('NonVeg','fish')
	t2.read_data()
	
	
    
