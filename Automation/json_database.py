__author__ = 'Sanchayan'
import json 
class saveonjasondb(object):
	def __init__(self,name):
		self.P={}
		self.dev_name = name + '.jd'
		self.load_old_jd()
		
	def load_old_jd(self):
		try :
			with open(self.dev_name) as source:
				self.P=json.load(source)
		except IOError:
			print("File is not there",self.dev_name)
			
			
	def commit(self,data):
		if len(self.P) !=0:
			if data['method']=='add':
				self.P['params'].append(data['params'])
			elif data['method'] == 'sub':
				for indx,intf in enumerate(self.P['params']):
					if intf[0]== data['params'][0]:
						del self.P['params'][indx]
		else:
			data['params']=[data['params']]
			self.P=data
		with open(self.dev_name,mode='w') as target:
			json.dump(self.P,target)
			
			
	def show(self):
		print('table',self.dev_name,self.P)
		
		
		
if __name__=='__main__':
	jstr1={'jsonrpc':'2.0','method':'add','id':14,'params':[1,2,3],'user':'sanchez'}
	jstr2={'jsonrpc':'2.0','method':'add','id':14,'params':[2,2,3],'user':'sanchez'}
	jstr3={'jsonrpc':'2.0','method':'add','id':14,'params':[3,2,3],'user':'sanchez'}
	jstr4={'jsonrpc':'2.0','method':'sub','id':14,'params':[3,2,3],'user':'sanchez'}
	dev1=saveonjasondb('Device1')
	dev1.commit(jstr1)
	dev1.commit(jstr2)
	dev1.commit(jstr3)
	dev1.commit(jstr4)
	dev1.show()
						
				