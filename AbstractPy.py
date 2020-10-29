#Abstarct in python
#Abstraction means hiding the information
#You can't create object for abstarct class
#you can't inherit if you have abstarct class or abstarct static defined in abtsract class

from abc import abstractmethod,ABC,abstractclassmethod,abstractstaticmethod

class RBI(ABC):

    @abstractmethod
    def HomeLoan(self):
        print("I'm abstract method loan percentage is 9%",)

    def PersonalMethod(self):
        print("I'm personal loan")




class SBI(RBI):

    def HomeLoan(self):
        print("I'm SBI method for home loan")




sbi=SBI()
sbi.HomeLoan()
sbi.PersonalMethod()