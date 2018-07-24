
from urllib import request
# 导入ssl处理模块
import ssl

# 代码
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn/mormhweb"
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)