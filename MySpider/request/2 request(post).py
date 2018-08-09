import requests

data = {'name':'qiao','age':'22'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

