class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print('姓名:', self.name, '年龄:', self.age, '性别', self.sex)

    def cmpChar(self, a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    def __cmp__(self, other):
        a_list = list(self.name)
        b_list = list(other.name)
        a_len = len(a_list)
        b_len = len(b_list)
        if a_len <= b_len:
            length = a_len
        else:
            length = b_len
        for i in range(length):
            temp = self.cmpChar(a_list[i], b_list[i])
            if temp < 0:
                return -1
            elif temp > 0:
                return 1
            else:
                continue
        if a_len < b_len:
            return -1
        elif a_len > b_len:
            return 1
        elif self.age > other.age:
            return 1
        elif self.age < other.age:
            return -1
        else:
            return 0

    def cmpPerson(self, other):
        temp = self.__cmp__(other)
        if temp < 0:
            print('前者小于后者')
        elif temp > 0:
            print('前者大于后者')
        else:
            print('两者相同')


p = Person('cuppar', 22, '男')
p.print_info()
p2 = Person('cuppar', 20, '男')
p2.print_info()
p.cmpPerson(p2)
