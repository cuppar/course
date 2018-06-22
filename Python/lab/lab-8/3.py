import importlib
import compute
import area

def menu():
    print('1 四则运算')
    print('2 几何面积')
    print('3 重新加载模块')
    print('q 退出')
    return input('请选择: ')


def load_module(option):
    if option == '1':
        __import__('compute')
        print('加载compute模块。。。')
    elif option == '2':
        __import__('area')
        print('加载area模块。。。')
    elif option == '3':
        importlib.reload(compute)
        importlib.reload(area)
        print('重新加载模块。。。')
    


option = ''
while option != 'q':
    option = menu()
    load_module(option)
