#! /bin/bash

while true
do
  echo 简易四则运算
  echo '(n) 输入任意整数'
  echo '(+) 加法'
  echo '(-) 减法'
  echo '(x) 乘法'
  echo '(/) 除法'
  echo '(=) 等于'
  echo '(0) Exit Menu'

  read choose
  case $choose in
    n) echo -n 请输入整数:
       if [ -z "$n" ]
       then
       read n
       else
       read m
       fi
       ;;
    +) result=$((n+m))
       echo OK
       ;;
    -) result=$((n-m))
       echo OK
       ;;
    x) result=$((n*m))
       echo OK
       ;;
    /) result=`echo "scale=2; $n/$m" | bc`
       echo OK
       ;;
    =) echo $result
       ;;
    0) break
       ;;
  esac
done
