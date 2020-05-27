#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 02:06:22 2020

@author: krati
"""

import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('./ee18btech11050.dat')  
plt.plot(data[:,0],data[:,1])  
plt.xlim(72, 80)
plt.grid()
plt.xlabel("time")
plt.ylabel("oscillating response")
plt.title("Output from spice simulation")

#if using termux
plt.savefig('./figs/ee18btech11050/ee18btech11050_sim.pdf')
plt.savefig('./figs/ee18btech11050/ee18btech11050_sim.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_spice.pdf"))
#else
plt.show()