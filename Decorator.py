# #Example of closure
#
# def outerfunction(func):
#     def innerFunction(*args):
#         print("we are here")
#         x=func(*args)
#         print(func)
#         print("this is result from onemore decorator",x)
#         print("the result from outer decorator",list(reversed(x)))
#
#     return innerFunction
#
# def onemore(func):
#     def onemore_inner(*args):
#         print("we are in one more ")
#         x=func(*args)
#         print(func,x)
#         return x
#     return onemore_inner
#
# @outerfunction
# @onemore
# def sortedList(x):
#
#     return x
#
#
# # z=outerfunction(sortedList)
# # z([1,5,2,6,9,7])
#
# sortedList([1,5,2,6,9,7])
#

#
# def closure(func):
#     def inner(*args):
#
#         func(*args)
#
#     return inner
#
# def multiply(func):
#     def inner(*args):
#
#         func(*args)
#
#     return inner
#
# @closure
# #the above @closure is equal to below lines
# # y=closure(add)
#
# def add(x,y):
#     print(x+y)
#
# add(4,5)
#
# @multiply
# #the above @multiply is equal to below lines
# # y=closure(multiple)
# def multiple(x,y):
#     print(x*y)
#
# multiple(5,6)

# # while wriitng multiple decorators the sequence of execution always goes from bottom to tom
# def adddecorator(func):
#     def inner():
#         print("first")
#         x=func()
#         print(x)
#         return 3*x
#     return inner
#
# def seconddecor(func):
#     def inner():
#         print("second")
#         x=func()
#
#         return x*x
#     return inner
#
# @adddecorator
# @seconddecor
# def multiply():
#     return 2
#
# print(multiply())


def cashwithdrawal(func):
    def inner(*args):
        x=func(*args)
        print(x)
        print(args)
        if x==True and len(args)==2:
            print("we are in condition")
            balance=args[0]-args[1]
            print("remaining balance::",balance)

    return inner

def amountcheck(func):
    def inner(*args):
        x=func(*args)

        if x[0]>=x[1]:
            return True
        else:
            return False
    return inner

@cashwithdrawal
@amountcheck #amountcheck(amountdebitter)(10000,2000)
def amountdebbiter(balance,amount):
    return balance,amount

amountdebbiter(10000,2000)


