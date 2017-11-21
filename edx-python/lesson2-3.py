# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = np.array([1,2,3])
y = np.array([2,4,6])
X = np.array([[1,2,3], [4,5,6]])
Y = np.array([[2,4,6], [8,10,12]])






import numpy as np
import matplotlib.pyplot as plt
x = np.logspace(-1, 1, 40)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x, y1, "bo-", linewidth=2, markersize=5, label="First")
plt.loglog(x, y2, "gs-", linewidth=2, markersize=5, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")

import numpy as np
import matplotlib.pyplot as plt
x = np.logspace(-1, 1, 40)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x, y1, "bo-", linewidth=2, markersize=5, label="First")
plt.loglog(x, y2, "gs-", linewidth=2, markersize=5, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")


import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=1000)
plt.hist(x, bins = 30, normed = True, cumulative = True, histtype = "step")

## video 2.3.1 and .2

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=12, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")

# video 2.3.3 plotting use logarithmic axes

# semilogx() logx, normal y
# semilogy() normal x, logy
# plotplot() log and log

import matplotlib.pyplot as plt
import numpy as np
x = np.logspace(-1, 1, 40)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.loglog(x, y2, "gs-", linewidth=2, markersize=12, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")


# 2.3.4 generating histograms

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)
plt.hist(x);
plt.hist(x, normed=True); #number now proportion on y axis
plt.hist(x, normed=True, bins=np.linspace(-5, 5, 21)); # 20 bins you need
# 21 pts along the x axis


# gamma distribution and subplot
# a 2x3 subplot has two rows, 1,2,3 and then 4,5,6

x = np.random.gamma(2, 3, 100000)
plt.hist(x, bins = 30, cumulative = True, normed = True, histtype = "step")
plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30, normed = True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative = 30)
plt.subplot(224)
plt.hist(x, bins = 30, normed = True, cumulative = True, histtype = "step")


























