# 参数化
import yaml
import pytest
def inc(x):
    return x + 10
class TestDemo:
    # @pytest.mark.parametrize('x, y', [(1, 2), (3, 4)])
    @pytest.mark.parametrize('x, y', yaml.safe_load(open('data.yml')))
    def test_answer(self, x, y):
        print(x)
        assert inc(x) == y

if __name__ == '__main__':
    pytest.main(['test_demo02.py::TestDemo', '-vs'])