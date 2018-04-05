#! /bin/bash

echo "*****************************"
file="/home/cuppar/projects/course/Linux/learnshell/expr.sh"
echo "file=\"/home/cuppar/projects/course/Linux/learnshell/expr.sh\""

[ -b $file ]&&b=true||b=false
echo "[ -b $file ]"
echo "块设备文件: $b"
echo
[ -c $file ]&&c=true||c=false
echo "[ -c $file ]"
echo "字符设备文件: $c"
echo
[ -d $file ]&&d=true||d=false
echo "[ -d $file ]"
echo "目录: $d"
echo
[ -f $file ]&&f=true||f=false
echo "[ -f $file ]"
echo "普通文件(既不是目录，也不是设备文件): $f"
echo
[ -g $file ]&&g=true||g=false
echo "[ -g $file ]"
echo "是否设置了SGID位: $g"
echo
[ -k $file ]&&k=true||k=false
echo "[ -k $file ]"
echo "是否设置了粘着位(Sticky Bit): $k"
echo
[ -p $file ]&&p=true||p=false
echo "[ -p $file ]"
echo "有名管道: $p"
echo
[ -u $file ]&&u=true||u=false
echo "[ -u $file ]"
echo "是否设置了SUID位: $u"
echo
[ -r $file ]&&r=true||r=false
echo "[ -r $file ]"
echo "可读: $r"
echo
[ -w $file ]&&w=true||w=false
echo "[ -w $file ]"
echo "可写: $w"
echo
[ -x $file ]&&x=true||x=false
echo "[ -x $file ]"
echo "可执行: $x"
echo
[ -s $file ]&&s=true||s=false
echo "[ -s $file ]"
echo "大小大于0: $s"
echo
[ -e $file ]&&e=true||e=false
echo "[ -e $file ]"
echo "存在: $e"
echo

echo "*****************************"
