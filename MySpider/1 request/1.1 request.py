# 添加headers
import requests

# 没有添加请求头  不能正常获取信息
r = requests.get('http://www.zhihu.com/explore')
print(r.text)


print('==' * 20)
# 加上User-Agent信息
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'

}
r = requests.get('http://www.zhihu.com/explore', headers=headers)
print(r.text)

print('=='*20)


# 添加参数
data = {
    'name':'qiao',
    'age':22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)