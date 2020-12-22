import unittest
import HTMLTestRunner

if __name__ == "__main__":
    # 测试用例目录
    test_dir = "./pytest"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    # 测试报告路径
    report_path = "./report.html"
    with open(report_path,"wb") as report:
        runner = HTMLTestRunner(stream = report,
                                title = "测试报告",
                                description = "系统登录测试用例执行")
        runner.run(discover)