#Types of inheritance
#single inheritance
#multiple inheritance
#multilevel inheritance
#Hybrid inheritance
#Hirarical inheritance

#Example for single inheritance
# you will be having a single super class for a subclass
# super class here is father
# and child is inheriting from father

# class father:
#     bankbalance=100000
#     age=50
#
#     def __init__(self,age,bankbalance):
#         self.age=age
#         self.bankbalance =bankbalance
#         print("I'm father",self.age,self.bankbalance)
#
#
#     def amount(self):
#         print("I'm having >>>",self.bankbalance)
#
#
# class child(father):
#
#     def __init__(self,age,hobbies,bankbalance):
#            self.hobbies=hobbies
#            self.age=age
#            self.bankbalance=bankbalance
#
#            father.age
#            father.bankbalance
#
#            diffage=father.age-self.age
#            print(diffage)
#            print("I'm from child")
#
#
#
#     def isGoingSchoool(self):
#         print("yes i'm going to school")
#
#
# child=child(12,"cricket",2500)
# child.isGoingSchoool()
# child.amount()
# father=father(60,10000)

class RBI:


    def __init__(self):
        print("I am RBI")

    def homeLoaninterestRate(self):
        return 6.90

    def personalLoan(self):
        return 11.25


class HDFC(RBI):

    def __init__(self):
        print("I'm hDFC")
    #here you are overriding personal loan this concept is called method overriding
    def personalLoan(self):
        return 10.49


hdf=HDFC()
print(hdf.homeLoaninterestRate())
print(hdf.personalLoan())
