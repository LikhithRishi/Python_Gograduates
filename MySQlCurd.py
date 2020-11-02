#connect and execute operations on mysql

import mysql.connector

cnx = mysql.connector.connect(user='root', password='Python@2020',
                              host='127.0.0.1',
                              database='pythonbatch3')
#
# # Read operation
# dbcursor = cnx.cursor()
# dbcursor.execute("select count(*) from student;")
# count=dbcursor.fetchall()
# print(count[0][0])
#
# dbcursor1=cnx.cursor()
# dbcursor1.execute("select * from student;")
# #records=dbcursor.fetchall()
# counter=int(count[0][0])
# start=0
# itr=iter(dbcursor.fetchall())
# while start<counter:
#     print(next(itr))
#     start+=1
#
# #Create operation
# insertcursor=cnx.cursor()
# insertcursor.execute("insert into student values(1,'Python')")
# cnx.commit()
#
# #Delete operation
# deletecursor=cnx.cursor()
# deletecursor.execute("delete from pythonbatch3.student where name='Naveen';")
# cnx.commit()

#update operation
updstecursor=cnx.cursor()
updstecursor.execute("update pythonbatch3.student set name='Naveen' where name='Python';")
cnx.commit()
cnx.close()