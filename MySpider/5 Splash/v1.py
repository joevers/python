import requests

url = "http://localhost:8050/render.html?url=https://www.baidu.com"
response = requests.get(url)
print(response.text)


url = "http://localhost:8050/render.png?url=https://www.taobao.com&wait=5&width=1000&height=700"
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)