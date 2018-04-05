#! /bin/bash

a=10; b=20;

echo "*************************"
echo "a: 10; b: 20"
echo
[ $a -eq $b ]&&eq=true||eq=false
echo "[ \$q -eq \$b ]: $eq"
[ $a -ne $b ]&&ne=true||ne=false
echo "[ \$a -ne \$b ]: $ne"
[ $a -gt $b ]&&gt=true||gt=false
echo "[ \$a -gt \$b ]: $gt"
[ $a -lt $b ]&&lt=true||lt=false
echo "[ \$a -lt \$b ]: $lt"
[ $a -ge $b ]&&ge=true||ge=false
echo "[ \$a -ge \$b ]: $ge"
[ $a -le $b ]&&le=true||le=false
echo "[ \$a -le \$b ]: $le"
echo "*************************"
