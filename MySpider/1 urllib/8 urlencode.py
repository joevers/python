# 在构造GET请求参数的时候非常有用
# 可以将字典类型转换为GET参数
from urllib.parse import urlencode

params = {
    'name':'qiao',
    'age':22
}
base_url = 'http://baidu.com?'
url = base_url + urlencode(params)
print(url)