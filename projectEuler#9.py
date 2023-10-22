#  a < b < c 
# a b c = 1000
a = 1
b = 2
c = 997
check = 0

while True: 
    check = a*a + b*b 
    print(a,b,c)
    if check == c*c:
        print(a,b,c)
        break
    elif b > c:
        a = a + 1
        b = a + 1
        c = 1000-a-b
    else:
        b = b+1
        c = c-1
    if a > b:
        print("someone fucked up lmao")
    
    



