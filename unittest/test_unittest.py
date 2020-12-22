import unittest

class TestStringMethods(unittest.TestCase):
    # setUp和tearDown 方法是每条测试用例前后都会调用
    def setUp(self) -> None:
        print('setup')
    def tearDown(self) -> None:
        print('tearDown')

    # setUpClass和tearDownClass 方法是整个类前后分别调用一次
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod  #类方法  添加装饰器
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def test_upper(self):
        print('test_upper')
        # upper()方法将字符串中的小写字母转为大写字母
        # Assert.assertEquals();及其重载方法: 1.如果两者一致, 程序继续往下运行.2.如果两者不一致, 中断测试方法, 抛出异常信息AssertionFailedError.
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test_isupper')
        # isupper() 方法检测字符串中所有的字母是否都为大写。
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test_split')
        s = 'hello world'
        # split()通过指定分隔符对字符串进行切片，如果参数 num有指定值，则分隔num + 1个子字符串
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()