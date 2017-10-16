#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 27 11:24:45 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import sounddevice  as sd
import matplotlib.pyplot as plt
import Plotter as mp
import numpy as np


#Generate, plot and play a tone 
'''
FS=8000
f=440*2
n=np.arange(8000*4)
x=np.sin(2*np.pi*f*n/FS)

plt.plot(x[:500])
sd.play(x,FS)
'''


#Recording a sound
FS=8000
duration = 4  # seconds

myrecording = sd.rec(int(duration * FS), samplerate=FS, channels=1)

#Wait until recording is finished
sd.wait()


fig,axes =plt.subplots(1)
mp.myPlotterShow(fig)
mp.myPlotter(axes,np.arange(len(myrecording)),myrecording)

sd.play(myrecording*5,FS)


print("Finished")
