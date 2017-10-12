import mysql.connector

conn = mysql.conntector.connect(user = 'root', password = 'password', database='test')
cursor = conn.cursor()

# 创建user表
cursor.execute('CREATE TABLE user (id varchar(20) primary key, name varchar(20)')
# 插入一行记录
cursor.execute('INSERT INTO user (id, name) values (%s, %s)', ['1', 'John'])
cursor.rowcount

# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE id = %s', ('1',))
values = cursor.fetchall()
values

cursor.close()
conn.close()