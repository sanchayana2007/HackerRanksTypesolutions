
# Service mongod  status
Status=$(pgrep mongo | wc -l)
if [ "$Status" -ne 1 ];
then 	sudo  service mongod start

else
	echo "its already running"
	echo "$Status"
fi


