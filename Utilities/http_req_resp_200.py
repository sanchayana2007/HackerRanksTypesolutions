__author__ = 'Sanchayan'
from http.client import *
#import http

try:
 conn = HTTPConnection('www.flipkart.com', 80)
 conn.request('GET', '/mens-footwear?otracker=hp_nmenu_sub_men_0_All%20Footwear')
 response = conn.getresponse()

except Exception as e:
 print('Exception: ', type(e).__name__, e.args)
else:
 if response.status == 200:
  print('Page found')
  f = open('flipkart.txt', 'wb')
  f.write(response.read())
  f.close()
  #print()
 elif response.status == 404:
  print('Page not found')
 else:
  print("End")

conn.close()