__author__ = 'Sanchayan'
import socket
def find_service_name():
    # many of the Services Run on TCP and UDP Port
    protocol = 'tcp'
    for port in [80,25]:
        print('Port %s Service Name %s' %(port ,socket.getservbyport(port, protocol)))
    print('Port %s Service Name %s' %(port ,socket.getservbyport(53, 'udp')))


if __name__=="__main__":
    find_service_name()