
import time
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     time.sleep(5)
    #     self.driver.quit()

    def test_touchactionsscroll(self):

        '''
        打开Chrome
        打开URL : http://www.baidu.com
        向搜索框中输入'selenium测试'
        通过TouchAction 点击搜索框
        滑动到底部，点击下一页.
        关闭Chrome
        '''
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        el_find = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        # 指定元素上敲击
        action.tap(el_find)
        action.perform()
        # 从某个元素位置开始手势点击并滚动(向下滑动为负数，向上滑动为正数)
        action.scroll_from_element(el, 0, 10000).perform()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()

