import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

T = np.array([0,2, 3, 4, 5, 6, 10])
power = np.array([1000,2000, 4000, 2600, 5200, 6800, 10000])

xnew = np.linspace(T.min(), T.max(), 30)  # 300 represents number of points to make between T.min and T.max

power_smooth = spline(T, power, xnew)

plt.plot(xnew, power_smooth)
plt.show()
