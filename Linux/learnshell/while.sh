#! /bin/bash

echo '按下<CTRL-D>退出'
echo -n 输入你喜欢的东西:
while read like
do
    echo 是的！$like 是个好东西
done
