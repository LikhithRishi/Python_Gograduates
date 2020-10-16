#nested functions

# def outerFunction():
#     print("outer function")
#     def innerFunction():
#         print("we are in inner function")
#     return innerFunction
#
# inner=outerFunction()

#inner()

# def function1():
#     print("Hello world")
#     def innerfn(y):
#         print(y*2)
#
#     return innerfn
#
# x=function1()
# x(5)

#example 3
# def add(x):
#     print("I'm here to add two numbers")
#     x=x+5
#     print(x)
#     def multiply(y):
#
#       y*=x
#
#       print(y)
#     return multiply
#
# y=add(5)
# y(5)

#nested lambda
xyz=lambda x,y:lambda z:x+y+z
outer=xyz(3,4)
print(outer)

print(outer(5))

def outer(x,y):
    def inner(z):
        z=x+y+z
        return z
    return inner

zyx=outer(3,4)
print(zyx)
a=zyx(5)
print(a)
