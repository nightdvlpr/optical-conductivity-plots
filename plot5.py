import matplotlib.pyplot as plt
import numpy as np

# title
plt.title("(c)")

# X
plt.xlabel(r"$\hslash\omega(me V)$")
plt.xticks([0, 20, 40, 50])

# Y
plt.ylabel(r"$D(\omega)$")
plt.yticks([0, 10, 20, 30, 40, 50])

# axis
plt.axis([0, 50, 0, 50])

x1 = np.array([10, 10])
y1 = np.array([0, 3])

x2 = np.array([20, 20])
y2 = np.array([0, 3])

x3 = np.array([38, 38])
y3 = np.array([0, 3])

x4 = np.array([5, 5])
y4 = np.array([0, 8])

x5 = np.array([0, 2])
y5 = np.array([0.1, 0.1])

x6 = np.array([0.1, 0.1, 5, 15, 16, 17,18, 20, 20.1])
y6 = np.array([0, 9, 10, 12, 12.2, 12.8,13.5, 17, 48])

x7 = np.array([50, 40, 30, 25, 22, 21, 20.5, 20, 20])
y7 = np.array([3, 3.5, 4, 5, 5.5, 6, 6.5, 8, 50])

plt.plot(x1, y1, marker="", linestyle="-", color="#ff0000", label="(ii)")  # 0eV
plt.plot(x2, y2, marker="", linestyle="-", color="#ff0000", label="(iii)")  # 1ev
plt.plot(x3, y3, marker="", linestyle="-", color="#ff0000", label="(i)")  # 2ev
plt.plot(x4, y4, marker="", linestyle="--", color="#0000ff", label="")  # 3ev
plt.plot(x5, y5, marker="", linestyle="--", color="#0000ff", label="")  # 3ev
plt.plot(x6, y6, marker="", linestyle="--", color="#000000", label="")  # 3ev
plt.plot(x7, y7, marker="", linestyle="--", color="#0000ff", label="")  # 3ev

# show
plt.legend()
plt.show()
