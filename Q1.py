f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices=listItems
sum = 0
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])
 sum = sum + appleprices[i]
	
import numpy as np
average = sum/(i+1)
print("Mean: " +str(average))

stdevSum = 0
for i in range(0, len(listItems)):
    stdevSum = stdevSum + np.power((appleprices[i] - average), 2)

var = stdevSum/(i+1)
stdev = np.sqrt(var)
print("Standard Deviation: " + str(stdev))