#! /bin/bash

read -p "猜数(1~100): " num
right=88
while [ $num -ne $right ]
do
    if [ $num -gt $right ]
    then
        echo 太大了，重新猜！
        read num
    elif [ $num -lt $right ]
    then
        echo 太小了，重新猜！
        read num
    fi
done
echo you get it!
