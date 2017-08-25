# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:02:38 2017

@author: jabarraganno
"""

import numpy as np
import matplotlib.pyplot as plt
import time 
from timeit import default_timer as timer

def DFT_slow(x):
    x=np.asarray(x,dtype=float)
    N=x.shape[0]
    n=np.arange(N)
    n=n.reshape(1,N)
    k=n.reshape(N,1)
    M=np.exp(-2j*np.pi*k*n/N)

    print(n)
    print(n.shape)
    print(k)
    print(k.shape)

    return np.dot(M,x)


n=np.arange(4048)
x=np.sin(2*np.pi*8*n/64)

startTime=timer()
X1=abs(DFT_slow(x))
print("---- %s seconds ----" % (timer()-startTime))
startTime=timer()
X2=abs(np.fft.fft(x))
print("---- %s seconds ----" % (timer()-startTime))

plt.plot(x)
fig=plt.figure()
plt.plot(X1)
plt.plot(X2)

plt.show()