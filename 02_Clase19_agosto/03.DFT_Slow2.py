# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 23:40:59 2017

@author: jabarraganno
"""

import numpy as np 
from timeit import default_timer as timer
import matplotlib.pyplot as plt 


def DFT_slow2(x) :
    
    x=np.array(x)
    
    N=x.shape[0]
    X=np.zeros(N,dtype=np.complex_)

    for k in range(N):
        for n in range(N):
            
            X[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
            
    return X
         
    
n=np.arange(128)
x=np.sin(2*np.pi*8*n/64)

startTime=timer()
X1=abs(DFT_slow2(x))
print("\n\n")
print("DFT slow---- %s seconds ----" % (timer()-startTime))
startTime=timer()
X2=abs(np.fft.fft(x))
print("DFT FFT---- %s seconds ----" % (timer()-startTime))


plt.stem(x)
fig=plt.figure()
plt.stem(X1)
plt.stem(X2)

plt.show()
