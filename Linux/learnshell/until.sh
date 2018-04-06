#! /bin/bash

echo 输入exit结束程序
read -p '输入你喜欢的东西: ' like
until [ $like = 'exit' ]
do
    echo 我也喜欢 $like !
    read -p '还有其他的吗' like
done
