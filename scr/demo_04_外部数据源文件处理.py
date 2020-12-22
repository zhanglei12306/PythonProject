'''

#读取Excel
import xlrd
xls = xlrd.open_workbook("exce.xlsx")
sheet = xls.sheet_by_index(0)
print(sheet.nrows)  #打印总行数

print(sheet.ncols)  #打印总列数
print(sheet.row_values(1)[0])  #打印第二行第一个单元格
print('*' * 100)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(sheet.row_values(row)[col])
'''


#写入Excel
'''
import xlwt

wb = xlwt.Workbook()
sheet = wb.add_sheet('测试',cell_overwrite_ok=True)
sheet.write(0,0,"auto")
sheet.write(0,0,"sele")
wb.save('exc.xlsx')
'''



import xlwt
work_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = work_book.add_sheet('test', cell_overwrite_ok=True)
headings = ['职位类别', '工作地址', '职位月薪', '工作地点', '工作经验要求', '职位要求',  '最低学历要求']
for i in range(0, len(headings)):

    sheet.write(0, i, headings[i])
    # 写入第一行 的数据列为len(headings), 每次写入的是第1行第i列的值
work_book.save('exc.xlsx')