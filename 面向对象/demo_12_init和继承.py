class Animal(object):  #新写法
    def __init__(self):
        self.type = '动物'


class Dog(Animal):
    def __init__(self):  #重写了init属性  需要先调用父类的init方法来继承属性
        super().__init__()
        self.__color = '黑'

dag = Dog()
print(dag.type)

