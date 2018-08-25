import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.taobao
collection = db.products
results = collection.find({'location':'浙江 杭州'})
for result in results:
    print(result)