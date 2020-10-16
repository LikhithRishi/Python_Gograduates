#IO operations means Input and ouput operation 
#input() - we take input
#print() - we write output using print

#File input and out operations
#how to read from a file
#how to write to a file
#how to append to a file


#different modes while handling a file r,w,a,r+

#Eample for reading from a file
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileinput.txt","r") as ff:
#     lines=ff.readlines()
#     for line in lines:
#         print(line)

#Example for writiing into a file multiple lines
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","w") as val:
#     lines=["Hello Naveen good morning\n","Read write operations"]
#
#     val.writelines(lines)

#Example for writing line by line to a file
#When ever you try to write to a file it is overwriting the complete data in the file
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","w") as val:
#     lines=["Hello Naveen good morning\n","data getting overwritten"]
#     for line in lines:
#         val.write(line)


#Example for exapling the append mode to a file
#
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput123.txt","a") as val:
#     lines = ["we are trying to append the data \n", "Welcome here to append mode "]
#     val.writelines(lines)


#Example to demonstrate the read write mode
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","r+") as val:
#     lines=["\nopening it in read write mode"]
#     val.writelines(lines)
#     readlines=val.readlines()
#     for rdline in readlines:
#         print(rdline)
#     val.close()


#Example to demosntrate append+
# with open("C:\\Users\\navee\\OneDrive\\Desktop\\fileoutput.txt","a+") as val:
#     # lines=["\nopening it in read write mode"]
#     # val.writelines(lines)
#     readlines=val.readlines()
#     print(val.readline())
#     print(val.readline())
#     for rdline in readlines:
#         print(rdline)



# x=input("please enter a value:")
# print(x)
# audits and logs we use this print statements formatting
y="example"
# print(f"print {x} {y}")
print("Today is {} and {}".format("Input","output"))
print("Today is {2} {0} and {1}".format("Input","ouput","first"))

print("this is formatting {name}".format(name="naveen"))
