insert=open('学生信息表.csv', 'a')
message=','.join(['17010002', '赵四', '女', '自动化1701'])
insert.writelines(message)
insert.close()

file = open('学生信息表.csv')
for line in file:
    line=line.split(',')
    print(' '.join(line))
file.close()