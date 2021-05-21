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
t = np.arange(0, 10, 0.01)
M0,x0,vx0,y0,vy0=1,1.0,-0.0,0.0,1.0
M1,x1,vx1,y1,vy1=1,0.30901699437494745,-0.9510565162951535,0.9510565162951535,0.30901699437494745
M2,x2,vx2,y2,vy2=1,-0.8090169943749473,-0.5877852522924732,0.5877852522924732,-0.8090169943749473
M3,x3,vx3,y3,vy3=1,-0.8090169943749475,0.587785252292473,-0.587785252292473,-0.8090169943749475
M4,x4,vx4,y4,vy4=1,0.30901699437494723,0.9510565162951536,-0.9510565162951536,0.30901699437494723

params=[M0, M1, M2, M3, M4, f1]
def f(y, t, params):
   vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4=y
   M0, M1, M2, M3, M4,f1=params
   return[
       f1*M1*(x1-x0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(x2-x0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(x3-x0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(x4-x0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3,
       f1*M1*(y1-y0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(y2-y0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(y3-y0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(y4-y0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3,
       f1*M0*(x0-x1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(x2-x1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(x3-x1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(x4-x1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3,
       f1*M0*(y0-y1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(y2-y1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(y3-y1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(y4-y1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3,
       f1*M0*(x0-x2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(x1-x2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(x3-x2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(x4-x2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3,
       f1*M0*(y0-y2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(y1-y2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(y3-y2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(y4-y2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3,
       f1*M0*(x0-x3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(x1-x3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(x2-x3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(x4-x3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3,
       f1*M0*(y0-y3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(y1-y3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(y2-y3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(y4-y3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3,
       f1*M0*(x0-x4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(x1-x4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(x2-x4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(x3-x4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3,
       f1*M0*(y0-y4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(y1-y4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(y2-y4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(y3-y4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3,
       vx0,
       vy0,
       vx1,
       vy1,
       vx2,
       vy2,
       vx3,
       vy3,
       vx4,
       vy4
       ]
y0=[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4]
[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4]= odeint(f, y0, t, args=(params,), full_output=False).T
c1=M0*(x0*vy0-y0*vx0)+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)+M3*(x3*vy3-y3*vx3)+M4*(x4*vy4-y4*vx4)
U=f1*(M0*M1/(np.sqrt((x1-x0)**2+(y1-y0)**2))) + f1*(M0*M2/(np.sqrt((x0-x2)**2+(y0-y2)**2))) + f1*(M0*M3/(np.sqrt((x0-x3)**2+(y0-y3)**2))) + f1*(M0*M4/(np.sqrt((x0-x4)**2+(y0-y4)**2))) + f1*(M1*M2/(np.sqrt((x1-x2)**2+(y1-y2)**2))) + f1*(M1*M3/(np.sqrt((x1-x3)**2+(y1-y3)**2))) + f1*(M1*M4/(np.sqrt((x1-x4)**2+(y1-y4)**2))) + f1*(M2*M3/(np.sqrt((x2-x3)**2+(y2-y3)**2))) + f1*(M2*M4/(np.sqrt((x2-x4)**2+(y2-y4)**2))) + f1*(M3*M4/(np.sqrt((x3-x4)**2+(y3-y4)**2)))
H=M0/2*(vy0**2+vx0**2) +M1/2*(vy1**2+vx1**2) +M2/2*(vy2**2+vx2**2) +M3/2*(vy3**2+vx3**2) +M4/2*(vy4**2+vx4**2)-U
HH=H[0]/H
CC=c1[0]/c1
text_filec0 = open('Nbody/Coords/coord0_NumOne.txt', 'w')
text_files0=open('Nbody/Coords/speed0_NumOne.txt', 'w')
text_filec1 = open('Nbody/Coords/coord1_NumOne.txt', 'w')
text_files1=open('Nbody/Coords/speed1_NumOne.txt', 'w')
text_filec2 = open('Nbody/Coords/coord2_NumOne.txt', 'w')
text_files2=open('Nbody/Coords/speed2_NumOne.txt', 'w')
text_filec3 = open('Nbody/Coords/coord3_NumOne.txt', 'w')
text_files3=open('Nbody/Coords/speed3_NumOne.txt', 'w')
text_filec4 = open('Nbody/Coords/coord4_NumOne.txt', 'w')
text_files4=open('Nbody/Coords/speed4_NumOne.txt', 'w')
for i in range(len(x0)):
   text_filec0.write(str(x0[i])+';'+str(y0[i])+'\n')
   text_files0.write(str(vx0[i])+';'+str(vy0[i])+'\n')
   text_filec1.write(str(x1[i])+';'+str(y1[i])+'\n')
   text_files1.write(str(vx1[i])+';'+str(vy1[i])+'\n')
   text_filec2.write(str(x2[i])+';'+str(y2[i])+'\n')
   text_files2.write(str(vx2[i])+';'+str(vy2[i])+'\n')
   text_filec3.write(str(x3[i])+';'+str(y3[i])+'\n')
   text_files3.write(str(vx3[i])+';'+str(vy3[i])+'\n')
   text_filec4.write(str(x4[i])+';'+str(y4[i])+'\n')
   text_files4.write(str(vx4[i])+';'+str(vy4[i])+'\n')
Hfile=open('Nbody/Coords/H_NumOne.txt', 'w')
Cfile=open('Nbody/Coords/C_NumOne.txt', 'w')
for i in range(len(t)):
   Hfile.write(str(round(t[i],3))+';'+str(round(HH[i],3))+'\n')
   Cfile.write(str(round(t[i],3))+';'+str(round(CC[i],3))+'\n')
text_filec0.close()
text_files0.close()
text_filec1.close()
text_files1.close()
text_filec2.close()
text_files2.close()
text_filec3.close()
text_files3.close()
text_filec4.close()
text_files4.close()
Hfile.close()
Cfile.close()
