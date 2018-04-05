#! /bin/bash

echo "*************************"
a=10;b=20
echo "a: 10; b: 20"
echo
[ $a != $b ]&&not=true||not=false
echo "[ \$a != \$b ]: $not"
[ $a -lt 20 -a $b -gt 100 ]&&and=true||and=false
echo "[ \$a -lt 20 -a \$b -gt 100 ]: $and"
[ $a -lt 20 -o $b -gt 100 ]&&or=true||or=false
echo "[ \$a -lt 20 -o \$b -gt 100 ]: $or"
echo "*************************"
echo 
echo "*************************"
echo "&& 和 || 用在[]外或者[[]]里，-a 和 -o用在[]里。"
echo "*************************"
