#! /bin/bash

a='abc'; b='abc'; c='ABC'
echo "***********************"
echo "a='$a'; b='$b'; c='$c'"
echo
[ $a = $b ]&&streq=true||streq=false
echo "[ \$a = \$b ]: $streq"
[ $a = $c ]&&streqc=true||streqc=false
echo "[ \$a = \$c ]: $streqc"
[ $a != $b ]&&strne=true||strne=false
echo "[ \$a != \$b ]: $strne"
[ -z $a ]&&strz=true||strz=false
echo "[ -z \$a ]: $strz (str长度为0返回true)"
[ -n $a ]&&strn=true||strn=false
echo "[ -n \$a ]: $strn (str长度不为0返回true)"
echo "***********************"
echo
echo "***********************"
[ $a ]&&str=true||str=false
echo "[ \$a ]: $str (str不为空返回true)"
echo
x=''; y=' '; z=; u=0; v=false; w=null
echo "x=''; y=' '; z=; u=0; v=false; w=null; o未定义"
[ $x ]&&strx=true||strx=false
echo "[ \$x ]: $strx"
[ $y ]&&stry=true||stry=false
echo "[ \$y ]: $stry"
[ $z ]&&strz=true||strz=false
echo "[ \$z ]: $strz"
[ $u ]&&stru=true||stru=false
echo "[ \$u ]: $stru"
[ $v ]&&strv=true||strv=false
echo "[ \$v ]: $strv"
[ $w ]&&strw=true||strw=false
echo "[ \$w ]: $strw"
[ $o ]&&stro=true||stro=false
echo "[ \$o ]: $stro"
echo "***********************"
