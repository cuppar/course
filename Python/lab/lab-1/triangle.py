import math

title = '''
5.编写程序，任意输入三条边长，经过简单的计算后，判断三条边长能否构成三角形，并在文本框中显示结果。
'''


def twoSideGreaterThreeSide(a: float, b: float, c: float) -> bool:
    return a+b > c


def canBeTriangle(a: float, b: float, c: float) -> bool:
    if twoSideGreaterThreeSide(a, b, c)\
       and twoSideGreaterThreeSide(b, c, a)\
       and twoSideGreaterThreeSide(c, a, b):
        return True
    return False


if __name__ == '__main__':
    print(title)
    a, b, c = (float(x) for x in input(
        'please input three number(such as "1 2 3"): ').split(' '))
    canBeTriangle = canBeTriangle(a, b, c)
    if(canBeTriangle):
        print('Three side can be triangle.')
    else:
        print('Three side cannot be triangle.')
