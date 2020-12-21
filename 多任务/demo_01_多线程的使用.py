'''
targe  [tɑ:dʒ]
thread  *[θred] 线程
'''

# # 导入线程模块
# import threading, time
#
# # 任务唱歌
# def sing():
#     for i in range(5):
#         print('唱歌...')
#         time.sleep(0.3)
#
#
# def dance():
#     for i in range(5):
#         print('跳舞...')
#         time.sleep(0.3)
#
# if __name__ == '__main__':
#
#     # 创建两个子进程执行任务
#     # targe=函数名（任务）
#     sing_thread = threading.Thread(target=sing)
#     dance_thread = threading.Thread(target=dance)
#
#     # 启动线程（cpu调度线程执行任务）  不确定执行哪个线程 等待cpu调度  调度那个线程  那个线程执行任务
#     sing_thread.start()
#     dance_thread.start()

# 导入模块
import _thread
import threading, time

def sing():
    for i in range(3):
        print('tiaowu...')
        time.sleep(0.2)

def dance():
    for i in range(3):
        print('changge....')
        time.sleep(0.2)


if __name__ == '__main__':

    # 创建子线程
    # target=函数名
    sing_threading = threading.Thread(target=sing)
    dance_threading = threading.Thread(target=dance)

    # 启动线程
    sing_threading.start()
    dance_threading.start()
    # 简便写法
    # _thread.start_new_thread(sing, ())
    # _thread.start_new_thread(dance, ())
    # 查看线程的数量
    while True:
        length = len(threading.enumerate())
        print(f'线程数为：{length}')
        if length <= 1:
            break
