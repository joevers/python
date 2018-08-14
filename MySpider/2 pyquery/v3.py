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

items = doc('.list')
print(items)
print("=="*20)
lis = items.find('li')
print(type(lis))
print(lis)
print("=="*20)
l = items.children('.active')
print(l)
print("=="*20)
print("=="*20)
container = items.parent()
print(container)
print("*"*50)
parents = items.parents()
print(parents)
print("//"*20)
parents = items.parents('.wrap')
print(parents)
print("=="*20)
print("=="*20)
li = doc('.list .item-0.active')
print(li.siblings())
print("*"*50)
print(li.siblings('.active'))
print("=="*20)
print("=="*20)
print("=="*20)
b = doc('li').items()
for li in b:
    print(li, type(li))