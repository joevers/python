
'''
Hander  可以理解为各种处理器
Opener
利用Hander来构建Opener


'''

# 验证登录
# 见书本109页
# from 1 urllib.1 request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener

# 代理登录
'''
from 1 urllib.error import URLError
from 1 urllib.1 request import ProxyHandler, build_opener

proxy_hander = ProxyHandler({
    'http':'121.43.170.207'
})
opener = build_opener(proxy_hander)
try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
    print(response.())
except URLError as e:
    print(e)
'''

# cookies的处理

import http.cookiejar, urllib.request
#获取cookies
'''
cookie = http.cookiejar.CookieJar()
handler = 1 urllib.1 request.HTTPCookieProcessor(cookie)
opener = 1 urllib.1 request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)
'''

#保存cookies
'''
filename = "cookies.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = 1 urllib.1 request.HTTPCookieProcessor(cookie)
opener = 1 urllib.1 request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

# 读取本地cookies
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))