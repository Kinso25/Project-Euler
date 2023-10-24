# 2^1000 is too big a number to add all the digits to so there has to be some sort of trick
import math

def getSum(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)

def square(n):
    return pow(2,n)

size = 5
numbers = [0] * size
for i in range(size):
    numbers[i] = i+1

test = map(square, numbers)
test = map(getSum,test)

result = list(test)
total = sum(result)
'''
totalList = [0] *(size+1)
powerTotalMain = 0

for i in range(size+1):
    x = pow(2,i)
    powerTotal = getSum(x)
    powerTotalMain = powerTotalMain + powerTotal
    print(i)
    totalList[i] = powerTotal
    print(pow(2,i),powerTotal,powerTotalMain)
print(totalList)
'''

#print(numbers)
print(numbers)
print(result) 
print(total)