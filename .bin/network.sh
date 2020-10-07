#!/bin/bash
INTERFACE='enp2s0'
#Mbit/s
MIN_SPEED=0
while :
do
CURRENT_SPEED=`ifstat  enp2s0 1 1 | awk '{print $2}' | sed -n '4p'`
  if [ $CURRENT_SPEED -lt $MIN_SPEED ]; 
  then
    	  shutdown -h now
  fi
done
