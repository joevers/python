import pytesseract as pt

from PIL import Image

#生成跟图片案例
image = Image.open('/home/tlxy/桌面/1.jpeg')

# 调用pytesseract, 把图片转换成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)

print(text)