'''
from selenium import webdriver
import time
from datetime import datetime, date, timedelta
from selenium.webdriver.common.action_chains import ActionChains

def start_login(n):
    return str((date.today() + timedelta(days = +int(n))).strftime('%Y-%m-%d'))

from_station = '上海'
to_station = '杭州'
TOMO = start_login(1)
print(TOMO)
driver = webdriver.Chrome()
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_id('departCityName').send_keys(from_station)
time.sleep(2)
driver.find_element_by_id('arriveCityName').send_keys(to_station)
time.sleep(2)
driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
driver.find_element_by_id('departDate').clear()
driver.find_element_by_id('departDate').send_keys(TOMO)
# 点击其他地方去除时间下拉框
ActionChains(driver).move_by_offset(0,0).click().perform()
time.sleep(2)
driver.find_element_by_css_selector("input[class='searchbtn']").click()
time.sleep(2)
driver.find_element_by_xpath('//div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a').click()
time.sleep(2)
driver.find_element_by_css_selector("input[class='input-name']").send_keys('张晓')

if __name__ == '__main__':
    start_login()
'''
'''
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
from_station = '上海'
to_station = '杭州'
TOMO = date_n(1)
print(TOMO)
driver = webdriver.Chrome()
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
driver.maximize_window()
time.sleep(2)
id('departCityName').send_keys(from_station)
time.sleep(2)
id('arriveCityName').send_keys(to_station)
time.sleep(2)
js('departDate')
id('departDate').clear()
id('departDate').send_keys(TOMO)
# 点击其他地方去除时间下拉框
ActionChains(driver).move_by_offset(0,0).click().perform()
time.sleep(2)
css("input[class='searchbtn']").click()
time.sleep(2)
driver.find_element_by_xpath('//div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a').click()
time.sleep(2)
css("input[class='input-name']").send_keys('张晓')
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from functions import date_n, id, css, js, return_driver, open_base_site

def search_tickets(from_station, to_station, n):
    driver = return_driver()
    open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    from_station = from_station

    to_station = to_station

    TOMO = date_n(n)
    print(TOMO)
    driver.maximize_window()
    time.sleep(2)
    id('departCityName').send_keys(from_station)
    time.sleep(2)
    id('arriveCityName').send_keys(to_station)
    time.sleep(2)
    js('departDate')
    id('departDate').clear()
    id('departDate').send_keys(TOMO)
    # 点击其他地方去除时间下拉框
    ActionChains(driver).move_by_offset(0,0).click().perform()
    time.sleep(2)
    css("input[class='searchbtn']").click()



