from selenium import webdriver
import time

open_driver = webdriver.Chrome()
# open_driver = webdriver.Firefox()
# open_driver = webdriver.PhantomJS()
open_driver.get('https://www.baidu.com')
time.sleep(5)
