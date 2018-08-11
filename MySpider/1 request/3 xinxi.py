import requests

r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)
print('==' * 20)
print(type(r.headers), r.headers)
print('==' * 20)
print(type(r.cookies), r.cookies)
print('==' * 20)
print(type(r.url), r.url)
print('==' * 20)
print(type(r.history), r.history)
print('==' * 20)