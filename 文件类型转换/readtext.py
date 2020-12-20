'''
text文件
f2 = open("./asd", "r")
print(f2.read(2))
print('*'*100)
lines = f2.readlines()
for line3 in lines:
    print(line3)
'''
'''
csv文件  EXCEL
import csv
f2 = csv.reader(open("tes", "r"))
print(type(f2))
print('*'*100)
for line3 in f2:
    print('*' * 100)
    print(line3[0])
'''
