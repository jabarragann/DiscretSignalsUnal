#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:46:16 2017

@author: santi
"""



'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y)

y2 = np.cos(x)
ax.plot(x, y2)

ax.set_ylim(-1.5, 2.0)

ax.legend(['sine', 'cosine'])



ax.set_xlabel("$x$")
ax.set_ylabel("$\sin(x)$")
ax.set_title("I like $\pi$")

plt.show()

'''

'''
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

fig = plt.figure()
plt.plot(t,s)
plt.draw()
plt.waitforbuttonpress(0) # this will wait for indefinite time
plt.close(fig)

'''
'''
#from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt


def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
    elif event.key=='q':
        plt.close(fig)

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()

'''