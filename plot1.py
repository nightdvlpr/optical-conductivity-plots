import matplotlib.pyplot as plt
import numpy as np

# title
plt.title('FIG. 2.')

# X
plt.xlabel(r'Ꞷ(eV)')
plt.xticks([0, .01, .02, .03, .04, .05, .06, .07, .08, .09])

# Y
plt.ylabel(r'(Ꞷ)in unit of (2 e2/h)')
plt.yticks([0, .1, .2, .3, .4, .5, .6])

# axis
plt.axis([0, .9, 0, .6])

x1 = np.array([0, .1, .2, .24, .3, .34, .4, .6, .9])
y1 = np.array([.06, .06, .06,.06, .07, .077, .11, .25, .55])

x2 = np.array([0, .2, .2, .24, .3, .34, .4, .6, .9])
y2 = np.array([0, 0, .06, .06, .07, .077,.11, .25, .55])

x3 = np.array([0, .4, .4, .6, .9])
y3 = np.array([0, 0, .11, .25, .55])

x4 = np.array([0, .6, .6, .9])
y4 = np.array([0, 0, .25, .55])

plt.plot(x1, y1, marker='', linestyle='-', color='#000', label='0eV')  # 0eV
plt.plot(x2, y2, marker='', linestyle='--',color='#ff0000', label='1eV')  # 1ev
plt.plot(x3, y3, marker='', linestyle='-.',color='#00ff00', label='2eV')  # 2ev
plt.plot(x4, y4, marker='', linestyle='--',color='#0000ff', label='3eV')  # 3ev

# show
plt.legend()
plt.show()
