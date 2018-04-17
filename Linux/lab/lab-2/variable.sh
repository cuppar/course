#! /bin/bash

echo 程序名: $0
echo 所有参数: $@
echo 前三个参数: $1 $2 $3
shift
echo 程序名: $0
echo 所有参数: $@
echo 前三个参数: $1 $2 $3
shift 3
echo 程序名: $0
echo 所有参数: $@
echo 前三个参数: $1 $2 $3
exit 0
