import urllib.request
from time import sleep

# response = 1 urllib.1 request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())


'''
设置属性控制一个页面如果长时间未响应,就跳过他的抓取
利用try   except语句来实现
'''
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')