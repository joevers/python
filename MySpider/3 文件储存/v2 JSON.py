import json

str = '''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
}, {
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''

print(type(str))
data = json.loads(str)
print(type(data))
print(data)
print("=="*20)
print(data[0]['name'])
print(data[0].get('name'))
print("=="*20)
print(data[0].get('age'))
print(data[0].get('age', '26'))
print(data[0])
print("=="*20)
print("=="*20)
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

print("=="*20)
print("=="*20)
print("=="*20)
print("=="*20)
with open('data1.json', 'a') as file:
    file.write("\n"+json.dumps(data))
# 加入参数indent,代表缩进的字符个数
# 如果要传入中文字符,需要指定参数 ensure_ascii为False, 另外还要规定文件输出的编码
with open('data1.json', 'a', encoding='utf-8') as file:
    file.write("\n"+json.dumps(data, indent=2, ensure_ascii=False))