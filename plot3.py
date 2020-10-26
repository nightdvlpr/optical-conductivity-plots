import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# title
plt.title('FIG. 3.')

# X
plt.xlabel(r'$\mathcal{\omega (eV)} $', fontsize=24)
plt.xticks([-.5, -.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])

# Y
plt.ylabel('DOS', fontsize=24)
plt.yticks([0, .2, .4, .6])


# axis
plt.axis([-0.5, 0.5, 0, .7])

x1 = [-.5, 0, .5]
y1 = [.65, 0, .65]

x2 = [-.5, -.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5]
y2 = [.3, .29, .27, .22, .13, 0, .13, .22, .27, .29, .3]

x3 = [-.5, -.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5]
y3 = [.18, .2, .2, .2, .13, 0, .13, .2, .2, .2, .18]

plt.plot(x1, y1, marker='x', linestyle='solid',
         color='#000000', label=r'$\lambda=0$', markersize=4)

plt.plot(x2, y2, marker='X', linestyle='-',
         color='#ff0000', label=r'$\lambda=0.1$', markersize=5)

plt.plot(x3, y3, marker='D', linestyle='dotted',
         color='#0000ff', label=r'$\lambda=0.2$', markersize=6)

# show
plt.legend()
plt.show()