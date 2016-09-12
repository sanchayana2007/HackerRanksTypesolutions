__author__ = 'Sanchayan'
'''
Inputs
1> file with holidays : Csv format
2> Link of cleartrip and yatra an indigo website
'''
import sys
import os
import logging
import time
import bs4

timestr=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
LOGFILENAME= "Password_change" + timestr + ".log"





#if os.isfile(LOGFILENAME):
#  os.remove(LOGFILENAME)

from sys import platform
if platform == "linux" or platform == "linux2":
  print("Not Optimised for Linux System Need to be tested")
  exit(1)
elif platform == "win32" :
  print("Not Optimised for Windows")
  exit(1)

def process_arg():
  from optparse import OptionParser
  usage = "Password_change.py -f Filename"
  parser=OptionParser(usage)
  parser.add_option("-f", dest="filename",help="File Name")
  return parser.parseargs(sys.argv)


def bor_holidays():
    print("Inside the ")
def bou_holidays():
    print("Inside the main")


def flight_tickets_crawler():
    print("Inside the main")


def best_journey_report():
    print("Inside the main")

def send_gmail():
    print('dd')



if __name__=="__main__":
    print("Inside the main")
    (opt,args)=process_arg()
    bor_holidays(opt.filename)
    flight_tickets_crawler()
