#!/bin/bash

REMOTE_HOST=your.ssh.host
USER_NAME=someuser
# RPORT is the port you want to ssh to from the remote host
RPORT=1080
KEYFILE=YOUR_SSH_KEY
PORTS=( 22 443 80 8080 25 21 53 )

for i in "${PORTS[@]}"; do
	ssh -i $KEYFILE -q -N -R $RPORT:localhost:22 $USER_NAME@$REMOTE_HOST -p $i &
	sleep 10
	ps -ef |grep $REMOTE_HOST |grep -v grep > /dev/null 2>&1
	if [[ $? -ne 0 ]]; then
		echo "SSH tunnel on $i failed"
	else
		echo "SSH tunnel on $i succeeded"
		echo " "
		echo "on $REMOTE_HOST:"
		echo "		ssh user@localhost -p $RPORT"
		echo " "
		exit 0
	fi
done
