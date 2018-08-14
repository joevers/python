import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/68.0.3440.84 Safari/537.36',
}
html = requests.get(url=url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n'+'='*50+'\n')
    file.close()
#  文件写入可以简写成:
'''
with open(...) as file:
    file.write()
    file.write()
with控制块结束的时候,文件自动关闭,所以不用再调用close()方法
'''