import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# title
plt.title('FIG. 3.')

# X
plt.xlabel(r'$\mathcal{\omega (eV)} $', fontsize=24)
plt.xticks([0.35, .40, .45, .50, .60, .65, .70])

# Y
plt.ylabel(r'$\sigma (\omega) in-unit-of (2 \pi e^2/h)$', fontsize=24)
plt.yticks([0, .1, .2, .3, .4])


# axis
plt.axis([0.35, .70, 0, .4])

x1 = [.37, .38, .39, .40, .70]
y1 = [0, .008, .011, .06, .06]

x2 = [.37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y2 = [0, .009, .011, .07, .08, .081, .083, .085, .087, .1]

x3 = [.37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y3 = [0, .008, .011, .09, .1, .11, .12, .14, .15, .18]

x4 = [.37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y4 = [0, .008, .011, .12, .15, .19, .22, .26, .29, .35]

plt.plot(x1, y1, marker='x', linestyle='solid',
         color='#000', label='Lambda=0', markersize=4)

plt.plot(x2, y2, marker='X', linestyle='-',
         color='#ff0000', label='Lambda=0.05',markersize=5)

plt.plot(x3, y3, marker='D', linestyle='-.',
         color='#00ff00', label='Lambda=0.1', markersize=6)

plt.plot(x4, y4, marker='P', linestyle='--',
         color='#0000ff', label='3eV', markersize=7) 

# show
plt.legend()
plt.show()
