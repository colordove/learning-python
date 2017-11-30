import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('1234@gmail.com', '123456'))
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('1234@gmail.com',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
