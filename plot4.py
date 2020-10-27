import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
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
plt.axis([-2, 2, -2, 2])

fig, ax = plt.subplots()
N = 3
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []
circle = Circle((x, y), radii)

colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)



# show
plt.show()