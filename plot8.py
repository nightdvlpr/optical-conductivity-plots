import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"hw(me V)")
plt.xticks([0, 20, 40, 50])


# Y
plt.ylabel(r"")
plt.yticks([0, 5, 10, 15, 20])

# axis
plt.axis([0, 50, 0, 20])

x1 = np.array([0, 1, 1, 2, 2.9, 19, 20, 20, 20.2, 21.5, 22.5, 23, 24, 25, 28, 50])
y1 = np.array([0, 0, 4, 3.3, 3, 3.8, 5.1, 15, 5, 3.5, 3, 2.7, 2.2, 1.8, 1.4, 0.4])


x2 = np.array([0, 1,1,20,20.1,20.5,       20.2, 21.5, 22.5, 23, 24, 25, 28, 50         ])
y2 = np.array([15,15, 18,10,22,9,          8.5, 7, 6.5, 6.1, 5.9, 5.5, 4.4, 2          ])

x3 = np.array([0, 0, 17, 17,19,20,20,   20.2, 21.5, 22.5, 23, 24, 25, 28, 50])
y3 = np.array([0, 1, 0.5, 4.2,5,6,16,   5.9, 3.9, 3.4, 3.1, 2.5, 1.9, 1.5, 0.4])

plt.plot(x2, y2, marker="", linestyle="-.", color="#0000ff", label="", linewidth=1.1)
plt.plot(x3, y3, marker="", linestyle="--", color="#ff0000", label="", linewidth=2.1)
plt.plot(x1, y1, marker="", linestyle="-", color="#000", label="", linewidth=2)

# show
plt.legend()
plt.show()