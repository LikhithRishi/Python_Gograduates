from mysql import connector


connection = connector.connect(host='localhost',
                                         database='pythonbatch2',
                                         user='root',
                                         password='Python@2020',auth_plugin='mysql_native_password')

cursor = connection.cursor()
cursor.execute("select * from Example;")
records=cursor.fetchall()
for row in records:
    for x in row:
        print(x)
cursor.execute("insert into Example (Exname,age) values('from',35)")
connection.commit()
cursor.execute("delete from Example where Exname='from'")
connection.commit()





