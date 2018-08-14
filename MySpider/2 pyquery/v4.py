html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""
from pyquery import PyQuery as pq
doc = pq(html)

a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)
print("=="*30)
b = doc('a')
for item in b.items():
    print(item.attr('href'))
print("=="*30)
print("=="*30)
a = doc('.item-0.active a')
print(a)
print(a.text())
print("=="*20)
li = doc('.item-0.active')
print(li)
print(li.html())
print("=="*20)
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))
print("=="*30)
print("=="*30)
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)
print("=="*30)
print("=="*30)