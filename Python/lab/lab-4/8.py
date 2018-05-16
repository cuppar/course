import math


def triangleArea(*, a, b, c):
    if a+b < c or a+c < b or b+c < a:
        raise 'ERROR: 不能构成三角形'
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area


print('三角形边长分别为3,4,5 面积为:', triangleArea(a=3, b=4, c=5))
