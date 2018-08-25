import tesserocr
from PIL import Image

image = Image.open('test.jpeg')
result = tesserocr.image_to_text(image)
print(result)
print(tesserocr.file_to_text('test.jpeg'))