stdout=open('stdout.txt', 'w')
print('重定向输出到文件', file=stdout)
stdout.close()