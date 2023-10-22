primes = [2,3,5]
addedPrimes = 10
for i in range(1,10000000):
    if primes[-1] >= 2000000:
        break
    
    y = 6*i - 1
    x = 6*i + 1

    counter = 0
    for j in primes:
        if y%j == 0:
            break

        else:
            counter += 1

        if counter == len(primes):
            addedPrimes += y
            primes.append(y)

    counter = 0
    for j in primes:
        if x%j == 0:
            
            break
        else:
            counter += 1   

        if counter == len(primes):
            
            addedPrimes += x
            primes.append(x)
            print(primes[-1], len(primes))
print(addedPrimes)
print(primes[-1])

