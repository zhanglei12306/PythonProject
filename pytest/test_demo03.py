# 数据驱动
import yaml
import pytest

class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('env.yml')))
    def test_one(self, env):
        if 'test' in env:
            print('测试环境')
            print(env)
            print(env['test'])
            print(yaml.safe_load(open('env.yml')))
        elif 'dev' in env:
            print('开发环境')
    # def test_yaml(self):


if __name__ == '__main__':
    pytest.main(['test_demo03.py::TestDemo', '-vs'])