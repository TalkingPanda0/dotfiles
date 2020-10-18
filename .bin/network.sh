#!/bin/bash
INTERFACE='enp2s0'
#Mbit/s
MIN_SPEED=0
while :
do
CURRENT_SPEED=`ifstat  enp2s0 1 1 | awk '{print $2}' | sed -n '4p'`
echo $CURRENT_SPEED $MIN_SPEED
  if [ $CURRENT_SPEED -eq $MIN_SPEED ]; 
  then
	  echo a
    	  shutdown -h now
  fi
done
