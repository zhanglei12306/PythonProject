from time import sleep

from selenium import webdriver
class Bash:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def teardown(self):
        sleep(5)
        self.driver.quit()