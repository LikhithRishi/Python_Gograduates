#deque
#FIFO concept first in first out
#deque it is nothing but double ended queue
from collections import deque
smlist=[1,2,3,4]
smlist.append("naveen")
smlist.extend([5,6,7,8])
x=deque(smlist)
x.append("Python")
x.appendleft("Left append")

x.extend(["1234","5678"])
x.extendleft([0,9,8,7])
x.pop()
x.popleft()
print(x.count(8))
x.remove(8)
x.remove(8)
print(x)
x.rotate(9)
print(x)
x.reverse()
print(x)
print(x.index(1))
x.insert(10,"Akshitha")
print(x)

#userList
#userString
#userDict