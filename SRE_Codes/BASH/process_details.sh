# Service Run ps and awk for 1st row and 2nd column 
# to remove the matches of the grep procerss( grep -v "grep")
processid=$(ps -ef | grep "run.py" |  grep -v "grep" | awk  'NR==1 {print $2}')

#check the NUll Value
if [[ ! -z "$processid"  ]];
	then 
		echo "$processid"	
		lsofprocess=$(lsof | grep  $processid)
		#All files it has opened 
		 echo "#######################  PROCESS AND CHILD PROCESS################################"
		 echo "All Opened files #################################"
		echo "${lsofprocess}" | grep "REG" | tail  
		
		 echo "Child process IDs################################"
		 ps --ppid  $processid
		 echo "Thread Spawned  IDs################################"
		 ps -T -p $processid
		#All Network Ports it has opened
		 echo "#######################  NETWORK PROCESS ################################"
		 echo "Listning Ports#################################"
	         echo "${lsofprocess}" | grep "IPv4" | grep "LISTEN"| tail 	
		#All 
		 echo "ESTABLISHED Ports################################"
	         echo "${lsofprocess}" | grep "IPv4" | grep "ESTABLISHED" | tail 	
		 echo "#######################  MEMORY PROCESS  CPU UTILISATION  ################################"
		 avgmemcpu=$(ps -p   $processid -o %cpu,%mem,cmd)	
	         echo "AVG USES"  	
	         echo "${avgmemcpu}"  	
		 echo "#######################  IO PROCESS ################################"
		 if hash stap  2>/dev/null; then
        			stap -v iotop.stp
    			else
        		        echo "Stap is not installed "
			fi
		 echo "AVG USES"  	
		 echo "#######################  LOG DETAILS   ################################"
		 
else
	echo "Process ID is not found"
	echo "Process Name is Incorrect or the Process is not running "

fi


