'''
URLError
HTTPError
'''
from urllib import request, error
import socket
try:
    response = request.urlopen('https://www.cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code)
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

#  reason属性返回的不一定都是字符串, 也可能是一个对象,
# 例如  强制超时  结果是一个socket.timeout类 