'''dic = {'name':'json'}
dic['name']='Jason'
print("dic['name']=" +dic['name'])'''
from selenium import webdriver
import time
from PIL import Image
driver = webdriver.Chrome()
'''
driver.get("https://www.baidu.com/")
driver.maximize_window()
time.sleep(5)
cookies = driver.get_cookies()
print(cookies)
'''

def start_login():

    driver = webdriver.Chrome()
    driver.get("https://qzone.qq.com/")
    driver.maximize_window()
    driver.switch_to.frame('login_frame')  # 切换到登陆界面
    driver.find_element_by_id('switcher_plogin').click()   # 选择帐号密码
    time.sleep(2)
    driver.find_element_by_name('u').clear()
    time.sleep(2)
    driver.find_element_by_name('u').send_keys('2624424668')  # 此处输入你的QQ号
    time.sleep(2)
    driver.find_element_by_name('p').clear()
    time.sleep(2)
    driver.find_element_by_name('p').send_keys('a8593698')  # 此处输入你的QQ密码
    time.sleep(5)
    driver.find_element_by_id('login_button').click()  # 点击登陆按键
    time.sleep(5)
    cookies = driver.get_cookies()
    for cookie in cookies:
       print(cookie)
'''
    driver = webdriver.Chrome()
    driver.get("https://qzone.qq.com/")
    driver.maximize_window()
    cook= [{'name': 'pgv_pvid', 'expiry': 2147385600, 'path': '/', 'secure': False, 'value': '3948180847', 'domain': '.qq.com', 'httpOnly': False},
          {'name': 'p_skey', 'path': '/', 'secure': True, 'value': '9FEGxq5HHhs4rhq1iqeD9SgGAlFmvP5SnfzOSqX8YXg_', 'domain': '.qzone.qq.com', 'httpOnly': False},
          {'name': 'Loading', 'expiry': 1604073600, 'path': '/', 'secure': False, 'value': 'Yes', 'domain': '.qzone.qq.com', 'httpOnly': False},
          {'name': 'pt4_token', 'path': '/', 'secure': False, 'value': 'oFGvd3bM5bbuuTHVz2hKTuHq9xciMCKDLnsSrmrJRhY_', 'domain': '.qzone.qq.com', 'httpOnly': False},
          {'name': 'qz_screen', 'expiry': 1606651834, 'path': '/', 'secure': False, 'value': '1916x928', 'domain': '.user.qzone.qq.com', 'httpOnly': False},
          {'name': 'p_uin', 'path': '/', 'secure': False, 'value': 'o2624424668', 'domain': '.qzone.qq.com', 'httpOnly': False},
          {'name': 'RK', 'expiry': 2147483647, 'path': '/', 'secure': False, 'value': 'IWR1Wk5jk8', 'domain': '.qq.com', 'httpOnly': False},
          {'name': 'skey', 'path': '/', 'secure': False, 'value': '@unODfuqaQ', 'domain': '.qq.com', 'httpOnly': False}, {'name': 'ptcz', 'expiry': 2147483647, 'path': '/', 'secure': False, 'value': '6cdb58c683d9a768407283802c5fc5c13c3c53aeedd93b6490b1be3e09592534', 'domain': '.qq.com', 'httpOnly': False}, {'name': 'uin', 'path': '/', 'secure': False, 'value': 'o2624424668', 'domain': '.qq.com', 'httpOnly': False}, {'name': 'ptui_loginuin', 'expiry': 1606651830, 'path': '/', 'secure': False, 'value': '2624424668', 'domain': '.qq.com', 'httpOnly': False}, {'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s3608718580', 'domain': '.qq.com', 'httpOnly': False}]
    for cookie in cook:
        if 'expiry' in cookie:
            del cookie['expiry']
        print(cookie)
        driver.add_cookie(cookie)
    driver.refresh()
'''


if __name__ == '__main__':
    start_login()