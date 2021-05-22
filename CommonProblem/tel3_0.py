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

M0_M1_data = open('CommonProblem/Params/M0-M1.txt', 'r').read()
M2_f_data = open('CommonProblem/Params/M2-f.txt', 'r').read()
steps_t_data = open('CommonProblem/Params/steps-t.txt', 'r').read()

r1x_r1y_data = open('CommonProblem/Params/r1x-r1y.txt', 'r').read()
r2x_r2y_data = open('CommonProblem/Params/r2x-r2y.txt', 'r').read()
v1x_v1y_data = open('CommonProblem/Params/v1x-v1y.txt', 'r').read()
v2x_v2y_data = open('CommonProblem/Params/v2x-v2y.txt', 'r').read()

M0_M1 = M0_M1_data.split('\n')
M2_f = M2_f_data.split('\n')
steps_t = steps_t_data.split('\n')

r1x_r1y = r1x_r1y_data.split('\n')
r2x_r2y = r2x_r2y_data.split('\n')
v1x_v1y = v1x_v1y_data.split('\n')
v2x_v2y = v2x_v2y_data.split('\n')

r1x_date, r1y_date, r2x_date, r2y_date = [], [], [], []
v1x_date, v1y_date, v2x_date, v2y_date = [], [], [], []

for line in r1x_r1y:
    if len(line) > 1:
        x, y = line.split(';')
        r1x_date.append(float(x))
        r1y_date.append(float(y))
for line in r2x_r2y:
    if len(line) > 1:
        x, y = line.split(';')
        r2x_date.append(float(x))
        r2y_date.append(float(y))
for line in v1x_v1y:
    if len(line) > 1:
        x, y = line.split(';')
        v1x_date.append(float(x))
        v1y_date.append(float(y))
for line in v2x_v2y:
    if len(line) > 1:
        x, y = line.split(';')
        v2x_date.append(float(x))
        v2y_date.append(float(y))

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
t = np.arange(0, steps_date[0], t_date[0])
params = [M0, M1, M2, f1]


def f(y, t, params):  # 14.1' с 731
    vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2 = y
    M0, M1, M2, f1 = params
    return [f1 * M1 * (x1 - x0) / (np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)) ** 3 + f1 * M2 * (x2 - x0) / (
        np.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2)) ** 3,
            f1 * M1 * (y1 - y0) / (np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)) ** 3 + f1 * M2 * (y2 - y0) / (
                np.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2)) ** 3,
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


# pir = result[0]
x1 = r1x_date[0]#133.97685159
y1 = r1y_date[0]#0
vx1 = v1x_date[0]#0
vy1 = v1y_date[0]#1492.79519281
x2 = r2x_date[0]#-133.902558073980
y2 = r2y_date[0]#1.63983339142942e-14
vx2 = v2x_date[0]#-1.82713310151027e-13
vy2 = v2y_date[0]#-1491.96740054552
# поиск координат и скоростей 1 тела по 14.3
vx0 = (-vx2 * M2 - vx1 * M1) / M0
vy0 = (-vy1 * M1 - vy2 * M2) / M0
x0 = (-x1 * M1 - x2 * M2) / M0
y0 = (-y2 * M2 - y1 * M1) / M0

y0 = [vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2]
[vx0, vy0, vx1, vy1, vx2, vy2, x0, y0, x1, y1, x2, y2] = odeint(f, y0, t, args=(params,), full_output=False).T
c = M0 * (x0 * vy0 - y0 * vx0) + M1 * (x1 * vy1 - y1 * vx1) + M2 * (x2 * vy2 - y2 * vx2)  # проверка 14.3'
U = f1 * (M0 * M1 / (np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)) + M0 * M2 / (
    np.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2)) + M2 * M1 / (
              np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))  # полная силовая функция 14.2
H = M0 / 2 * (vy0 ** 2 + vx0 ** 2) + M1 / 2 * (vy1 ** 2 + vx1 ** 2) + M2 / 2 * (
            vy2 ** 2 + vx2 ** 2) - U  # проверка 14.3"


#Create text file
if os.path.exists("CommonProblem/Coords"):
    print("Папка Coords уже существует")
else:
    os.mkdir("CommonProblem/Coords")
    print("Папка Coords создана")
text_file = open("CommonProblem/Coords/coord0_NumOne.txt", "w")
text_file1 = open("CommonProblem/Coords/coord1_NumOne.txt", "w")
text_file2 = open("CommonProblem/Coords/coord2_NumOne.txt", "w")
text_file3 = open("CommonProblem/Coords/speed0_NumOne.txt", "w")
text_file4 = open("CommonProblem/Coords/speed1_NumOne.txt", "w")
text_file5 = open("CommonProblem/Coords/speed2_NumOne.txt", "w")

for i in range(len(x0)):
    text_file.write(str(x0[i]) + ";" + str(y0[i]) + "\n")
    text_file1.write(str(x1[i]) + ";" + str(y1[i]) + "\n")
    text_file2.write(str(x2[i]) + ";" + str(y2[i]) + "\n")
    text_file3.write(str(vx0[i]) + ";" + str(vy0[i]) + "\n")
    text_file4.write(str(vx1[i]) + ";" + str(vy1[i]) + "\n")
    text_file5.write(str(vx2[i]) + ";" + str(vy2[i]) + "\n")
text_file.close()
text_file1.close()
text_file2.close()
text_file3.close()
text_file4.close()
text_file5.close()


text_file11 = open("CommonProblem/Coords/H_NumOne.txt", "w")
text_file12 = open("CommonProblem/Coords/C_NumOne.txt", "w")
hh = H/H[0]
cc = c/c[0]
for i in range(len(t)):
    text_file11.write(str(round(t[i], 3)) + ";" + str(round(hh[i], 3)) + "\n")
    text_file12.write(str(round(t[i], 3)) + ";" + str(round(cc[i], 3)) + "\n")
text_file11.close()
text_file12.close()
# print(c)
# print((M0*vx0+M1*vx1+M2*vx2)/(M0+M1+M2))
# print(H)
# plt.plot(x1, y1, linewidth=1, color='red')
# plt.plot(x2, y2, linewidth=1, color='blue')
# plt.plot(x0, y0, linewidth=1, color='black')
# plt.grid(True)

# plt.axis('scaled')


# plt.show()
