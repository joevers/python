from bs4 import BeautifulSoup

html = """
<div class="panle">
<div class="panle-heading">
<h4>Hello<h4>
</div>
<div class="panle-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""

soup =BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[1]))
print('=='*20)
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
print('=='*20)
print(soup.find_all(attrs={'id':'list-1'}))
print('=='*20)
print(soup.find_all(attrs={'name':'elements'}))
print('=='*20)
print('=='*20)
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
print('=='*20)
print('=='*20)
print('=='*20)