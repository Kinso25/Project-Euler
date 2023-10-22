x = 999*999
found = 0
OldZ = 0
z = 0
for y in range(-999, 1):
    z= int(z)
    if z > OldZ:
        OldZ = z

    found = 0
    for x in range(-999, 1):
        if found == 1:
            break
        z = x * y
        z = str(z)
        counter = 0
        
        for i in range(0,len(z)):
                if z[i] == z[len(z)-1-i]:
                    counter += 1
                    if counter == len(z):
                        print(str(z) + " is a pallindrome!")
                        
                        found = 1   
                        break
        
print(OldZ)
# this code is so messy but it works i guess