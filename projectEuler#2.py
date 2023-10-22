x = 1
y = 2
sum = 2
yes = " is the sum rn"
for i in range(1, 41):
    z = x + y
    x = y
    y = z
    if z < 4000000:
        if z%2 == 0:
            sum = sum + z
            print("adding " + str(sum) + " to " + str(z))

            print(str(sum) + yes)


print(sum)
    
'''
    if z%2 == 0:
        sum = z + sum
        print(str(sum) + yes)
    elif z > 4000000:
        break
    print(z)

    print(str(sum) + yes)
print(str(sum) + yes)
'''