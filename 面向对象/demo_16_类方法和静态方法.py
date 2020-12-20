# 类方法
# 类对象所拥有的方法
# 需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数。
class Dog:
    __type = "狗"  # 私有类属性
    # 类方法使用场景: 方法中只使用了类对象,但没有使用实例对象
    @classmethod  # @classmethod下边定义的第一个方法会变为类方法   装饰器
    def get_type(cls):  #get_type方法 访问私有属性
    # 类方法第一个形参默认为cls,对应的实参是类对象,而且也是自动传递
        return cls.__type

# 调用类方法  类对象/实例对象都可以
print(Dog.get_type())
dog1 = Dog()
print(dog1.get_type())

# 静态方法
# 需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）。
# 静态方法 也能够通过 实例对象 和 类对象 去访问。
class Cat:
    # def eat(self):
    #     print("吃东西")

    # 静态方法使用场景: 方法中既不使用类对象,也不使用实例对象  取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
    @staticmethod
    def eat():  # 静态方法不会自动传递实例对象和类对象
        print("吃东西")

# 调用静态方法  类对象/实例对象都可以
Cat.eat()
dog1 = Cat()
dog1.eat()

# 调用对象方法
# class Dog:
#     def eat(self):
#         print("吃东西")
#
# dog1 = Dog()
# dog1.eat()  # 实例对象调用对象方法
# Dog.eat(dog1)  # 类对象调用对象方法,必须手动传递实例对象
# 调用被重写的方法 父类名.方法(对象)

# 注意点：
# 类中定义了同名的对象方法、类方法、静态方法时，调用方法会优先执行最后定义的方法
class Animal:
    def demo_method(self):
        print("对象方法")

    @classmethod
    def demo_method(cls):
        print("类方法")

    @staticmethod
    def demo_method():  # 被最后定义,调用时优先执行
        print("静态方法")

dog1 = Animal()
Animal.demo_method()  # 结果: 静态方法
dog1.demo_method()  # 结果: 静态方法


