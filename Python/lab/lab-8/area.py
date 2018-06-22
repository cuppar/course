"""
求圆、三角形、矩形、梯形面积的模块
"""
import math


def circle(r):
    """
    求圆的面积
    r: 圆的半径
    return: 面积
    """
    return math.pi*r**2


def triangle(a, b, c):
    """
    求三角形的面积
    a, b, c: 三角形的三边长
    return: 面积
    """
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def rect(w, h):
    """
    求矩形的面积
    w: 矩形的宽
    h: 矩形的高
    return: 面积
    """
    return w*h


def trape(top, bottom, h):
    """
    求矩形的面积
    top: 梯形的上底
    bottom: 梯形的下底
    h: 梯形的高
    return: 面积
    """
    return (top+bottom)*h/2


if __name__ == "__main__":
    import area
    print('半径为5的圆面积:', area.circle(5))
    print('三边为3,4,5的三角形面积:', area.triangle(3, 4, 5))
    print('宽为5，高为10的矩形面积:', area.rect(5, 10))
    print('上底为5，下底为10， 高为8的梯形面积:', area.trape(5, 10, 8))
