#you will have one super class and multiple child classes

class grandfather:
    age=72
    eyecolour="brown"
    def __init__(self):
        print("i'm Grandfather")

class granddaughter(grandfather):
    def __init__(self):
        print(self.eyecolour)
        print(self.age)

class grandson(grandfather):
    def __init__(self):
        print("we are in grandson")
        print(self.age)
        print(self.eyecolour)

gs=grandson()
gd=granddaughter()
