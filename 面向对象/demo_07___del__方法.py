
# __del__()方法
# 创建对象后，python解释器默认调用__init__()方法；
# 当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法
# 当有1个变量保存了某个对象的引用时，此对象的引用计数就会加1
# 当使用del删除变量时，只有当变量指向的对象的所有引用都被删除后，也就是引用计数为0时，才会真删除该对象（释放内存空间），这时才会触发__del__()方法

import time
class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name
    # 析构方法
    # 当对象被删除时，会自动被调用,查看对象的删除情况  垃圾处理机制
    def __del__(self):
        print("__del__方法被调用")
        print(f"{self.__name}对象马上被干掉了...")

# 创建对象
dog = Animal("哈皮狗")  #dog为全局变量
print('数据')
# 删除对象
del dog  #可以删除变量  删除后变量无法使用
cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print("---马上 删除cat的对象引用")
del cat
print("---马上 删除cat2的对象引用")
del cat2
print("---马上 删除cat3的对象引用")
del cat3

print("程序2秒钟后结束")
time.sleep(2)
