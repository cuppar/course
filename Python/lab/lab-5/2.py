class Person:
    def __init__(self, name='cuppar', age=22, sex='男'):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别:', self.sex)


p1 = Person()
p1.print_info()
p2 = Person(name='abc')
p2.print_info()
p3 = Person(name='abc', age='100')
p3.print_info()
