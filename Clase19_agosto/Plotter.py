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
    ax.grid(b=True)
    if stem:
        out = ax.stem(data1, data2, **param_dict)
    else:    
        out = ax.plot(data1, data2, **param_dict)
    
    return out

def myPlotterShow(fig):
    #fig.canvas.mpl_connect('key_press_event', keyStrokeQuit)
    fig.canvas.mpl_connect('key_press_event', lambda event: keyStrokeQuit(event, fig) )
    plt.show()
    plt.pause(1e-9)
    fig.canvas.manager.window.activateWindow()
    fig.canvas.manager.window.raise_()
    fig.canvas.manager.window.move(500,300)
    fig.set_size_inches(10, 12)
        


