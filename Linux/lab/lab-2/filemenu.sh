#! /bin/bash

until 0
do
    echo  "(1)List  you  selected  directory"

    echo  "(2)Change  to  you  selected  directory"

    echo  "(3)Creat  a  new  file"

    echo  "(4)Edit  you  selected  file"

    echo  "(5)Remove  you  selected  file"

    echo  "(6)Exit  Menu"

    read  input

    if test  $input  =  6  
    then

	exit 0

    fi

    case  $input  in

       1) ls;;

       2) echo -n "Enter  target  directory:"

           read  dir

           cd  $dir

           ;;

       3) echo -n "Enter  a  file  name:"

           read  file

           touch  $file

           ;;

       4) echo -n "Enter  a  file  name:"

           read  file

           vi  $file

           ;;

       5) echo -n  "Enter  a  file  name:"

           read  file

           rm  $file

           ;;

       *) echo  "Please  selected  1\2\3\4\5\6 " ;;

    esac

done
