import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',22])
    writer.writerow(['10003','Jordan',23])

# 修改列与列之间的分割符  可以传入delimiter

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',22])
    writer.writerow(['10003','Jordan',23])

# 也可以调用writerows写入多行
with open('data.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerows([['10001','Mike',20],['10002','Bob',22],['10003','Jordan',23]])

# 字典写入
with open('data.csv', 'a') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id':'10002','name':'Bob','age':22})
    writer.writerow({'id':'10003','name':'Jordan','age':23})

# 如果存在字符编码问题,需要给open()函数指定编码格式

with open('data.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id':'10002','name':'Bob','age':22})
    writer.writerow({'id':'10003','name':'Jordan','age':23})
    writer.writerow({'id':'10004','name':'王伟', 'age': 23})



# 读取
import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile1:
    reader = csv.reader(csvfile1)
    for row in reader:
        print(row)

print("=="*20)
# 使用pandas中的read_csv()方法读取
import pandas as pd
df = pd.read_csv('data.csv')
print(df)