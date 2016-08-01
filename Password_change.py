import sys
import os 
import logging
import time

timestr=time.strftime()
LOGFILENAME= "Password_change" + timestr + ".log"
if os.isfile(LOGFILENAME):
  os.remove(LOGFILENAME)
  
from sys import platform
if platform == "linux" or platform == "linux2":
  print("Not Optimised for Linux System Need to be tested")
  exit(1)
elif platform == "win32 :
  print("Not Optimised for Windows")
  exit(1) 
elif platform == "sunos5":
  print("Solaris is Supported ")
else:
  print("Didnt got the OS Exiting .....")
  exit(1)
  
  
import imp
try :
  imp.find_module(pxpect)
  from pexpect import *
expect ImportError:
  print("No pexpect Module is found")
  
def process_arg():  
  import optparse import OptionParser
  usage = "Password_change.py -f Filename"
  parser=Optionparesr(usage)
  parser.add_option("-f", dest="filename",help="File Name")
  return parser.parseargs(sys.argv)
  
def exceptionCheck(row):
  Servername=row[0]
  Username=row[1]
  OldPasswd=row[2]
  NewPassword=row[3]
  
  if not Servername or Servername.isspace():
    print("Servername Not Found")
    logging.error('ERROR as SERVERNAME Not NOT FOUND')
    return False
  eif not Username or Username.isspace():
    print("Username Not Found")
    logging.error('ERROR as USERNAME Not NOT FOUND')
    return False
  eif not OldPasswd or OldPasswd.isspace():
    print("OldPasswd Not Found")
    logging.error('ERROR as OLDPASSWORD Not NOT FOUND')  
    return False
  eif not NewPassword or NewPassword.isspace():
    print("NewPassword Not Found")
    logging.error('ERROR as NEWPASSWORD Not NOT FOUND') 
    returm False
  else:
    return True


def LogServers(row):
  Servername=row[0]
  Username=row[1]
  OldPasswd=row[2]
  NewPassword=row[3]
  
  ServerLogonStr= "ssh " + Username + "@" + Servername
  cmnd= "set /SP/users" + Username + " password="+NewPassword
  child=spawn(ServerLogonStr)
  try:
    child.expect('(?)Password',timeout=60)
    t=child.sendline(OldPasswd)
    i=child.expect(['->','(?)Password'])
    if i ==0:
      t=child.sendline(cmnd)
      child.expect("(?)again:")
      child.sendline(NewPassword)
      child('->')
      print(child.before)
      logging.debug('Password Changed from %s to %s',OldPasswd,NewPassword)
      
    else:
      logging.error("Wrong username or password ")
    child.sendline(exit)
    child.close()
  except Exception as e:
    logging.error("The Server has TIME OUT ")
    
  
  def process_file(filename):
    if filename == None:
      print('No file provided')
      logging.error('NO FILE PROVIDED ')
    elif path.isfile(filename):
      import csv 
      
      try :
      
        f = open(filename,'rt')
        reader=csv.reader(f)
        count=0
        for row in reader:
          count = count = 1
          print('Server No: %s',count)
          logging.debug('logging in Server : %s  with IP %s', count , row[0])
          if exceptionCheck(row):
            LogServers(row)
      except IOError:
        logging.error('Error in reading File ')
      finally :
        f.close()
    else:
      logging.error('Reading failed ')
      
if __name__=="__main__":
  (opt,args)=process_arg()
  process_file(opt.filename)
  
          
      
      
  
