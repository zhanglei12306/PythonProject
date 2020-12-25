import allure
import pytest

from selenium import webdriver
import time
@allure.testcase("https://www.baidu.com/")
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data):
    with allure.step('打开百度'):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        time.sleep(10)
    with allure.step(f'输入：{test_data}'):
        driver.find_element_by_id("kw"). send_keys(test_data)
        time.sleep(10)
        driver.find_element_by_id("su"). click()
        time.sleep(10)
    with allure.step('图片'):
        driver.save_screenshot("./result/b.png")
        allure.attach.file('./result/b.png', name='这是图片', attachment_type=allure.attachment_type.PNG)
    with allure.step('关闭'):
        driver.quit()
