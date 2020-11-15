import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"hw(me V)")
plt.xticks([0, 15, 30, 45, 50])

# Y
plt.ylabel(r"D(w)")
plt.yticks([0, 15, 30, 45])

# axis
plt.axis([0, 50, 0, 45])

x1 = np.array([0,15.5, 15.5, 16, 17,18, 20, 20.1])
y1 = np.array([0, 0,9, 10.2,10.8,11.5, 17, 43])
x2 = np.array([50, 40, 30, 25, 22, 21, 20.5, 20, 20])
y2 = np.array([3, 3.5, 4, 5, 5.5, 6, 6.5, 8, 43])

x3 = np.array([2, 2, 5, 15, 16, 17,18, 20, 20.1])
y3 = np.array([0, 9, 9.1, 9.6, 10.2,10.8,11.5, 17, 43])
x4 = np.array([50, 40, 30, 25, 22, 21, 20.5, 20, 20])
y4= np.array([3, 3.5, 4, 5, 5.5, 6, 6.5, 8, 43])

plt.plot(x1, y1, marker="", linestyle="dotted", color="#ff0000", label="", linewidth=3)
plt.plot(x2, y2, marker="", linestyle="dotted", color="#ff0000", label="", linewidth=3)
plt.plot(x3, y3, marker="", linestyle="-", color="#000000", label="")
plt.plot(x4, y4, marker="", linestyle="-", color="#000000", label="")

# show
plt.legend()
plt.show()
