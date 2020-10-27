import numpy as np
import matplotlib.pyplot as plt

# title
plt.title('FIG. 1.')

# X
plt.xlabel('K<------r------>K', fontsize=24)
plt.xticks([-2, 1.5, -1, -.5, 0, .5, 1, 1.5, 2])

# Y
plt.ylabel('M<------r------>M', fontsize=24)
plt.yticks([-2, -1.5, -1, -.5, 0, .5, 1, 1.5, 2])


# axis

#plt.plot(x1, y1, marker='x', linestyle='solid', color='#000000', label=r'$\lambda=0$', markersize=4)
# show
plt.show()
