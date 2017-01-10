#!/bin/bash

host=$1
file=$2
TIME='date +%s'
KEY=''
logdir=''


echo "dbhost::$TIME - Preparing to rotate the file $file on server $host" >> $logfile
TIME='date +%s'
scp -i $KEY log_slow.cnf fk-mysql-deployer@$host:/tmp/log_slow.cnf
if [ $? == 0 ]
then
	echo "dbhost::$TIME - Copied config for  $file on server $host" >> $logfile
	echo "dbhost::$TIME - preparing copy: $file on server $host to mydash" >> $logfile
	scp -i $KEY fk-mysql-deployer@$host:$file $logdir/$host
	if [ $? == 0 ]
	then
		TIME='date +%s'
		echo "dbhost::$TIME - Successfully copied $file on server $host to dash" >> $logfile
		echo "dbhost::$TIME - invoking rotater for  $file on server $host" >> $logfile
		ssh -i $KEY -l fk-mysql-deployer $host "sudo logrotate -f /tmp/log_slow.cnf"
		if [ $? == 0 ]
		then
			TIME='date +%s'
			echo "dbhost::$TIME - Successfully rotated $file on server $host" >> $logfile
		else
			TIME='date +%s'
			echo "dbhost::$TIME - error in rotating  $file on server $host" >> $logfile
		fi

	else
		TIME='date +%s'
		echo "dbhost::$TIME - failed copy $file on server $host to dash" >> $logfile
	fi
	ssh -i $KEY -l fk-mysql-deployer $host "sudo rm -f /tmp/log_slow.cnf"
else
	echo "dbhost::$TIME - failed to copy config for  $file on server $host" >> $logfile
fi

