#write a function for division and modulo and pass it into closure

def outerfunction(func):
    def innerfunction(*args):
         z=func(*args)
         print(z)
    return innerfunction

def div(x,y):
    return x/y
def modulo(x,y):
    return x%y
outerfunction(div)(3,4)
outerfunction(modulo)(12,5)

# write function for r+ and pass it into fileIOClosure

def fileIOclosure(func):
    def innerFileIO(*args):
        func(*args)
    return innerFileIO

def readWriteFile(filename,mode):
    with open(filename, mode) as val:
        lines = ["\nopening it in read write mode"]
        val.writelines(lines)
        readlines = val.readlines()
        for rdline in readlines:
            print(rdline)
fileIOclosure(readWriteFile)("myfile.txt","r+")
