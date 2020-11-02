from mysql import connector

try:
    connection=connector.connect(host='localhost',
                                         database='pythonbatch2',
                                         user='root',
                                         password='Python@2020',auth_plugin='mysql_native_password')
    dbcursor = connection.cursor()
    dbcursor.execute("select * from Example;")
    records=dbcursor.fetchall()
    for row in records:
        print(row)

    dbcursor.close()
    dbcursor=connection.cursor()
    dbcursor.execute("insert into Example (Exname,age,test) values ('anil',35,test);")
    connection.commit()
    connection.close
    dbcursor.close()

    dbcursor=connection.cursor()
    dbcursor.execute("delete from Example where Exname='anil'")
    connection.commit()
    connection.close
    dbcursor.close()


    dbcursor=connection.cursor()
    dbcursor.execute("update Example set Exname='DB' where Exname='Vijay'")
    connection.commit()
    connection.close
    dbcursor.close()
except Exception as e:
    connection.rollback()
    print(e)
finally:
    print("to connect close")




