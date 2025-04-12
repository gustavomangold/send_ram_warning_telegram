while : 
do
	free -m | grep Mem: | awk '{print $3/($2)}' >> free_output.txt
	python3 send_ram_warning.py
	# remove temporary file and wait 5 minutes till next check
	rm free_output.txt
	sleep 300 
done
