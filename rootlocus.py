import numpy as np
import matplotlib.pyplot as plt
import control as cnt

G = cnt.tf([1],[1,4,3,0])
cnt.rlocus(G, xlim = (-4,1), ylim = (-2,2))
plt.grid()
plt.show()
