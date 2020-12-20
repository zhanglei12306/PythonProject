
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('kw').send_keys('test')
driver.save_screenshot('qu.png')
'''
from selenium import webdriver
import time
from PIL import Image
driver = webdriver.Chrome()
driver.get("https://www.ctrip.com/")
driver.maximize_window()
time.sleep(5)
driver.save_screenshot('qu.png')
imgcode = driver.find_element_by_id("vcodeImg")
left = imgcode.location['x']
top = imgcode.location['y']
right = left + imgcode.size['width']
bottom = top + imgcode.size['height']
im = Image.open('qu.png')
im = im.crop((left,top,right,bottom))
im.save(t.png)
'''

from selenium import webdriver
import time
from PIL import Image



# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element_by_id('kw').send_keys('test')
# driver.find_element_by_id('su').click()

