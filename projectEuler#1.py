sum = 0

for i in range(1, 1000): 
    x = i
    if (x%5) == 0:
        sum = i + sum
        print(i)
    elif (x%3) == 0:
        sum = i + sum
        print(i)
    else:
        print(i)

print(sum)

