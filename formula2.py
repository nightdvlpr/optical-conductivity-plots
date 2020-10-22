import matplotlib.pyplot as plt
import numpy as np

# title
plt.title('FIG. 2.')

# X
plt.xlabel('Ꞷ(eV)')
plt.xticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9])

# Y
plt.ylabel('(Ꞷ)in unit of (2 e2/h)')
plt.yticks([0, .1, .2, .3, .4, .5, .6])

#axis
plt.axis([0, .9, 0, .6])

x1 = [0, .2, .4, .6, .9]
y1 = [.06, .06, .11, .25, .55]

x2 = [0, .2, .2, .4, .6, .9]
y2 = [0, 0, .06, .11, .25, .55]

x3 = [0, .4, .4, .6, .9]
y3 = [0, 0, .11, .25, .55]

x4 = [0, .6, .6, .9]
y4 = [0, 0, .25, .55]

plt.plot(x1, y1, marker='x', linestyle='-', color='#000', label='0eV')  # 0eV
plt.plot(x2, y2, marker='X', linestyle='--', color='#ff0000', label='1eV')  # 1ev
plt.plot(x3, y3, marker='D', linestyle='-.', color='#00ff00', label='2eV')  # 2ev
plt.plot(x4, y4, marker='P', linestyle='--', color='#0000ff', label='3eV')  # 3ev

# show
plt.legend()
plt.show()