# 对象中包含两个组成部分:
# 属性: 用于记录与对象相关的数据，比如姓名，年龄，身高，肤色等
# 方法: 用于实现与对象相关的操作
# 定义类
class Cat:
    # 方法
    def eat(self):
        print('猫吃鱼')

    def play(self):
        print('猫玩游戏')
创建对象的格式： 引用对象的变量名 = 类名()
根据类，创建一个对象
tom = Cat()
创建对象的格式为 引用对象的变量名.方法名()
tom = Cat()
tom.eat() # 调用对象的eat方法
tom.play()



'''
class Person:
    name = 'zhangsan '
    age = 15
    gender = 'man'
    weight = 110

    def set_param(self, name):
        self.name = name
        print(self.name)

    def eat(self):
        print('eat')

    def play(self):
        print('play')

    def jump(self):
        print('jump')

Person().eat()
zs = Person().set_param('lisi')
print(zs)
'''