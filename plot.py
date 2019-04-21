import matplotlib.pyplot as plt
import numpy as np

T = np.array([0, 3, 4, 5, 6, 10])
power = np.array([0, 4, 2.6, 5.2, 4.1, 10])

plt.plot(T, power)
plt.show()
