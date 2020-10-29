from abc import ABC,abstractmethod,abstractproperty,abstractclassmethod,abstractstaticmethod

class RBI(ABC):

    interestrate=7.5
    @abstractmethod
    def homeLoans(self):
        print("Home loans starndard rate :",8.35)

    def personalLoans(self):
        print("PL percentage:",11.25)



class SBI(RBI):

     def personalLoans(self):
         print("PL percentage of SBI:",13.5)

     def homeLoans(self):
         print("HL percentage in SBI:",9)

sbi=SBI()
sbi.homeLoans()
sbi.personalLoans()
