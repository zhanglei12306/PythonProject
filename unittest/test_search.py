'''

'''

import unittest


class Search:
    def search_func(self):
        print('search')
        return True

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print('setUpClass')

    @classmethod  # 类方法  添加装饰器
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def test_search(self):
        print('test_search')
        assert True == self.search.search_func()

    def test_search1(self):
        print('test_search1')
        assert True == self.search.search_func()

    def test_equal(self):
        print('断言相等')
        self.assertEqual(1, 1, '判断1 == 1')

    def test_notequal(self):
        print('断言不相等')
        self.assertNotEqual(1, 2, '判断1 == 2')
class TestSearch1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print('setUpClass')

    @classmethod  # 类方法  添加装饰器
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def test_search1(self):
        print('test_search')
        assert True == self.search.search_func()

# 执行方法一
# if __name__ == '__main__':
#     unittest.main()
# 执行方法二
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestSearch('test_equal'))
#     unittest.TextTestRunner().run(suite)

# 执行方法三
# if __name__ == '__main__':
#     suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
#     suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
#     suite = unittest.TestSuite([suite1, suite2])
#     unittest.TextTestRunner(verbosity=2).run(suite)
# 执行方法四
# 匹配某个目录下的所有的test开头的py文件 执行这些文件下的所有的测试用例
if __name__ == '__main__':
    test_dir = '.pytest'
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(dis)
