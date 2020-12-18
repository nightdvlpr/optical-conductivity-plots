import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"$\hslash\omega(me V)$")
plt.xticks([0, 10, 20, 30, 40, 50])


# Y
plt.ylabel(r"$\sigma xx (e^2/\hslash)$")
plt.yticks([0, 0.1, 0.2, 0.3])

# axis
plt.axis([0, 50, 0, 0.3])

x1 = np.array([0.2, 0.2, 15, 20, 21, 24, 50])
y1 = np.array([0, 0.27, 0.265, 0.259, 0.257, 0.256, 0.251])

x2 = np.array([0,1, 1, 15, 20, 21, 24, 50])
y2 = np.array([0.005,0.005, 0.273, 0.269, 0.26, 0.259, 0.258, 0.252])

x3 = np.array([0, 2, 15, 16, 20, 23, 30, 40, 50])
y3 = np.array([0.03, 0.029, 0.025, 0.279, 0.270, 0.267, 0.261, 0.258, 0.254])


plt.plot(x1, y1, marker="", linestyle="-", color="#000", label="")
plt.plot(x2, y2, marker="", linestyle="--", color="#0000ff", label="", linewidth=2)
plt.plot(x3, y3, marker="", linestyle=":", color="#ff0000", label="", linewidth=3)


# show
plt.legend()
plt.show()
