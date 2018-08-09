# parse_qs()
# 反序列化
# 将GET参数转换为字典
from urllib.parse import parse_qs, urlparse, parse_qsl

url = 'http://www.baidu.com?name=qiao&age=22'
query = urlparse(url).query
# query = 'name=qiao&age=22'
print(parse_qs(query))



# parse_qsl()   将参数转换为元组组成的列表
print(parse_qsl(query))