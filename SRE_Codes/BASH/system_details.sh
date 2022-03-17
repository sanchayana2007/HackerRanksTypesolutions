# to remove the matches of the grep procerss( grep -v "grep")
		#All files it has opened 
		 echo "####################### HEALTH CHECK ################################"
		 echo "#######################  MEMORY PROCESS ################################"
		 echo "#######################  MEMORY PROCESS ################################"
		 echo "#######################  IO PROCESS ################################"
		 echo "#######################  CPU UTILISATION  ################################"
		
	         echo "${lsofprocess}" | grep "IPv4" | grep "ESTABLISHED" | tail 	
		 


