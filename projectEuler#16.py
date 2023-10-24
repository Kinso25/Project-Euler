#I completely overthought this and thought it was asking for the sum of all digit of the powers of 2 up to 2^1000
#but this was pretty easy
import math

def getSum(n):
    strn = str(n)
    listn = list(map(int, strn.strip()))
    return sum(listn)

bigNum = pow(2,1000)
print(bigNum) 
result = getSum(bigNum)
print(result)
