processid=$(ps -ef | grep "run.py" |  grep -v "grep" | awk  'NR==1 {print $2}')
FILE="/proc/$processid"
if [ -d "$FILE" ]; then
    echo "$FILE exists."
	#All files it has opened 
                 echo "#######################  File descriptors openend ################################"
                 echo "All Opened files #################################"
		 filedescp=$(ls -l  "/proc/$processid/fd")
		 echo "$filedescp"
                 echo "#######################  Link to Working Dir of Application  ################################"
		 filedescp=$(ls -lt  "/proc/$processid/cwd")
		 echo "$filedescp"
                 echo "#######################  Full Memory maps to executables and library files ################################"
		 filedescp=$(sudo cat "/proc/$processid/map")
		 echo "$filedescp"
                 echo "#######################  Full VMsize , Threads , Signals Used , Conetxt Swithches ################################"

		 filedescp=$(sudo cat "/proc/$processid/status")
		 keywords=("Threads" "Sig*" "voluntary_ctxt_switches" "Cpus_allowed")
		 textwords=("No of threads" "Signals" "Context Switches" "Cpus_allowed")
		 for i in ${!keywords[@]};
			do
                 		echo "####################### ${textwords[$i]} ################################"
     				echo "$filedescp" | grep "${keywords[$i]}"
		 done
else
    echo "$FILE does not exist."
fi
