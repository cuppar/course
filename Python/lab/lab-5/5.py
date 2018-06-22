class Person:
    def __init__(self):
        pass

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'sex':
            if value not in ['男', '女']:
                raise Exception('性别只能为男或女。')
        if key == 'age':
            if value not in range(120):
                raise Exception('年龄只能在0-120之间。')
        object.__setattr__(self, key, value)


p = Person()
p.name = 'cuppar'
p.sex = 'man'
p.age = 22
