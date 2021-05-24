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
M0,x0,vx0,y0,vy0=1,1.5,-0.0,0.0,1.5
M1,x1,vx1,y1,vy1=1,1.2135254915624212,-0.8816778784387097,0.8816778784387097,1.2135254915624212
M2,x2,vx2,y2,vy2=1,0.4635254915624212,-1.4265847744427302,1.4265847744427302,0.4635254915624212
M3,x3,vx3,y3,vy3=1,-0.463525491562421,-1.4265847744427305,1.4265847744427305,-0.463525491562421
M4,x4,vx4,y4,vy4=1,-1.213525491562421,-0.8816778784387098,0.8816778784387098,-1.213525491562421
M5,x5,vx5,y5,vy5=1,-1.5,-1.8369701987210297e-16,1.8369701987210297e-16,-1.5
M6,x6,vx6,y6,vy6=1,-1.2135254915624212,0.8816778784387096,-0.8816778784387096,-1.2135254915624212
M7,x7,vx7,y7,vy7=1,-0.46352549156242134,1.4265847744427302,-1.4265847744427302,-0.46352549156242134
M8,x8,vx8,y8,vy8=1,0.46352549156242084,1.4265847744427305,-1.4265847744427305,0.46352549156242084
M9,x9,vx9,y9,vy9=1,1.213525491562421,0.88167787843871,-0.88167787843871,1.213525491562421

params=[M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, f1]
def f(y, t, params):
   vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9=y
   M0, M1, M2, M3, M4, M5, M6, M7, M8, M9,f1=params
   return[
       f1*M1*(x1-x0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(x2-x0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(x3-x0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(x4-x0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3 + f1*M5*(x5-x0)/(np.sqrt((x5-x0)**2+(y5-y0)**2))**3 + f1*M6*(x6-x0)/(np.sqrt((x6-x0)**2+(y6-y0)**2))**3 + f1*M7*(x7-x0)/(np.sqrt((x7-x0)**2+(y7-y0)**2))**3 + f1*M8*(x8-x0)/(np.sqrt((x8-x0)**2+(y8-y0)**2))**3 + f1*M9*(x9-x0)/(np.sqrt((x9-x0)**2+(y9-y0)**2))**3,
       f1*M1*(y1-y0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(y2-y0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(y3-y0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(y4-y0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3 + f1*M5*(y5-y0)/(np.sqrt((x5-x0)**2+(y5-y0)**2))**3 + f1*M6*(y6-y0)/(np.sqrt((x6-x0)**2+(y6-y0)**2))**3 + f1*M7*(y7-y0)/(np.sqrt((x7-x0)**2+(y7-y0)**2))**3 + f1*M8*(y8-y0)/(np.sqrt((x8-x0)**2+(y8-y0)**2))**3 + f1*M9*(y9-y0)/(np.sqrt((x9-x0)**2+(y9-y0)**2))**3,
       f1*M0*(x0-x1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(x2-x1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(x3-x1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(x4-x1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3 + f1*M5*(x5-x1)/(np.sqrt((x5-x1)**2+(y5-y1)**2))**3 + f1*M6*(x6-x1)/(np.sqrt((x6-x1)**2+(y6-y1)**2))**3 + f1*M7*(x7-x1)/(np.sqrt((x7-x1)**2+(y7-y1)**2))**3 + f1*M8*(x8-x1)/(np.sqrt((x8-x1)**2+(y8-y1)**2))**3 + f1*M9*(x9-x1)/(np.sqrt((x9-x1)**2+(y9-y1)**2))**3,
       f1*M0*(y0-y1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(y2-y1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(y3-y1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(y4-y1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3 + f1*M5*(y5-y1)/(np.sqrt((x5-x1)**2+(y5-y1)**2))**3 + f1*M6*(y6-y1)/(np.sqrt((x6-x1)**2+(y6-y1)**2))**3 + f1*M7*(y7-y1)/(np.sqrt((x7-x1)**2+(y7-y1)**2))**3 + f1*M8*(y8-y1)/(np.sqrt((x8-x1)**2+(y8-y1)**2))**3 + f1*M9*(y9-y1)/(np.sqrt((x9-x1)**2+(y9-y1)**2))**3,
       f1*M0*(x0-x2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(x1-x2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(x3-x2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(x4-x2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3 + f1*M5*(x5-x2)/(np.sqrt((x5-x2)**2+(y5-y2)**2))**3 + f1*M6*(x6-x2)/(np.sqrt((x6-x2)**2+(y6-y2)**2))**3 + f1*M7*(x7-x2)/(np.sqrt((x7-x2)**2+(y7-y2)**2))**3 + f1*M8*(x8-x2)/(np.sqrt((x8-x2)**2+(y8-y2)**2))**3 + f1*M9*(x9-x2)/(np.sqrt((x9-x2)**2+(y9-y2)**2))**3,
       f1*M0*(y0-y2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(y1-y2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(y3-y2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(y4-y2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3 + f1*M5*(y5-y2)/(np.sqrt((x5-x2)**2+(y5-y2)**2))**3 + f1*M6*(y6-y2)/(np.sqrt((x6-x2)**2+(y6-y2)**2))**3 + f1*M7*(y7-y2)/(np.sqrt((x7-x2)**2+(y7-y2)**2))**3 + f1*M8*(y8-y2)/(np.sqrt((x8-x2)**2+(y8-y2)**2))**3 + f1*M9*(y9-y2)/(np.sqrt((x9-x2)**2+(y9-y2)**2))**3,
       f1*M0*(x0-x3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(x1-x3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(x2-x3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(x4-x3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3 + f1*M5*(x5-x3)/(np.sqrt((x5-x3)**2+(y5-y3)**2))**3 + f1*M6*(x6-x3)/(np.sqrt((x6-x3)**2+(y6-y3)**2))**3 + f1*M7*(x7-x3)/(np.sqrt((x7-x3)**2+(y7-y3)**2))**3 + f1*M8*(x8-x3)/(np.sqrt((x8-x3)**2+(y8-y3)**2))**3 + f1*M9*(x9-x3)/(np.sqrt((x9-x3)**2+(y9-y3)**2))**3,
       f1*M0*(y0-y3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(y1-y3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(y2-y3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(y4-y3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3 + f1*M5*(y5-y3)/(np.sqrt((x5-x3)**2+(y5-y3)**2))**3 + f1*M6*(y6-y3)/(np.sqrt((x6-x3)**2+(y6-y3)**2))**3 + f1*M7*(y7-y3)/(np.sqrt((x7-x3)**2+(y7-y3)**2))**3 + f1*M8*(y8-y3)/(np.sqrt((x8-x3)**2+(y8-y3)**2))**3 + f1*M9*(y9-y3)/(np.sqrt((x9-x3)**2+(y9-y3)**2))**3,
       f1*M0*(x0-x4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(x1-x4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(x2-x4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(x3-x4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3 + f1*M5*(x5-x4)/(np.sqrt((x5-x4)**2+(y5-y4)**2))**3 + f1*M6*(x6-x4)/(np.sqrt((x6-x4)**2+(y6-y4)**2))**3 + f1*M7*(x7-x4)/(np.sqrt((x7-x4)**2+(y7-y4)**2))**3 + f1*M8*(x8-x4)/(np.sqrt((x8-x4)**2+(y8-y4)**2))**3 + f1*M9*(x9-x4)/(np.sqrt((x9-x4)**2+(y9-y4)**2))**3,
       f1*M0*(y0-y4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(y1-y4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(y2-y4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(y3-y4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3 + f1*M5*(y5-y4)/(np.sqrt((x5-x4)**2+(y5-y4)**2))**3 + f1*M6*(y6-y4)/(np.sqrt((x6-x4)**2+(y6-y4)**2))**3 + f1*M7*(y7-y4)/(np.sqrt((x7-x4)**2+(y7-y4)**2))**3 + f1*M8*(y8-y4)/(np.sqrt((x8-x4)**2+(y8-y4)**2))**3 + f1*M9*(y9-y4)/(np.sqrt((x9-x4)**2+(y9-y4)**2))**3,
       f1*M0*(x0-x5)/(np.sqrt((x0-x5)**2+(y0-y5)**2))**3 + f1*M1*(x1-x5)/(np.sqrt((x1-x5)**2+(y1-y5)**2))**3 + f1*M2*(x2-x5)/(np.sqrt((x2-x5)**2+(y2-y5)**2))**3 + f1*M3*(x3-x5)/(np.sqrt((x3-x5)**2+(y3-y5)**2))**3 + f1*M4*(x4-x5)/(np.sqrt((x4-x5)**2+(y4-y5)**2))**3 + f1*M6*(x6-x5)/(np.sqrt((x6-x5)**2+(y6-y5)**2))**3 + f1*M7*(x7-x5)/(np.sqrt((x7-x5)**2+(y7-y5)**2))**3 + f1*M8*(x8-x5)/(np.sqrt((x8-x5)**2+(y8-y5)**2))**3 + f1*M9*(x9-x5)/(np.sqrt((x9-x5)**2+(y9-y5)**2))**3,
       f1*M0*(y0-y5)/(np.sqrt((x0-x5)**2+(y0-y5)**2))**3 + f1*M1*(y1-y5)/(np.sqrt((x1-x5)**2+(y1-y5)**2))**3 + f1*M2*(y2-y5)/(np.sqrt((x2-x5)**2+(y2-y5)**2))**3 + f1*M3*(y3-y5)/(np.sqrt((x3-x5)**2+(y3-y5)**2))**3 + f1*M4*(y4-y5)/(np.sqrt((x4-x5)**2+(y4-y5)**2))**3 + f1*M6*(y6-y5)/(np.sqrt((x6-x5)**2+(y6-y5)**2))**3 + f1*M7*(y7-y5)/(np.sqrt((x7-x5)**2+(y7-y5)**2))**3 + f1*M8*(y8-y5)/(np.sqrt((x8-x5)**2+(y8-y5)**2))**3 + f1*M9*(y9-y5)/(np.sqrt((x9-x5)**2+(y9-y5)**2))**3,
       f1*M0*(x0-x6)/(np.sqrt((x0-x6)**2+(y0-y6)**2))**3 + f1*M1*(x1-x6)/(np.sqrt((x1-x6)**2+(y1-y6)**2))**3 + f1*M2*(x2-x6)/(np.sqrt((x2-x6)**2+(y2-y6)**2))**3 + f1*M3*(x3-x6)/(np.sqrt((x3-x6)**2+(y3-y6)**2))**3 + f1*M4*(x4-x6)/(np.sqrt((x4-x6)**2+(y4-y6)**2))**3 + f1*M5*(x5-x6)/(np.sqrt((x5-x6)**2+(y5-y6)**2))**3 + f1*M7*(x7-x6)/(np.sqrt((x7-x6)**2+(y7-y6)**2))**3 + f1*M8*(x8-x6)/(np.sqrt((x8-x6)**2+(y8-y6)**2))**3 + f1*M9*(x9-x6)/(np.sqrt((x9-x6)**2+(y9-y6)**2))**3,
       f1*M0*(y0-y6)/(np.sqrt((x0-x6)**2+(y0-y6)**2))**3 + f1*M1*(y1-y6)/(np.sqrt((x1-x6)**2+(y1-y6)**2))**3 + f1*M2*(y2-y6)/(np.sqrt((x2-x6)**2+(y2-y6)**2))**3 + f1*M3*(y3-y6)/(np.sqrt((x3-x6)**2+(y3-y6)**2))**3 + f1*M4*(y4-y6)/(np.sqrt((x4-x6)**2+(y4-y6)**2))**3 + f1*M5*(y5-y6)/(np.sqrt((x5-x6)**2+(y5-y6)**2))**3 + f1*M7*(y7-y6)/(np.sqrt((x7-x6)**2+(y7-y6)**2))**3 + f1*M8*(y8-y6)/(np.sqrt((x8-x6)**2+(y8-y6)**2))**3 + f1*M9*(y9-y6)/(np.sqrt((x9-x6)**2+(y9-y6)**2))**3,
       f1*M0*(x0-x7)/(np.sqrt((x0-x7)**2+(y0-y7)**2))**3 + f1*M1*(x1-x7)/(np.sqrt((x1-x7)**2+(y1-y7)**2))**3 + f1*M2*(x2-x7)/(np.sqrt((x2-x7)**2+(y2-y7)**2))**3 + f1*M3*(x3-x7)/(np.sqrt((x3-x7)**2+(y3-y7)**2))**3 + f1*M4*(x4-x7)/(np.sqrt((x4-x7)**2+(y4-y7)**2))**3 + f1*M5*(x5-x7)/(np.sqrt((x5-x7)**2+(y5-y7)**2))**3 + f1*M6*(x6-x7)/(np.sqrt((x6-x7)**2+(y6-y7)**2))**3 + f1*M8*(x8-x7)/(np.sqrt((x8-x7)**2+(y8-y7)**2))**3 + f1*M9*(x9-x7)/(np.sqrt((x9-x7)**2+(y9-y7)**2))**3,
       f1*M0*(y0-y7)/(np.sqrt((x0-x7)**2+(y0-y7)**2))**3 + f1*M1*(y1-y7)/(np.sqrt((x1-x7)**2+(y1-y7)**2))**3 + f1*M2*(y2-y7)/(np.sqrt((x2-x7)**2+(y2-y7)**2))**3 + f1*M3*(y3-y7)/(np.sqrt((x3-x7)**2+(y3-y7)**2))**3 + f1*M4*(y4-y7)/(np.sqrt((x4-x7)**2+(y4-y7)**2))**3 + f1*M5*(y5-y7)/(np.sqrt((x5-x7)**2+(y5-y7)**2))**3 + f1*M6*(y6-y7)/(np.sqrt((x6-x7)**2+(y6-y7)**2))**3 + f1*M8*(y8-y7)/(np.sqrt((x8-x7)**2+(y8-y7)**2))**3 + f1*M9*(y9-y7)/(np.sqrt((x9-x7)**2+(y9-y7)**2))**3,
       f1*M0*(x0-x8)/(np.sqrt((x0-x8)**2+(y0-y8)**2))**3 + f1*M1*(x1-x8)/(np.sqrt((x1-x8)**2+(y1-y8)**2))**3 + f1*M2*(x2-x8)/(np.sqrt((x2-x8)**2+(y2-y8)**2))**3 + f1*M3*(x3-x8)/(np.sqrt((x3-x8)**2+(y3-y8)**2))**3 + f1*M4*(x4-x8)/(np.sqrt((x4-x8)**2+(y4-y8)**2))**3 + f1*M5*(x5-x8)/(np.sqrt((x5-x8)**2+(y5-y8)**2))**3 + f1*M6*(x6-x8)/(np.sqrt((x6-x8)**2+(y6-y8)**2))**3 + f1*M7*(x7-x8)/(np.sqrt((x7-x8)**2+(y7-y8)**2))**3 + f1*M9*(x9-x8)/(np.sqrt((x9-x8)**2+(y9-y8)**2))**3,
       f1*M0*(y0-y8)/(np.sqrt((x0-x8)**2+(y0-y8)**2))**3 + f1*M1*(y1-y8)/(np.sqrt((x1-x8)**2+(y1-y8)**2))**3 + f1*M2*(y2-y8)/(np.sqrt((x2-x8)**2+(y2-y8)**2))**3 + f1*M3*(y3-y8)/(np.sqrt((x3-x8)**2+(y3-y8)**2))**3 + f1*M4*(y4-y8)/(np.sqrt((x4-x8)**2+(y4-y8)**2))**3 + f1*M5*(y5-y8)/(np.sqrt((x5-x8)**2+(y5-y8)**2))**3 + f1*M6*(y6-y8)/(np.sqrt((x6-x8)**2+(y6-y8)**2))**3 + f1*M7*(y7-y8)/(np.sqrt((x7-x8)**2+(y7-y8)**2))**3 + f1*M9*(y9-y8)/(np.sqrt((x9-x8)**2+(y9-y8)**2))**3,
       f1*M0*(x0-x9)/(np.sqrt((x0-x9)**2+(y0-y9)**2))**3 + f1*M1*(x1-x9)/(np.sqrt((x1-x9)**2+(y1-y9)**2))**3 + f1*M2*(x2-x9)/(np.sqrt((x2-x9)**2+(y2-y9)**2))**3 + f1*M3*(x3-x9)/(np.sqrt((x3-x9)**2+(y3-y9)**2))**3 + f1*M4*(x4-x9)/(np.sqrt((x4-x9)**2+(y4-y9)**2))**3 + f1*M5*(x5-x9)/(np.sqrt((x5-x9)**2+(y5-y9)**2))**3 + f1*M6*(x6-x9)/(np.sqrt((x6-x9)**2+(y6-y9)**2))**3 + f1*M7*(x7-x9)/(np.sqrt((x7-x9)**2+(y7-y9)**2))**3 + f1*M8*(x8-x9)/(np.sqrt((x8-x9)**2+(y8-y9)**2))**3,
       f1*M0*(y0-y9)/(np.sqrt((x0-x9)**2+(y0-y9)**2))**3 + f1*M1*(y1-y9)/(np.sqrt((x1-x9)**2+(y1-y9)**2))**3 + f1*M2*(y2-y9)/(np.sqrt((x2-x9)**2+(y2-y9)**2))**3 + f1*M3*(y3-y9)/(np.sqrt((x3-x9)**2+(y3-y9)**2))**3 + f1*M4*(y4-y9)/(np.sqrt((x4-x9)**2+(y4-y9)**2))**3 + f1*M5*(y5-y9)/(np.sqrt((x5-x9)**2+(y5-y9)**2))**3 + f1*M6*(y6-y9)/(np.sqrt((x6-x9)**2+(y6-y9)**2))**3 + f1*M7*(y7-y9)/(np.sqrt((x7-x9)**2+(y7-y9)**2))**3 + f1*M8*(y8-y9)/(np.sqrt((x8-x9)**2+(y8-y9)**2))**3,
       vx0,
       vy0,
       vx1,
       vy1,
       vx2,
       vy2,
       vx3,
       vy3,
       vx4,
       vy4,
       vx5,
       vy5,
       vx6,
       vy6,
       vx7,
       vy7,
       vx8,
       vy8,
       vx9,
       vy9
       ]
y0=[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9]
[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9]= odeint(f, y0, t, args=(params,), full_output=False).T
c1=M0*(x0*vy0-y0*vx0)+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)+M3*(x3*vy3-y3*vx3)+M4*(x4*vy4-y4*vx4)+M5*(x5*vy5-y5*vx5)+M6*(x6*vy6-y6*vx6)+M7*(x7*vy7-y7*vx7)+M8*(x8*vy8-y8*vx8)+M9*(x9*vy9-y9*vx9)
U=f1*(M0*M1/(np.sqrt((x1-x0)**2+(y1-y0)**2))) + f1*(M0*M2/(np.sqrt((x0-x2)**2+(y0-y2)**2))) + f1*(M0*M3/(np.sqrt((x0-x3)**2+(y0-y3)**2))) + f1*(M0*M4/(np.sqrt((x0-x4)**2+(y0-y4)**2))) + f1*(M0*M5/(np.sqrt((x0-x5)**2+(y0-y5)**2))) + f1*(M0*M6/(np.sqrt((x0-x6)**2+(y0-y6)**2))) + f1*(M0*M7/(np.sqrt((x0-x7)**2+(y0-y7)**2))) + f1*(M0*M8/(np.sqrt((x0-x8)**2+(y0-y8)**2))) + f1*(M0*M9/(np.sqrt((x0-x9)**2+(y0-y9)**2))) + f1*(M1*M2/(np.sqrt((x1-x2)**2+(y1-y2)**2))) + f1*(M1*M3/(np.sqrt((x1-x3)**2+(y1-y3)**2))) + f1*(M1*M4/(np.sqrt((x1-x4)**2+(y1-y4)**2))) + f1*(M1*M5/(np.sqrt((x1-x5)**2+(y1-y5)**2))) + f1*(M1*M6/(np.sqrt((x1-x6)**2+(y1-y6)**2))) + f1*(M1*M7/(np.sqrt((x1-x7)**2+(y1-y7)**2))) + f1*(M1*M8/(np.sqrt((x1-x8)**2+(y1-y8)**2))) + f1*(M1*M9/(np.sqrt((x1-x9)**2+(y1-y9)**2))) + f1*(M2*M3/(np.sqrt((x2-x3)**2+(y2-y3)**2))) + f1*(M2*M4/(np.sqrt((x2-x4)**2+(y2-y4)**2))) + f1*(M2*M5/(np.sqrt((x2-x5)**2+(y2-y5)**2))) + f1*(M2*M6/(np.sqrt((x2-x6)**2+(y2-y6)**2))) + f1*(M2*M7/(np.sqrt((x2-x7)**2+(y2-y7)**2))) + f1*(M2*M8/(np.sqrt((x2-x8)**2+(y2-y8)**2))) + f1*(M2*M9/(np.sqrt((x2-x9)**2+(y2-y9)**2))) + f1*(M3*M4/(np.sqrt((x3-x4)**2+(y3-y4)**2))) + f1*(M3*M5/(np.sqrt((x3-x5)**2+(y3-y5)**2))) + f1*(M3*M6/(np.sqrt((x3-x6)**2+(y3-y6)**2))) + f1*(M3*M7/(np.sqrt((x3-x7)**2+(y3-y7)**2))) + f1*(M3*M8/(np.sqrt((x3-x8)**2+(y3-y8)**2))) + f1*(M3*M9/(np.sqrt((x3-x9)**2+(y3-y9)**2))) + f1*(M4*M5/(np.sqrt((x4-x5)**2+(y4-y5)**2))) + f1*(M4*M6/(np.sqrt((x4-x6)**2+(y4-y6)**2))) + f1*(M4*M7/(np.sqrt((x4-x7)**2+(y4-y7)**2))) + f1*(M4*M8/(np.sqrt((x4-x8)**2+(y4-y8)**2))) + f1*(M4*M9/(np.sqrt((x4-x9)**2+(y4-y9)**2))) + f1*(M5*M6/(np.sqrt((x5-x6)**2+(y5-y6)**2))) + f1*(M5*M7/(np.sqrt((x5-x7)**2+(y5-y7)**2))) + f1*(M5*M8/(np.sqrt((x5-x8)**2+(y5-y8)**2))) + f1*(M5*M9/(np.sqrt((x5-x9)**2+(y5-y9)**2))) + f1*(M6*M7/(np.sqrt((x6-x7)**2+(y6-y7)**2))) + f1*(M6*M8/(np.sqrt((x6-x8)**2+(y6-y8)**2))) + f1*(M6*M9/(np.sqrt((x6-x9)**2+(y6-y9)**2))) + f1*(M7*M8/(np.sqrt((x7-x8)**2+(y7-y8)**2))) + f1*(M7*M9/(np.sqrt((x7-x9)**2+(y7-y9)**2))) + f1*(M8*M9/(np.sqrt((x8-x9)**2+(y8-y9)**2)))
H=M0/2*(vy0**2+vx0**2) +M1/2*(vy1**2+vx1**2) +M2/2*(vy2**2+vx2**2) +M3/2*(vy3**2+vx3**2) +M4/2*(vy4**2+vx4**2) +M5/2*(vy5**2+vx5**2) +M6/2*(vy6**2+vx6**2) +M7/2*(vy7**2+vx7**2) +M8/2*(vy8**2+vx8**2) +M9/2*(vy9**2+vx9**2)-U
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
text_filec5 = open('Nbody/Coords/coord5_NumOne.txt', 'w')
text_files5=open('Nbody/Coords/speed5_NumOne.txt', 'w')
text_filec6 = open('Nbody/Coords/coord6_NumOne.txt', 'w')
text_files6=open('Nbody/Coords/speed6_NumOne.txt', 'w')
text_filec7 = open('Nbody/Coords/coord7_NumOne.txt', 'w')
text_files7=open('Nbody/Coords/speed7_NumOne.txt', 'w')
text_filec8 = open('Nbody/Coords/coord8_NumOne.txt', 'w')
text_files8=open('Nbody/Coords/speed8_NumOne.txt', 'w')
text_filec9 = open('Nbody/Coords/coord9_NumOne.txt', 'w')
text_files9=open('Nbody/Coords/speed9_NumOne.txt', 'w')
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
   text_filec5.write(str(x5[i])+';'+str(y5[i])+'\n')
   text_files5.write(str(vx5[i])+';'+str(vy5[i])+'\n')
   text_filec6.write(str(x6[i])+';'+str(y6[i])+'\n')
   text_files6.write(str(vx6[i])+';'+str(vy6[i])+'\n')
   text_filec7.write(str(x7[i])+';'+str(y7[i])+'\n')
   text_files7.write(str(vx7[i])+';'+str(vy7[i])+'\n')
   text_filec8.write(str(x8[i])+';'+str(y8[i])+'\n')
   text_files8.write(str(vx8[i])+';'+str(vy8[i])+'\n')
   text_filec9.write(str(x9[i])+';'+str(y9[i])+'\n')
   text_files9.write(str(vx9[i])+';'+str(vy9[i])+'\n')
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
text_filec5.close()
text_files5.close()
text_filec6.close()
text_files6.close()
text_filec7.close()
text_files7.close()
text_filec8.close()
text_files8.close()
text_filec9.close()
text_files9.close()
Hfile.close()
Cfile.close()
