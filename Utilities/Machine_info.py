__author__ = 'Sanchayan'

# Getting the Machine Information from the different OSs System
# and this fetch Information,

import socket
import uuid
import pstats
from binascii import hexlify


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name %s" %host_name)
    print('IPaddress %s' %ip_address)
    mac=uuid.getnode()
    mac=':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    print('mac Addr %s'%mac)


if __name__=="__main__":
    print_machine_info()
