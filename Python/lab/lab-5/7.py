class Person:
    def __init__(self):
        pass

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别', self.sex)

    @classmethod
    def resolver(cls, str):
        list = str.split(',')
        cls.name = list[0]
        cls.age = list[1]
        cls.sex = list[2]
        return cls


p = Person.resolver('cuppar,22,男')
p().print_info()
