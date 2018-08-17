- 新建的mongodb的数据存在    /var/lib/mongodb/  下

- 连接MongoDB    
        import pymongo
        client = pymongo.MongoClient(host='localhost', port=27017)
        
- 指定数据库       
        db = client.test
        
- 指定集合
        collection = db.students
        
- 插入数据
    - 在MongoDB中,每条数据其实都有一个_id属性唯一识别
    - insert()方法会在执行后返回_id值
    - 推荐使用insert_one()和insert_many()分别插入单条和多条数据
    - insert_one()返回的是InsertOneResult对象,调用inserted_id属性获取_id
    - insert_many()返回的是InsertManyResult对象,调用inserted_ids属性获取_id列表
    
- 查询
    - 使用find_one()或find()方法进行查询
        - find_one()查询到的是单个结果
            - 返回的结果多了_id属性,是自动添加的
            - 也可以根据ObjectID来查询,需要使用bson库里面的objectid
        - find()返回一个生成器对象
            - 返回的结果是Cursor类型,相当与一个生成器,需要遍历取到所有结果,每个结果都是字典类型
    - 比较符号
        - $lt         小于
        - $gt         大于
        - $lte        小于等于
        - $gte        大于等于
        - $ne         不等于
        - $in         在范围内
        - $nin        不在范围内
    - 可以使用正则匹配查询
        - results =collection.find({'name':{'$regex':'^M.*'}})
        - 使用$regex来指定使用正则匹配  后跟正则表达式
        - 功能符号详见P218
        
- 计数
    - 调用count()方法,统计所有数据条数   .find().count()
    - 符合某个条件的数据   在find中加入条件
    
- 排序
    - 调用sort()方法   .find().sort('name',pymongo.ASCENDING)
    - pymongo.ASCENDING 指定升序
    - pymongo.DESCENDING 指定降序
    
- 偏移
    - 利用skip()方法偏移几个位置  .skip(2)忽略前两个元素,得到第三个及以后的元素
    - 利用limit()方法指定要取的结果个数  .limit(2)取两个元素
    
- 更新
    - 使用update()方法,指定更新的条件和更新后的数据
    - 返回的是字典形式  {'ok': 1, 'nModified': 1, 'n': 1, 'updatedExisting': True}
        - ok 代表执行成功
        - nModified  代表影响的数据条数
    - 使用$set操作符对数据进行更新
    - 推荐使用update_one()和update_many()方法

- 删除
    - 使用remove()
        - 括号内写入条件, 把所有符合条件的数据全部删除
    - 使用 delete_one()和delete_many()  删除第一条和删除所有
    
- 其他用法
    - 参见官方文档  http://api.mongodb.com/python/current/api/pymongo/