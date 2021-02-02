import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

M0_M1_data = open('Params/M0-M1.txt', 'r').read()
M2_f_data = open('Params/M2-f.txt', 'r').read()
steps_t_data = open('Params/steps-t.txt', 'r').read()

M0_M1 = M0_M1_data.split('\n')
M2_f = M2_f_data.split('\n')
steps_t = steps_t_data.split('\n')

M0_date = []
M1_date = []

M2_date = []
f_date = []

steps_date = []
t_date = []
for line in M0_M1:
    if len(line) > 1:
        x, y = line.split(';')
        M0_date.append(float(x))
        M1_date.append(float(y))
for line in M2_f:
    if len(line) > 1:
        x, y = line.split(';')
        M2_date.append(float(x))
        f_date.append(float(y))
for line in steps_t:
    if len(line) > 1:
        x, y = line.split(';')
        steps_date.append(float(x))
        t_date.append(float(y))
f1 = f_date[0]
M0 = M0_date[0]
M1 = M1_date[0]
M2 = M2_date[0]
M=M0+M1+M2
t = np.arange(0, steps_date[0], t_date[0])
#fig = plt.figure(facecolor='white', figsize=(6, 6))
params = [M0, M1, M2,f1]


def f(y, t, params):# 14.6 14.6' с 735
    vx1, vy1, vx2, vy2, x1, y1, x2, y2= y
    M0,M1,M2, f1 = params
    return [
        -f1 * (M0+M2) * x1 / (np.sqrt(x1**2+y1**2) ** 3) +f1 * M2 * ((x2 - x1) /(np.sqrt((x2-x1)**2+(y2-y1)**2) ** 3)-x2/(np.sqrt(x2**2+y2**2))**3),
        -f1 * (M0 + M1) * y1 / (np.sqrt(x1 ** 2 + y1 ** 2) ** 3) + f1 * M2 * (
                    (y2 - y1) / (np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 3) - y2 / (
                np.sqrt(x2 ** 2 + y2 ** 2)) ** 3),
        -f1 * (M0 + M2) * x2 / (np.sqrt(x2 ** 2 + y2 ** 2) ** 3) + f1 * M1 * (
                    (x1 - x2) / (np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 3) - x1 / (
                np.sqrt(x1 ** 2 + y1 ** 2)) ** 3),
        -f1 * (M0 + M2) *y2 / (np.sqrt(x2 ** 2 + y2 ** 2) ** 3) + f1 * M1 * (
                    (y1 - y2) / (np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 3) - y1 / (
                np.sqrt(x1 ** 2 + y1 ** 2)) ** 3),
        vx1,
        vy1,
        vx2,
        vy2
            ]
r1_X_Y_data = open('Coords/coord01.txt', 'r').read()
r2_X_Y_data = open('Coords/coord02.txt', 'r').read()
v1_X_Y_data = open('Coords/speed01.txt', 'r').read()
v2_X_Y_data = open('Coords/speed02.txt', 'r').read()
r1_X_Y_data = r1_X_Y_data.split('\n')
r2_X_Y_data = r2_X_Y_data.split('\n')
v1_X_Y_data = v1_X_Y_data.split('\n')
v2_X_Y_data = v2_X_Y_data.split('\n')
r1_x_new = []
r1_y_new = []
r2_x_new = []
r2_y_new = []
v1_x_new = []
v1_y_new = []
v2_x_new = []
v2_y_new = []
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
#c=M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)
#c=20000
y0 = [v1_x_new[0], v1_y_new[0], v2_x_new[0], v2_y_new[0], r1_x_new[0], r1_y_new[0], r2_x_new[0], r2_y_new[0]]
[vx1, vy1, vx2, vy2, x1, y1, x2, y2] = odeint(f, y0, t, args=(params,), full_output=False).T
#главная система координат переход с 735 ниже 14.7'
xx0=-M1/M*x1-M2/M*x2
xx1=(M2+M0)/M*x1-M2/M*x2
xx2=-M1/M*x1+(M1+M0)/M*x2
yy0=-M1/M*y1-M2/M*y2
yy1=(M2+M0)/M*y1-M2/M*y2
yy2=-M1/M*y1+(M1+M0)/M*y2
print(np.sqrt((xx1-xx2)**2+(yy1-yy2)**2))
print(np.sqrt((xx0-xx2)**2+(yy0-yy2)**2))
print(np.sqrt((xx1-xx0)**2+(yy1-yy0)**2))
#plt.plot(xx1, yy1, linewidth=1, color='red')
#plt.plot(xx2, yy2, linewidth=1, color='blue')
#plt.plot(xx0, yy0, linewidth=1, color='black')
#plt.grid(True)

#plt.axis('scaled')


#plt.show()