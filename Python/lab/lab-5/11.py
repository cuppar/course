class Animal:
    def quack(self):
        print('动物叫')


class Dog(Animal):
    def quack(self):
        print('狗叫')


class Cat(Animal):
    def quack(self):
        print('猫叫')


class DogCat(Dog, Cat):
    pass


a=Animal()
d=Dog()
c=Cat()
dc=DogCat()
a.quack()
d.quack()
c.quack()
dc.quack()
