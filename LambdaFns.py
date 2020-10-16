#Lambda expressions
#They are called anonymous functions because they don't have any name
#lambda keyword is used to define lambda expressions
#We can pass any infinity number of arguments (no limit for passing arguents )
#
#def add():

#Examples
# x="Naveen"
# y=lambda xyz:x+"\tpython"
# # def y(x):
# #     x=x+"\tpython"
# #     return x
# z=y(x)
# print(z)

#Example2
# x="Naveen"
# y=lambda x: print("Hello::",x)
# y(x)#line 3 and line 4 are similar
# (lambda x:print("Hello",x))(x)
# (lambda x,a,b:print(x,a,b))(x,"class","lambda")
# (lambda *x: print("Hello::",x))(x,"class","lambda")
# (lambda **x:print("Hello::",x))(a="python",b="scala",c="hive")
# (lambda y:print(input("taking input")))(x)

#Example 3
#How to return a lambda from a function
# def example3(y):
#     return lambda x:x*y
    # return lambda x:x*y
#when lambda expression is returned from above it will be like
#lambda x:x*4
#when you call y(5) it will be like
#lambda x:5*4 result 20 will get returned
#printing 20 here
# y=example3(4)
# print(type(y))
# z=example3(6)
# print(type(z))
# print("printing z::",z(5))
# print(y(5))

# def example4(*args,**kwargs):
#     return lambda z:print(args,kwargs)
#
# # Y=example4(1,2,3,4,a="python",b="scala",c="hive")
# # Y("Pyton")
# (example4(1,2,3,4,a="python",b="scala",c="hive"))("Python")

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






