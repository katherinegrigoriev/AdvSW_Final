import matplotlib.pyplot as plt
import numpy as np
f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices=listItems
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])
 
plt.plot(range(1, len(appleprices)+1), appleprices)
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.xlabel("Day")
plt.ylabel("Trading price")
plt.show()
