from requests import  Request, Session

url = 'http://httpbin.org/post'
data = {
    'name':'qiao',
    'age':22
}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
}
s = Session()
req = Request('POST', url=url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)