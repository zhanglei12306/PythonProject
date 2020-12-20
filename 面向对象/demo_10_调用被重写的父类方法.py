
# 调用被重写的父类方法
# 子类重写了父类方法，仍然想执行父类中的方法，则可以在类中使用super（）来调用方法
class Animal(object):  # 新写法
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")
class Dog(Animal):
    def playing(self):
        print("-----玩-----")

class Cat(Dog):
    def playing(self):
        print("-----玩游戏-----")

    def pao(self):
        print("-----跑-----")
        # 调用被重写的方法
        # 一 父类名.方法名（对象）
        # Dog.playing(self)
        # 二 super(类名, 对象).方法()
        # super(Cat, self).playing()
        super().playing()

wang_cai = Cat()
wang_cai.eat()
wang_cai.drink()
wang_cai.playing()
wang_cai.pao()

