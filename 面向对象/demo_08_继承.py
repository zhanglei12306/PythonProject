
# 继承：某个类直接具备另一个类的能力（属性和方法）
# 格式：
# class 子类名:(父类名)
# class Animal:  经典写法
class Animal(object):  #新写法
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")
class Dog(Animal):

    def playing(self):
        print("-----玩-----")

class Cat(Dog):
    def pao(self):
        print("-----跑-----")

wang_cai = Cat()
wang_cai.eat()
wang_cai.drink()
wang_cai.playing()
wang_cai.pao()
