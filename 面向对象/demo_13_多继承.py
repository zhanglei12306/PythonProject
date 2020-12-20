# 继承：某个类直接具备另一个类的能力（属性和方法）
# print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
# 格式：
# class 子类名:(父类名)
# class Animal:  经典写法
class Animal(object):  #新写法
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")
class Dog(object):
    def playing(self):
        print("-----玩-----")

    def drink(self):
        print("-----喝shui-----")
class Cat(Dog,Animal):
    def pao(self):
        print("-----跑-----")
        Animal.drink(self)


cat = Cat()
cat.eat()
cat.drink()
cat.playing()
cat.pao()
print(Cat.__mro__)