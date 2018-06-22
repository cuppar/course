class UserIdentify:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        user_name = input('用户名:')
        password = input('密码:')
        if user_name == 'root' and password == 'root':
            self.func()
        else:
            print('登录失败，请重新输入用户名密码。')


@UserIdentify
def login():
    print('登录成功！')


login()
