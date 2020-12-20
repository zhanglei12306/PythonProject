# 多态: 使用父类对象的地方,可以使用子类对象代替
# 鸭子类型: python是动态语言, 不强制约束数据类型,只要数据可以满足要求,就会执行
# 鸭子类型语言中，函数/方法可以接受一个任意类型的对象作为参数/返回值，只要该对象实现了代码后续用到的属性和方法就不会报错
class Meat:  # 肉类
    def __init__(self):
        self.name = "肉"

class Ham(Meat):  # 火腿类
    def __init__(self):
        super().__init__()
        self.name = "火腿"

class DiGua:  # 地瓜类
    def __init__(self):
        self.name = "地瓜"

# def eat(Meat meat):  #  对于大多数面向对象语言(java c++),参数会约束类型,必须传递指定类型/或其子类的数据,否则报错
def eat(meat):
    print(f"吃:{meat.name}")

m1 = Meat()
a = Ham()
digua1 = DiGua()
eat(m1)
eat(a)