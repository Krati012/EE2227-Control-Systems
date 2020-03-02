#import numpy as np
import matplotlib.pyplot as plt
import control as cnt

g2 = cnt.tf([1],[1,3,0])
cnt.rlocus(g2, xlim = (-4,1), ylim = (-2,2))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

g3 = cnt.tf([1,3],[1,-1,-2])
cnt.rlocus(g3, xlim = (-7,1), ylim = (-5,5))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

g4 = cnt.tf([1,1],[1,4,6,4])
cnt.rlocus(g4, xlim = (-4,1), ylim = (-4,4))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

g5 = cnt.tf([1,2,2],[1,9,33,51,26,0])
cnt.rlocus(g5, xlim = (-4,1), ylim = (-5,5))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

G1 = cnt.tf([1],[1,4,3,0])
cnt.rlocus(G1, xlim = (-4,1), ylim = (-3,3))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.show()

