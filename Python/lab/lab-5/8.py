from multimethod import multimethod


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别', self.sex)

    @multimethod
    def hello(self, id):
        print('hello, id:', id)

    @multimethod
    def hello(self, id, str):
        print('hello, id:', id, 'str:', str)


p = Person('cuppar', 22, '男')
p.print_info()
p.hello(123)
p.hello(123, 'haha')
