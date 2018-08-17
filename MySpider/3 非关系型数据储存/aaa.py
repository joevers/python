import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

'''
student1 = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2 = {
    'id':'20170202',
    'name':'Mike',
    'age':21,
    'gender':'male'
}
result = collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)
'''

print("=="*20)
result = collection.find_one({'name':'Mike'})
print(type(result))
print(result)

print("=="*20)
from bson.objectid import ObjectId
result = collection.find_one({'_id':ObjectId('5b752fdfbbd75f0bc276dadf')})
print(result)

print("=="*20)
results = collection.find({'age':20})
print(results)
for result in results:
    print(result)

print("=="*20)
condition = {'name':'Jordan'}
student =collection.find_one(condition)
student['age'] = 25
result = collection.update(condition,student)
# result = collection.update(condition,{'$set':student})
print(result)

print("=="*20)
condition = {'age':{'$gt':20}}
# 这里指定查询条件为 年龄大于20,然后更新条件为年龄加1
result = collection.update_many(condition,{'$inc':{'age':1}})
print(result)
print(result.matched_count, result.modified_count)