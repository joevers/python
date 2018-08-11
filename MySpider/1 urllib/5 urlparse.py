'''
1 urllib 提供了parse模块
urlparse   实现url的识别和分段
'''

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
'''
输出结果为:
<class '1 urllib.parse.ParseResult'>
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', 
            query='id=5', fragment='comment')
1. :// 前面就是scheme,代表协议
2. 地一个符号/前面就是 netloc  即域名
3. 后面是path  即访问路径
4. 分号;后面是params  代表参数
5. 问好?后面是 查询条件query  一般作用与get类型的url
6.井号#后面 fragment是锚点    用于直接定位页面内部的下拉位置
'''

# urlunparse
# 它接受的参数是一个可迭代的对象,但是 长度必须为6

from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))