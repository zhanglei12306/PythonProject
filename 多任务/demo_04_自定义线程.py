"""
使用一个线程（子线程）执行多个任务（依次按顺序执行）
"""
import threading

# # 方案1
# # 任务1
# def work1():
#     print(threading.current_thread())
#     print('任务1...3')
#
#
# def work2():
#     print(threading.current_thread())
#     print('任务2...')
#
#
# def func():
#     work1()
#     work2()
#
# if __name__ == '__main__':
#     print(threading.current_thread())
#     # 创建子线程
#     work_thread = threading.Thread(target=func)
#     # 启动线程
#     work_thread.start()
#     print(threading.active_count())

# 方案2
import threading
class MyThread(threading.Thread):
    # 重写
    # 自定义线程中 如果子类重写了父类以后的同名init方法
    # 子类需要调用父类的同名init方法
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def work1(self):
        print(self.name)
        print(threading.current_thread())
        print('任务1...')

    def work2(self):
        print(self.name)
        print(threading.current_thread())
        print('任务2...')

    # 实现一个方法  方法名 run
    def run(self):
        print(threading.current_thread())
        self.work1()
        self.work2()

if __name__ == '__main__':
    # 创建一个子线程
    work_thread = MyThread('自定义线程')
    # 启动线程
    work_thread.start()
"""
使用一个子线程执行多个任务 依次执行
"""

# import threading
#
# def sing():
#     print(threading.current_thread())
#     print('changge...')
#
#
# def dance():
#     print(threading.current_thread())
#     print('tiaowu')
#
# def func():
#     sing()
#     dance()
#
# if __name__ == '__main__':
#
#     func_therad = threading.Thread(target=func)
#
#     func_therad.start()

# class MyThread(threading.Thread):
#     def __init__(self, name):
#         super(MyThread, self).__init__()
#         self.name = name
#
#     def sing(self):
#         print(self.name)
#         print(threading.current_thread())
#         print('changge...')
#
#
#     def dance(self):
#         print(self.name)
#         print(threading.current_thread())
#         print('tiaowu...')
#
#
#     def run(self):
#         print(threading.current_thread())
#         self.sing()
#         self.dance()
# if __name__ == '__main__':
#
#     fanc_thread = MyThread('自定义线程')
#     fanc_thread.start()
