# quote
# 该方法可以将内容转换为url编码的格式
# URL中带有中文参数时,可用此方法将中文字符转换为URL编码
from urllib.parse import quote, unquote

keyword = '壁纸'
url = 'http://www.baidu.com/s?wd='+quote(keyword)
print(url)


# unquote
# 可以进行url编码
url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))