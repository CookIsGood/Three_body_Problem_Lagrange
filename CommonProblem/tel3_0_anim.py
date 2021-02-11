import numpy as np
import math as math
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import sympy as sym
from sympy import Symbol
from sympy import simplify
from sympy import re
from sympy.solvers import solve
import matplotlib.animation as animation
from celluloid import Camera

f1=1
M0= 1.9885*10**8
M1= M0/332940
M2= M1*317.8
t = np.linspace(0, 2, 101)
# t = t / np.sqrt(f1)


params = [M0, M1, M2,f1]


def f(y, t, params):
    vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2= y
    M0,M1,M2, f1 = params
    return [f1*M1*(x1-x0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(x2-x0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3,
            f1*M1*(y1-y0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(y2-y0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3,
            f1 * M0 * (x0 - x1) / (np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)) ** 3 + f1 * M2 * (x2 - x1) / (
                np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 3,
            f1 * M0 * (y0 - y1) / (np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)) ** 3 + f1 * M2 * (y2 - y1) / (
                np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 3,
            f1 * M0 * (x0 - x2) / (np.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)) ** 3 + f1 * M1 * (x1 - x2) / (
                np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3,
            f1 * M0 * (y0 - y2) / (np.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)) ** 3 + f1 * M1 * (y1 - y2) / (
                np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3,
            vx0,
            vy0,
            vx1,
            vy1,
            vx2,
            vy2
            ]

#x = Symbol('x')
#DX = 0
#Y = 0
#X = 3
#ert = simplify(
 #       (x ** 2 + DX ** 2 - 2 * k / sym.sqrt(Y ** 2 + X ** 2)) * (X * x - Y * DX) ** 2 + k ** 2 * (1 - e ** 2))
#print(ert)
#result = solve(ert,
 #                  x)
#pir = result[0]


x1=133.97685159
y1=0
vx1=0
vy1=1492.79519281
x2=-133.902558073980
y2=1.63983339142942e-14
vx2=-1.82713310151027e-13
vy2=-1491.96740054552
vx0=-vx2*M2/M0
vy0=-vy1*M1/M0
x0=-x1*M1/M0
y0=-y2*M2/M0


y0 = [vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2]
[vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2] = odeint(f, y0, t, args=(params,), full_output=False).T
c=M0*(x0*vy0-y0*vx0)+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)
U=f1*(M0*M1/((np.sqrt((x1-x0)**2+(y1-y0)**2)))+M0*M2/((np.sqrt((x2-x0)**2+(y2-y0)**2)))+M2*M1/((np.sqrt((x1-x2)**2+(y1-y2)**2))))
H=M0/2*(vy0**2+vx0**2)+M1/2*(vy1**2+vx1**2)+M2/2*(vy2**2+vx2**2)-U
print(c)
print(U)
print(H)
#plt.plot(x1, y1, linewidth=1, color='red')

fig = plt.figure()
ax_1 = fig.add_subplot(111)
camera = Camera(fig)

for i in range(len(t)):
    #plt.plot([i] * 10)
    pc1 = plt.Circle((x0[i], y0[i]), 0.1, fc='black')
    pc2= plt.Circle((x1[i], y1[i]), 5, fc='red')
    pc3=plt.Circle((x2[i], y2[i]), 5, fc='blue')
    plt.plot((x0[i], x1[i], x2[i], x0[i]), (y0[i], y1[i], y2[i], y0[i]), linewidth=1, color='magenta')
    ax_1.add_patch(pc1)
    ax_1.add_patch(pc2)
    ax_1.add_patch(pc3)
    plt.plot(x1, y1, linewidth=1, color='red')
    plt.plot(x2, y2, linewidth=1, color='blue')
    plt.plot(x0, y0, linewidth=1, color='black')
    camera.snap()
animation = camera.animate()
#animation.save('celluloid_minimal.gif')
plt.grid(True)
plt.axis('scaled')
plt.show()
