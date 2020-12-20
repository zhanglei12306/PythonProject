import json
ata = {'j1': 1, 'j2': 2}
'''dumps()将python对象转换为JSON字符串'''
'''loads()将JSON字符串转换为python对象'''
json1 = json.dumps(ata)
print(json1)
print(type(json1))

atae = '{"j1": 1, "j2": 2}'
json2 = json.loads(atae)
print(json2)
print(type(json2))

f = open('testjson', 'r')
print(json.load(f))

f = open('testjson', 'w')
js = {'j3': 'op', 'j4': 'ui'}
json.dump(js,f)