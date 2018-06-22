from functools import wraps
import time


def use_logging(path='./log.txt'):
    def decorater(func):
        def wrapper(*args, **kwords):
            with open(path, 'a') as f:
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(time.time()))
                        + '  ' + func.__name__+'  strat.\n')
                result = func()
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(time.time()))
                        + '  ' + func.__name__+'  end.\n')
            return result
        return wrapper
    return decorater


@use_logging('./log.txt')
def fun1():
    print('操作1')


@use_logging('./log.txt')
def fun2():
    print('操作2')


@use_logging('./log.txt')
def fun3():
    print('操作3')


fun1()
fun2()
fun3()
