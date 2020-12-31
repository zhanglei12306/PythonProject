import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    def test_selenium_demo(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element_by_id('kw').send_keys('pytest').click()
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('pytest')
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys('pytest')
        self.driver.find_element(By.ID, 'su').click()


