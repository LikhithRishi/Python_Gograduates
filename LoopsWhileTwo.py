#Example to print characters using while loop
# x="Python1234xyz"
# count=0
# while count<len(x):
#     print(x[count])
#     count+=1


#break statement example
#count=0 len(x)=13 0<13 x[0]=P
#count=1 len=13 1<13 x[1]=y
#count=2 len=13 2<13 x[2]=t
#count=3 len=13 3<13 x[3]=h
#count=4 len=13 4<13 x[4]=o
#count=5 len=13 5<13 x[5]=n
#count=6 len=13 6<13 x[6]=1 1 is decimal =True we have break inside it so the loop gets terminated at this point
# x="Python1234xyz"
# count=0
# while count<len(x):
#     if x[count].isdecimal():
#         break
#     print(x[count])
#     count+=1

#Example for continue statement
# x="Python1234xyz"
# count=0
# while count<len(x):
#     if x[count].isdecimal():
#         count+=1
#         continue
#     else:
#         print(x[count])
#
#     count+=1

#While loops with lists
samplelist=[1,2,3,4,5,6,7,8,9]
# count=0
# while count<len(samplelist):
#     print(samplelist[count])
#     count+=1

#While loops with set
#count=0 < 9 next(x) =1
#count=1 <9 next(x)=2
#count=2 <9 next(x) =3
# sampleset=set([1,2,3,4,5,6,7,8,9])
# x=iter(sampleset)
# print(type(x))
# count=0
# while count<len(sampleset):
#     print(next(x)) # next will internally move a step forward and fetch values
#     count+=1

#This is example for iterator using lists
# itr=iter(samplelist)
# count=0
# while count<len(samplelist):
#     print(next(itr))
#     count+=1


#Example with tuple
# sampletuple=(1,2,"naveen")
# count=0
# while count<len(sampletuple):
#
#     print(sampletuple[count])
#     count+=1

#Example with tuple iterator
# tupleitr=iter(sampletuple)
# x=0
# while x<len(sampletuple):
#     print(next(tupleitr))
#     x+=1

# Iterating on dictionary using while iterator concept
sampledict=dict()
sampledict["class1"]="python"
sampledict["class2"]="scala"
sampledict["class3"]="java"
#
# dictitr=iter(sampledict.items())
# count=0
# while count<len(sampledict):
#      y=next(dictitr)
#      print(y)
#      print("keys are :",y[0],"values are:",y[1])
#      count+=1

#iterating dictionary using keys
# keyitr=iter(sampledict.keys())
# count=0
# while count<len(sampledict):
#     y=next(keyitr)
#     print(y,"value is >>>",sampledict[y])
#     count+=1

#iterating dictionary using values
# valitr=iter(sampledict.values())
# count=0
# while count<len(sampledict):
#     print(next(valitr))
#     count+=1


#Their is no such concept like do while in python

