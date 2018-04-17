#! /bin/bash

read -p 请输入路径: DORF
if [ -d $DORF ]
then
  ls $DORF
elif [ -f $DORF ]
then
  cat $DORF
fi
