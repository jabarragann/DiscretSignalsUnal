#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:40:23 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""


#import Plotter
#Plotter.IPythonReset()

import Plotter
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 


#Diseño de un filtro pasabajas de orden N con frecuencia de corte de FL HZ

#orden del filtro 
N=101
#Frecuencia de corte 
FL=500
#Frecuencia de muestreo 
FS=8000
TS=1/FS


#Calculo coeficientes
temp= int( (N-1)/2 )

hCoeff=np.zeros(N)

#Calcular ventana-arange no incluye el final del intervalo especìfícado
window=0.54+0.46*np.cos(2*np.pi*np.arange(-temp,temp+1)/(N-1))

for i in range(1,temp+1):
    
    hCoeff[temp+i] = np.sin(2*np.pi*i*FL/FS)/(np.pi*i)
    hCoeff[temp-i] = hCoeff[temp+i]
    
hCoeff[temp]=2*FL/FS

hCoeff=hCoeff*window

#Respuesta en frecuencia
w, h = signal.freqz(hCoeff)
f = FS*w/(2*np.pi)

#Generar senal seno para comprobar el funcionamiento del filtro
f0=200

n=np.arange(0,100,1)
t=n*TS
x=np.sin(2*np.pi*f0*t)

#filtrar la señal
y=signal.lfilter(hCoeff,[1.0],x)


#Crear Graficas de la simulación
fig,ax =plt.subplots(3)

#graficar coeficientes
Plotter.myPlotter(ax[0],np.arange(0,len(hCoeff),1),hCoeff,stem=True)
#Graficar respuesta en frecuencia
Plotter.myPlotter(ax[1],f,abs(h))
#Graficar señal de entrada y salida del filtro
Plotter.myPlotter(ax[2],t,x,{'color':'blue'})
Plotter.myPlotter(ax[2],t,y,{'color':'green'})

Plotter.myPlotterShow(fig)

