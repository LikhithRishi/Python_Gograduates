class Example():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def clsmth(cls,name,age):
        name="naveen"
        print("we are in class method")
        return cls(name,age-2)

    @staticmethod
    def sttcmthd():
        print("we are in static method")

    def normal(self):
        print("we are in normal method")

ex=Example("prakash",34)
x=Example.clsmth("Naveen",34)
print(x.age)
#Example.normal() # this will throw error because normal methods are defined to object
Example.sttcmthd()

#classmethod can change the behaviour of tjhe class
#static method can't modify or change the behaviour of the class
# apart from that both class method and static method are of CLASS LEVEL AND not object leve;