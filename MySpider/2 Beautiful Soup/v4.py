from bs4 import BeautifulSoup

html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
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

soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print('=='*20)
print(soup.select('ul li'))
print('=='*20)
print(soup.select('#list-2 .element'))

print('=='*20)
print('=='*20)
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

print('=='*20)
print('=='*20)
print('=='*20)
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)