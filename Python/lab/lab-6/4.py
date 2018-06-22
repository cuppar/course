from functools import wraps
import time

logined = False
last_login_time = 0


def userIdentify(func):

    @wraps(func)
    def wrapper(*args, **kwords):
        global logined
        global last_login_time
        if not logined or (time.time()-last_login_time) > 120:
            with open('password.txt', 'r') as f:
                user_name = f.readline().strip()
                password = f.readline().strip()
            user_name_input = input('请输入用户名:')
            password_input = input('请输入密码:')
            if user_name == user_name_input and password == password_input:
                logined = True
                last_login_time = time.time()
                print('登录成功！')
                return func()
            else:
                print('用户名或密码错误，登录失败。')
                print('无法使用功能。')
        else:
            print('已登录。')
            return func()
    return wrapper


@userIdentify
def fun1():
    print('使用功能1')
    print()


@userIdentify
def fun2():
    print('使用功能2')
    print()


@userIdentify
def fun3():
    print('使用功能3')
    print()


@userIdentify
def fun4():
    print('使用功能4')
    print()


fun1()
fun2()
fun3()
time.sleep(120)
print('等待两分钟。。。')
fun4()
