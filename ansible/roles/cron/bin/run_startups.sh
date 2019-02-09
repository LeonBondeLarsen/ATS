#!/bin/bash

_files=$(find "/home/pi/Services/" -maxdepth 3 -type f -iname "startup.sh")

if [ -z "$_files" ]
then
    echo "no startup scripts found"
else
    while read file 
    do
        echo "running startup file $file"
        exec $file
    done <<< $_files
fi 

