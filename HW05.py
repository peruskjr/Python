def hasFinalLetter(strList, letters):
    goodList = []
    for i in strList:
        if i[-1] in letters:
            goodList.append(i)
    return goodList

strList = ['hello', 'goodbye', 'Chao']
letters = 'zo'

print(hasFinalLetter(strList, letters))

def isDivisible(maxInt, twoInts):  
    rtnList = []

    for i in range(1, maxInt):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            rtnList.append(i)
    
    return rtnList

maxInt = 9
twoInts = (2, 4)

print(isDivisible(maxInt, twoInts))