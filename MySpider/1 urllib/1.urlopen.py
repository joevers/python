import urllib.request
import urllib.parse

res = urllib.request.urlopen('https://www.python.org')
print(type(res))
print(res)
print(res.getheaders())