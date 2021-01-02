from time import sleep

from selenium import webdriver
class TestWindowHandle:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_window_handle(self):
        self.driver.get('https://www.baidu.com/')
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        window_handle = self.driver.window_handles
        self.driver.switch_to_window(window_handle[-1])
        print(self.driver.window_handles)
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('username')
        sleep(10)
        self.driver.switch_to_window(window_handle[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('username')
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('password')
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()







