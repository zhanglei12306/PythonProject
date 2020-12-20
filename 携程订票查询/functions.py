# coding=utf-8
from datetime import datetime, date, timedelta
from selenium import webdriver
import xlrd
driver = webdriver.Chrome()
#返回driver对象
def return_driver():
    return driver
#函数打开网址首页
def open_base_site(url):
    return driver.get(url)
#函数返回n天后的日期
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))).strftime('%Y-%m-%d'))

def id(element):
    return driver.find_element_by_id(element)
def css(element):
    return driver.find_element_by_css_selector(element)
def js(element):
    return driver.execute_script("document.getElementById(" + "'" + element + "'" + ").removeAttribute('readonly')")
def xpath(element):
    return driver.find_element_by_xpath(element)

#添加函数 处理和获取excel中的数据
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data
    return dic
def log(str):
    logging


