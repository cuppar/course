#! /bin/bash

echo "please input your password: "
read pwd
while [ "$pwd" != "secret" ]
do
echo 'password wrong!'
echo 'please input your password: '
read pwd
done

echo 'ok!'
