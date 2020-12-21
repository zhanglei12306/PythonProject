import threading, time

# 创建一个全局变量（可变的空列表）
# list == []
my_list = []
# 任务1 往列表中添加数据
def write():
    for i in range(5):
        my_list.append(i)
        print('write:', my_list)
        time.sleep(0.2)
    print('完成', my_list)

# 任务2 读取列表中的数据
def read():
    print('read', my_list)

if __name__ == '__main__':
    # 创建两个子线程（写入数据 一个读取数据）
    write_thread = threading.Thread(target=write)
    read_thread = threading.Thread(target=read)

    #启动线程
    write_thread.start()

    # 使用线程同步
    # 如果使用多个线程执行多个任务
    # 一个线程执行任务的结果要作为当前第二个线程执行任务的使用  必须等待第一个线程执行完
    # 再执行第二个线程
    # writte_thread.join() 告知主线程等待这个线程执行完然后再往下执行
    # 为了数据安全 牺牲性能
    write_thread.join()
    read_thread.start()

# import threading,time
#
# list = []
# def write():
#     for i in range(5):
#         list.append(i)
#         print('write', list)
#         time.sleep(0.2)
#     print('jiesu', list)
#
#
# def read():
#     print('read', list)
#
# if __name__ == '__main__':
#     write_thread = threading.Thread(target=write)
#     read_thread = threading.Thread(target=read)
#
#     write_thread.start()
#     write_thread.join()
#     read_thread.start()
