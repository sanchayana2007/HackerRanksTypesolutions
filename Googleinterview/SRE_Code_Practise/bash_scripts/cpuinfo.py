import subprocess
import re

command = "cat /proc/cpuinfo"
c_flag= False
m_flag= False

all_info = subprocess.check_output(command, shell=True).strip()

for line in all_info.decode().split("\n"):
    #print("################################################")
    #print(line)
    if "cpu MHz" in line and c_flag == False :
        
        print(re.sub( ".*cpu MHz .*:", "", line,1))
        c_flag = True

    if "model name" in line and m_flag == False :
        print(re.sub( ".*model name.*:", "", line,1))
        m_flag = True
        
