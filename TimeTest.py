import time

def getFactors1(input):
    factorIndex = 0
    arrOfFactors = [0] * input
    for i in range(1,input+1):
        x = input%i
        if x == 0:
            arrOfFactors[factorIndex] = i
            factorIndex += 1

    for i in (range(len(arrOfFactors)-1,-1,-1)):
        if arrOfFactors[i] == 0:
            arrOfFactors.pop(i)
        
    
    return arrOfFactors

def getFactors2(input):
    factorIndex = 0
    arrOfFactors = [0] * input
    for i in range(1,input+1):
        x = input%i
        if x == 0:
            arrOfFactors[factorIndex] = i
            factorIndex += 1

    for i in (range(len(arrOfFactors)-1,-1,-1)):
        if arrOfFactors[i] == 0:
            arrOfFactors = arrOfFactors[0:i]
           
        
    
    return arrOfFactors

def getFactors3(input):
    factorIndex = 0
    arrOfFactors = [0] * input
    for i in range(1,input+1):
        x = input%i
        if x == 0:
            arrOfFactors[factorIndex] = i
            factorIndex += 1

    for i in (range(0,len(arrOfFactors))):
        if arrOfFactors[i] == 0:
            NEWarrOfFactors = arrOfFactors[:i]
            break
        
    
    return NEWarrOfFactors

def getFactors4(input):
    arrOfFactors = [] 
    for i in range(1,input+1):
        x = input%i
        if x == 0:
            arrOfFactors.append(i)

    
    return arrOfFactors

def getTime(function, input):
    first = time.time()
    factor1 = function(input)
    second = time.time()

    timeTaken = second-first

    print(function," took", timeTaken)

factors = 40000



getTime(getFactors1,factors)
getTime(getFactors2,factors)
getTime(getFactors3,factors)
getTime(getFactors4,factors)
