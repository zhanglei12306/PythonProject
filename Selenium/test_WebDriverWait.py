import time

from selenium import webdriver
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
        self.driver.find_element(By.XPATH, '//*[@title="招聘内推"]').click()
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="posts sortable num"]')) >= 1
        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="posts sortable num"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()



