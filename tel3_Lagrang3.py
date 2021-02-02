import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


f1=1
M0= 1.9885*10**8
M1= M0/332940
M2= M1*317.8
t = np.linspace(0, 4, 101)
#fig = plt.figure(facecolor='white', figsize=(6, 6))
params = [M0, M1, M2,f1]


def f(y, t, params):#14.1' с 731
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


print('ffff',M1)
r1_X_Y_data = open('coord0.txt', 'r').read()
r2_X_Y_data = open('coord1.txt', 'r').read()
r3_X_Y_data = open('coord2.txt', 'r').read()
v1_X_Y_data = open('speed0.txt', 'r').read()
v2_X_Y_data = open('speed1.txt', 'r').read()
v3_X_Y_data = open('speed2.txt', 'r').read()
r1_X_Y_data = r1_X_Y_data.split('\n')
r2_X_Y_data = r2_X_Y_data.split('\n')
r3_X_Y_data = r3_X_Y_data.split('\n')
v1_X_Y_data = v1_X_Y_data.split('\n')
v2_X_Y_data = v2_X_Y_data.split('\n')
v3_X_Y_data = v3_X_Y_data.split('\n')
r1_x_new = []
r1_y_new = []
r2_x_new = []
r2_y_new = []
r3_x_new = []
r3_y_new = []
v1_x_new = []
v1_y_new = []
v2_x_new = []
v2_y_new = []
v3_x_new = []
v3_y_new = []
for line in r1_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        r1_x_new.append(float(x))
        r1_y_new.append(float(y))
for line in r2_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        r2_x_new.append(float(x))
        r2_y_new.append(float(y))

for line in r3_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        r3_x_new.append(float(x))
        r3_y_new.append(float(y))
for line in v1_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        v1_x_new.append(float(x))
        v1_y_new.append(float(y))
for line in v2_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        v2_x_new.append(float(x))
        v2_y_new.append(float(y))
for line in v3_X_Y_data:
    if len(line) > 1:
        x, y = line.split(';')
        v3_x_new.append(float(x))
        v3_y_new.append(float(y))
y0 = [v1_x_new[0], v1_y_new[0], v2_x_new[0], v2_y_new[0], v3_x_new[0], v3_y_new[0], r1_x_new[0], r1_y_new[0], r2_x_new[0], r2_y_new[0], r3_x_new[0],
      r3_y_new[0]]
print(v1_x_new[0])
print(v2_x_new[0])
print(v3_x_new[0])
print(r1_x_new[0])
print(r2_x_new[0])
print(r3_x_new[0])
[vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2] = odeint(f, y0, t, args=(params,), full_output=False).T
c=M0*(x0*vy0-y0*vx0)+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)#проверка 14.3'
U=f1*(M0*M1/(np.sqrt((x1-x0)**2+(y1-y0)**2))+M0*M2/(np.sqrt((x2-x0)**2+(y2-y0)**2))+M2*M1/(np.sqrt((x1-x2)**2+(y1-y2)**2)))#полная силовая функция 14.2
H=M0/2*(vy0**2+vx0**2)+M1/2*(vy1**2+vx1**2)+M2/2*(vy2**2+vx2**2)-U#проверка 14.3"
print('rrr',v1_x_new)
k = (y1- y0)/(x1 - x0)
k1 = (y2 - y1)/(x2 - x1)
k2 = (y2 - y0)/(x2 - y0)
print('k',k)
print('k1',k1)
print('k2',k2)

print(c)
print((M0*vx0+M1*vx1+M2*vx2)/(M0+M1+M2))
print(H)
#plt.plot(x1, y1, linewidth=1, color='red')
#plt.plot(x2, y2, linewidth=1, color='blue')
#plt.plot(x0, y0, linewidth=1, color='black')
#plt.grid(True)

#plt.axis('scaled')


#plt.show()
