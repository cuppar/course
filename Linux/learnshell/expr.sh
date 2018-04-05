#! /bin/bash

val=`expr 1 + 2`
echo "*******************"
echo "\`expr 1 + 2\`: $val"
echo ""
echo "在.sh文件中要用反引号\"\`\"把\"expr 1 + 2\"括起来"
echo "加号两边要有空格"
echo "*******************"
echo
echo "*******************"
val2=$((1+2))
echo "\$((1+2)): $val2"
echo
echo "\$(())中不需要空格，也不需要反引号包围，乘法的\"\*\"号也不需要转义"
echo "*******************"
echo
echo "*******************"

a=10
b=20
echo "a: 10; b: 20"
echo
v1=`expr $a + $b`
echo "expr \$a + \$b: $v1"
v2=`expr $a - $b`
echo "expr \$a - \$b: $v2"
v3=`expr $a \* $b`
echo "expr \$a \* \$b: $v3"
v4=`expr $a / $b`
echo "expr \$a / \$b: $v4"
v5=`expr $a % $b`
echo "expr \$a % \$b: $v5"
if [ $a == $b ]
then
    v6=true
else
    v6=false
fi
echo "[ \$a == \$b ]: $v6"
if [ $a != $b ]
then
    v7=true
else
    v7=false
fi
echo "[ \$a != \$b ]: $v7"
echo "*******************"
