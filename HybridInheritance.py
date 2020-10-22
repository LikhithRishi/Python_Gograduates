#Hybrid inheritance is some this whil have diamond shaped relationship
#Grandfather
#son and daughter in law
#grandchildren
# this is a combination of heirarichal and multiple inheritance

class GrandFather:
    age=72
    colour="brown"
    def __init__(self):
        print("i'm in grand father")
    def healthcondition(self):
        print("i'm doing good")

class Father(GrandFather):
      age =56
      colour = "blue"
      def __init__(self):
          print("we are in father")

      def bankbalance(self):
           print("My bank balance from father is 2500")

class Mother(GrandFather):
      height=5.6
      mothertounge="telugu"
      def __init__(self):
          print("i'm his mother")

class child(Father,Mother):
     def __init__(self):
         print("I'm the child")


cld=child()
cld.healthcondition()
print(cld.height)
cld.bankbalance()
print(cld.mothertounge)