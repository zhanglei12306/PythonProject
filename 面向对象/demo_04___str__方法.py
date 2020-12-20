# __str__()方法
# 如果直接print打印对象，会看到创建出来的对象在内存中的地址
# 当使用print（xx）输出对象的时候，只要对象定义了__str__(self)方法，就会 打印该方法return的信息描述
# 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法

class Cat:
    """定义一个猫类"""

    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        # self.name = "汤姆"
        # self.age = 20
        self.new_name = new_name
        self.new_age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
        # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量

    def __str__(self):
        """返回一个对象的描述信息"""
        # print(num)
        return f"名字是:{self.new_name}, 年龄是:{self.new_age}"

    def eat(self):
        print(f"{self.new_name}在吃鱼....")

    def drink(self):
        print(f"{self.new_name}在喝可乐...")

    def introduce(self):
        # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
        # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
        print(f"名字是:{self.new_name}, 年龄是:{self.new_age}")

# 创建了一个对象
tom = Cat("汤姆", 30)
tom.introduce()
tom.eat()
tom.drink()
print(tom)
