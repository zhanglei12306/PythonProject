# 线程
import _thread
import threading
import logging
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)
'''    
def sing():
    logging.info('sing start time' + ctime())
    sleep(5)
    logging.info('sing end time' + ctime())

def dance():
    logging.info('dance start time' + ctime())
    sleep(10)
    logging.info('dance end time' + ctime())

def main():
    logging.info('loop main time' + ctime())
    # sing()
    # dance()
    _thread.start_new_thread(sing, ())
    _thread.start_new_thread(dance, ())  #
    sleep(20)  
    logging.info('loop main time' + ctime())
if __name__ == '__main__':
    main()
'''
loops = [2, 4]
# class MyThread(threading.Thread):
#     # 重写
#     # 自定义线程中 如果子类重写了父类以后的同名init方法
#     # 子类需要调用父类的同名init方法
#     def __init__(self, func, args, name):
#         super(MyThread, self).__init__()
#         self.func = func
#         self.args = args
#         self.name = name
#
#     def run(self):
#         self.func(*self.args)

def loop(nloop, nsec):
    logging.info('start time loop:' + str(nloop) + ctime())
    sleep(nsec)
    logging.info('end time loop:' + str(nloop) + ctime())

def main():
    logging.info('loop main time:' + ctime())
    threads = []
    nloops = range(len(loops))
    #创建两个线程
    for i in nloops:
        work_thread = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(work_thread)
    # 启动两个线程
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info('loop main time' + ctime())
if __name__ == '__main__':
    main()