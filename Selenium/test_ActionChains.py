import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    @pytest.mark.skip
    def test_selenium_demo(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element_by_id('kw').send_keys('pytest').click()
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('pytest')
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys('pytest')
        dianji = self.driver.find_element(By.ID, 'su')
        action = ActionChains(self.driver)
        action.click(dianji)
        action.perform()
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        # ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        # 鼠标移动到某个元素上
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    def test_keys(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]')
        dianji = self.driver.find_element(By.ID, 'su')
        action = ActionChains(self.driver)
        action.send_keys('pytest')
        action.send_keys(Keys.CLEAR, 'c')
        action.send_keys(Keys.BACK_SPACE)
        # 等待3秒
        time.sleep(3)
        action.send_keys(Keys.CLEAR)
        # action.click(dianji).pause(3)
        action.perform()
