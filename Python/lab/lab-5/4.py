class Person:
    count = 0

    def __init__(self, name='cuppar', age=22, sex='男'):
        self.__name = name
        self.__age = age
        self.__sex = sex
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    def print_info(self):
        print('姓名:', self.__name, '年龄:', self.__age, '性别:', self.__sex)

    def print_count(self):
        print('count =', Person.count)

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, val):
    #     self.__name = val

    # @property
    # def age(self):
    #     return self.__age

    # @name.setter
    # def age(self, val):
    #     self.__age = val

    # @property
    # def sex(self):
    #     return self.__sex

    # @name.setter
    # def sex(self, val):
    #     self.__sex = val

    def getName(self):
        return self.__name

    def setName(self, val):
        self.__name = val

    def getAge(self):
        return self.__age

    def setAge(self, val):
        self.__age = val

    def getSex(self):
        return self.__sex

    def setSex(self, val):
        self.__sex = val
    name = property(getName, setName)
    age = property(getAge, setAge)
    sex = property(getSex, setSex)


p = Person()
p.print_info()
p.name = 'abc'
p.age = 100
p.sex = '女'
p.print_info()
