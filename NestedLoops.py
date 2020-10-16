# Nested loops are writing a loop inside another loop

#Example of nested loop with lists
#
# smlist=[1,2,3,4,5,6,7,[8,3,4,5,7],(1,2,3)]
#
# for val in smlist:
#     print(val)
#     y=str(val)
#     if len(y)>1:
#      for x in val: # [8,3,4,5,7] and (1,2,3)- these values are iterated and getting printed
#         print(x,"These are values from nested loop")

#Example -2 sorting
# srlist=[1,5,2,9,2,5,13,11,18,19,25,56,23,24,28,55]
# [5,1,2,9,2,5,13,11,18,19,25,56,23,24,28,55]
#print(srlist)
#step 1 val=0 and in 2nd for loop val1=0 now we compare srlist[0]=1>srlist[0]=1
#step2 val1=1 srlist[1]=5 srlist[0]=1 1>5
# for val in range(0,len(srlist)):
#     for val1 in range(0,len(srlist)):
#         if srlist[val]>srlist[val1]:
#             temp=srlist[val1] #1 in temp
#             srlist[val1]=srlist[val] #replacing 1 with 5
#             srlist[val]=temp #replacing 5 with 1
#             print(srlist)
# print(srlist)

#sorting logic is very important Big O notaion time complexity O(n2)


#nested while loop
#
# srlist=[3,4,5,6,7,9,[87,62],(1,2,3,4)]
# count=0;
# while count<len(srlist):
#     print(srlist[count])
#     x=0
#     while len(str(srlist[count]))>1 and x<len(srlist[count]):
#         print(srlist[count][x])
#         x+=1
#     count+=1

#nested loops writing for inside while loop
# srlist=[3,4,5,6,7,9,[87,62],(1,2,3,4)]
# count=0;
# while count<len(srlist):
#     print(srlist[count])
#     y = str(srlist[count])
#     if len(y)>1:
#          for x in srlist[count]: # [8,3,4,5,7] and (1,2,3)- these values are iterated and getting printed
#             print(x,"These are values from nested loop")
#     count+=1

