import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"hw(me V)")
plt.xticks([0, 10, 20, 30, 40, 50])


# Y
plt.ylabel(r"")
plt.yticks([0, 0.1, 0.2, 0.3])

# axis
plt.axis([0, 50, 0, 0.3])

x1 = np.array([0.1, 0.1, 20, 50])
y1 = np.array([0, 0.27, 0.26, 0.25])

x2 = np.array([0, 1, 1,2, 20, 50])
y2 = np.array([0, 0, 0.275,0.28, 0.26, 0.25])

x3 = np.array([0, 2, 15, 16, 30, 40, 50])
y3 = np.array([0.03, 0.029, 0.015, 0.28, 0.265, 0.260, 0.258])


plt.plot(x1, y1, marker="", linestyle="--", color="#000", label="")
plt.plot(x2, y2, marker="", linestyle="-.", color="#0000ff", label="")
plt.plot(x3, y3, marker="", linestyle="--", color="#ff0000", label="")


# show
plt.legend()
plt.show()
