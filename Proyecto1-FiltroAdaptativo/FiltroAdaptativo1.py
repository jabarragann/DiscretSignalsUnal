# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:01:51 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


import Plotter
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 
import padasip as pa 


#Diseño de un filtro pasabandas de orden N con frecuencia de corte de FL HZ

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

#Generate Input
t=np.linspace(0,8*np.pi,1000)
x=np.sin(t)
noise=np.random.normal(0,1,1000)
x=x+noise
x=x/max(x)

d=signal.lfilter(hCoeff,[1.0],x)

# identification
f = pa.filters.FilterLMS(n=N, mu=0.4, w="random")
y, e, w = f.run(d, x)

#######Plotting functions#########
fig,ax =plt.subplots(3)

#graficar coeficientes
Plotter.myPlotter(ax[0],np.arange(0,len(hCoeff),1),hCoeff,stem=True)
#Graficar respuesta en frecuencia
Plotter.myPlotter(ax[1],t,x)
Plotter.myPlotter(ax[2],t,d)

Plotter.myPlotterShow(fig)