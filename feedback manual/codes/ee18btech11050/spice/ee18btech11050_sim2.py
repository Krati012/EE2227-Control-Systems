#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:10:32 2020

@author: krati
"""

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11050.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.xlim(78.9,78.93)
x1 = 78.908846
x2 = 78.91131

plt.plot([78.9,78.93],[0,0],'r--',lw=1,label ='0V')
plt.plot(x1,0,'o')
plt.plot(x2,0,'o')
plt.legend(loc = 'upper right', frameon = True)
plt.grid()
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from spice simulation')

T = x2 - x1
f = 1/T
print("Frequency is:",f)
print("Amplitude is:",max(data[:,1]))

#if using termux
plt.savefig('./figs/ee18btech11050/ee18btech11050_sim2.pdf')
plt.savefig('./figs/ee18btech11050/ee18btech11050_sim2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_spice2.pdf"))
#else
plt.show()
