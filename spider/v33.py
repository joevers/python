from lxml import etree

# 只能读取xml格式内容,html报错
html = etree.parse("./v31.html")
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath的意思是,查找带有category属性值为sport的book元素
rst = html.xpath('//book[@category="sport"]')
print(rst)

# xpath的意思是,查找带有category属性值为sport的book元素下的year元素
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(rst)
print(rst.tag)
print(rst.text)