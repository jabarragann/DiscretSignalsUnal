# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:02:40 2017

@author: jabarraganno
"""

import numpy as np

x = np.arange(4)
x = x.reshape(1,4)
print(x)
print(x.shape)

y= np.ones(4)
y = y.reshape(4,1)
print(y)
print(y.shape)

z=x*y
print(z)
print(z.shape)
