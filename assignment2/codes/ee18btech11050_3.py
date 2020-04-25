#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:01:33 2020

@author: krati
"""

import matplotlib.pyplot as plt
import numpy as np
import control

#if using termux
import subprocess
import shlex
#end if

k = (928.035)

T = control.TransferFunction([k],[1,27,207,405+k])
U = control.TransferFunction([1],[1,0])
Y = T*U
t = np.linspace(0,5,100)
t, y =control.impulse_response(Y,t)
y = np.array(y)

ymax = np.amax(y)
ysteady = y[-1]

print(ymax/ysteady)
for i in range(len(t)):
    if(y[i]==(1.2000000398067896)*ysteady):
        tp = t[i]
        print("tp: ", tp)
        break
ysteady
plt.plot(t,y)
plt.text(tp+0.2,ysteady+0.05, '(ymax=0.83542)')
#plt.text(tp+0.2,0, '(tp={})'.format(0.50505))
plt.axhline(y = ysteady,xmin=0,color = 'g',linestyle='dashed')
plt.axvline(x = tp, ymin=0, color='k',linestyle='dashed')
plt.grid()
plt.xlabel('time')
plt.ylabel('y(t)')
plt.title('Response of system to unit step')

#if using termux
plt.savefig('./figs/ee18btech11050/ee18btech11050_3.pdf')
plt.savefig('./figs/ee18btech11050/ee18btech11050_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_2.pdf"))
#else
#plt.show()

