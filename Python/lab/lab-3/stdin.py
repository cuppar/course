import sys
inFile = open('stdin.txt', 'r')
sys.stdin = inFile
print(input('从文件输入: '))
inFile.close()