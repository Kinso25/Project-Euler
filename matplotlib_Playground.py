import math
import numpy
import pandas as pd
import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]
y2 = [0] * 10
for i in range(10):
    y2[i] = y[i] * 20


plt.plot(x,y)
plt.plot(x,y2)

plt.xlabel('Time')
plt.ylabel('Money')
                        

plt.show()