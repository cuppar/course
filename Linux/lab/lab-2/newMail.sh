#! /bin/bash

while true
do
  count1=`ls -l /var/mail/cuppar | awk '{print $5}'`
  echo $count1
  sleep 300
  count2=`ls -l /var/mail/cuppar | awk '{print $5}'`
  echo $count2
  if [ $count1 -eq $count2 ]
  then
    date=`date`
    echo '新邮件到达！请及时查看！ $date'
  fi
done
