import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("FIG. Curve Fitting")

# X
plt.xlabel(r"X")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Y
plt.ylabel(r"Y")
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# axis
plt.axis([0, 9, 0, 9])

x1 = [3] + list(np.arange(3.90, 4.2)) + [5]
y1 = [1] + list(np.arange(1.4, 1.7)) + [4]
print(x1)
print(y1)

# print(y1)


plt.plot(x1, y1, marker=".", linestyle="-", color="#000", label="1st")

# show
plt.legend()
plt.show()
