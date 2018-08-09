'''
urljoin  完成链接的合并,生成链接
可以提供一个基础的链接base_url作为地一个参数, 将新的链接作为第二个参数
该方法会分析base_url的scheme netloc path这三个内容并对新的链接进行补全,对后返回结果
'''

from urllib.parse import urljoin

print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','http://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com','?category=2#comment'))