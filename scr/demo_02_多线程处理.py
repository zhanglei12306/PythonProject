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
def loop(nloop, nsec, lock):
    logging.info('start time loop' + str(nloop) + ctime())
    sleep(nsec)
    logging.info('end time loop' + str(nloop) + ctime())
    lock.release()


def main():
    logging.info('loop main time' + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
# ab
    logging.info('loop main time' + ctime())
if __name__ == '__main__':
    main()