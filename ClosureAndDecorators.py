from Functions import ATM as atm


#Nested function

# def outerfunction():
#     def innerfunction():
#         print("we are here")
#     innerfunction()
#
# outerfunction()

#closure Example

# def outerfunction():
#     def innerfunction():
#         print("first closure example")
#     return innerfunction
#
# outerfunction()

# def fun1(func):
#     print("one")
#     return func
#
# def add(x,y):
#     x+=y
#     print(x)
#
# y=fun1(add(2,3))


#why should one use closure
#what is closure
#We should use closure because it will be generic and you can pass any function you want into to and you can get it executed
#A closure is something which will return the reference of inner function
# def outerfunction(func):
#     def innerfunction(*args):# arguments are getting passed from closure innerfunction reference
#          print("the arguments that which we passed here ",args)
#          z=func(*args) #add(3,4) #multiply(2,3,4)
#          print(z)
#     return innerfunction
#
# def add(x,y):
#     return x+y
# def multiply(x,y,z):
#     return x*y*z
# y=outerfunction(add)
# print(y)
# y(3,4)
#
# mul=outerfunction(multiply)
# mul(2,3,4)
# assigment - write a function for division and modulo and pass it into closure
#Assignment 2- write function for r+ and pass it into fileIOClosure
# def fileIOclosure(func):
#
#     def innerFileIO(*args):
#         func(*args)
#     return innerFileIO
#
# def readFile(filename,mode):
#     with open(filename, mode) as ff:
#         lines = ff.readlines()
#         for line in lines:
#             print(line)
#
# def writeFile(filename,mode):
#     with open(filename, mode) as val:
#         lines = ["Hello Naveen good morning\n", "Read write operations"]
#
#         val.writelines(lines)
#
# readOps=fileIOclosure(readFile)
# readOps("C:\\Users\\navee\\OneDrive\\Desktop\\fileinput.txt","r")
#
# writeops=fileIOclosure(writeFile)
# writeops("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","w")

