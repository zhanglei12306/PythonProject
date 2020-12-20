# __init__()方法
# __init__()方法叫做 对象的初始化方法，在 创建一个对象后默认会被调用，不需要手动调用
# 开发者可以 实现这个方法，并在该方法中定义属性并设置初始值
# init方法 设置的自定义参数必须和创建对象时传递的参数保持一致
class Cat:
    # 初始化方法
    # def __init__(self):
    #     # 设置对象的默认属性及初始值
    #     self.type = "小型动物"
    """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def gaibian(self):
        print(f"名字是:{self.name}, 年龄是:{self.age}")
# 创建了一个对象
tom = Cat("汤姆", 30)
tom.gaibian()
# 获取对象的属性
# print(tom.type)
