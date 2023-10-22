'''

In this problem you have to figre out how many routes there are through a grid using only right and down movements while starting at the top left.

The grid is 20 x 20 (kind of, you can only travel through edges) and tbh its pretty overwhelming


INITIAL THOUGHTS:
gonna try with a smaller sample size
see if there is patterns

0 0 0
0 0 0
0 0 0 

'''

'''
1100
1010
1001
0110
0101
0011
'''
import numpy as np
size = 21
matrix = np.zeros((size, size))

# Setup for matrix 
for i in range(size):
    matrix[i, 0] = 1
for i in range(size):
    matrix[0, i] = 1

print(matrix)
print(" ")

for row in range(1, size):
    for col in range(1, size):
        matrix[row, col] = matrix[row - 1, col] + matrix[row, col - 1]

for i in range(20):
    print(matrix[i])



print(matrix[size-1, size-1])


