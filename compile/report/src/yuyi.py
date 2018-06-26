siyuan = []
table = []
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
operater = '+-*/()'

dic = {}  # 符号表


def cifa(string):  # 词法分析
    print('')
    m = 0
    state = 0  # 1：为标识符 2：为数字串 3：为运算符
    for i in range(len(string)):
        if string[i] in operater:  # 如果是运算符
            if state == 1:  # state=1表明其前面的为标识符
                print(string[m:i], '是标识符,类型码：1')
                dic[string[m:i]] = 1
                table.append(string[m:i])
            elif state == 2:  # state=2表明其前面的为数字
                print(string[m:i], '是数字，类型码：2')
                dic[string[m:i]] = 2
                table.append(string[m:i])
            m = i + 1
            state = 3
            print(string[i], '是运算符，类型码：3')
            dic[string[i]] = 3
            table.append(string[i])
        elif string[i] in number:  # 如果是数字
            if i == m:  # 判断此时的数字是否为整数的第一个数字，若是则改变状态为无符号整数
                state = 2
        elif string[i] in letter:  # 如果是字母
            if state == 2:  # 判断此时的状态，若state=2表明状态为无符号整数，而整数内不能包含字母，故报错
                print('词法分析检测到错误,数字串中不能包含字母')
                exit(0)
            if i == m:  # 判断此时的字母是否为标识符的第一个字母，若是则改变状态为标识符
                state = 1
        else:  # 当输入的字符均不符合以上判断，则说明为非法字符，故报错
            print('词法分析检测到非法字符')
            exit(0)
    if state == 1:  # 当字符串检查完后，若字符串最后部分为标识符，应将其print出来
        print(string[m:], '是标识符，类型码：3')
        dic[string[m:]] = 1
        table.append(string[m:])
    elif state == 2:  # 若字符串最后部分为无符号整数，应将其print出来
        print(string[m:], '是无符号整数，类型码：2')
        dic[string[m:]] = 2
        table.append(string[m:])
    table.append('#')
    print('字符栈:', table, '\n词法正确')


class yuyi:
    def __init__(self):
        print('\n语义分析结果(四元式):')
        self.i = 0  # 栈指针
        self.flag = 0  # 记录临时变量T数目
        self.m()
        for i in siyuan:  # 输出四元式结果
            print(i)

    def m(self):  # PM程序
        if (table[self.i] == '+'):
            self.i += 1
            ret1 = self.e()
            siyuan.append('(+,0,' + ret1 + ',out)')
            self.flag += 1
        elif (table[self.i] == '-'):
            self.i += 1
            ret2 = self.e()
            siyuan.append('(-,0,' + ret2 + ',out)')
            self.flag += 1
        else:
            ret3 = self.e()
            siyuan.append('(=,' + ret3 + ',0,out)')

    def e(self):  # PE程序
        ret1 = self.t()
        ret2, ret3 = self.e1()
        if (ret2 != '&'):  # 若ret2不为&，则可以产生四元式，否则将变量传递给父项
            self.flag += 1
            siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
            return 'T' + str(self.flag)
        else:
            return ret1

    def e1(self):  # PE1程序
        if (table[self.i] == '+'):
            self.i += 1
            ret1 = self.t()
            ret2, ret3 = self.e1()
            if (ret2 == '&'):
                return '+', ret1
            else:
                self.flag += 1
                siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '+', 'T' + str(self.flag)
        elif (table[self.i] == '-'):
            self.i += 1
            ret1 = self.t()
            ret2, ret3 = self.e1()
            if (ret2 == '&'):
                return '-', ret1
            else:
                self.flag += 1
                siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '-', 'T' + str(self.flag)
        else:
            return '&', '&'

    def t(self):  # PT程序
        ret1 = self.f()
        ret2, ret3 = self.t1()
        if (ret2 != '&'):
            self.flag += 1
            siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
            return 'T' + str(self.flag)
        else:
            return ret1

    def t1(self):  # PT1程序
        if (table[self.i] == '*'):
            self.i += 1
            ret1 = self.f()
            ret2, ret3 = self.t1()
            if (ret2 == '&'):
                return '*', ret1
            else:
                self.flag += 1
                siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '*', 'T' + str(self.flag)
        elif (table[self.i] == '/'):
            self.i += 1
            ret1 = self.f()
            ret2, ret3 = self.t1()
            if (ret2 == '&'):  # 若ret2不为&，则可以产生四元式，否则将变量传递给父项
                return '/', ret1
            else:
                self.flag += 1
                siyuan.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '/', 'T' + str(self.flag)
        else:
            return '&', '&'

    def f(self):  # PF程序
        if (table[self.i] == '('):
            self.i += 1
            ret1 = self.e()
            self.i += 1
            return str(ret1)
        elif (dic[table[self.i]] == 1):  # 当为标识符时，传递给父项
            temp = self.i
            self.i += 1
            return table[temp]
        elif (dic[table[self.i]] == 2):  # 当为整数时，传递给父项
            temp = self.i
            self.i += 1
            return table[temp]


# 主程序
if __name__ == '__main__':
    string = input('请输入表达式：')
    cifa(string)
    yuyi()
