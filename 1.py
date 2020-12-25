
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(10)

driver.find_element_by_id("kw"). send_keys('test_data')
time.sleep(10)
driver.find_element_by_id("su"). click()
time.sleep(10)



