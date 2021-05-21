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
M0,x0,vx0,y0,vy0=1,2.0,-0.0,0.0,2.0
M1,x1,vx1,y1,vy1=1,1.8270909152852017,-0.8134732861516003,0.8134732861516003,1.8270909152852017
M2,x2,vx2,y2,vy2=1,1.3382612127177165,-1.4862896509547883,1.4862896509547883,1.3382612127177165
M3,x3,vx3,y3,vy3=1,0.6180339887498949,-1.902113032590307,1.902113032590307,0.6180339887498949
M4,x4,vx4,y4,vy4=1,-0.20905692653530666,-1.9890437907365468,1.9890437907365468,-0.20905692653530666
M5,x5,vx5,y5,vy5=1,-0.9999999999999996,-1.7320508075688774,1.7320508075688774,-0.9999999999999996
M6,x6,vx6,y6,vy6=1,-1.6180339887498947,-1.1755705045849465,1.1755705045849465,-1.6180339887498947
M7,x7,vx7,y7,vy7=1,-1.9562952014676114,-0.41582338163551863,0.41582338163551863,-1.9562952014676114
M8,x8,vx8,y8,vy8=1,-1.9562952014676114,0.41582338163551813,-0.41582338163551813,-1.9562952014676114
M9,x9,vx9,y9,vy9=1,-1.618033988749895,1.175570504584946,-1.175570504584946,-1.618033988749895
M10,x10,vx10,y10,vy10=1,-1.0000000000000009,1.732050807568877,-1.732050807568877,-1.0000000000000009
M11,x11,vx11,y11,vy11=1,-0.20905692653530847,1.9890437907365466,-1.9890437907365466,-0.20905692653530847
M12,x12,vx12,y12,vy12=1,0.6180339887498945,1.9021130325903073,-1.9021130325903073,0.6180339887498945
M13,x13,vx13,y13,vy13=1,1.338261212717717,1.486289650954788,-1.486289650954788,1.338261212717717
M14,x14,vx14,y14,vy14=1,1.827090915285202,0.8134732861516003,-0.8134732861516003,1.827090915285202

params=[M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, f1]
def f(y, t, params):
   vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, vx10, vy10, vx11, vy11, vx12, vy12, vx13, vy13, vx14, vy14, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14=y
   M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14,f1=params
   return[
       f1*M1*(x1-x0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(x2-x0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(x3-x0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(x4-x0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3 + f1*M5*(x5-x0)/(np.sqrt((x5-x0)**2+(y5-y0)**2))**3 + f1*M6*(x6-x0)/(np.sqrt((x6-x0)**2+(y6-y0)**2))**3 + f1*M7*(x7-x0)/(np.sqrt((x7-x0)**2+(y7-y0)**2))**3 + f1*M8*(x8-x0)/(np.sqrt((x8-x0)**2+(y8-y0)**2))**3 + f1*M9*(x9-x0)/(np.sqrt((x9-x0)**2+(y9-y0)**2))**3 + f1*M10*(x10-x0)/(np.sqrt((x10-x0)**2+(y10-y0)**2))**3 + f1*M11*(x11-x0)/(np.sqrt((x11-x0)**2+(y11-y0)**2))**3 + f1*M12*(x12-x0)/(np.sqrt((x12-x0)**2+(y12-y0)**2))**3 + f1*M13*(x13-x0)/(np.sqrt((x13-x0)**2+(y13-y0)**2))**3 + f1*M14*(x14-x0)/(np.sqrt((x14-x0)**2+(y14-y0)**2))**3,
       f1*M1*(y1-y0)/(np.sqrt((x1-x0)**2+(y1-y0)**2))**3 + f1*M2*(y2-y0)/(np.sqrt((x2-x0)**2+(y2-y0)**2))**3 + f1*M3*(y3-y0)/(np.sqrt((x3-x0)**2+(y3-y0)**2))**3 + f1*M4*(y4-y0)/(np.sqrt((x4-x0)**2+(y4-y0)**2))**3 + f1*M5*(y5-y0)/(np.sqrt((x5-x0)**2+(y5-y0)**2))**3 + f1*M6*(y6-y0)/(np.sqrt((x6-x0)**2+(y6-y0)**2))**3 + f1*M7*(y7-y0)/(np.sqrt((x7-x0)**2+(y7-y0)**2))**3 + f1*M8*(y8-y0)/(np.sqrt((x8-x0)**2+(y8-y0)**2))**3 + f1*M9*(y9-y0)/(np.sqrt((x9-x0)**2+(y9-y0)**2))**3 + f1*M10*(y10-y0)/(np.sqrt((x10-x0)**2+(y10-y0)**2))**3 + f1*M11*(y11-y0)/(np.sqrt((x11-x0)**2+(y11-y0)**2))**3 + f1*M12*(y12-y0)/(np.sqrt((x12-x0)**2+(y12-y0)**2))**3 + f1*M13*(y13-y0)/(np.sqrt((x13-x0)**2+(y13-y0)**2))**3 + f1*M14*(y14-y0)/(np.sqrt((x14-x0)**2+(y14-y0)**2))**3,
       f1*M0*(x0-x1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(x2-x1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(x3-x1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(x4-x1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3 + f1*M5*(x5-x1)/(np.sqrt((x5-x1)**2+(y5-y1)**2))**3 + f1*M6*(x6-x1)/(np.sqrt((x6-x1)**2+(y6-y1)**2))**3 + f1*M7*(x7-x1)/(np.sqrt((x7-x1)**2+(y7-y1)**2))**3 + f1*M8*(x8-x1)/(np.sqrt((x8-x1)**2+(y8-y1)**2))**3 + f1*M9*(x9-x1)/(np.sqrt((x9-x1)**2+(y9-y1)**2))**3 + f1*M10*(x10-x1)/(np.sqrt((x10-x1)**2+(y10-y1)**2))**3 + f1*M11*(x11-x1)/(np.sqrt((x11-x1)**2+(y11-y1)**2))**3 + f1*M12*(x12-x1)/(np.sqrt((x12-x1)**2+(y12-y1)**2))**3 + f1*M13*(x13-x1)/(np.sqrt((x13-x1)**2+(y13-y1)**2))**3 + f1*M14*(x14-x1)/(np.sqrt((x14-x1)**2+(y14-y1)**2))**3,
       f1*M0*(y0-y1)/(np.sqrt((x0-x1)**2+(y0-y1)**2))**3 + f1*M2*(y2-y1)/(np.sqrt((x2-x1)**2+(y2-y1)**2))**3 + f1*M3*(y3-y1)/(np.sqrt((x3-x1)**2+(y3-y1)**2))**3 + f1*M4*(y4-y1)/(np.sqrt((x4-x1)**2+(y4-y1)**2))**3 + f1*M5*(y5-y1)/(np.sqrt((x5-x1)**2+(y5-y1)**2))**3 + f1*M6*(y6-y1)/(np.sqrt((x6-x1)**2+(y6-y1)**2))**3 + f1*M7*(y7-y1)/(np.sqrt((x7-x1)**2+(y7-y1)**2))**3 + f1*M8*(y8-y1)/(np.sqrt((x8-x1)**2+(y8-y1)**2))**3 + f1*M9*(y9-y1)/(np.sqrt((x9-x1)**2+(y9-y1)**2))**3 + f1*M10*(y10-y1)/(np.sqrt((x10-x1)**2+(y10-y1)**2))**3 + f1*M11*(y11-y1)/(np.sqrt((x11-x1)**2+(y11-y1)**2))**3 + f1*M12*(y12-y1)/(np.sqrt((x12-x1)**2+(y12-y1)**2))**3 + f1*M13*(y13-y1)/(np.sqrt((x13-x1)**2+(y13-y1)**2))**3 + f1*M14*(y14-y1)/(np.sqrt((x14-x1)**2+(y14-y1)**2))**3,
       f1*M0*(x0-x2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(x1-x2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(x3-x2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(x4-x2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3 + f1*M5*(x5-x2)/(np.sqrt((x5-x2)**2+(y5-y2)**2))**3 + f1*M6*(x6-x2)/(np.sqrt((x6-x2)**2+(y6-y2)**2))**3 + f1*M7*(x7-x2)/(np.sqrt((x7-x2)**2+(y7-y2)**2))**3 + f1*M8*(x8-x2)/(np.sqrt((x8-x2)**2+(y8-y2)**2))**3 + f1*M9*(x9-x2)/(np.sqrt((x9-x2)**2+(y9-y2)**2))**3 + f1*M10*(x10-x2)/(np.sqrt((x10-x2)**2+(y10-y2)**2))**3 + f1*M11*(x11-x2)/(np.sqrt((x11-x2)**2+(y11-y2)**2))**3 + f1*M12*(x12-x2)/(np.sqrt((x12-x2)**2+(y12-y2)**2))**3 + f1*M13*(x13-x2)/(np.sqrt((x13-x2)**2+(y13-y2)**2))**3 + f1*M14*(x14-x2)/(np.sqrt((x14-x2)**2+(y14-y2)**2))**3,
       f1*M0*(y0-y2)/(np.sqrt((x0-x2)**2+(y0-y2)**2))**3 + f1*M1*(y1-y2)/(np.sqrt((x1-x2)**2+(y1-y2)**2))**3 + f1*M3*(y3-y2)/(np.sqrt((x3-x2)**2+(y3-y2)**2))**3 + f1*M4*(y4-y2)/(np.sqrt((x4-x2)**2+(y4-y2)**2))**3 + f1*M5*(y5-y2)/(np.sqrt((x5-x2)**2+(y5-y2)**2))**3 + f1*M6*(y6-y2)/(np.sqrt((x6-x2)**2+(y6-y2)**2))**3 + f1*M7*(y7-y2)/(np.sqrt((x7-x2)**2+(y7-y2)**2))**3 + f1*M8*(y8-y2)/(np.sqrt((x8-x2)**2+(y8-y2)**2))**3 + f1*M9*(y9-y2)/(np.sqrt((x9-x2)**2+(y9-y2)**2))**3 + f1*M10*(y10-y2)/(np.sqrt((x10-x2)**2+(y10-y2)**2))**3 + f1*M11*(y11-y2)/(np.sqrt((x11-x2)**2+(y11-y2)**2))**3 + f1*M12*(y12-y2)/(np.sqrt((x12-x2)**2+(y12-y2)**2))**3 + f1*M13*(y13-y2)/(np.sqrt((x13-x2)**2+(y13-y2)**2))**3 + f1*M14*(y14-y2)/(np.sqrt((x14-x2)**2+(y14-y2)**2))**3,
       f1*M0*(x0-x3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(x1-x3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(x2-x3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(x4-x3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3 + f1*M5*(x5-x3)/(np.sqrt((x5-x3)**2+(y5-y3)**2))**3 + f1*M6*(x6-x3)/(np.sqrt((x6-x3)**2+(y6-y3)**2))**3 + f1*M7*(x7-x3)/(np.sqrt((x7-x3)**2+(y7-y3)**2))**3 + f1*M8*(x8-x3)/(np.sqrt((x8-x3)**2+(y8-y3)**2))**3 + f1*M9*(x9-x3)/(np.sqrt((x9-x3)**2+(y9-y3)**2))**3 + f1*M10*(x10-x3)/(np.sqrt((x10-x3)**2+(y10-y3)**2))**3 + f1*M11*(x11-x3)/(np.sqrt((x11-x3)**2+(y11-y3)**2))**3 + f1*M12*(x12-x3)/(np.sqrt((x12-x3)**2+(y12-y3)**2))**3 + f1*M13*(x13-x3)/(np.sqrt((x13-x3)**2+(y13-y3)**2))**3 + f1*M14*(x14-x3)/(np.sqrt((x14-x3)**2+(y14-y3)**2))**3,
       f1*M0*(y0-y3)/(np.sqrt((x0-x3)**2+(y0-y3)**2))**3 + f1*M1*(y1-y3)/(np.sqrt((x1-x3)**2+(y1-y3)**2))**3 + f1*M2*(y2-y3)/(np.sqrt((x2-x3)**2+(y2-y3)**2))**3 + f1*M4*(y4-y3)/(np.sqrt((x4-x3)**2+(y4-y3)**2))**3 + f1*M5*(y5-y3)/(np.sqrt((x5-x3)**2+(y5-y3)**2))**3 + f1*M6*(y6-y3)/(np.sqrt((x6-x3)**2+(y6-y3)**2))**3 + f1*M7*(y7-y3)/(np.sqrt((x7-x3)**2+(y7-y3)**2))**3 + f1*M8*(y8-y3)/(np.sqrt((x8-x3)**2+(y8-y3)**2))**3 + f1*M9*(y9-y3)/(np.sqrt((x9-x3)**2+(y9-y3)**2))**3 + f1*M10*(y10-y3)/(np.sqrt((x10-x3)**2+(y10-y3)**2))**3 + f1*M11*(y11-y3)/(np.sqrt((x11-x3)**2+(y11-y3)**2))**3 + f1*M12*(y12-y3)/(np.sqrt((x12-x3)**2+(y12-y3)**2))**3 + f1*M13*(y13-y3)/(np.sqrt((x13-x3)**2+(y13-y3)**2))**3 + f1*M14*(y14-y3)/(np.sqrt((x14-x3)**2+(y14-y3)**2))**3,
       f1*M0*(x0-x4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(x1-x4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(x2-x4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(x3-x4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3 + f1*M5*(x5-x4)/(np.sqrt((x5-x4)**2+(y5-y4)**2))**3 + f1*M6*(x6-x4)/(np.sqrt((x6-x4)**2+(y6-y4)**2))**3 + f1*M7*(x7-x4)/(np.sqrt((x7-x4)**2+(y7-y4)**2))**3 + f1*M8*(x8-x4)/(np.sqrt((x8-x4)**2+(y8-y4)**2))**3 + f1*M9*(x9-x4)/(np.sqrt((x9-x4)**2+(y9-y4)**2))**3 + f1*M10*(x10-x4)/(np.sqrt((x10-x4)**2+(y10-y4)**2))**3 + f1*M11*(x11-x4)/(np.sqrt((x11-x4)**2+(y11-y4)**2))**3 + f1*M12*(x12-x4)/(np.sqrt((x12-x4)**2+(y12-y4)**2))**3 + f1*M13*(x13-x4)/(np.sqrt((x13-x4)**2+(y13-y4)**2))**3 + f1*M14*(x14-x4)/(np.sqrt((x14-x4)**2+(y14-y4)**2))**3,
       f1*M0*(y0-y4)/(np.sqrt((x0-x4)**2+(y0-y4)**2))**3 + f1*M1*(y1-y4)/(np.sqrt((x1-x4)**2+(y1-y4)**2))**3 + f1*M2*(y2-y4)/(np.sqrt((x2-x4)**2+(y2-y4)**2))**3 + f1*M3*(y3-y4)/(np.sqrt((x3-x4)**2+(y3-y4)**2))**3 + f1*M5*(y5-y4)/(np.sqrt((x5-x4)**2+(y5-y4)**2))**3 + f1*M6*(y6-y4)/(np.sqrt((x6-x4)**2+(y6-y4)**2))**3 + f1*M7*(y7-y4)/(np.sqrt((x7-x4)**2+(y7-y4)**2))**3 + f1*M8*(y8-y4)/(np.sqrt((x8-x4)**2+(y8-y4)**2))**3 + f1*M9*(y9-y4)/(np.sqrt((x9-x4)**2+(y9-y4)**2))**3 + f1*M10*(y10-y4)/(np.sqrt((x10-x4)**2+(y10-y4)**2))**3 + f1*M11*(y11-y4)/(np.sqrt((x11-x4)**2+(y11-y4)**2))**3 + f1*M12*(y12-y4)/(np.sqrt((x12-x4)**2+(y12-y4)**2))**3 + f1*M13*(y13-y4)/(np.sqrt((x13-x4)**2+(y13-y4)**2))**3 + f1*M14*(y14-y4)/(np.sqrt((x14-x4)**2+(y14-y4)**2))**3,
       f1*M0*(x0-x5)/(np.sqrt((x0-x5)**2+(y0-y5)**2))**3 + f1*M1*(x1-x5)/(np.sqrt((x1-x5)**2+(y1-y5)**2))**3 + f1*M2*(x2-x5)/(np.sqrt((x2-x5)**2+(y2-y5)**2))**3 + f1*M3*(x3-x5)/(np.sqrt((x3-x5)**2+(y3-y5)**2))**3 + f1*M4*(x4-x5)/(np.sqrt((x4-x5)**2+(y4-y5)**2))**3 + f1*M6*(x6-x5)/(np.sqrt((x6-x5)**2+(y6-y5)**2))**3 + f1*M7*(x7-x5)/(np.sqrt((x7-x5)**2+(y7-y5)**2))**3 + f1*M8*(x8-x5)/(np.sqrt((x8-x5)**2+(y8-y5)**2))**3 + f1*M9*(x9-x5)/(np.sqrt((x9-x5)**2+(y9-y5)**2))**3 + f1*M10*(x10-x5)/(np.sqrt((x10-x5)**2+(y10-y5)**2))**3 + f1*M11*(x11-x5)/(np.sqrt((x11-x5)**2+(y11-y5)**2))**3 + f1*M12*(x12-x5)/(np.sqrt((x12-x5)**2+(y12-y5)**2))**3 + f1*M13*(x13-x5)/(np.sqrt((x13-x5)**2+(y13-y5)**2))**3 + f1*M14*(x14-x5)/(np.sqrt((x14-x5)**2+(y14-y5)**2))**3,
       f1*M0*(y0-y5)/(np.sqrt((x0-x5)**2+(y0-y5)**2))**3 + f1*M1*(y1-y5)/(np.sqrt((x1-x5)**2+(y1-y5)**2))**3 + f1*M2*(y2-y5)/(np.sqrt((x2-x5)**2+(y2-y5)**2))**3 + f1*M3*(y3-y5)/(np.sqrt((x3-x5)**2+(y3-y5)**2))**3 + f1*M4*(y4-y5)/(np.sqrt((x4-x5)**2+(y4-y5)**2))**3 + f1*M6*(y6-y5)/(np.sqrt((x6-x5)**2+(y6-y5)**2))**3 + f1*M7*(y7-y5)/(np.sqrt((x7-x5)**2+(y7-y5)**2))**3 + f1*M8*(y8-y5)/(np.sqrt((x8-x5)**2+(y8-y5)**2))**3 + f1*M9*(y9-y5)/(np.sqrt((x9-x5)**2+(y9-y5)**2))**3 + f1*M10*(y10-y5)/(np.sqrt((x10-x5)**2+(y10-y5)**2))**3 + f1*M11*(y11-y5)/(np.sqrt((x11-x5)**2+(y11-y5)**2))**3 + f1*M12*(y12-y5)/(np.sqrt((x12-x5)**2+(y12-y5)**2))**3 + f1*M13*(y13-y5)/(np.sqrt((x13-x5)**2+(y13-y5)**2))**3 + f1*M14*(y14-y5)/(np.sqrt((x14-x5)**2+(y14-y5)**2))**3,
       f1*M0*(x0-x6)/(np.sqrt((x0-x6)**2+(y0-y6)**2))**3 + f1*M1*(x1-x6)/(np.sqrt((x1-x6)**2+(y1-y6)**2))**3 + f1*M2*(x2-x6)/(np.sqrt((x2-x6)**2+(y2-y6)**2))**3 + f1*M3*(x3-x6)/(np.sqrt((x3-x6)**2+(y3-y6)**2))**3 + f1*M4*(x4-x6)/(np.sqrt((x4-x6)**2+(y4-y6)**2))**3 + f1*M5*(x5-x6)/(np.sqrt((x5-x6)**2+(y5-y6)**2))**3 + f1*M7*(x7-x6)/(np.sqrt((x7-x6)**2+(y7-y6)**2))**3 + f1*M8*(x8-x6)/(np.sqrt((x8-x6)**2+(y8-y6)**2))**3 + f1*M9*(x9-x6)/(np.sqrt((x9-x6)**2+(y9-y6)**2))**3 + f1*M10*(x10-x6)/(np.sqrt((x10-x6)**2+(y10-y6)**2))**3 + f1*M11*(x11-x6)/(np.sqrt((x11-x6)**2+(y11-y6)**2))**3 + f1*M12*(x12-x6)/(np.sqrt((x12-x6)**2+(y12-y6)**2))**3 + f1*M13*(x13-x6)/(np.sqrt((x13-x6)**2+(y13-y6)**2))**3 + f1*M14*(x14-x6)/(np.sqrt((x14-x6)**2+(y14-y6)**2))**3,
       f1*M0*(y0-y6)/(np.sqrt((x0-x6)**2+(y0-y6)**2))**3 + f1*M1*(y1-y6)/(np.sqrt((x1-x6)**2+(y1-y6)**2))**3 + f1*M2*(y2-y6)/(np.sqrt((x2-x6)**2+(y2-y6)**2))**3 + f1*M3*(y3-y6)/(np.sqrt((x3-x6)**2+(y3-y6)**2))**3 + f1*M4*(y4-y6)/(np.sqrt((x4-x6)**2+(y4-y6)**2))**3 + f1*M5*(y5-y6)/(np.sqrt((x5-x6)**2+(y5-y6)**2))**3 + f1*M7*(y7-y6)/(np.sqrt((x7-x6)**2+(y7-y6)**2))**3 + f1*M8*(y8-y6)/(np.sqrt((x8-x6)**2+(y8-y6)**2))**3 + f1*M9*(y9-y6)/(np.sqrt((x9-x6)**2+(y9-y6)**2))**3 + f1*M10*(y10-y6)/(np.sqrt((x10-x6)**2+(y10-y6)**2))**3 + f1*M11*(y11-y6)/(np.sqrt((x11-x6)**2+(y11-y6)**2))**3 + f1*M12*(y12-y6)/(np.sqrt((x12-x6)**2+(y12-y6)**2))**3 + f1*M13*(y13-y6)/(np.sqrt((x13-x6)**2+(y13-y6)**2))**3 + f1*M14*(y14-y6)/(np.sqrt((x14-x6)**2+(y14-y6)**2))**3,
       f1*M0*(x0-x7)/(np.sqrt((x0-x7)**2+(y0-y7)**2))**3 + f1*M1*(x1-x7)/(np.sqrt((x1-x7)**2+(y1-y7)**2))**3 + f1*M2*(x2-x7)/(np.sqrt((x2-x7)**2+(y2-y7)**2))**3 + f1*M3*(x3-x7)/(np.sqrt((x3-x7)**2+(y3-y7)**2))**3 + f1*M4*(x4-x7)/(np.sqrt((x4-x7)**2+(y4-y7)**2))**3 + f1*M5*(x5-x7)/(np.sqrt((x5-x7)**2+(y5-y7)**2))**3 + f1*M6*(x6-x7)/(np.sqrt((x6-x7)**2+(y6-y7)**2))**3 + f1*M8*(x8-x7)/(np.sqrt((x8-x7)**2+(y8-y7)**2))**3 + f1*M9*(x9-x7)/(np.sqrt((x9-x7)**2+(y9-y7)**2))**3 + f1*M10*(x10-x7)/(np.sqrt((x10-x7)**2+(y10-y7)**2))**3 + f1*M11*(x11-x7)/(np.sqrt((x11-x7)**2+(y11-y7)**2))**3 + f1*M12*(x12-x7)/(np.sqrt((x12-x7)**2+(y12-y7)**2))**3 + f1*M13*(x13-x7)/(np.sqrt((x13-x7)**2+(y13-y7)**2))**3 + f1*M14*(x14-x7)/(np.sqrt((x14-x7)**2+(y14-y7)**2))**3,
       f1*M0*(y0-y7)/(np.sqrt((x0-x7)**2+(y0-y7)**2))**3 + f1*M1*(y1-y7)/(np.sqrt((x1-x7)**2+(y1-y7)**2))**3 + f1*M2*(y2-y7)/(np.sqrt((x2-x7)**2+(y2-y7)**2))**3 + f1*M3*(y3-y7)/(np.sqrt((x3-x7)**2+(y3-y7)**2))**3 + f1*M4*(y4-y7)/(np.sqrt((x4-x7)**2+(y4-y7)**2))**3 + f1*M5*(y5-y7)/(np.sqrt((x5-x7)**2+(y5-y7)**2))**3 + f1*M6*(y6-y7)/(np.sqrt((x6-x7)**2+(y6-y7)**2))**3 + f1*M8*(y8-y7)/(np.sqrt((x8-x7)**2+(y8-y7)**2))**3 + f1*M9*(y9-y7)/(np.sqrt((x9-x7)**2+(y9-y7)**2))**3 + f1*M10*(y10-y7)/(np.sqrt((x10-x7)**2+(y10-y7)**2))**3 + f1*M11*(y11-y7)/(np.sqrt((x11-x7)**2+(y11-y7)**2))**3 + f1*M12*(y12-y7)/(np.sqrt((x12-x7)**2+(y12-y7)**2))**3 + f1*M13*(y13-y7)/(np.sqrt((x13-x7)**2+(y13-y7)**2))**3 + f1*M14*(y14-y7)/(np.sqrt((x14-x7)**2+(y14-y7)**2))**3,
       f1*M0*(x0-x8)/(np.sqrt((x0-x8)**2+(y0-y8)**2))**3 + f1*M1*(x1-x8)/(np.sqrt((x1-x8)**2+(y1-y8)**2))**3 + f1*M2*(x2-x8)/(np.sqrt((x2-x8)**2+(y2-y8)**2))**3 + f1*M3*(x3-x8)/(np.sqrt((x3-x8)**2+(y3-y8)**2))**3 + f1*M4*(x4-x8)/(np.sqrt((x4-x8)**2+(y4-y8)**2))**3 + f1*M5*(x5-x8)/(np.sqrt((x5-x8)**2+(y5-y8)**2))**3 + f1*M6*(x6-x8)/(np.sqrt((x6-x8)**2+(y6-y8)**2))**3 + f1*M7*(x7-x8)/(np.sqrt((x7-x8)**2+(y7-y8)**2))**3 + f1*M9*(x9-x8)/(np.sqrt((x9-x8)**2+(y9-y8)**2))**3 + f1*M10*(x10-x8)/(np.sqrt((x10-x8)**2+(y10-y8)**2))**3 + f1*M11*(x11-x8)/(np.sqrt((x11-x8)**2+(y11-y8)**2))**3 + f1*M12*(x12-x8)/(np.sqrt((x12-x8)**2+(y12-y8)**2))**3 + f1*M13*(x13-x8)/(np.sqrt((x13-x8)**2+(y13-y8)**2))**3 + f1*M14*(x14-x8)/(np.sqrt((x14-x8)**2+(y14-y8)**2))**3,
       f1*M0*(y0-y8)/(np.sqrt((x0-x8)**2+(y0-y8)**2))**3 + f1*M1*(y1-y8)/(np.sqrt((x1-x8)**2+(y1-y8)**2))**3 + f1*M2*(y2-y8)/(np.sqrt((x2-x8)**2+(y2-y8)**2))**3 + f1*M3*(y3-y8)/(np.sqrt((x3-x8)**2+(y3-y8)**2))**3 + f1*M4*(y4-y8)/(np.sqrt((x4-x8)**2+(y4-y8)**2))**3 + f1*M5*(y5-y8)/(np.sqrt((x5-x8)**2+(y5-y8)**2))**3 + f1*M6*(y6-y8)/(np.sqrt((x6-x8)**2+(y6-y8)**2))**3 + f1*M7*(y7-y8)/(np.sqrt((x7-x8)**2+(y7-y8)**2))**3 + f1*M9*(y9-y8)/(np.sqrt((x9-x8)**2+(y9-y8)**2))**3 + f1*M10*(y10-y8)/(np.sqrt((x10-x8)**2+(y10-y8)**2))**3 + f1*M11*(y11-y8)/(np.sqrt((x11-x8)**2+(y11-y8)**2))**3 + f1*M12*(y12-y8)/(np.sqrt((x12-x8)**2+(y12-y8)**2))**3 + f1*M13*(y13-y8)/(np.sqrt((x13-x8)**2+(y13-y8)**2))**3 + f1*M14*(y14-y8)/(np.sqrt((x14-x8)**2+(y14-y8)**2))**3,
       f1*M0*(x0-x9)/(np.sqrt((x0-x9)**2+(y0-y9)**2))**3 + f1*M1*(x1-x9)/(np.sqrt((x1-x9)**2+(y1-y9)**2))**3 + f1*M2*(x2-x9)/(np.sqrt((x2-x9)**2+(y2-y9)**2))**3 + f1*M3*(x3-x9)/(np.sqrt((x3-x9)**2+(y3-y9)**2))**3 + f1*M4*(x4-x9)/(np.sqrt((x4-x9)**2+(y4-y9)**2))**3 + f1*M5*(x5-x9)/(np.sqrt((x5-x9)**2+(y5-y9)**2))**3 + f1*M6*(x6-x9)/(np.sqrt((x6-x9)**2+(y6-y9)**2))**3 + f1*M7*(x7-x9)/(np.sqrt((x7-x9)**2+(y7-y9)**2))**3 + f1*M8*(x8-x9)/(np.sqrt((x8-x9)**2+(y8-y9)**2))**3 + f1*M10*(x10-x9)/(np.sqrt((x10-x9)**2+(y10-y9)**2))**3 + f1*M11*(x11-x9)/(np.sqrt((x11-x9)**2+(y11-y9)**2))**3 + f1*M12*(x12-x9)/(np.sqrt((x12-x9)**2+(y12-y9)**2))**3 + f1*M13*(x13-x9)/(np.sqrt((x13-x9)**2+(y13-y9)**2))**3 + f1*M14*(x14-x9)/(np.sqrt((x14-x9)**2+(y14-y9)**2))**3,
       f1*M0*(y0-y9)/(np.sqrt((x0-x9)**2+(y0-y9)**2))**3 + f1*M1*(y1-y9)/(np.sqrt((x1-x9)**2+(y1-y9)**2))**3 + f1*M2*(y2-y9)/(np.sqrt((x2-x9)**2+(y2-y9)**2))**3 + f1*M3*(y3-y9)/(np.sqrt((x3-x9)**2+(y3-y9)**2))**3 + f1*M4*(y4-y9)/(np.sqrt((x4-x9)**2+(y4-y9)**2))**3 + f1*M5*(y5-y9)/(np.sqrt((x5-x9)**2+(y5-y9)**2))**3 + f1*M6*(y6-y9)/(np.sqrt((x6-x9)**2+(y6-y9)**2))**3 + f1*M7*(y7-y9)/(np.sqrt((x7-x9)**2+(y7-y9)**2))**3 + f1*M8*(y8-y9)/(np.sqrt((x8-x9)**2+(y8-y9)**2))**3 + f1*M10*(y10-y9)/(np.sqrt((x10-x9)**2+(y10-y9)**2))**3 + f1*M11*(y11-y9)/(np.sqrt((x11-x9)**2+(y11-y9)**2))**3 + f1*M12*(y12-y9)/(np.sqrt((x12-x9)**2+(y12-y9)**2))**3 + f1*M13*(y13-y9)/(np.sqrt((x13-x9)**2+(y13-y9)**2))**3 + f1*M14*(y14-y9)/(np.sqrt((x14-x9)**2+(y14-y9)**2))**3,
       f1*M0*(x0-x10)/(np.sqrt((x0-x10)**2+(y0-y10)**2))**3 + f1*M1*(x1-x10)/(np.sqrt((x1-x10)**2+(y1-y10)**2))**3 + f1*M2*(x2-x10)/(np.sqrt((x2-x10)**2+(y2-y10)**2))**3 + f1*M3*(x3-x10)/(np.sqrt((x3-x10)**2+(y3-y10)**2))**3 + f1*M4*(x4-x10)/(np.sqrt((x4-x10)**2+(y4-y10)**2))**3 + f1*M5*(x5-x10)/(np.sqrt((x5-x10)**2+(y5-y10)**2))**3 + f1*M6*(x6-x10)/(np.sqrt((x6-x10)**2+(y6-y10)**2))**3 + f1*M7*(x7-x10)/(np.sqrt((x7-x10)**2+(y7-y10)**2))**3 + f1*M8*(x8-x10)/(np.sqrt((x8-x10)**2+(y8-y10)**2))**3 + f1*M9*(x9-x10)/(np.sqrt((x9-x10)**2+(y9-y10)**2))**3 + f1*M11*(x11-x10)/(np.sqrt((x11-x10)**2+(y11-y10)**2))**3 + f1*M12*(x12-x10)/(np.sqrt((x12-x10)**2+(y12-y10)**2))**3 + f1*M13*(x13-x10)/(np.sqrt((x13-x10)**2+(y13-y10)**2))**3 + f1*M14*(x14-x10)/(np.sqrt((x14-x10)**2+(y14-y10)**2))**3,
       f1*M0*(y0-y10)/(np.sqrt((x0-x10)**2+(y0-y10)**2))**3 + f1*M1*(y1-y10)/(np.sqrt((x1-x10)**2+(y1-y10)**2))**3 + f1*M2*(y2-y10)/(np.sqrt((x2-x10)**2+(y2-y10)**2))**3 + f1*M3*(y3-y10)/(np.sqrt((x3-x10)**2+(y3-y10)**2))**3 + f1*M4*(y4-y10)/(np.sqrt((x4-x10)**2+(y4-y10)**2))**3 + f1*M5*(y5-y10)/(np.sqrt((x5-x10)**2+(y5-y10)**2))**3 + f1*M6*(y6-y10)/(np.sqrt((x6-x10)**2+(y6-y10)**2))**3 + f1*M7*(y7-y10)/(np.sqrt((x7-x10)**2+(y7-y10)**2))**3 + f1*M8*(y8-y10)/(np.sqrt((x8-x10)**2+(y8-y10)**2))**3 + f1*M9*(y9-y10)/(np.sqrt((x9-x10)**2+(y9-y10)**2))**3 + f1*M11*(y11-y10)/(np.sqrt((x11-x10)**2+(y11-y10)**2))**3 + f1*M12*(y12-y10)/(np.sqrt((x12-x10)**2+(y12-y10)**2))**3 + f1*M13*(y13-y10)/(np.sqrt((x13-x10)**2+(y13-y10)**2))**3 + f1*M14*(y14-y10)/(np.sqrt((x14-x10)**2+(y14-y10)**2))**3,
       f1*M0*(x0-x11)/(np.sqrt((x0-x11)**2+(y0-y11)**2))**3 + f1*M1*(x1-x11)/(np.sqrt((x1-x11)**2+(y1-y11)**2))**3 + f1*M2*(x2-x11)/(np.sqrt((x2-x11)**2+(y2-y11)**2))**3 + f1*M3*(x3-x11)/(np.sqrt((x3-x11)**2+(y3-y11)**2))**3 + f1*M4*(x4-x11)/(np.sqrt((x4-x11)**2+(y4-y11)**2))**3 + f1*M5*(x5-x11)/(np.sqrt((x5-x11)**2+(y5-y11)**2))**3 + f1*M6*(x6-x11)/(np.sqrt((x6-x11)**2+(y6-y11)**2))**3 + f1*M7*(x7-x11)/(np.sqrt((x7-x11)**2+(y7-y11)**2))**3 + f1*M8*(x8-x11)/(np.sqrt((x8-x11)**2+(y8-y11)**2))**3 + f1*M9*(x9-x11)/(np.sqrt((x9-x11)**2+(y9-y11)**2))**3 + f1*M10*(x10-x11)/(np.sqrt((x10-x11)**2+(y10-y11)**2))**3 + f1*M12*(x12-x11)/(np.sqrt((x12-x11)**2+(y12-y11)**2))**3 + f1*M13*(x13-x11)/(np.sqrt((x13-x11)**2+(y13-y11)**2))**3 + f1*M14*(x14-x11)/(np.sqrt((x14-x11)**2+(y14-y11)**2))**3,
       f1*M0*(y0-y11)/(np.sqrt((x0-x11)**2+(y0-y11)**2))**3 + f1*M1*(y1-y11)/(np.sqrt((x1-x11)**2+(y1-y11)**2))**3 + f1*M2*(y2-y11)/(np.sqrt((x2-x11)**2+(y2-y11)**2))**3 + f1*M3*(y3-y11)/(np.sqrt((x3-x11)**2+(y3-y11)**2))**3 + f1*M4*(y4-y11)/(np.sqrt((x4-x11)**2+(y4-y11)**2))**3 + f1*M5*(y5-y11)/(np.sqrt((x5-x11)**2+(y5-y11)**2))**3 + f1*M6*(y6-y11)/(np.sqrt((x6-x11)**2+(y6-y11)**2))**3 + f1*M7*(y7-y11)/(np.sqrt((x7-x11)**2+(y7-y11)**2))**3 + f1*M8*(y8-y11)/(np.sqrt((x8-x11)**2+(y8-y11)**2))**3 + f1*M9*(y9-y11)/(np.sqrt((x9-x11)**2+(y9-y11)**2))**3 + f1*M10*(y10-y11)/(np.sqrt((x10-x11)**2+(y10-y11)**2))**3 + f1*M12*(y12-y11)/(np.sqrt((x12-x11)**2+(y12-y11)**2))**3 + f1*M13*(y13-y11)/(np.sqrt((x13-x11)**2+(y13-y11)**2))**3 + f1*M14*(y14-y11)/(np.sqrt((x14-x11)**2+(y14-y11)**2))**3,
       f1*M0*(x0-x12)/(np.sqrt((x0-x12)**2+(y0-y12)**2))**3 + f1*M1*(x1-x12)/(np.sqrt((x1-x12)**2+(y1-y12)**2))**3 + f1*M2*(x2-x12)/(np.sqrt((x2-x12)**2+(y2-y12)**2))**3 + f1*M3*(x3-x12)/(np.sqrt((x3-x12)**2+(y3-y12)**2))**3 + f1*M4*(x4-x12)/(np.sqrt((x4-x12)**2+(y4-y12)**2))**3 + f1*M5*(x5-x12)/(np.sqrt((x5-x12)**2+(y5-y12)**2))**3 + f1*M6*(x6-x12)/(np.sqrt((x6-x12)**2+(y6-y12)**2))**3 + f1*M7*(x7-x12)/(np.sqrt((x7-x12)**2+(y7-y12)**2))**3 + f1*M8*(x8-x12)/(np.sqrt((x8-x12)**2+(y8-y12)**2))**3 + f1*M9*(x9-x12)/(np.sqrt((x9-x12)**2+(y9-y12)**2))**3 + f1*M10*(x10-x12)/(np.sqrt((x10-x12)**2+(y10-y12)**2))**3 + f1*M11*(x11-x12)/(np.sqrt((x11-x12)**2+(y11-y12)**2))**3 + f1*M13*(x13-x12)/(np.sqrt((x13-x12)**2+(y13-y12)**2))**3 + f1*M14*(x14-x12)/(np.sqrt((x14-x12)**2+(y14-y12)**2))**3,
       f1*M0*(y0-y12)/(np.sqrt((x0-x12)**2+(y0-y12)**2))**3 + f1*M1*(y1-y12)/(np.sqrt((x1-x12)**2+(y1-y12)**2))**3 + f1*M2*(y2-y12)/(np.sqrt((x2-x12)**2+(y2-y12)**2))**3 + f1*M3*(y3-y12)/(np.sqrt((x3-x12)**2+(y3-y12)**2))**3 + f1*M4*(y4-y12)/(np.sqrt((x4-x12)**2+(y4-y12)**2))**3 + f1*M5*(y5-y12)/(np.sqrt((x5-x12)**2+(y5-y12)**2))**3 + f1*M6*(y6-y12)/(np.sqrt((x6-x12)**2+(y6-y12)**2))**3 + f1*M7*(y7-y12)/(np.sqrt((x7-x12)**2+(y7-y12)**2))**3 + f1*M8*(y8-y12)/(np.sqrt((x8-x12)**2+(y8-y12)**2))**3 + f1*M9*(y9-y12)/(np.sqrt((x9-x12)**2+(y9-y12)**2))**3 + f1*M10*(y10-y12)/(np.sqrt((x10-x12)**2+(y10-y12)**2))**3 + f1*M11*(y11-y12)/(np.sqrt((x11-x12)**2+(y11-y12)**2))**3 + f1*M13*(y13-y12)/(np.sqrt((x13-x12)**2+(y13-y12)**2))**3 + f1*M14*(y14-y12)/(np.sqrt((x14-x12)**2+(y14-y12)**2))**3,
       f1*M0*(x0-x13)/(np.sqrt((x0-x13)**2+(y0-y13)**2))**3 + f1*M1*(x1-x13)/(np.sqrt((x1-x13)**2+(y1-y13)**2))**3 + f1*M2*(x2-x13)/(np.sqrt((x2-x13)**2+(y2-y13)**2))**3 + f1*M3*(x3-x13)/(np.sqrt((x3-x13)**2+(y3-y13)**2))**3 + f1*M4*(x4-x13)/(np.sqrt((x4-x13)**2+(y4-y13)**2))**3 + f1*M5*(x5-x13)/(np.sqrt((x5-x13)**2+(y5-y13)**2))**3 + f1*M6*(x6-x13)/(np.sqrt((x6-x13)**2+(y6-y13)**2))**3 + f1*M7*(x7-x13)/(np.sqrt((x7-x13)**2+(y7-y13)**2))**3 + f1*M8*(x8-x13)/(np.sqrt((x8-x13)**2+(y8-y13)**2))**3 + f1*M9*(x9-x13)/(np.sqrt((x9-x13)**2+(y9-y13)**2))**3 + f1*M10*(x10-x13)/(np.sqrt((x10-x13)**2+(y10-y13)**2))**3 + f1*M11*(x11-x13)/(np.sqrt((x11-x13)**2+(y11-y13)**2))**3 + f1*M12*(x12-x13)/(np.sqrt((x12-x13)**2+(y12-y13)**2))**3 + f1*M14*(x14-x13)/(np.sqrt((x14-x13)**2+(y14-y13)**2))**3,
       f1*M0*(y0-y13)/(np.sqrt((x0-x13)**2+(y0-y13)**2))**3 + f1*M1*(y1-y13)/(np.sqrt((x1-x13)**2+(y1-y13)**2))**3 + f1*M2*(y2-y13)/(np.sqrt((x2-x13)**2+(y2-y13)**2))**3 + f1*M3*(y3-y13)/(np.sqrt((x3-x13)**2+(y3-y13)**2))**3 + f1*M4*(y4-y13)/(np.sqrt((x4-x13)**2+(y4-y13)**2))**3 + f1*M5*(y5-y13)/(np.sqrt((x5-x13)**2+(y5-y13)**2))**3 + f1*M6*(y6-y13)/(np.sqrt((x6-x13)**2+(y6-y13)**2))**3 + f1*M7*(y7-y13)/(np.sqrt((x7-x13)**2+(y7-y13)**2))**3 + f1*M8*(y8-y13)/(np.sqrt((x8-x13)**2+(y8-y13)**2))**3 + f1*M9*(y9-y13)/(np.sqrt((x9-x13)**2+(y9-y13)**2))**3 + f1*M10*(y10-y13)/(np.sqrt((x10-x13)**2+(y10-y13)**2))**3 + f1*M11*(y11-y13)/(np.sqrt((x11-x13)**2+(y11-y13)**2))**3 + f1*M12*(y12-y13)/(np.sqrt((x12-x13)**2+(y12-y13)**2))**3 + f1*M14*(y14-y13)/(np.sqrt((x14-x13)**2+(y14-y13)**2))**3,
       f1*M0*(x0-x14)/(np.sqrt((x0-x14)**2+(y0-y14)**2))**3 + f1*M1*(x1-x14)/(np.sqrt((x1-x14)**2+(y1-y14)**2))**3 + f1*M2*(x2-x14)/(np.sqrt((x2-x14)**2+(y2-y14)**2))**3 + f1*M3*(x3-x14)/(np.sqrt((x3-x14)**2+(y3-y14)**2))**3 + f1*M4*(x4-x14)/(np.sqrt((x4-x14)**2+(y4-y14)**2))**3 + f1*M5*(x5-x14)/(np.sqrt((x5-x14)**2+(y5-y14)**2))**3 + f1*M6*(x6-x14)/(np.sqrt((x6-x14)**2+(y6-y14)**2))**3 + f1*M7*(x7-x14)/(np.sqrt((x7-x14)**2+(y7-y14)**2))**3 + f1*M8*(x8-x14)/(np.sqrt((x8-x14)**2+(y8-y14)**2))**3 + f1*M9*(x9-x14)/(np.sqrt((x9-x14)**2+(y9-y14)**2))**3 + f1*M10*(x10-x14)/(np.sqrt((x10-x14)**2+(y10-y14)**2))**3 + f1*M11*(x11-x14)/(np.sqrt((x11-x14)**2+(y11-y14)**2))**3 + f1*M12*(x12-x14)/(np.sqrt((x12-x14)**2+(y12-y14)**2))**3 + f1*M13*(x13-x14)/(np.sqrt((x13-x14)**2+(y13-y14)**2))**3,
       f1*M0*(y0-y14)/(np.sqrt((x0-x14)**2+(y0-y14)**2))**3 + f1*M1*(y1-y14)/(np.sqrt((x1-x14)**2+(y1-y14)**2))**3 + f1*M2*(y2-y14)/(np.sqrt((x2-x14)**2+(y2-y14)**2))**3 + f1*M3*(y3-y14)/(np.sqrt((x3-x14)**2+(y3-y14)**2))**3 + f1*M4*(y4-y14)/(np.sqrt((x4-x14)**2+(y4-y14)**2))**3 + f1*M5*(y5-y14)/(np.sqrt((x5-x14)**2+(y5-y14)**2))**3 + f1*M6*(y6-y14)/(np.sqrt((x6-x14)**2+(y6-y14)**2))**3 + f1*M7*(y7-y14)/(np.sqrt((x7-x14)**2+(y7-y14)**2))**3 + f1*M8*(y8-y14)/(np.sqrt((x8-x14)**2+(y8-y14)**2))**3 + f1*M9*(y9-y14)/(np.sqrt((x9-x14)**2+(y9-y14)**2))**3 + f1*M10*(y10-y14)/(np.sqrt((x10-x14)**2+(y10-y14)**2))**3 + f1*M11*(y11-y14)/(np.sqrt((x11-x14)**2+(y11-y14)**2))**3 + f1*M12*(y12-y14)/(np.sqrt((x12-x14)**2+(y12-y14)**2))**3 + f1*M13*(y13-y14)/(np.sqrt((x13-x14)**2+(y13-y14)**2))**3,
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
       vy9,
       vx10,
       vy10,
       vx11,
       vy11,
       vx12,
       vy12,
       vx13,
       vy13,
       vx14,
       vy14
       ]
y0=[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, vx10, vy10, vx11, vy11, vx12, vy12, vx13, vy13, vx14, vy14, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14]
[vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, vx9, vy9, vx10, vy10, vx11, vy11, vx12, vy12, vx13, vy13, vx14, vy14, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14]= odeint(f, y0, t, args=(params,), full_output=False).T
c1=M0*(x0*vy0-y0*vx0)+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)+M3*(x3*vy3-y3*vx3)+M4*(x4*vy4-y4*vx4)+M5*(x5*vy5-y5*vx5)+M6*(x6*vy6-y6*vx6)+M7*(x7*vy7-y7*vx7)+M8*(x8*vy8-y8*vx8)+M9*(x9*vy9-y9*vx9)+M10*(x10*vy10-y10*vx10)+M11*(x11*vy11-y11*vx11)+M12*(x12*vy12-y12*vx12)+M13*(x13*vy13-y13*vx13)+M14*(x14*vy14-y14*vx14)
U=f1*(M0*M1/(np.sqrt((x1-x0)**2+(y1-y0)**2))) + f1*(M0*M2/(np.sqrt((x0-x2)**2+(y0-y2)**2))) + f1*(M0*M3/(np.sqrt((x0-x3)**2+(y0-y3)**2))) + f1*(M0*M4/(np.sqrt((x0-x4)**2+(y0-y4)**2))) + f1*(M0*M5/(np.sqrt((x0-x5)**2+(y0-y5)**2))) + f1*(M0*M6/(np.sqrt((x0-x6)**2+(y0-y6)**2))) + f1*(M0*M7/(np.sqrt((x0-x7)**2+(y0-y7)**2))) + f1*(M0*M8/(np.sqrt((x0-x8)**2+(y0-y8)**2))) + f1*(M0*M9/(np.sqrt((x0-x9)**2+(y0-y9)**2))) + f1*(M0*M10/(np.sqrt((x0-x10)**2+(y0-y10)**2))) + f1*(M0*M11/(np.sqrt((x0-x11)**2+(y0-y11)**2))) + f1*(M0*M12/(np.sqrt((x0-x12)**2+(y0-y12)**2))) + f1*(M0*M13/(np.sqrt((x0-x13)**2+(y0-y13)**2))) + f1*(M0*M14/(np.sqrt((x0-x14)**2+(y0-y14)**2))) + f1*(M1*M2/(np.sqrt((x1-x2)**2+(y1-y2)**2))) + f1*(M1*M3/(np.sqrt((x1-x3)**2+(y1-y3)**2))) + f1*(M1*M4/(np.sqrt((x1-x4)**2+(y1-y4)**2))) + f1*(M1*M5/(np.sqrt((x1-x5)**2+(y1-y5)**2))) + f1*(M1*M6/(np.sqrt((x1-x6)**2+(y1-y6)**2))) + f1*(M1*M7/(np.sqrt((x1-x7)**2+(y1-y7)**2))) + f1*(M1*M8/(np.sqrt((x1-x8)**2+(y1-y8)**2))) + f1*(M1*M9/(np.sqrt((x1-x9)**2+(y1-y9)**2))) + f1*(M1*M10/(np.sqrt((x1-x10)**2+(y1-y10)**2))) + f1*(M1*M11/(np.sqrt((x1-x11)**2+(y1-y11)**2))) + f1*(M1*M12/(np.sqrt((x1-x12)**2+(y1-y12)**2))) + f1*(M1*M13/(np.sqrt((x1-x13)**2+(y1-y13)**2))) + f1*(M1*M14/(np.sqrt((x1-x14)**2+(y1-y14)**2))) + f1*(M2*M3/(np.sqrt((x2-x3)**2+(y2-y3)**2))) + f1*(M2*M4/(np.sqrt((x2-x4)**2+(y2-y4)**2))) + f1*(M2*M5/(np.sqrt((x2-x5)**2+(y2-y5)**2))) + f1*(M2*M6/(np.sqrt((x2-x6)**2+(y2-y6)**2))) + f1*(M2*M7/(np.sqrt((x2-x7)**2+(y2-y7)**2))) + f1*(M2*M8/(np.sqrt((x2-x8)**2+(y2-y8)**2))) + f1*(M2*M9/(np.sqrt((x2-x9)**2+(y2-y9)**2))) + f1*(M2*M10/(np.sqrt((x2-x10)**2+(y2-y10)**2))) + f1*(M2*M11/(np.sqrt((x2-x11)**2+(y2-y11)**2))) + f1*(M2*M12/(np.sqrt((x2-x12)**2+(y2-y12)**2))) + f1*(M2*M13/(np.sqrt((x2-x13)**2+(y2-y13)**2))) + f1*(M2*M14/(np.sqrt((x2-x14)**2+(y2-y14)**2))) + f1*(M3*M4/(np.sqrt((x3-x4)**2+(y3-y4)**2))) + f1*(M3*M5/(np.sqrt((x3-x5)**2+(y3-y5)**2))) + f1*(M3*M6/(np.sqrt((x3-x6)**2+(y3-y6)**2))) + f1*(M3*M7/(np.sqrt((x3-x7)**2+(y3-y7)**2))) + f1*(M3*M8/(np.sqrt((x3-x8)**2+(y3-y8)**2))) + f1*(M3*M9/(np.sqrt((x3-x9)**2+(y3-y9)**2))) + f1*(M3*M10/(np.sqrt((x3-x10)**2+(y3-y10)**2))) + f1*(M3*M11/(np.sqrt((x3-x11)**2+(y3-y11)**2))) + f1*(M3*M12/(np.sqrt((x3-x12)**2+(y3-y12)**2))) + f1*(M3*M13/(np.sqrt((x3-x13)**2+(y3-y13)**2))) + f1*(M3*M14/(np.sqrt((x3-x14)**2+(y3-y14)**2))) + f1*(M4*M5/(np.sqrt((x4-x5)**2+(y4-y5)**2))) + f1*(M4*M6/(np.sqrt((x4-x6)**2+(y4-y6)**2))) + f1*(M4*M7/(np.sqrt((x4-x7)**2+(y4-y7)**2))) + f1*(M4*M8/(np.sqrt((x4-x8)**2+(y4-y8)**2))) + f1*(M4*M9/(np.sqrt((x4-x9)**2+(y4-y9)**2))) + f1*(M4*M10/(np.sqrt((x4-x10)**2+(y4-y10)**2))) + f1*(M4*M11/(np.sqrt((x4-x11)**2+(y4-y11)**2))) + f1*(M4*M12/(np.sqrt((x4-x12)**2+(y4-y12)**2))) + f1*(M4*M13/(np.sqrt((x4-x13)**2+(y4-y13)**2))) + f1*(M4*M14/(np.sqrt((x4-x14)**2+(y4-y14)**2))) + f1*(M5*M6/(np.sqrt((x5-x6)**2+(y5-y6)**2))) + f1*(M5*M7/(np.sqrt((x5-x7)**2+(y5-y7)**2))) + f1*(M5*M8/(np.sqrt((x5-x8)**2+(y5-y8)**2))) + f1*(M5*M9/(np.sqrt((x5-x9)**2+(y5-y9)**2))) + f1*(M5*M10/(np.sqrt((x5-x10)**2+(y5-y10)**2))) + f1*(M5*M11/(np.sqrt((x5-x11)**2+(y5-y11)**2))) + f1*(M5*M12/(np.sqrt((x5-x12)**2+(y5-y12)**2))) + f1*(M5*M13/(np.sqrt((x5-x13)**2+(y5-y13)**2))) + f1*(M5*M14/(np.sqrt((x5-x14)**2+(y5-y14)**2))) + f1*(M6*M7/(np.sqrt((x6-x7)**2+(y6-y7)**2))) + f1*(M6*M8/(np.sqrt((x6-x8)**2+(y6-y8)**2))) + f1*(M6*M9/(np.sqrt((x6-x9)**2+(y6-y9)**2))) + f1*(M6*M10/(np.sqrt((x6-x10)**2+(y6-y10)**2))) + f1*(M6*M11/(np.sqrt((x6-x11)**2+(y6-y11)**2))) + f1*(M6*M12/(np.sqrt((x6-x12)**2+(y6-y12)**2))) + f1*(M6*M13/(np.sqrt((x6-x13)**2+(y6-y13)**2))) + f1*(M6*M14/(np.sqrt((x6-x14)**2+(y6-y14)**2))) + f1*(M7*M8/(np.sqrt((x7-x8)**2+(y7-y8)**2))) + f1*(M7*M9/(np.sqrt((x7-x9)**2+(y7-y9)**2))) + f1*(M7*M10/(np.sqrt((x7-x10)**2+(y7-y10)**2))) + f1*(M7*M11/(np.sqrt((x7-x11)**2+(y7-y11)**2))) + f1*(M7*M12/(np.sqrt((x7-x12)**2+(y7-y12)**2))) + f1*(M7*M13/(np.sqrt((x7-x13)**2+(y7-y13)**2))) + f1*(M7*M14/(np.sqrt((x7-x14)**2+(y7-y14)**2))) + f1*(M8*M9/(np.sqrt((x8-x9)**2+(y8-y9)**2))) + f1*(M8*M10/(np.sqrt((x8-x10)**2+(y8-y10)**2))) + f1*(M8*M11/(np.sqrt((x8-x11)**2+(y8-y11)**2))) + f1*(M8*M12/(np.sqrt((x8-x12)**2+(y8-y12)**2))) + f1*(M8*M13/(np.sqrt((x8-x13)**2+(y8-y13)**2))) + f1*(M8*M14/(np.sqrt((x8-x14)**2+(y8-y14)**2))) + f1*(M9*M10/(np.sqrt((x9-x10)**2+(y9-y10)**2))) + f1*(M9*M11/(np.sqrt((x9-x11)**2+(y9-y11)**2))) + f1*(M9*M12/(np.sqrt((x9-x12)**2+(y9-y12)**2))) + f1*(M9*M13/(np.sqrt((x9-x13)**2+(y9-y13)**2))) + f1*(M9*M14/(np.sqrt((x9-x14)**2+(y9-y14)**2))) + f1*(M10*M11/(np.sqrt((x10-x11)**2+(y10-y11)**2))) + f1*(M10*M12/(np.sqrt((x10-x12)**2+(y10-y12)**2))) + f1*(M10*M13/(np.sqrt((x10-x13)**2+(y10-y13)**2))) + f1*(M10*M14/(np.sqrt((x10-x14)**2+(y10-y14)**2))) + f1*(M11*M12/(np.sqrt((x11-x12)**2+(y11-y12)**2))) + f1*(M11*M13/(np.sqrt((x11-x13)**2+(y11-y13)**2))) + f1*(M11*M14/(np.sqrt((x11-x14)**2+(y11-y14)**2))) + f1*(M12*M13/(np.sqrt((x12-x13)**2+(y12-y13)**2))) + f1*(M12*M14/(np.sqrt((x12-x14)**2+(y12-y14)**2))) + f1*(M13*M14/(np.sqrt((x13-x14)**2+(y13-y14)**2)))
H=M0/2*(vy0**2+vx0**2) +M1/2*(vy1**2+vx1**2) +M2/2*(vy2**2+vx2**2) +M3/2*(vy3**2+vx3**2) +M4/2*(vy4**2+vx4**2) +M5/2*(vy5**2+vx5**2) +M6/2*(vy6**2+vx6**2) +M7/2*(vy7**2+vx7**2) +M8/2*(vy8**2+vx8**2) +M9/2*(vy9**2+vx9**2) +M10/2*(vy10**2+vx10**2) +M11/2*(vy11**2+vx11**2) +M12/2*(vy12**2+vx12**2) +M13/2*(vy13**2+vx13**2) +M14/2*(vy14**2+vx14**2)-U
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
text_filec10 = open('Nbody/Coords/coord10_NumOne.txt', 'w')
text_files10=open('Nbody/Coords/speed10_NumOne.txt', 'w')
text_filec11 = open('Nbody/Coords/coord11_NumOne.txt', 'w')
text_files11=open('Nbody/Coords/speed11_NumOne.txt', 'w')
text_filec12 = open('Nbody/Coords/coord12_NumOne.txt', 'w')
text_files12=open('Nbody/Coords/speed12_NumOne.txt', 'w')
text_filec13 = open('Nbody/Coords/coord13_NumOne.txt', 'w')
text_files13=open('Nbody/Coords/speed13_NumOne.txt', 'w')
text_filec14 = open('Nbody/Coords/coord14_NumOne.txt', 'w')
text_files14=open('Nbody/Coords/speed14_NumOne.txt', 'w')
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
   text_filec10.write(str(x10[i])+';'+str(y10[i])+'\n')
   text_files10.write(str(vx10[i])+';'+str(vy10[i])+'\n')
   text_filec11.write(str(x11[i])+';'+str(y11[i])+'\n')
   text_files11.write(str(vx11[i])+';'+str(vy11[i])+'\n')
   text_filec12.write(str(x12[i])+';'+str(y12[i])+'\n')
   text_files12.write(str(vx12[i])+';'+str(vy12[i])+'\n')
   text_filec13.write(str(x13[i])+';'+str(y13[i])+'\n')
   text_files13.write(str(vx13[i])+';'+str(vy13[i])+'\n')
   text_filec14.write(str(x14[i])+';'+str(y14[i])+'\n')
   text_files14.write(str(vx14[i])+';'+str(vy14[i])+'\n')
Hfile=open('Nbody/Coords/H_NumOne.txt', 'w')
Cfile=open('Nbody/Coords/C_NumOne.txt', 'w')
for i in range(len(t)):
   Hfile.write(str(t[i])+';'+str(HH[i])+'\n')
   Cfile.write(str(t[i])+';'+str(CC[i])+'\n')
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
text_filec10.close()
text_files10.close()
text_filec11.close()
text_files11.close()
text_filec12.close()
text_files12.close()
text_filec13.close()
text_files13.close()
text_filec14.close()
text_files14.close()
Hfile.close()
Cfile.close()
