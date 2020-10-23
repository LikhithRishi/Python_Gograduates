
class Encapsulate:
    #if you want something to be public just give it normal representation
    #public variable
    x=10
    #protected variable
    _y=20
    #private variable
    __z=30

    def publicmethod(self):
        print("I'm public method")

    def _protectedMethod(self):
        print("protected method")

    def __privatemethod(self):
        print("Private method")



class subclass(Encapsulate):
    def __init__(self):
        print(self.x)
        print(self._y)
    def publicmethod(self):
        print("came here 1")
    #protected are only accesible for subclasses
    def _protectedMethod(self):
        print("came here 2")
    #private methods can't be oberriden
    def __privatemethod(self):
        print("came here 3")

enc=Encapsulate()
enc.publicmethod()
enc._protectedMethod()
enc.__privatemethod()
sub=subclass()
sub._protectedMethod()
sub.publicmethod()
