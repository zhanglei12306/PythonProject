
# self
# 关键字 self 主要用于对象方法中，表示调用该方法的对象
# 在方法中使用 self，可以获取到调用当前方法的对象，进而获取到该对象的属性和方法

class Cat:
    # 方法
    def introduce(self):
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))
        print(f"名字是:{self.name}, 年龄是:{self.age}")

# 创建了一个对象
tom = Cat()
# 给对象tom添加了一个属性,叫name,,里面的值是"汤姆"
tom.name = "汤姆"
tom.age = 5
tom.introduce() # 打印结果：名字是汤姆, 年龄是5

# 创建另一个对象
lan_mao = Cat()
lan_mao.name = "蓝猫"
lan_mao.age = 20
lan_mao.introduce()  # 打印结果：名字是蓝猫, 年龄是20

# 使用self操作属性 和对象的变量名操作属性效果上相同，如果属性在赋值时还没有定义，则会自动定义属性并赋值
class Cat:
    # 方法
    def introduce(self):
        self.type = "小型动物"

# 创建了一个对象
tom = Cat()
# 调用对象的方法
tom.introduce()
# 获取对象的属性
print(tom.type)

# 创建另一个对象
lanmao = Cat()
# 获取对象的属性
print(tom.type)  # 会发生什么？
# 调用对象的方法
tom.introduce()
