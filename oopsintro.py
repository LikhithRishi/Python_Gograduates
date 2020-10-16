#oops means object oriented programming
#class
#class variavle
#function overloading
#inheritance
#object
#opearator overloading

#syntax of a class
class Naveen:
    #block of code
    #statements
    pass

#whenever you write a class any method present inside a class should have self as their first argument

# class Bird:
#     birdnature="not a mamal"
#     def __init__(self,name,color,size):
#         self.name=name
#         self.color=color
#         self.size=size
#
#     def lifespan(self,name):
#         print("bird lifespan varies from 0 - 500 days",name)
#
#     def birdReproduction(self):
#         print("Bird lays eggs for reproduction")
#         print(self.name)
#         print(self.color)
#         print(self.size)
#
#
# x=Bird("parrot","green","0.5 feet ") # this statement shows you how to create an object
# print(type(x))
# print(x.birdnature)
# print(x.birdReproduction())
# x.lifespan("parrot")

#__init__ this init is called constructor it can accept any no of arguments
#and they get executed only once when object is created
class Dog:

    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour

GSheperd=Dog("German sheppered","brownish black")
Pug=Dog("Pug","Brownish")

print(Pug.breed,Pug.colour)