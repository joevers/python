import pymysql


db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id':'20120001',
    'name':'Bob',
    'age':21

}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUE({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ",".join(["{key}=%s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()