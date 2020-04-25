#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:16:36 2020

@author: krati
"""

from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

s2 = signal.lti([1781.558],[1,27,207,405])

w2, mag2, phase2 = signal.bode(s2)

plt.figure()

plt.subplot(2,1,1)
plt.text(8.09623,0, '({}, {})'.format(8.09623,0))
plt.axhline(y = 0,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 8.09623,ymin=0,color='k',linestyle='dashed')
plt.semilogx(w2, mag2)    # Bode magnitude plot
plt.title('Magnitude Plot')
plt.grid()


plt.subplot(2,1,2)
plt.text(8.09623,-140, '({}, {})'.format(8.09623,-140))
plt.axhline(y = -140,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 8.09623,ymin=0,color='k',linestyle='dashed')
plt.semilogx(w2, phase2)  # Bode phase plot
plt.title('Phase Plot')
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11050/ee18btech11050_2.pdf')
plt.savefig('./figs/ee18btech11050/ee18btech11050_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11050/ee18btech11050_2.pdf"))
#else
#plt.show()
