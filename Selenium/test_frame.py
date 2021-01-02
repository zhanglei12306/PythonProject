from time import sleep

from Selenium.base import Bash


class TestWindowHandle(Bash):


    def test_window_handle(self):
        self.driver.get('https://qzone.qq.com/')
        print(self.driver.current_window_handle)
        # 切换至frame
        self.driver.switch_to.frame('login_frame')
        self.driver.find_element_by_id("switcher_plogin").click()
        # self.driver.switch_to.frame('loginform')
        self.driver.find_element_by_id("u").send_keys('username')
        self.driver.find_element_by_id("p").send_keys('password')
        self.driver.find_element_by_id("login_button").click()







