#! /bin/bash

array=(A B "C" D)
echo "array=(A B \"C\" D)"
echo "\${array[@]}: ${array[@]}"
echo "\${array[*]}: ${array[*]}"
echo "\${array[0]}: ${array[0]}"
echo "\${array[1]}: ${array[1]}"
echo "\${array[2]}: ${array[2]}"
echo "\${#array[*]}: ${#array[*]}"
echo "\${#array[@]}: ${#array[@]}"
echo "\${#array[0]}: ${#array[0]}"
