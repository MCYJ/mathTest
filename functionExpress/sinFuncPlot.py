import math
import numpy as np
import matplotlib.pyplot as plt

data = []
step = 0.01
deg = 0

for i in range(1000):
    data.append(np.sin(math.pi*deg))
    deg += step
    print(i+1,': sin -',deg,':',data[i])

plt.plot(data)
plt.show()