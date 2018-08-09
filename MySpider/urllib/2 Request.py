import urllib.request

'''
Request包含的参数:
url, data=None, headers={}, origin_req_host=None, unverifiable=False,method=None):
1. url 用于请求URL, 必传参数, 其他都是可选参数
2. data 参数,  必须传bytes类型, 如果是字典,可以先用urllib.parse模块里的urlencode()进行编码
3.headers 请求头, 是一个字典, 可以通过headers参数直接构造,也可通过add_header()方法添加
            添加请求头最常用的方法就是修改 User-Agent 来伪装浏览器
4.origin_req_host  表示请求方的host名称或者IP地址
5.unverifiable 表示这个请求是否是无法验证的   默认为False
6.method   请求的方法   包括GET和POST以及PUT等
'''


# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)

# print(response.read().decode('utf-8'))


from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Host':'httpbin.org',
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 使用add_headers
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')

res = request.urlopen(req)
print(res.read().decode('utf-8'))