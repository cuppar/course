#! /bin/bash

n=1
for i in $*
do
    echo $n: $i
    n=`expr $n + 1`
done
