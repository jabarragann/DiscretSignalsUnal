# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:12:44 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import numpy as np
import matplotlib.pylab as plt
import padasip as pa 
from scipy import signal 

#orden del filtro 
N=101
#Frecuencia de corte 
FL=700;FH=1200
#Frecuencia de muestreo 
FS=8000
TS=1/FS


#Calculo coeficientes
temp= int( (N-1)/2 )

hCoeff=np.zeros(N)

#Calcular ventana-arange no incluye el final del intervalo especìfícado
window=0.54+0.46*np.cos(2*np.pi*np.arange(-temp,temp+1)/(N-1))

for i in range(1,temp+1):
    
    hCoeff[temp+i] = ( np.sin(2*np.pi*i*FH/FS) - np.sin(2*np.pi*i*FL/FS) )/(np.pi*i)
    hCoeff[temp-i] = hCoeff[temp+i]
    
hCoeff[temp]=2*FH/FS-2*FL/FS

hCoeff=hCoeff*window

#Respuesta en frecuencia
w, h = signal.freqz(hCoeff)
f = FS*w/(2*np.pi)


#generate input
t=np.linspace(0,8*np.pi,1000)
xin=np.sin(t)
noise=np.random.normal(0,1,1000)
xin=xin+noise
xin=xin/max(xin)

dout=signal.lfilter(hCoeff,[1.0],xin)



# these two function supplement your online measurment
def measure_x():
    # it produces input vector of size 3
    x = np.random.random(1)
    return x
    
def measure_d(dout,k):
    # meausure system output
    d =dout[k] # + 1*x[1] - 1.5*x[2]
    return d
    
N = 1000
log_d = np.zeros(N)
log_y = np.zeros(N)
filt = pa.filters.FilterLMS(1, mu=0.4)
for k in range(N):
    # measure input
    x = xin[k]#measure_x()
    # predict new value
    y = filt.predict(x)
    # do the important stuff with prediction output
    pass    
    # measure output
    d = measure_d(dout,k)
    # update filter
    filt.adapt(d, x)
    # log values
    log_d[k] = d
    log_y[k] = y
    
### show results
plt.figure(figsize=(15,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("samples - k")
plt.plot(log_d,"b", label="d - target")
plt.plot(log_y,"g", label="y - output");plt.legend()
plt.subplot(212);plt.title("Filter error");plt.xlabel("samples - k")
plt.plot(10*np.log10((log_d-log_y)**2),"r", label="e - error [dB]")
plt.legend(); plt.tight_layout(); plt.show()
plt.tight_layout()