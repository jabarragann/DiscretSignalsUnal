#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:15:43 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

from IPython import get_ipython
import matplotlib.pyplot as plt


def IPythonReset():
    get_ipython().magic('reset -sf')
    get_ipython().magic('clear')
    #get_ipython().magic('matplotlib qt')

def keyStrokeQuit(event,fig):
    print('press', event.key)
    if event.key=='q':
        plt.close(fig)

'''
myPlotter example syntax
myPlotter(ax[1],[0,1,2],[1,2,3],{'color':'green'},stem=True)
'''
def myPlotter(ax, data1, data2, param_dict={'color':'blue'},stem=False):
    ax.grid(True)
    if stem:
        markerline, stemlines, baseline = ax.stem(data1, data2, **param_dict)
        plt.setp(stemlines, linestyle='dotted', linewidth=3)
        plt.setp(stemlines, **param_dict)
        plt.setp(markerline, **param_dict)
        out=markerline
    
    else:    
        out = ax.plot(data1, data2, **param_dict)
        
    return out

def myPlotterBode(ax0,ax1, omega, mag,phase, param_dict={'color':'blue'}):
    ax0.grid(b=True,which='both')
    ax1.grid(b=True,which='both')
    out1 = ax0.semilogx(omega,mag, **param_dict)
    out2 = ax1.semilogx(omega,phase, **param_dict)    
    print("Hello")
    return out1,out2

def myPlotterBodeLabels(ax0,ax1):
    ax1.set_xlabel("Frequency (rad/sec)", fontsize=12)
    ax0.set_ylabel("Magnitude(dB)", fontsize=12)
    ax1.set_ylabel("Phase(deg)", fontsize=12)
    
    return ax0,ax1

def myPlotterShow(fig):
    #fig.canvas.mpl_connect('key_press_event', keyStrokeQuit)
    fig.canvas.mpl_connect('key_press_event', lambda event: keyStrokeQuit(event, fig) )
    plt.show()
    plt.pause(1e-9)
    fig.canvas.manager.window.activateWindow()
    fig.canvas.manager.window.raise_()
    fig.canvas.manager.window.move(300,0)
    fig.set_size_inches(8, 8)
