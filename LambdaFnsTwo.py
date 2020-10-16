# filter in python accepts a lambda expression and an iterable object
#Iterable objects (lists,tuple,set,dictionary)

# add=lambda x,y:x+y
# print(add(5,6))
#
# mul=lambda x,y:x*y
# print(mul(4,5))
#
# div=lambda x,y:x/y
# print(div(10,5))
#
# x=20
# mod=lambda x:x%2==0
# if mod(int(input())):
#     print("moduloud is returning reminder 0")
# def modulo(val):
#     print(val)
#     if val%2==0:
#         return True
# smlist=[2,3,4,5,6,7,8,9,10]
# x=filter(modulo,smlist)
# print(list(x))

# simplelist=[1,2,3,4,5,6,7,8,9,10]
# filteredList=list()
# for val in simplelist:
#     if val%2==0:
#         filteredList.append(val)
# print(filteredList)
# a=lambda x:x%2==0
# y=filter(a,simplelist)
# print(list(y))
# z=filter(a,[11,12,13,14,15,16,17,18,19,20])
# print(list(z))

#mob- it will filter all categories that starts with mob
# smtuple=("Naveen","Naresh","Neeraj","Krishna","Ranjith","manoj","Kinnera")
#
# x=lambda y:str(y).startswith("m") # first element naveen - m (False)
# fil=filter(x,smtuple)
# print(tuple(fil))


# We take two arrays and sort out common elements from both
# arr1=[2,3,4,5]
# arr2=[5,6,7,8]
# def result(arr1,arr2):
#  x=list(filter(lambda y:y in arr1,arr2))
#  print(x)
#
# result(arr1,arr2)


#Assigment
# 1) Create a lambda function that filters numbers greater than 25 [26,27,1,2,3,4,5,29,30]
#2) Create a lambda function that filters strings having length greater than 5 ["nav","naveen"]
#3)take a file read data and write it to new file
#4)write a function  filter palindromes "Dad" even after reversing it shoudl be the same
