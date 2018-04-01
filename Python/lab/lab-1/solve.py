from math import *
title = '''
7.编写程序，计算一元二次方程 ax2+bx+c 的根（公式）。
因为负数的平方根是虚的，所以可以使用平方根里面的表达式
（称为差别式）先进地判别，检查根型。如果判别式是负数，
根是虚的。如果判别式是零，只有一个根；如果判别式是正的，
有两个根。写一个程序，使用二次方根式得到实根，即忽略虚根。
使用判别式确定有一个根或两个根，然后显示出答案。
'''


def solve(a: float, b: float, c: float) -> dict:
    flag = b**2-4*a*c
    result = {}
    if flag == 0:
        result['left'] = -b-sqrt(flag)/(2*a)
    elif flag > 0:
        result['left'] = -b-sqrt(flag)/(2*a)
        result['right'] = -b+sqrt(flag)/(2*a)
    return result


def printResult(a: float, b: float, c: float) -> None:
    result = solve(a, b, c)
    if len(result) == 0:
        print('该方程无实根')
    elif len(result) == 1:
        print('该方程有一个实根，为 {0}'.format(result['left']))
    else:
        print('该方程有两个实根，分别为 {0}， {1}'.format(result['left'], result['right']))


if __name__ == '__main__':
    print(title)
    print('计算 ax**2+bx+c :')
    a = float(input('请输入a: '))
    while a == 0:
        print('a不能为0,请重新输入！')
        a = float(input('请输入a: '))
    b = float(input('请输入b: '))
    c = float(input('请输入c: '))
    printResult(a, b, c)
