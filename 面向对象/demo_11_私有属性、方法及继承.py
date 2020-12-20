# 私有方法、属性，继承问题
# 父类中的 私有方法、属性，不会被子类继承
# 可以通过调用继承的父类的共有方法，间接的访问父类的私有方法、属性

class Animal(object):
    def __init__(self):
        self.type = '动物'
        self.__color = '黑'

    def __run(self):
        print("----跑---")

    def eat(self):
        print("-----吃-----")

    def test(self):
        print(self.__color)
        self.__run()

class Dog(Animal):
    def bark(self):
        print("-----汪汪叫------")
        # self.__run()  # 父类中的私有方法，没有被子类继承
        print(self.type)

wang_cai = Dog()
wang_cai.bark()
wang_cai.eat()
wang_cai.test()