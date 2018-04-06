#! /bin/bash

while :
do
    echo -n 输入1-5之间的数字:
    read i
    case $i in
        1|2|3|4|5) echo 你输入的数字为 $i !
        ;;
        *) echo 你输入的不是1-5之间的数字！游戏结束
           break
        ;;
    esac
done
