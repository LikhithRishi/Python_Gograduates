#Syntax of function
# function syntax always start with 'def' keyword
# def function(args):
#     #Block of code
#     return

# def function():
#     pass
#def here means a generic return type for a function
# def function(name):
#     print(name)
#     name+="python"
#     return name
#
# x=function("naveen")
# print(x)
#
# def sort(srlist):
#     for val in range(0, len(srlist)):  # 20
#         for val1 in range(0, len(srlist)):  # 20*20
#             if srlist[val] > srlist[val1]:  # [56,1,2,5,2,5,9,11,13,18,19,25,23,24,28,55]
#                 # [56,55,1,2,2,5,5,9,11,13,18,19,23,24,25,28]
#                 temp = srlist[val1]  # 1 in temp
#                 srlist[val1] = srlist[val]  # replacing 1 with 5
#                 srlist[val] = temp  # replacing 5 with 1
#
#     return srlist
#
# x=sort([2,1,5,9,0])
# y=sort([35,21,13,9])
# print(x)
# print(y)

#How to pass variables into a function
#passbyvalue and passbyreference
#no concept of pass by reference in python
# def pasValues(name,age):
#     print(name,age)
#
# pasValues("naveen",input("enter the age :"))
#
# pasValues(age=35,name="krishna")

#*args and **kwargs
#*args are called as varibale length aruguments
#*kwargs are called as keyword arguments


#*args variable length where you can pass N number of values

# def variableLenghthArgs(*naveen):
#     for x in naveen:
#         print(x)

#variableLenghthArgs("dinesh","ranjith","likith")
#variableLenghthArgs("dinesh","ranjith","manoj","likith","saikrishna","Naveen",23,[2,3,4,5],(1,2,3),set([1,2,3]))


#when ever you are writing varibale length arguments vargs the vargs should always be the last element inside
#function definition
# def vargs(name,*args):
#     print(args,name)
#
# vargs("naveen",[1,2,3,4],"naveen")

#keyword arguments
#
# def keyFun(name="naveen",age=30):
#     print(name,age)
#
# keyFun("krishna",40)

#multple key word arguments **kwargs
#first normal arguments
#next vargs
#kwargs
def keyVargs(*args,**manoj):
    for key,val in manoj.items():
        print(key,val)
    print(args)

keyVargs(1,2,3,4,5,6,name="naveen",age=30,salary=20,address="Hyderabd")

