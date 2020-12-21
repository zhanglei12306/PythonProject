# 导入线程模块
import threading, time

# 任务一跳舞
def sing():
    print(threading.current_thread())
    for i in range(3):
        print('唱歌...')
        time.sleep(0.3)

def dance():
    # print(threading.current_thread())
    for i in range(3):
        print('跳舞...')
        time.sleep(0.3)

if __name__ == '__main__':
    # 查看一个运行的程序中的某个程序是由哪个线程执行的
    # <_MainThread(MainThread, started 2268)>
    # print(threading.current_thread())
    # # 查看一个运行的程序总执行任务的线程列表
    # print(threading.enumerate())
    # # 查看一个运行的程序中执行的线程个数
    # print(len(threading.enumerate()))
    # # print(threading.active_count())
    # print(threading.active_count())

    # 创建两个子线程执行任务
    # target=函数名（任务）
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    # 启动线程
    sing_thread.start()
    dance_thread.start()
    print(threading.enumerate())
    print(threading.active_count())

# # 导入线程模块
# import threading, time
#
# def sing():
#     print(threading.current_thread())
#     print(threading.enumerate())
#     for i in range(3):
#         print('changge...')
#         time.sleep(0.3)
#
#
# def dance():
#     print(threading.current_thread())
#     print(threading.enumerate())
#     for i in range(3):
#         print('tiaowu...')
#         time.sleep(0.3)
#
#
# if __name__ == '__main__':
#
#     # 查看一个运行的程序中运行的某个程序是由哪个线程执行的
#     print(threading.current_thread())
#     # 查看一个运行程序的总执行任务的线程列表
#     print(threading.enumerate())
#     # 查看一个运行程序中执行的线程个数
#     # print(len(threading.enumerate()))
#     # print(threading.active_count())
#
#     #创建子线程
#     sing_thread = threading.Thread(target=sing)
#     dance_thread = threading.Thread(target=dance)
#
#     # 启动线程
#     sing_thread.start()
#     dance_thread.start()
#     print(threading.active_count())
