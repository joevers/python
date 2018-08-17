import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end

'''

url ='http://localhost:8050/execute?lua_source='+quote(lua)
response = requests.get(url)
print(response.text)

lua ='''
function main(splash)
    splash:go("http://www.baidu.com")
    return splash:html()
end
'''
url ='http://localhost:8050/execute?lua_source='+quote(lua)
response = requests.get(url)
print(response.text)