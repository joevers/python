import pytesseract as pt

from PIL import Image

#生成跟图片案例
image = Image.open('test1.jpeg')

# 调用pytesseract, 把图片转换成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)

print(text)


image = Image.open('test.jpeg')

image = image.convert('L')
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
image.show()
result = pt.image_to_string(image)
print(result)