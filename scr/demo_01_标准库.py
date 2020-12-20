import os
import time
import datetime
import urllib.request
import math
# 创建目录
# os.mkdir('testdir')
# 查看文件及目录
# print(os.listdir('./'))
# # 查看当前路径
# print(os.getcwd())
# # 查看文件是否存在
# print(os.path.exists("test"))
# if not os.path.exists("test"):
#     os.mkdir('test')
# if not os.path.exists("test/test.txt"):
#     f = open('test/test.txt','w')
#     f.write('hi,os useing')
#     f.close()
# f = open('test/test.txt', 'r')
# print(f.read())

# print(time.time())   # 时间戳
# print(time.asctime())  # 国外的时间格式
# time.sleep(2)
# print(time.localtime())  # 时间戳转换为元组
# print(time.localtime())
# print(time.strftime("%Y-%m-%d, %H:%M:%S"))  # 当前时间戳转换为带格式的的时间
#
# # 获取三天前的时间
# # 先获得时间数组格式的日期
# threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
# threeDayAgo1 = (datetime.datetime.now() + datetime.timedelta(days=3))
# # 转换为时间戳
# timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# timeStamp1 = int(time.mktime(threeDayAgo1.timetuple()))
# # 转换为其他字符串格式
# otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
# otherStyleTime1 = threeDayAgo1.strftime("%Y-%m-%d %H:%M:%S")
# print(otherStyleTime)
# print(otherStyleTime1)

# response = urllib.request.urlopen('https://www.baidu.com/')
# print(response.status)
# print(response.read())
# print(response.headers)

print(math.ceil(5.5)) #大于参数的最小整数
print(math.floor(5.5)) #小于参数的最小整数
print(math.sqrt(9)) #参数的开方根
print(math.ceil(5.6))