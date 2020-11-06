import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"hw(me V)")
plt.xticks([0, .5, 1, 1.5, 1.6])

# Y
plt.ylabel(r"D(w)")
plt.yticks([0, 10, 20, 30, 40, 50])

# axis
plt.axis([0, 50, 0, 1.6])

x1 = np.array([0, 1,1,1])
y1 = np.array([1.1, 1.1,1.6,.4])

x2 = np.array([20, 20])
y2 = np.array([0, 3])

x3 = np.array([38, 38])
y3 = np.array([0, 3])


plt.plot(x1, y1, marker="", linestyle="--", color="#0000ff", label="(ii)")
#plt.plot(x2, y2, marker="", linestyle="-", color="#000000", label="(iii)")
#plt.plot(x3, y3, marker="", linestyle="-", color="#ff0000", label="(i)") 


# show
plt.legend()
plt.show()
