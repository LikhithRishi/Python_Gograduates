#ordered dictitonary is also a sub class of dictionary
from collections import OrderedDict,defaultdict,ChainMap,namedtuple
# x=OrderedDict()
# x["Naveen"]="Python"
# x["Ranjith"]="scala"
# x["Likith"]="Java"
# print(x)
#
# x.update(age=32,name="krishna")
# print(x)

#Example for default dictionary
#
# y=defaultdict(int)
# z=[9,8,5,4,2,1,6]
#
# for i in z:
#      y[i]+=1
#
# print(y)

#Example of chainmap
#This collection is also for dictionaries

# one={1:"naveen",2:"ranjith",3:"manoj"}
# two={4:"bindu",5:"sai",6:"akshitha"}
# three={7:7,8:8,9:9}
# result=ChainMap(one,two,three)
# print(result)
# print(result.keys())
# print(result.values())
# for key,val in result.items():
#     print(key,val)
# for val in result.values():
#     print(val)
#
# for key in result.keys():
#     print(key)


#Example to demonstrate named tuple


sample=tuple(["naveen",30,"hyderabad"])
print(sample)
example=namedtuple("example",["name","age","address"])
print(example)
x=example("naveen",30,"hyderbad")
print(x)
print(x[0],x[1],x[2])
print(x.name,x.age,x.address)
y=["Ranjith",28,"hyderabad"]
z=("likith",22,"vyzag")
print(example._make(y))
print(example._make(z))
print(example._asdict(x))
print(example._replace(x,name="Krishna"))

