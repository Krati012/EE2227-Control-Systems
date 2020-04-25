#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:26:24 2020

@author: krati
"""

from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

s1 = signal.lti([16.406],[1,27,207,405])

w1, mag1, phase1 = signal.bode(s1)

plt.figure()

plt.subplot(2,1,1)
plt.text(14.38,-50, '({}, {})'.format(14.38,-50))
plt.axhline(y = -50,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 14.38,ymin=0,color='k',linestyle='dashed')
plt.semilogx(w1, mag1)    # Bode magnitude plot
plt.title('Magnitude Plot')
plt.grid()

plt.subplot(2,1,2)
plt.text(14.38,-180, '({}, {})'.format(14.38,-180))
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 14.38,ymin=0,color='k',linestyle='dashed')
plt.semilogx(w1, phase1)  # Bode phase plot
plt.title('Phase Plot')
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11050/ee18btech11050_1.pdf')
plt.savefig('./figs/ee18btech11050/ee18btech11050_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11050/ee18btech11050_1.pdf"))
#else
#plt.show()
