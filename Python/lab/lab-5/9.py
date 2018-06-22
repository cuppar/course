class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别', self.sex)


class Student(Person):
    def __init__(self, name, age, sex, stuNo):
        Person.__init__(self, name, age, sex)
        self.stuNo = stuNo

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别:'
        , self.sex, '学号:', self.stuNo)


p = Person('cuppar', 22, '男')
p.print_info()
s = Student('cuppar', 22, '男', 20151120237)
s.print_info()
