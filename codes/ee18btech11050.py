#import numpy as np
import matplotlib.pyplot as plt
import control as cnt

G1 = cnt.tf([1],[1,4,3,0])
cnt.rlocus(G1, xlim = (-4,1), ylim = (-3,3))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

plt.savefig('./figs/ee18btech11050.pdf')
