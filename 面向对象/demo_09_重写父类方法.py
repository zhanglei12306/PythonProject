# 重写父类方法
# 当子类实现一个和父类同名的方法时，叫做 重写父类方法
# 子类重写了父类方法，子类再调用该方法将不会执行父类的处理

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

    def playing(self):
        print("-----玩游戏-----")

wang_cai = Cat()
wang_cai.eat()
wang_cai.drink()
wang_cai.playing()
wang_cai.pao()
