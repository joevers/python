import urllib.parse
import urllib.request

'''
如果需要添加data参数, 需要使用bytes()方法将参数转换为字节流编码格式的内容,即bytes类型
如果传递了这个参数,则他的请求方式不是GET方式,而是POST方式
'''


data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())