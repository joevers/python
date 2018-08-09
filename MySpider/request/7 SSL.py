# SSL证书验证
# 使用verify参数    默认为  True

import requests
try:
    response = requests.get('https://www.12306.cn')
    print(response.status_code)
except Exception as e:
    print(e)
    print('SSLError')


print('=='*50)
# 添加verify参数
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)

# 上述情况出现一个警告  建议我们给他指定证书,


print('=='*50)
# 可以通过设置忽略警告的方式来屏蔽这个警告
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

print('=='*50)
# 或者捕获警告到日志的方式忽略警告
import logging

logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


print('=='*50)
# 我们可可以制定一个本地证书作为客户端证书,  这可以是单个文件(包含密匙和证书)或一个包含两个文件路径的元组

response = requests.get('https://www.12306.cn', cert=())