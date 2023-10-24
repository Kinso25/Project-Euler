import math
import numpy as np
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

size = 999
numbers = [0] * size

for i in range(size):
    numbers[i] = i+1

oneToNineteen = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,0,6,6,5,5,5,7,6,6]
hundreds = [0,13,13,15,14,14,13,15,15,14]

#Number Letter Counter Function (ncl)

def nlc(n):

    strn = str(n)
    numCount = 0

    #reverses the string so the first digit is always at index 0
    strn = strn[::-1]

    #Single digit calculations
    if len(strn) == 1:
        numCount = oneToNineteen[n]
        return numCount
    
    #Double digit calculations   
    if len(strn) ==2:
        if int(strn[1]) == 1:
            numCount = oneToNineteen[int(strn[0])+10]
            return numCount
        if int(strn[1]) > 1:
            
            numCount = numCount + tens[int(strn[1])]
            if int(strn[0]) != 0:
                numCount = numCount + oneToNineteen[int(strn[0])]
            return numCount
        
    #Triple digit calculations 
    if len(strn) ==3:
        if n % 100 == 0:
            numCount = hundreds[int(strn[2])]-3
            return numCount
        if int(strn[1]) == 0:
            numCount = oneToNineteen[int(strn[0])] 
            numCount = numCount + hundreds[int(strn[2])]
            return numCount
        if int(strn[1]) == 1:
            numCount = oneToNineteen[int(strn[0])+10]
            numCount = numCount + hundreds[int(strn[2])]
            return numCount
        if int(strn[1]) > 1:
            
            numCount = tens[int(strn[1])]
            if int(strn[0]) != 0:
                numCount = numCount + oneToNineteen[int(strn[0])]
            numCount = numCount + hundreds[int(strn[2])]
            return numCount
        
        if len(strn) == 4:
            numCount = 11
            return numCount
    
        
    
    


    
'''
for i in range(99):
    test = nlc(i)
    total = test

    print(test)
'''


test = map(nlc,numbers)

x = list(test)
y = sum(x)
#print(x)
print(y)
print(len(x))
result = y + 11
print(result)
'''
#print(numbers)
for i in range(len(x)):
    
    print(i+1, x[i])

'''


'''
one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty 
twenty thirty forty fifty sixty seventy eighty ninety one hundred and one
'''