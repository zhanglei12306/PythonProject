import pytest
import allure

# 添加链接
@allure.link('https://www.baidu.com/', name='百度')
def test_login_success():
    print("这是百度的链接")
    pass
wendang = 'https://docs.qameta.io/allure/#_python'
@allure.link(wendang, name='百度')
def test_login_succes():
    print("这是百度的链接")
    pass
