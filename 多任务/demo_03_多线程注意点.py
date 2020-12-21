# import threading
# import time
#
# # 任务
# def work(num, name, age):
#     print(name, age)
#     for i in range(num):
#         print('工作...')
#         time.sleep(0.3)
#
#
# if __name__ == '__main__':
#      """
#      在使用多线程技术中  先执行测试  或者先执行工作 都是有可能的
#      （cpu调度线程执行任务） 所以不确定
#      """
#      # 创建一个子线程执行任务
#      # 传递参数
#      # arges 元组（实参）
#      # kwargs 字典（实参）
#      # 建议在实际中 使用一种即可 args 或 kwargs字典
#      work_thread = threading.Thread(target=work, args=(10,), kwargs={'name':'xm', 'age': 15})
#      # 需求：无论子线程的任务是否完成 如果主线程执行完任务 程序必须退出
#      # 解决： 主线程守护
#      work_thread.setDaemon(True)
#      # 启动线程
#      work_thread.start()
#      time.sleep(0.2)
#      print('测试')
"""
如果当前有且只有一个线程（主线程） 主线程任务执行完 那么程序退出
如果当前主线程中创建子线程执行任务 默认情况下主线程需要等待子线程执行

"""

import threading, time

def work(num, name, age):
    print(name, age)
    for i in range(num):
        print('工作....')
        time.sleep(0.3)

if __name__ == '__main__':
    """
    在使用多线程技术中  先执行测试  或者先执行工作  都是有可能的
    因为由cpu调度线程执行任务  即不确定先执行哪个
    """
    # 传递参数
    # arges 元组（实参）
    # kwargs 字典 （实参）
    # 建议实际使用中  使用一种即可  args和kwargs 任选其一
    work_thread = threading.Thread(target=work, args=(6,), kwargs={'name':'小邵', 'age':89})

    # 需求：无论子线程的任务是否完成  如果主线程的任务完成 程序必须退出
    # 解决：主线程守护
    work_thread.setDaemon(True)
    work_thread.start()
    time.sleep(0.3)
    print('测试....')

"""
如果当前有且只有一个线程（主线程） 主线程任务执行完 那么程序退出
如果当前主线程中创建子线程执行任务  默认情况下主线程需要等待子线程执行完 程序再退出
"""

