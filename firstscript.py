x=10
if x>=10:
 print("hello world")
 

print(x)

y=15
print("this is to demonstrate if and else ")
if x>y:
  print(x,y)
else :
  print("we are in else as the condion failed")
  
#this is example for multiple condition in if block 
if x>y and x==y:
   print("condition for x and y passed ")
   
if x>y or x==y:
   print("or condition with if ")
   
   
#This example is for if and elif 

if x>y:
   print("making if false as 10>15 will fail")
elif y==x:
   print("we are in else if block")
elif y==10:
   print("we are here 2")
elif y!=15:
   print ("we are here 3")
else:
   print("the end case")
   
#nested conditions (condition within another condition
if y>x:
    print("outside if got passed")
    if y==15:
      print("y value is 15")
    else:
      print("y value is not 15")
else:
  print("we are in nested condition else ")


name="naveen"
len(name)
print(len(name))

for i in name:
    print(i)
    
    