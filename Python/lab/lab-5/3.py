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

    def print_count(self):
        print('count =', Person.count)


p1 = Person()
p1.print_count()
p2 = Person(name='abc')
p2.print_count()
p3 = Person(name='abc', age='100')
p3.print_count()
del p1
print('count =', Person.count)
