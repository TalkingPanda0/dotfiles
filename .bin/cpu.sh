MIN_USAGE=5
while :
do
USAGE=$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]4p'`
  if [ $USAGE -lt $MIN_SPEED ];
  then
    	  shutdown -h now
  fi
done
