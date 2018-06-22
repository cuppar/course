from functools import wraps


logined = False


def userIdentify(func):

    @wraps(func)
    def wrapper(*args, **kwords):
        global logined
        if not logined:
            with open('password.txt', 'r') as f:
                user_name = f.readline().strip()
                password = f.readline().strip()
            user_name_input = input('请输入用户名:')
            password_input = input('请输入密码:')
            if user_name == user_name_input and password == password_input:
                logined = True
                print('登录成功！')
                print('logined:', logined)
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


@userIdentify
def fun2():
    print('使用功能2')


@userIdentify
def fun3():
    print('使用功能3')


@userIdentify
def fun4():
    print('使用功能4')


fun1()
fun2()
fun3()
fun4()
