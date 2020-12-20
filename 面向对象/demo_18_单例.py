# 设计模式: 开发者总结出的针对某种需求的编程思路
# 单例模式: 可以让类创建出的对象始终只有一个
class ShoppingCart:  # 购物车是典型的单例
    # 细节1: 定义私有类属性  避免外部修改
    __instance = None   # 类属性  记录创建的对象
    __has_init = False   # 类属性  记录是否进行过初始化

    def __new__(cls, *args, **kwargs):
        # 第一次调用new,创建对象并且记录该对象;
        # 第2-n次调用new,直接返回记录的对象
        # 判断是否为第一次调用
        if cls.__instance is None:
            # 创建对象
            new_obj = object.__new__(cls)
            # 记录对象
            cls.__instance = new_obj
        return cls.__instance

    # 细节2: 单例中的对象只能初始化一次
    def __init__(self):
        # 判断是否进行过初始化
        if not ShoppingCart.__has_init:
            self.total_price = 0  # 购物车商品总价
            # 修改类属性的值
            ShoppingCart.__has_init = True
# 网页1
cart1 = ShoppingCart()
cart1.total_price += 100  # 添加商品  total_price = 100
print(cart1.total_price)  # total_price = 100

# 网页2
cart2 = ShoppingCart()  # total_price = 0
print(cart2.total_price)  # total_price = 0