with open('welcome.txt', 'r') as file:
    lines = file.readlines()

sumOf = 0

testSum = int(lines[0]) + int(lines[1])
print(testSum)
for i in range(0,len(lines)):
    sumOf += int(lines[i])

sumOf = str(sumOf)
for j in range(0,10):
    print(sumOf[j])

print(sumOf)

