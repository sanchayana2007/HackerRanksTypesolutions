__author__ = 'Sanchayan'
import pickle
P={}
class Password_Store(object):
	def __init__(self,Servername,passwords_list):
		self.Servername = Servername
		self.password_list=passwords_list
		
	def append_password(self,password):
		if password in password_list:
			
			return False
		else:
			password_list.append(password)
			return True	



def Populate_Server_passwords():
	try :
		with open("Passwords.p","rb") as source:
			servers_present= pickle.load(source)
			
			#for server in servers_present:
			#	P[server.Servername]=Password_Store(server.Servername,server.password_list)
			P=	servers_present
			print('Populate_Server_passwords',P)
		
	except IOError:
				print('password keeping file is deleted or You dont havent kept it as Now')
		
		
	

def Write_Server_info(servername,password):
	if len(P) != 0:
		
		if servername in P :
			print('Serevr file is present',servername)
			if password not in P[servername]:
				P[servername].append(password)
				print("password not Present")
			else: 
			
				print("password  Present")
		else:
			print('Serevr is new entry ',servername)
			P[servername]=[password,]
	else:	
		P[servername]=[password,]

	with open('Passwords.p','wb') as target:
		pickle.dump(P,target)

	
if __name__== '__main__':
	Populate_Server_passwords()
	'''
	Write_Server_info('1.com','11')
	Write_Server_info('12.com','112')
	Write_Server_info('12.com','113')
	Write_Server_info('12.com','115')
	Write_Server_info('13.com','113')
	Write_Server_info('14.com','114')
	'''

    # The pickel object Load will produce the same as normal object
    
