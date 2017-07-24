import csv
import time
import re
from time import clock
from collections import deque,defaultdict
import os


class Excel():
	summary_list=[]
	liecycles_list=[]
	repo=[]
	total_count=0
	dellhosts=[]
	hphosts=[]
	ibmhosts=[]
	oraclehosts=[]
	
	def __init__(self,filename=None):
		self.excel_filename=filename
		self.groups= defaultdict(list)
		self.ungroupdata=[]
		self.load_excel()
		
	
		
		
	def get_last_row(self,filename):
		with open(filename,'r') as f:
			return (deque(csv.reader(f),1)[0])
			
					
					
	def check_SRS(Manufacturer):
		def row_present(x): return x
		
		if re.search(Manufacturer,"Dell"):
			return len([row_present(True) for dellhost in dellhosts if (host.upper()+type.upper())== dellhost[0]])
			
			
	def csv_writer(filename,data):
		with open(filename,"w",newline="") as csv_file:
			writer=csv.writer(csv_file)
			writer.writerows(data)
			
	def load_excel(self,group_by=None):
		last_row=self.get_last_row(self.excel_filename)
		valid_rows=[]
		
		header=[]
		counter=0
		with open(self.excel_filename,'rt',encoding='utf-8') as f:
			reader = csv.reader(f)
			for index,row in enumerate(reader):
				counter+=1
				if index == 0:
					header.append(row)
					continue
				if group_by:
					#Lets group by the data for more faster search
					if row[group_by] not in self.groups.keys():
						self.groups[row[group_by]]=row
					else:
						self.groups[row[group_by]].append(row)
				else:
					print("group_by None is not implemented")
					self.ungroupdata.append(row)
				
					
				
				#print(self.groups.keys)
				valid_rows.append(row)
				
				#if re.search(row[11],"Dell"):
					#if check_SRS("Dell",row[0],row[12]):
						#valid_rows.append(row)
			print(self.groups.items())
			print(self.ungroupdata)
			#valid_rows=sorted(valid_rows,key=itemgetter(4))
			valid_rows=header+ valid_rows
			#print(valid_rows)
			#csv_writer("Output"+Missing_filename,valid_rows)
		

	
		
if __name__=="__main__":
	start= clock()
	file1=Excel('test1.csv')
	end=clock()
	print("Time taken",end -start)



