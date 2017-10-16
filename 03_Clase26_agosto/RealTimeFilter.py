# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:28:01 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


import sounddevice as sd
import queue
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Plotter as mp
from scipy import signal 

#online Filter
class FIR_loop():
    def __init__(self, h):
        self.h = h
        self.ix = 0
        self.M = len(h)
        self.buf = np.zeros(self.M)

    def filter(self, x):
        y = 0
        self.buf[self.ix] = x
        for n in range(0, self.M):
            y += self.h[n] * self.buf[(self.ix+self.M-n) % self.M]
        self.ix = (self.ix + 1) % self.M
        return y

#Sound stream Variables
q=queue.Queue() 
duration = 5.5  # seconds
FS=8000

#Animation Variables
plt.ion()
fig, ax = plt.subplots(2)
ax[0].grid()
xdata=np.arange(4000)
ydata=np.zeros(4000)
ln1, = ax[0].plot(xdata, ydata, animated=True)
ln2, = ax[1].plot(xdata, ydata)

#Bandpass filter variables
N=71           #Orden del filtro
FL=200;FH=1000   #Frecuencias de corte 
TS=1/FS         #Periodo de muestreo 

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
mp.myPlotter(ax[1],f,abs(h))

fir_loop1 = FIR_loop(hCoeff)


#Main
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    for i in range(len(indata)):    
        outdata[i] =  fir_loop1.filter(indata[i])
    
    q.put(outdata[:])
    
def init():
    ax[0].set_xlim(1200, 1400)
    ax[0].set_ylim([-0.2,0.2])
    return ln1,

def update(frame):    
    if not q.empty():
        dataBlock=q.get_nowait()
        index=0
        for data1 in dataBlock:
            ydata[frame*100+index]=data1
            index+=1
            
    ln1.set_data(xdata, ydata)
    return ln1,

try:
    stream=sd.Stream(samplerate=FS,channels=1,blocksize=100, callback=callback)
    ani = FuncAnimation(fig, update, frames=40,init_func=init,  interval=10,blit=True)
    mp.myPlotterStreamShow(fig,stream)
    plt.show()
    stream.start()
     
except Exception as e:
    stream.stop()
    print(e)
