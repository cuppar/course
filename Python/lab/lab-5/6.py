class Person:
    count = 0

    def __init__(self, name='cuppar', age=22, sex='男'):
        self.name = name
        self.age = age
        self.sex = sex
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别:', self.sex)

    @staticmethod
    def print_count():
        print('count =', Person.count)


p1 = Person()
Person.print_count()
p2 = Person(name='abc')
Person.print_count()
p3 = Person(name='abc', age='100')
Person.print_count()
del p1
Person.print_count()
