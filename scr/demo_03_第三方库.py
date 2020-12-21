import requests

r = requests.get('https://www.baidu.com/')
print(r.status_code)
print(r.encoding)
r.encoding = 'utf-8'
print(r.text)

r = requests.post('https://www.baidu.com/',data={'key':'value'})
print(r.text)