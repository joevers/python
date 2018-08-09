'''
与 urlparse()方法非常相似不单独解析params这一部分, 之返回5个结果
'''
from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

# urlunsplit
# 与unlunparse类似, 传入的长度必须为5