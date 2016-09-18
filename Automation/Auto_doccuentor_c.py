import sys
from os import walk,listdir
from os.path import isfile, join
import logging
import time
import re 
timestr=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
LOGFILENAME= "Password_change" + timestr + ".log"

from sys import platform
if platform == "linux" or platform == "linux2":
	print("Not Optimised for Linux System Need to be tested")
	#exit(1)
elif platform == "win32" :
	print("Not Optimised for Windows")
	exit(1)
elif platform == "sunos5":
	print("Solaris is Supported ")
else:
	print("Didnt got the OS Exiting .....")
	exit(1)


def files_collector():
	files=[]
	pathnames=[]
	dirnames=[]
	Src = '/home/san/quagga-0.99.19/'
    	for (paths,dirnames,filenames)in walk(Src):
		print("Number of Modules", len(dirnames))
		for dir in dirnames:
 			#print("dir",dir)   
			path=paths+dir
			onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		#	print("filenames",onlyfiles) 
			h_pat=re.compile(r'.h')
			C_pat=re.compile(r'.C')
			c_pat=re.compile(r'.c')
			h_files=[]
			c_files=[]
			for filename in onlyfiles:
			#	print(filename)
				if  filename.endswith('.h'):
					h_files.append(filename)
				elif filename.endswith('.c') or filename.endswith('.c'):
					c_files.append(filename)
			if len(h_files) !=0:
				print("Module Name:",dir)
				print("Module Name:",path)
				print('h files',h_files)

				print('c files',c_files)			
   		break
			
def open_parse_file():
	filename='/home/san/quagga-0.99.19/isisd/isis_pdu.h'	
	contents=None
	with open(filename,'r') as f:
        	contents=f.read()
		print(contents)
	#Parse Diagrams Logic 
	pat=re.compile(r'/\*([^*]|[\r\n])*\*/')
	contents=pat.findall(contents) 
	print(contents)
	#Parse comments 
	#Parse Structure

def main():
	#files_collector()	
    	open_parse_file()
if __name__ == '__main__':
	main()                                                                                                                    
