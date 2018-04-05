#! /bin/bash

n=1
echo n: $n
n=`expr $n + 1`
echo n=\`expr \$n + 1\`: $n
n=$[$n+1]
echo n=\$[\$n+1]: $n
n=$((n+1))
echo n=\$\(\(n+1\)\): $n
let 'n++'
echo let \'n++\': $n
