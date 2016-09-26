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
import requests
import re
import math 

from selenium import webdriver
timestr=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
LOGFILENAME= "Password_change" + timestr + ".log"
url='https://www.cleartrip.com/flights/results?from=BLR&to=CCU&depart_date=25/09/2016&adults=1&childs=0&infants=0&class=Economy&airline=&carrier=&intl=n&sd=1474230239314&page=loaded&view=calendar'

url1='http://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=BLR&originCountry=IN&destination=CCU&destinationCountry=IN&flight_depart_date=01/10/2016&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home'

#browser = webdriver.Firefox()
#browser.get(url)
#print(browser.page_source)

#if os.isfile(LOGFILENAME):
#  os.remove(LOGFILENAME)

def date_creator():
	no_of_dates=3
	today=datetime.date.today()
	print(today.month)
	day = today.day
	month= today.month
	year = today.year
	count = 0 
	while True:
		if count==no_of_dates:
			break
		count+=1
		
		day=day+1
		if day==1:
			month = month +1
		elif day>28 and month==2:
			day=1
			month = month +1
		elif day>=31:
			if month not in [1,3,5,7,8,10,12]:
				day=1
				month = month +1
			elif day > 31:
				day=1
				month = month +1
		if month > 12:
			year=year+1
			month =1
		#print(day,month,year)
		datestr=str(day)+','+str(month)+','+str(year)
		departdate=str(day)+'/'+str(month)+'/'+str(year)
		weekday=datetime.datetime.strptime(datestr, '%d,%m,%Y').strftime('%A')
		print(weekday)
		
		#Date creator should call the Url creator 
		Orig='BLR'
		Dest='CCU'
		url='http://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin='+Orig+'&originCountry=IN&destination='+Dest+'&destinationCountry=IN&flight_depart_date='+departdate+'&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home'
		print(url)
from sys import platform
if platform == "linux" or platform == "linux2":
  print("Not Optimised for Linux System Need to be tested")
elif platform == "win32" :
  print("Not Optimised for Windows")
  
  #exit(1)

def process_arg():
  from optparse import OptionParser
  usage = "Password_change.py -f Filename"
  parser=OptionParser(usage)
  parser.add_option("-f", dest="filename",help="File Name")
  return parser.parse_args(sys.argv)


def bor_holidays():
    print("Inside the")
def bou_holidays():
    print("Inside the main")


def flight_tickets_crawler():
		print("Inside the flight crawler")
		r = requests.get(url1)
		print(r.text)

def best_journey_report():
    print("Inside the main")

def send_gmail():
    print('dd')

def file_parser():
	Src='t.txt'
	start=':"BLRCCU'
	end='BLRCCU'
	parse_str='BLRCCU'
	count=0
	with open(Src,'r') as f:
		contents=f.read()
		print(len(contents))
		chop_len=math.ceil(len(contents)/2)
		contents=contents[chop_len:]
		chop_len=math.ceil(len(contents)/2)
		contents=contents[:chop_len]
		#print('contents',contents)
		
	pat=re.compile(start)
	
	 
	res=re.search(pat,contents)
	
	while(res):
		if count >=4:
			break 
		contents=contents[res.end():]
		flight_info=contents[:15]
		price_pat=re.search('"tf":',contents)
		price= contents[price_pat.end():]
		price=price[:8]
		
		print("flight_info",flight_info,price)
		count+=1
		#print(contents)
		res=re.search(pat,contents)

if __name__=="__main__":
    print("Inside the main")
    (opt,args)=process_arg()
    #bor_holidays(opt.filename)
    flight_tickets_crawler()
