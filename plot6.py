import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"hw(me V)")
plt.xticks([0, 10, 20, 30, 40, 50])


# Y
plt.ylabel(r"")
plt.yticks([0, 0.5, 1, 1.5, 1.6])

# axis
plt.axis([0, 50, 0, 1.6])

x1 = np.array([0, 1, 1, 5,                     10,   15,        20, 30, 40, 50])
y1 = np.array([1.1, 1.1, 1.5, 1.1,             0.85,  0.70,       0.55, 0.46, 0.4, 0.4])

x2 = np.array([0, 1, 1, 1.5, 2,   2.5,    3, 4,  6,  8, 10, 50])
y2 = np.array([0, 0, .5, .41, .38,  .35,  .32, .3, .29,  0.3, 0.3, 0.31])

x3 = np.array([0, 16,16,50])
y3 = np.array([.05, .02,.31,.3])


plt.plot(x1, y1, marker="", linestyle="-.", color="#0000ff", label="",linewidth=3)
plt.plot(x2, y2, marker="", linestyle="-", color="#000000", label="",linewidth=2)
plt.plot(x3, y3, marker="", linestyle="--", color="#ff0000", label="")


# show
plt.legend()
plt.show()
