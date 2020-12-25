import pytest
def inc(x):
    return x + 1

@pytest.mark.parametrize('x, y',[(1,2),(3,4)])
def test_answer(x, y):
    assert inc(x) == y

@pytest.fixture()
def login():
    print('执行前先登录')
    name = 'join'
    return name


class TestDemo:
    def test_one(self, login):
        print(f'test_one={login}')

    def test_two(self):
        print('test_two')

    def test_three(self):
        print('test_three')

if __name__ == '__main__':
    pytest.main(['test_demo01.py::TestDemo', '-v'])