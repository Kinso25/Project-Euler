'''
This problem is based around "Collatz Conjecture" which is a famous unsolved problem in mathemathics.

You start with a random positive integer (n)
    then if its postive you divide it by 2 (n/2 | n % 2 = 0)
    if the number is odd you multiply it by 3 and add 1 (3n + 1 | n % 2 = 1)

    You then repeat the process until it should reach 1. 
    Though this is the problem that is unsolved, the fact that all numbers should end up at 1
    is theoritical as no one has actually proven this rule.

    
Project Euler problem #14 is to find which starting number under 1 million produces the longest chain of operations.

INITIAL THOUGHTS:
    Ive done some research about the Collatz Conjecture (looked at the wiki page lmao) and it seems that the obvious bigger number equals bigger chain is not always true.
    I mean thats kind of a given since its a problem but regardless with that info ill have to write some code that with sort through these numbers and iterate through the chains
    to find the longest one. 

    Like the optimisation for PE#12 the actual contents of the numbers dont matter just the amount of iterations.
    Maybe.. i think that there could be a method that could check against numbers it has already ran and add the numbers of that itteration to current one
    Not sure which is quicker big I have time test tools now to help with that.

    I think ill just make a brute force strategy and measure the time complexity and see if its viable before going further


FINAL THOUGHTS:
    Well that was alot quicker than expected almost anticlimatic but it does mean two important things:
        - im getting the hang of this(im improving to some degree)
        - Researching the problem and writing it out like this is very helpful and quicker than just diving in and hoping for the best

    There wasnt anything too hard about this problem and there was no need to optimise the code 
    Maybe could clean up the main for loop into another user defined function for readabilites sake but i  dont think its worth it tbh(did it anyway)
 
'''

import math
import numpy
import pandas as pd
import matplotlib.pyplot as plt 

def CollatzAlgr(input): 
    counter = 0
    while input != 1:
        if input % 2 == 0:
            input = input/2
            counter += 1
        else:
            input = 3*input + 1
            counter += 1
    return counter

def main(input):
    big =  0
    theNum = 0

    for i in range(1,input):
        current = CollatzAlgr(i)
        if current >= big: 
            big = current
            theNum = i
            print(big , i)
    return theNum

theNum = main(1000000)


print("The number with the biggest chain is:", theNum)



