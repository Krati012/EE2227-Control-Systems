#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:50:06 2020

@author: krati 
"""
import numpy as np
#from scipy import signal
import control

num = np.array([1,5])
den = np.array([1,3,3,2,1])

H = control.tf(num,den)

n = np.size(den)

if (den[0] < 0):
    den = den*-1

A = np.zeros((n,int((n+1)/2)))

i = 0
while(2*i<n):
    A[0][i] = den[2*i]
    i += 1
j = 0
while((2*j)+1<n):
    A[1][j] = den[2*j+1]
    j += 1
    
i = 2
while(i<n):
    j = 0
    while(j<int(((n+1)/2)-1)):
        A[i][j] = ((A[i-1][0]*A[i-2][j+1])-(A[i-2][0]*A[i-1][j+1]))/A[i-1][0]
        j += 1
    i += 1

stab = True
for i in range(n):
    if(A[i][0]<0):
        stab = False
 
print(A)       
if stab:
    print("System is stable")
else:
    print("System is unstable")