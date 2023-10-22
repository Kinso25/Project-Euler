theNumber = 600851475143
primes = [] * 4
for x in range (1,4):
    for i in range(1, 10000):
        if theNumber%i == 0:
            newNumber = theNumber/i
            theNumber = newNumber   

            print(i)
            print(newNumber)
print 
        
        
        