# Loops with numbers , lists
# for variable in sequence:
#     body of loop
#Example-1
# for i in range (0,11):#0,1,2,3,4,5,6,7,8,9,10
#     print(i)

#Sum of n numbers
#if i gave input 10 (1+2+3+4+5+6+7+8+9+10)
#x=1+2+3+4+5+6+7+8+9+10
#x+=y (x=x+y)
# x=int(input("Please enter a value :")) #we are reading input from console
# print(x)
# sum=0 # We took intial sum value as 0
# for d in range(0,x+1):  #in range (0,6) which means it will be looped or iterated from 0-5
#
#     sum+=d #first step sum=0 d=0 (sum=sum+d=0)
#     #second step sum=0 d=1 (sum=sum+d (sum=0+1))=1
#     #third step sum=1 d=2 sum=sum+d (1+2=3)
#     #step 4 sum=3 d=3 sum=sum+d (3+3)=6
#     #step 5 sum=6 d=4 sum=sum+d (6+4)=10
#     #step 6 sum=10 d=5  sum=sum+d (10+5)=15
#
#
# print(sum)
#
# result= x*(x+1)/2
# print(result)

#Example -2 factorial (5!) = 5*4*3*2*1
# mul=1
# for i in range(1,6):
#     mul*=i
#
# print(mul)

#For loops with lists
# ietrating over values
# samplelist=[1,2,3,4,5,6,7,8]
# for i in samplelist:
#     samplelist.append("xyz")
#     print(i)
#by using range we iterate with index
# if len(samplelist)!=0:
#     for i in range(0,len(samplelist)):
#         print(samplelist[i])

# samplelist.append(4)
# print(samplelist)
# samplelist.remove(4)
# print(samplelist)

# for i in range(0,len(samplelist)):
#     samplelist.append(6)
#     # samplelist.remove(4)
#     print(samplelist)


# sampleset=set(["naveen","python","Gograds"])
# print(sampleset)
# #looping over the values
#Fail condition- sets
# for val in sampleset:
#     #sampleset.add("xyz") # this commented line throws exception
#     sampleset.remove("naveen")
#     print(val)
# print(sampleset)


#looping over tuples
# sampletuple=(1,2,"naveen")
# print(type(sampletuple))
# print(sampletuple)
#iterating over the values using tuple
# for val in sampletuple:
#     print(val)

# for i in range(0,len(sampletuple)):
#     print(sampletuple[i])

#looping over dictionary
#ietrating over the values
sampledict=dict()
sampledict["class1"]="python"
sampledict["class2"]="scala"
sampledict["class3"]="java"
print(sampledict)
#to print keys
# for key in sampledict.keys():
#     print(key)
#
#this is print values
# for val in sampledict.values():
#     print(val)
#This is ietrating over the items(both key and value pair is called a single item)
# for key,val in sampledict.items():
#     print(key,val)

#This is to read values by using keys
# for key in sampledict.keys():
#     print(key, sampledict[key])

#Modifying over the loop fails
# for key in sampledict.keys():
#      print(key, sampledict[key])
#      #sampledict["class4"]="testoverloop"
#      sampledict.pop()



#Assignment
#Go go google and take fibnocci series  and try to do it with loops
#subration of a number ex: 100
# input("enter a number:")
# input("how much value you wanted to deduct:20")
# input("how many times you wanted to deduct:2")

#print values from 10,1
# for i in reversed(range(0,10)):
#     print(i)