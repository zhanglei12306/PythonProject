import pytest
import allure

# 添加链接

def test_attach_text():
    allure.attach('文本', attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('<head></head><body>首页</body>', '这是错误页的结果信息', attachment_type=allure.attachment_type.HTML)

def test_attach_png():
    allure.attach.file('./登录页.png', name='这是图片', attachment_type=allure.attachment_type.PNG)