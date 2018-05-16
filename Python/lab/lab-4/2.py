def readFile():
    isContinue = True
    while isContinue:
        try:
            path = input('请输入文件路径: ')
            file = open(path, 'r')
            print('文件打开成功。')
            isContinue = False
            return file
        except Exception as e:
            print('文件打开失败，请重试。')
            print(str(e))
            isContinue = True


file = readFile()
file.close()
