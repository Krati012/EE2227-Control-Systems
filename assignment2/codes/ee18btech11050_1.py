#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26, 21:06:20 2020

@author: krati
"""
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#if using termux
import subprocess
import shlex
#end if

zeros = []  #zeros of transfer function
poles = [0,-3,-6] #poles of tf

H_s = signal.ZerosPolesGain(zeros, poles, [50])  #feed zeros and poles as inputs to this function to get H_s
omega= np.linspace(-100, 100,20000) #range of values over which H is taken

w, H = signal.freqresp(H_s, w=omega)   #this function returns frequency response H of H_s

plt.plot(H.real, H.imag, )
plt.ylabel("${Im}\{G(s)\}$")
plt.title("NYQUIST PLOT")
plt.xlabel("${Re}\{G(s)\}$")
plt.grid()
plt.xlim(-1.6, 0.2)
plt.ylim(-700, 700)

#if using termux
plt.savefig('./figs/ee18btech11050_1.eps')
plt.savefig('./figs/ee18btech11050_1.pdf')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11050_1.pdf"))
#else
#plt.show()
