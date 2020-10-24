import matplotlib.pyplot as plt
import numpy as np

# title
plt.title('FIG. 3.')

# X
plt.xlabel('W(eV)')
plt.xticks([0.35, .40, .45, .50, .60, .65, .70])

# Y
plt.ylabel('W(in unit of (2PIe^2/h))')
plt.yticks([ 0, .1, .2, .3, .4])

#axis
plt.axis([0.35, .70, 0, .4])

x1 = [ .37, .38, .39, .40, .70]
y1 = [ 0, .008, .011, .06, .06]

x2 = [ .37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y2 = [ 0, .008, .011, .07, .08, .081, .083, .085, .087, .1]

x3 = [ .37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y3 = [ 0, .008, .011, .09, .1, .11, .12, .14, .15, .18]

x4 = [ .37, .38, .39, .40, .45, .50, .55, .60, .65, .70]
y4 = [ 0, .008, .011, .12, .15, .19, .22, .26, .29, .35]

plt.plot(x1, y1, marker='x', linestyle='-', color='#000', label='Lambda=0')  # 0eV
plt.plot(x2, y2, marker='X', linestyle='--', color='#ff0000', label='Lambda=0.05')  # 1ev
plt.plot(x3, y3, marker='D', linestyle='-.', color='#00ff00', label='Lambda=0.1')  # 2ev
plt.plot(x4, y4, marker='P', linestyle='--', color='#0000ff', label='3eV')  # 3ev

# show
plt.legend()
plt.show()