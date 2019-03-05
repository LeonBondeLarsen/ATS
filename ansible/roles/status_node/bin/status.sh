#!/bin/bash
#!/bin/bash

_timestamp=$(date -u +%Y-%m-%dT%T)

sudo svstat /etc/service/* |
while read line
do
  _hostname=$(cat /etc/hostname)
  _service=$(echo $line | cut -d':' -f1 | cut -d'/' -f4)
  _status=$(echo $line | cut -d':' -f2 | cut -d' ' -f2)
  echo "{\"@timestamp\":\"$(date -u +%Y-%m-%dT%T)\",\"data\":{\"host\":\"$_hostname\",\"service\":\"$_service\",\"status\":\"$_status\"}}"  | kafkacat -b manna,hou,bisnap -t ats_service
done

