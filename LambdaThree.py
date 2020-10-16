from functools import reduce
#map function using lambda

#Example to demonstrate conditional operator concept inside filter
#0 is false 1 is true
# simplelist=[1,2,3,4,5,6,7,8,9,10]
# a=lambda x:x%2==0
# y=filter(a,simplelist)
# print(list(y))

#map it takes list as argument
#In map lambda expersion will be perfomed and each ana every value and will render the end result
# simplelist=[1,2,3,4,5,6,7,8,9,10]
# a=lambda x:x%2
# y=map(a,simplelist)
# print(list(y))

#reduce function in python
#reduce perform opertion in between the values present inside the lists
# simplelist=[1,2,3,4,5,6,7,8,9,10]
# a=lambda x,y:x+y
# y=reduce(a,simplelist)
# print(y)

