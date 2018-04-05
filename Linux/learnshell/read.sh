#! /bin/bash

echo "***********************"
echo read命令详解
echo read v1 v2 v3 ...
echo 输入数量大于需求量，最后一个需求参数接受剩余所有参数
read -p '需要两个参数，请输入四个：' v1 v2
echo v1=$v1 v2=$v2
echo "***********************"
echo "***********************"
echo 参数：
echo -p 输入提示
echo '-n 长度限制'
echo -t 时间限制
echo -s 隐藏输入内容，如密码
read -p '请输入六位密码: ' -n 6 -t 5 -s password
echo -e "\npassword is $password"
echo "***********************"
