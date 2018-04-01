title='''
6.编写程序，输入一个字符，判断该字符是大写字母、小写字母，数字还是其他字符，并作相应的显示。
提示：利用ord()函数来获得字符的ASCII。
'''

def distinguish(c: chr):
    c_ascii = ord(c)
    if c_ascii >= 48 and c_ascii <= 57:
        print('该字符为数字')
    elif c_ascii >= 65 and c_ascii <= 90:
        print('该字符为大写字母')
    elif c_ascii >= 97 and c_ascii <= 122:
        print('该字符为小写字母')
    else:
        print('该字符为其他字符')


if __name__ == '__main__':
    print(title)
    distinguish(input('input a char: '))