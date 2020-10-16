# 1) Create a lambda function that filters numbers greater than 25 [26,27,1,2,3,4,5,29,30]

l=[28,24,4,34,89,5,67,21,56,6]
x=lambda y:y>25
print(list(filter(x,l)))

#2) Create a lambda function that filters strings having length greater than 5 ["nav","naveen"]

l=["Likhith","Rishi","Manideep","Ajay","Naveen","Rithwik"]
x=lambda y:len(y)>5
print(list(filter(x,l)))

#3)take a file read data and write it to new file

with open("myfile.txt","r") as f:
    lines=f.readlines()
with open("copyfile.txt","w") as cf:
    for line in lines:
        cf.writelines(line)

#4)write a function  filter palindromes "Dad" even after reversing it shoudl be the same

l=['dad',"Likhith",'madam',"Rishi"'abcdcba']
x=lambda  y:y==y[::-1]
print(list(filter(x,l)))