primes = [2,3,5]

for i in range(1,100000):
    if len(primes) == 10001:
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
            primes.append(y)

    counter = 0
    for j in primes:
        if x%j == 0:
            
            break
        else:
            counter += 1   

        if counter == len(primes):
            primes.append(x)
            print(primes[-1], len(primes))

print(primes[-1])






    
    


    


