import math

title='''
3.编写程序，输入球体半径，计算出球的体积和表面积，并输出结果。
提示：球体表面积计算公式为 S=4πR²，球体体积计算公式为 V=(4/3)πR³。
'''
print(title)

r=float(input("please input the ball's radius:"))
s=4*math.pi*r**2
v=(4/3)*math.pi**3
print("This ball's surface is: ", s)
print("This ball's valume is: ", v)