#CURD means create update read and delete
from pymongo import MongoClient

client=MongoClient("127.0.0.1",27017)
dbnames=client.list_database_names()
print(dbnames)

dbnm=client.get_database("gograds")
table=dbnm.get_collection("naveen")
# print(table.name)
#inserting a recod
# table.insert_one({"name":"morning batch"})
# table.insert_many([{"name":"Likith"},{"name":"Ranjith"},{"name":"Hari chandana"}])

#deleting a record
#
# table.delete_one({"name":"Bindu"})
# table.delete_many({"name":"Ranjith"})

#read a recoerd
# records=table.find()
# for i in records:
#     print(i)
#

#read a record
# records=table.find({"name":"Hari chandana"})
# for i in records:
#     print(i)


#update a record

#table.update_many({"name":"Dinesh ambati"},{"$set":{"name":"Naveen"}})
#table.update_one({"name":"Dinesh ambati"},{"$set":{"name":"Naveen"}})