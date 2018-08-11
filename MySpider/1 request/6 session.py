# session
# 维持同一个会话   保持cookies不变


import requests

# 不使用session

requests.get('http://httpbin.org/cookies/set/nunmber/123465789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
print('=='*20)
# 使用session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/nunmber/123465789')
r = s.get('http://httpbin.org/cookies')
print(r.text)