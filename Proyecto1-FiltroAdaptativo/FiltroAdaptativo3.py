# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:10:06 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import numpy as np
import matplotlib.pylab as plt

import padasip as pa

# creation of x and d
N = 700
x = np.random.random((N, 4))
v = np.random.normal(0, 1, N) * 0.1
d = 2*x[:,0] + 0.1*x[:,1] - 4*x[:,2] + 0.5*x[:,3] + v

# identification
f = pa.filters.FilterNLMS(mu=0.5, n=4)
y, e, w = f.run(d, x)

# show results
plt.figure(figsize=(12.5,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("Number of iteration [-]")
plt.plot(d,"b", label="d - target")
plt.plot(y,"g", label="y - output")
plt.xlim(0, N)
plt.legend()

plt.subplot(212); plt.title("Filter error"); plt.xlabel("Number of iteration [-]")
plt.plot(pa.misc.logSE(e),"r", label="Squared error [dB]");plt.legend()
plt.xlim(0, N)
plt.tight_layout()
plt.show()
print("And the resulting coefficients are: {}".format(w[-1]))