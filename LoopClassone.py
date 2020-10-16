#print("ON loops")

# for variable in sequence:
#     body of loop ctrl+/

name="Python"
#Example1
# for i in name:
#     print(i)

#range you specify the start and end index
#Example2
# for i in range(2,6):
#     print(name[i])

#Example3 - to iterate in revrese for a string
# for i in reversed(range(len(name))):
#     print(name[i])

#Example4 - sliced string
# for i in name[-4:]:
#     print(i)

#Lets take a line and print words in it
#Example 5
# line="Hi all welcome to python with Go Graduates"
# formattedline=line.split()
# print(len(formattedline))
# for i in range(len(formattedline)):
#     print(formattedline[i])

#Example6 we include conditions inside loops
# example=input("Enter the string")
# for i in example:
#     if i=="o" or i=="a" or i=="e" or i=="i" or i=="u":
#      print(i)

#Example 7 string having both numbers and characters segregate the numbers
#this try catch we will learn in exception handling
example=input("Enter alphanumeric value::")
for i in example:

     try:
       num=int(i)
       print(num)
     except:
         print("Excepted because the chacter is a string")