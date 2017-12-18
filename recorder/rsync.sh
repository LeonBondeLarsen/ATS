#/usr/bin/zsh

# Check that new files are present
if [ "$(ls -A /home/llarsen/local)" ]
then
	# Check that ceph is mounted
	if [ -n "$(mount -l | grep ceph)" ]
	then
		_DIR=$(date +%Y-%m-%d)
		mkdir /home/llarsen/ceph/$_DIR

		# Run the rsync command
		rsync --remove-source-files /home/llarsen/local/$_DIR/* /home/llarsen/ceph/$_DIR
	else
		echo "$(date +%Y-%m-%d@%H:%M:%S) : Ceph storage is not mounted"
	fi
else
	echo "$(date +%Y-%m-%d@%H:%M:%S) : Nothing to be done"
fi


