# 超时
import requests
r = requests.get('http://www.taobao.com', timeout=1)
print(r.status_code)
# timeout默认为None,即永久等待


# 身份认证
# request自带身份认证功能
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username','password'))

# 上述简写如下
# auth后直接跟一个元组,会默认使用HTTPBasicAuth
r = requests.get('http://localhost:5000', auth=('username','password'))