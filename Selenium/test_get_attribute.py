import selenium
from selenium import webdriver
class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
    def test_selenium_demo(self):
        self.driver.get("https://www.baidu.com/")
        # 获取元素内get_attribute('value')
        search = self.driver.find_element_by_id('su').get_attribute('value')
        assert search == '百度'