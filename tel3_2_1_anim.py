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
from celluloid import Camera
f1=1
M0= 1.9885*10**8
M1= M0/332940
M2= M1*31711.8
#M0=1.9885*10**8
#M1=M0/332940
#M2=M1*317.8
M=M0+M1+M2
c=200000
po=c**2/(f1*M)
e=0
p= po/(1+e) #1000
phi=math.pi/3
#w=c/p**2
vp=0
F=0
params = [M0, M1, M2,f1,c]
t = np.linspace(0, 2, 101)
def f(y, t, params):
    vp,p,F= y
    M0,M1,M2, f1,c = params
    return [((c/(p**2))**2)*p-f1*(M0+M1+M2)/p**2,
            vp,
            c/(p**2)
            ]




y0 = [vp,p,F]
[vp,p,F] = odeint(f, y0, t, args=(params,), full_output=False).T
a11=np.cos(F)
a12=-np.sin(F)
a21=np.sin(F)
a22=np.cos(F)
x1=a11*p
y1=a21*p
x2=a11*p*np.cos(phi)+a12*p*np.sin(phi)
y2=a21*p*np.cos(phi)+a22*p*np.sin(phi)

xx0=-M1/M*x1-M2/M*x2
xx1=(M2+M0)/M*x1-M2/M*x2
xx2=-M1/M*x1+(M1+M0)/M*x2
yy0=-M1/M*y1-M2/M*y2
yy1=(M2+M0)/M*y1-M2/M*y2
yy2=-M1/M*y1+(M1+M0)/M*y2
print(np.sqrt((xx1-xx2)**2+(yy1-yy2)**2))
print(np.sqrt((xx0-xx2)**2+(yy0-yy2)**2))
print(np.sqrt((xx1-xx0)**2+(yy1-yy0)**2))
#стоп при неравных сторонах
fig = plt.figure()
ax_1 = fig.add_subplot(111)
camera = Camera(fig)

for i in range(len(t)):
    #plt.plot([i] * 10)
    pc1 = plt.Circle((xx0[i], yy0[i]), 1, fc='black')
    pc2= plt.Circle((xx1[i], yy1[i]), 1, fc='red')
    pc3=plt.Circle((xx2[i], yy2[i]), 1, fc='blue')
    ax_1.plot((xx0[i], xx1[i], xx2[i], xx0[i]), (yy0[i], yy1[i], yy2[i], yy0[i]), linewidth=1, color='magenta')
    ax_1.add_patch(pc1)
    ax_1.add_patch(pc2)
    ax_1.add_patch(pc3)
    ax_1.plot(xx1, yy1, linewidth=1, color='red')
    ax_1.plot(xx2, yy2, linewidth=1, color='blue')
    ax_1.plot(xx0, yy0, linewidth=1, color='black')
    camera.snap()
animation = camera.animate()
#animation.save('celluloid_minimal.gif')
ax_1.grid(True)
#plt.axis('scaled')
plt.show()



