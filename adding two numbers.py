def addTwoNumbers(l1, l2):
    l1 = list(reversed(l1))
    l2 = list(reversed(l2))
    int1 = ""
    for i in range(0, len(l1)):
        int1 += str(l1[i])

    int2 = ""
    for j in range(0, len(l2)):
        int2 += str(l2[j])

    result = int(int1) + int(int2)
    resultList = list()
    for i in str(result):
        resultList.append(int(i))
    print(list(reversed(resultList)))


addTwoNumbers([2, 4, 3], [5, 6, 4])
addTwoNumbers([0], [0])
addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
