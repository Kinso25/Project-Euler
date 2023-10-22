import math
import numpy
import pandas
import matplotlib.pyplot as plt 

def getTriNum(amount):
    arr = [1] * (amount+1)
    for i in range(2,amount+2):
        tN = 0
        for j in range(1,i+1):
            tN += j
            arr[i-1] = tN
    return arr



def getFactors(input):
    numFact = 0
    for i in range(1,math.ceil(numpy.sqrt(input))):
        x = input%i
        if x == 0:
            numFact += 2

    if numpy.sqrt(input) % 1 == 0:
        numFact += 1

    
    return numFact

#----------------------------------------------------------------------

x = 0
counter = 1
start = 1
end = 15000
TriNumArr = getTriNum(end)

for i in range(start+1,len(TriNumArr)-1):
    targetArr = getFactors(TriNumArr[i])
    
    if counter == 10:
        print("Still going")
        print("Working on: " , TriNumArr[i])
        print(TriNumArr[i], " has " , targetArr , " factors!")
        print(i," out of ", end)
        
        counter = 1
    else:
        counter +=1


    if targetArr >= 500:
        print(TriNumArr[i], " is the number!")
        print(i, " is the amount of factors")
        x = i
        break


#----------------------------------------------------------------------
TriNumArr = getTriNum(50)
factors = getFactors(TriNumArr[10])


#print(TriNumArr)S
yes = getFactors(TriNumArr[x])
print(TriNumArr[x])
print(yes)
