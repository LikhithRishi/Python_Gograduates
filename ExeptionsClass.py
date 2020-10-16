import sys
#syntax errors - parsing errors
# if 10>15:
# print("If fail")

# for val or range(0,10):
#     print("hello")

#Exceptions
# infinity - dividing any number by 0 10/0=infinity
#this is called exception because it is not syntax error it raises exception only when it is executed
# x=10
# print(10/0)
#Syntax of Exception handling
# try:
#     #Block of code where you are expecting exeception to occur
#     #try should be followed by except
# except:
#     #this where exception is handled

#Synatx for multiple exception
#
# try:
#  #block of code
# except #hadnling specific exception:
# except :# consider this like global except

#Finally syntax
# try:
#     #block of code
# finally:
#    #block of code
x=10
try:
    print(10)
except:
    print("Divided by zero is not accepted ",sys.exc_info())
else:
    print("hey i'm in else ")
print("Hello World")

#this is an example for type error
try:
    print("2"+2)
except:
    print("This is example for type error",sys.exc_info())

# try:
#     with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileinput.txt","r") as ff:
#         lines=ff.readlines()
#         for line in lines:
#             print(line)
# except:
#     print("File IO error ",sys.exc_info())

# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","w") as val:
#     try:
#         val.readline()
#     except:
#         print(sys.exc_info(),"File is in write mode so we can't perform read operation")
#     lines=["Hello Naveen good morning\n","data getting overwritten"]
#     for line in lines:
#         val.write(line)

#Example to demonstarte multiple exceptions
y=15
try:
 #print(y/0)# If exception found in first line the lines below it are not getting executed even inside try catch
 print("2"+2)
except ZeroDivisionError as err:
    print(err)
except TypeError as tyerr:
    print("I'm here in multiple except",sys.exc_info())
except:
   print("This is always good practice to define except with multiple exceptions")

#How to use raise keyword and raise your own exception

# x=10
# y=15
# if y>x:
#     try:
#      raise ValueError("This values are not as expected i don't want y to be greater than x ")
#     except:
#         print(sys.exc_info())
#     finally:
#         print("finally block")
#
# y=str(10)
# try:
#
#     raise TypeError("I want type only to be in interger format")
# except:
#     print(sys.exc_info())
# finally:
#     print("finally for type error")


#Example to demonstrate finally
# try:
#     print("2"+2)
# finally:
#     print("irrespective of your exception finally gets executed for sure ")

#
# try:
#
#     print(2+"3")
# except:
#     print(sys.exc_info())
# finally:
#     print("finally getting printed")