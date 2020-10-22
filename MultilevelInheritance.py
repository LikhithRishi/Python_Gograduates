#In multilevel inheritance you have grandparent and grand cild relationship
#grandfather
#father
#child

class GrandFather:
    age=72
    eyecolour="brown"
    def __init__(self,age,eyecolour):
        print("we are in grandfather")
        self.age=age
        self.eyecolour=eyecolour

    def healthcondition(self):
        print("he is doing fine")

class Father(GrandFather):
    age=56

    def __init__(self,age):
        print("we are in father")
        self.age=age

    def healthcondition(self):
        print("father health is fine")


class child(Father):

    def __init__(self):
        print("we are in child")
        print(self.age)
        print(self.eyecolour)




chld=child()
chld.healthcondition()