
# 私有属性
# 为了避免属性被设置为 脏数据，更好的保护属性安全，一般的处理方式为
# 添加一个方法，在方法内部先判断数据的有效性，再赋值属性
# 将属性定义为 私有属性，避免对象在外部直接操作属性
# 如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性
# 私有属性只能在类的内部访问

class Dag:
    def __init__(self):
        self.__age = 0  #私有属性 不能被类外部访问

    def set_age(self, age):
        # 是否判断合法
        if age >= 0 and age <= 20:
            self.__age = age
        else:
            self.__error_waring('age')

    def ge_age(self):
        return self.__age

    def __error_waring(self, property_name):  #私有方法 不能被类外部访问
        print(f"[error]:数据｛self.property_name｝赋值失败")

    def __send_msg(self):
        print("发送短信")


dag = Dag()
# dag.age = -15   #脏数据 破坏程序的稳定性
dag.set_age(-10)  #只能用这个方法的来设置属性
print(dag.ge_age())

