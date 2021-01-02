
import time

import pytest
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestJs:
    def setup(self):

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    @pytest.mark.skip
    def test_js(self):

        '''
        打开Chrome
        打开URL : http://www.baidu.com
        向搜索框中输入'selenium测试'
        滑动到底部，点击下一页.
        关闭Chrome
        '''
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element_by_id("kw").send_keys("selenium测试")
        js = "document.getElementById('kw').value = 'selenium测试'"
        self.driver.execute_script(js)
        el = self.driver.execute_script("return document.getElementById('su')")
        el.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_readonly(self):
        self.driver.get("https://www.12306.cn/index/")
        elm = self.driver.execute_script("document.getElementById('train_date') .removeAttribute ('readonly')")
        # elm = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute ('readonly')")

        self.driver.execute_script("document.getElementById('train_date').value = '2021-01-30'")






