from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs自动转码
content = soup.prettify()
#print(content)
print("=="*12)
print("=="*12)
print("=="*12)

#print(soup.head)
print("=="*12)
print("=="*12)
#print(soup.meta)
print("=="*12)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
#soup.link.attrs['type'] = 'hahahhaha'
#print(soup.link)
print("=="*12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("=="*12)
print(soup.name)
print(soup.attrs)
print(soup.name)


print("/"*60)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node)
print("=="*12)


import re

print("*"*60)
tags = soup.find_all(name="meta")
for tag in tags:
    print(tag)
print("=="*12)
tags = soup.find_all(re.compile('^me'), content='always' )
for tag in tags:
    print(tag)