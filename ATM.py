#this is ATM utilities closure
def atmUtilities(func):
    def atmFunc(*args):
        z=func(*args)
        return z
    return atmFunc


def pinValidation(pin):
    x=str(pin)
    if len(x)!=4:
        print("invalid pin")
        return False
    else:
        if x=='1234':
            return True

pinvalid=atmUtilities(pinValidation)
z=pinvalid(1234)
print("here ",z)
def cashWithdrawal(amount,balance):
    if amount<=balance:
        balance=balance-amount
        return balance
def pinchange(pin):
    if len(str(pin))==4:
        print("change the pin")


pin=atmUtilities(pinchange)
pin(3456)
if z==True:
   result=atmUtilities(cashWithdrawal)(2000,5000)
   print("after withdrawal the balance is ",result)
