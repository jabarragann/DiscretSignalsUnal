# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import matplotlib.pyplot as plt
from scipy import signal 

w, h = signal.freqz([1,1])

plt.plot(w,h)
plt.show()



