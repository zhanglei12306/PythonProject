
'''
# Case
# 使用 SweetPotato 类可以创建 地瓜对象
# 地瓜有两个属性：
# 状态 state：字符串
# 烧烤总时间 cooked_time：整数
# 定义 cook 方法, 提供参数 time 设置 本次烧烤的时间
# 使用 本次烧烤时间 对 烧烤总时间 进行 累加
# 根据 烧烤总时间, 设置地瓜的状态：
# [0, 3) -> 生的
# [3, 6) -> 半生不熟
# [6, 8) -> 熟了
# 大于等于8 -> 烤糊了
class SweetPotato:
    def __init__(self):
        self.state = '生的'
        self.cooked_time = 0
        self.condiments = []  # 佐料列表

    def __str__(self):
        """返回一个对象的描述信息"""
        # print(num)
        return f"地瓜的状态是:{self.state}, 烧烤总时间是:{self.cooked_time}, 佐料列表是:{self.condiments}"

    def cook_time(self,time):
        self.cooked_time += time
        if self.cooked_time > 0 and self.cooked_time < 3:
            self.state = '生的'
        if self.cooked_time > 3 and self.cooked_time < 6:
            self.state = '半生'
        if self.cooked_time > 6 and self.cooked_time < 9:
            self.state = '熟了'
        if self.cooked_time > 9:
            self.state = '糊了'

    def condiment(self,condi):
        self.condiments.append(condi)


digua = SweetPotato()
digua.cook_time(1)
digua.condiment('盐')
print(digua)
digua.cook_time(5)
digua.condiment('孜然')
print(digua)
digua.cook_time(7)
print(digua)
'''
class Item:
    def  __init__(self,type,area):
        self.type = type
        self.area = area

    def __str__(self):
        return f"家具类型:{self.type},家具面积:{self.area}"

class Home:
    def  __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area
        self.items = []

    def __str__(self):
        return f"地址:{self.address},家具面积:{self.area}，剩余家具面积:{self.free_area}"

    def add_item(self,item):
        result_area = self.free_area - item.area
        if result_area >=0:
            print(f"{item.type}添加成功")
            self.items.append(item)
            self.free_area -= item.area
        else:
            print(f"{item.type}添加s失败，面积不足")

item1 = Item('桌子', 4)
item2 = Item('椅子', 4)
print(item1)
fangzi = Home('烽火大厦', 400)
print(fangzi)
fangzi.add_item(item1)
print(fangzi)
fangzi.add_item(item2)
print(fangzi)
