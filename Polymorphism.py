#polymorphism
#method overriding you need to have same name for both the methods present in super class and sub class
#method overloading

class caterpillar:
     def __init__(self):
         print("I'm caterpillar i eat leaves")
     #mynature which got overriden in cocoon class
     def myNature(self):
         print("My nature is to creep")
         print("My nature is to eat lot of greens")

class Cocoon(caterpillar):
    def __init__(self):
        print("I'm cocoon i stay inside for a long time")
     #my nature oveririden from super class
    def myNature(self):
        print("My nature is to take rest inside and evaluate to butterfly")
    #this is the overloaded method
    # to overload you should have same method name and also methods should be in same class
    #and then the no of arguments that we pass should be differed
    def myNature(self,name,age):
        print("I'm the overloaded method",name,age)



cater=caterpillar()
cater.myNature()
coo=Cocoon()

coo.myNature("naveen",32)


