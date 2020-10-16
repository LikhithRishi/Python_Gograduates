from collections import Counter

#A collection is a container to store different types of objects
#Counters
#OrderedDict
#DefaultDict
#chainmap
#namedtuple
#Deque


#Counters -concept
#counter is a subclass of dictionary
# sampledict=dict()
# sampledict['dinesh']="value1"
# sampledict['naveen']='python'
# sampledict['krishna']='scala'
# print(sampledict)

sampleList=[1,1,1,2,2,3,3,3,3,9]
#counter with list
x=Counter(sampleList)
print(x)
x.update([9,9,9,9,9,9])
print(x)
x.subtract([9,9,9])
print(x)
for key,value in x.items():
    print(key,value)
print(x.elements())
for i in x.elements():
    print(i)
print(x.most_common())

#counter with dictionary
# y=Counter({"A":5,"B":6,"c":2})
# print(y)
# #counter with type
# z=Counter((1,2,3,1,2,3))
# print(z)
#
# print(Counter(A=3,B=6,C=9))

