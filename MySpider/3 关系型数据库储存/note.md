- 创建的MySQL数据库在   /usr/local/mysql/data/  下
    - db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
        - 这里通过pymysql的connect()方法声明一个MySQL链接对象db
    - cursor = db.cursor()
        - 调用cursor()方法获得MySQL的操作游标,利用游标来执行SQL语句
    - 使用execute()方法执行
    - 调用fetchone()方法获得数据



- MySQL
    - 创建表
        - 案例v1
    - 插入数据
        - 案例v2
            - 实现数据插入需要执行db对象的commit()方法
                - 对于数据的插入  更新   删除操作 都需要调用该方法  commit()
            - 异常处理,如果执行失败, 则调用rollback()执行数据回滚,相当于什么都没有发生
        - 这里涉及事务的问题,具有4个属性
            - 原子性  事务是一个不可分割的工作单位,事务中包括的诸多操作要么都做,要么都不做
            - 一致性  事务必须使数据库从一个一致性状态变到另一个一致性状态
            - 隔离性  一个事务的执行不能被其他事务干扰
                     并发执行的各事务间不能相互干扰
            - 持久性  一个事务一旦提交,它对数据库中的数据的改变就是永久性的
                     接下来的其他操作或故障不应该对其有任何影响
        - 标准写法 
                
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
        
        - 构造字典,做成通用方法
            - 案例v2
            - 这样就不需要再去修改SQL语句和插入操作了
            
    - 更新数据
        - 构建data,查重,去重
            - 案例v3
            - ON DUPLICATE KEY UPDATE   这行代码表示 如果主键存在,就执行更新操作
            
    - 删除数据
        - 使用DELETE语句即可, 需要指定删除的目标表名和删除条件,仍然需要使用commit()方法
        - 删除条件有多个时使用运算符连接
        - 案例v4
        
    - 查询数据
        - 使用SELECT语句
        - 案例v5