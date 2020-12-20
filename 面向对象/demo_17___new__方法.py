# __new__方法
# 创建对象时，系统会自动调用new方法
# 开发者可以实现new方法来自定义对象的创建过程
# 如果不重写new方法 默认会调用object的new方法来创建对象
# new方法 就是开辟内存空间 将创建的对象放入空间
class Cat:
    def __new__(cls, name):
        # 创建对象时  自动调用  负责创建对象
        # 需要将创建的对象返回  返回什么就创建什么
        print("创建对象")
        # return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self, name):
        print("对象初始化")
        self.name = name

    def __str__(self):
        return "%s" % self.name


lanmao = Cat("蓝猫")

print(lanmao)

# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
#
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
#
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
#
# 如果创建对象时传递了自定义参数，且重写了new方法，则new也必须 "预留" 该形参,否则init方法将无法获取到该参数