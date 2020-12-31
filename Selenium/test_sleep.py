import time

import selenium
from selenium import webdriver
# class TestSelenium:
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         # 添加隐式等待全局
#         self.driver.implicitly_wait(3)
#
#     def teardown(self):
#         self.driver.quit()
#     def test_selenium_demo(self):
#         self.driver.get("https://testerhome.com/")
#         self.driver.find_element_by_link_text('社团').click()
#         self.driver.find_element_by_link_text('神州数码质量测试三部').click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSleep:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.maximize_window()
        # 添加隐式等待全局
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_selenium_demo(self):
        category_name = (By.CSS_SELECTOR, '#ember313 .category-name')
        self.driver.find_element_by_link_text('所有分类').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(category_name))
        self.driver.find_element(*category_name).click()


