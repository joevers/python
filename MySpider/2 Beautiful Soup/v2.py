from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time three were three little sisters; am their name were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elise--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

print("=="*50)
print(soup.title.name)
print("=="*50)
print(soup.p.attrs)
print(soup.p.attrs['name'])
