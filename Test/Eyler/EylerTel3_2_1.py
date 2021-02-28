import numpy as np
import math as math
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from sympy import *
from datetime import datetime
import time

M0_M1_data = open('Test/Params/M0-M1.txt', 'r').read()
M2_f_data = open('Test/Params/M2-f.txt', 'r').read()
c_e_data = open('Test/Params/c-e.txt', 'r').read()
F_vp_data = open('Test/Params/F-vp.txt', 'r').read()
steps_t_data = open('Test/Params/steps-t.txt', 'r').read()
c_beforeafter = open('Test/Params/cbefore-cafter.txt', 'r').read()
c_steps = open('Test/Params/stepsc-stepsc.txt', 'r').read()
curr_dir_read1 = open('CurDir.txt', 'r')
text_cur_dir = curr_dir_read1.read()
M0_M1 = M0_M1_data.split('\n')
M2_f = M2_f_data.split('\n')
c_e = c_e_data.split('\n')
F_vp = F_vp_data.split('\n')
steps_t = steps_t_data.split('\n')
c_before_c_after = c_beforeafter.split('\n')
c_steps_c_steps = c_steps.split('\n')

M0_date = []
M1_date = []

M2_date = []
f_date = []

c_date = []
e_date = []

F_date = []
vp_date = []

steps_date = []
t_date = []

c_before = []
c_after = []
c_steps2 = []
c_steps1 = []
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
for line in c_e:
    if len(line) > 1:
        x, y = line.split(';')
        c_date.append(float(x))
        e_date.append(float(y))
for line in F_vp:
    if len(line) > 1:
        x, y = line.split(';')
        F_date.append(float(x))
        vp_date.append(float(y))
for line in steps_t:
    if len(line) > 1:
        x, y = line.split(';')
        steps_date.append(float(x))
        t_date.append(float(y))
for line in c_before_c_after:
    if len(line) > 1:
        x, y = line.split(';')
        c_before.append(float(x))
        c_after.append(float(y))
for line in c_steps_c_steps:
    if len(line) > 1:
        x, y = line.split(';')
        c_steps2.append(float(x))
        c_steps1.append(float(y))

f1 = f_date[0]
M0 = M0_date[0]
M1 = M1_date[0]
M2 = M2_date[0]
M = M0 + M1 + M2
a = Symbol('a', real=True)
eq1 = (M0 + M2) * a ** 5 + (2 * M0 + 3 * M2) * a ** 4 + (M0 + 3 * M2) * a ** 3 - (M0 + 3 * M1) * a ** 2 - (
        2 * M0 + 3 * M1) * a - (M0 + M1)
solve_a = solve(eq1, a)
B = solve_a[0]
A = N(B)
nu1 = f1 * ((M0 + M2) - M1 / (A) ** 2 + M1 / (A + 1) ** 2)
e = e_date[0]
#c_mass = np.arange(int(c_before[0]), int(c_after[0]), int(c_steps2[0]))
for c in range(int(c_before[0]), int(c_after[0]), int(c_steps2[0])):
    # c = c_date[0] # произвольная постоянная
    po = c ** 2 / nu1
    p = po / (1 + e)

    phi = math.pi  # задано
    vp = vp_date[0]  # скорость изменения стороны треугольника
    F = F_date[0]  # угол собственного вращения
    params = [M0, M1, M2, f1, c, nu1]
    t = np.arange(0, steps_date[0], t_date[0])


    def f(y, t, params):  # формула 14.26
        vp, p, F = y
        M0, M1, M2, f1, c, nu1 = params
        return [c ** 2 / p ** 3 - nu1 / p ** 2,
                vp,
                c / (p ** 2)
                ]


    y0 = [vp, p, F]
    [vp, p, F] = odeint(f, y0, t, args=(params,), full_output=False).T
    r2 = p
    r1 = A * p
    a11 = np.cos(F)  # направляющие косинусы из Маркеева с 50 51
    a12 = -np.sin(F)
    a21 = np.sin(F)
    a22 = np.cos(F)
    # подвижная система координат с 741 14.13
    x1 = a11 * r1  # vx1=da11*p+vp*a11
    y1 = a21 * r1
    x2 = a11 * r2 * np.cos(phi) + a12 * r2 * np.sin(phi)
    y2 = a21 * r2 * np.cos(phi) + a22 * r2 * np.sin(phi)
    w = c / (p ** 2)
    da11 = -np.sin(F) * w  # #направляющие косинусы из Маркеева для скоростей(производные а)
    da12 = -np.cos(F) * w
    da21 = np.cos(F) * w
    da22 = -np.sin(F) * w
    vx1 = da11 * r1 + vp * a11  # производные координат
    vy1 = da21 * r1 + vp * a21
    vx2 = (da11 * r2 + vp * a11) * np.cos(phi) + np.sin(phi) * (da12 * r2 + vp * a12)
    vy2 = (da21 * r2 + vp * a21) * np.cos(phi) + np.sin(phi) * (da22 * r2 + vp * a22)

    # главная система координат переход с 735 ниже 14.7'
    xx0 = -M1 / M * x1 - M2 / M * x2
    xx1 = (M2 + M0) / M * x1 - M2 / M * x2
    xx2 = -M1 / M * x1 + (M1 + M0) / M * x2
    yy0 = -M1 / M * y1 - M2 / M * y2
    yy1 = (M2 + M0) / M * y1 - M2 / M * y2
    yy2 = -M1 / M * y1 + (M1 + M0) / M * y2

    vvx0 = -M1 / M * vx1 - M2 / M * vx2
    vvx1 = (M2 + M0) / M * vx1 - M2 / M * vx2
    vvx2 = -M1 / M * vx1 + (M1 + M0) / M * vx2
    vvy0 = -M1 / M * vy1 - M2 / M * vy2
    vvy1 = (M2 + M0) / M * vy1 - M2 / M * vy2
    vvy2 = -M1 / M * vy1 + (M1 + M0) / M * vy2

    rr1 = (yy1 - yy0) / (xx1 - xx0)
    rr2 = (yy1 - yy2) / (xx1 - xx2)
    rr3 = (yy2 - yy0) / (xx2 - xx0)
    # усредненный общий коэффицент
    k1 = (rr1 / rr2 + rr2 / rr3 + rr1 / rr3) / 3
    k_date = k1
    # Create text file
    if os.path.exists(str(text_cur_dir) + "DataEyler"):
        print(str(text_cur_dir) + "DataEyler")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler")
        print(str(text_cur_dir) + "DataEyler")

    if os.path.exists(str(text_cur_dir) + "DataEyler/Coords"):
        print(str(text_cur_dir) + "DataEyler/Coords")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/Coords")
        print(str(text_cur_dir) + "DataEyler/Coords")

    if os.path.exists(str(text_cur_dir) + "DataEyler/Speed"):
        print(str(text_cur_dir) + "DataEyler/Speed")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/Speed")
        print(str(text_cur_dir) + "DataEyler/Speed")

    if os.path.exists(str(text_cur_dir) + "DataEyler/k_data"):
        print(str(text_cur_dir) + "DataEyler/k_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/k_data")
        print(str(text_cur_dir) + "DataEyler/k_data")

    if os.path.exists(str(text_cur_dir) + "DataEyler/H_data"):
        print(str(text_cur_dir) + "DataEyler/H_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/H_data")
        print(str(text_cur_dir) + "DataEyler/H_data")

    if os.path.exists(str(text_cur_dir) + "DataEyler/C_data"):
        print(str(text_cur_dir) + "DataEyler/C_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/C_data")
        print(str(text_cur_dir) + "DataEyler/C_data")

    if os.path.exists(str(text_cur_dir) + "DataEyler/Image_data"):
        print(str(text_cur_dir) + "DataEyler/Image_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataEyler/Image_data")
        print(str(text_cur_dir) + "DataEyler/Image_data")

    if k_date[1] != k_date[-1]:
        print(f"{k_date[1]} не равно {k_date[-1]}")
        text_file = open(str(text_cur_dir) + "DataEyler/Coords/coord0_NumOneTwoThree_"+str(c)+".txt", "w")
        text_file3 = open(str(text_cur_dir) + "DataEyler/Speed/speed0_NumOneTwoThree_"+str(c)+".txt", "w")
        steps_for_write = 0

        for i in range(len(xx0)):
            text_file.write(
                f"step = {i}" + "\n" +str(xx0[i]) + ";" + str(yy0[i]) + "\n" + str(xx1[i]) + ";" + str(
                    yy1[i]) + "\n" + str(xx2[i]) + ";" + str(yy2[i]) + "\n")
            text_file3.write(
                f"step = {i}" + "\n" + str(vvx0[i]) + ";" + str(vvy0[i]) + "\n" + str(vvx1[i]) + ";" + str(
                    vvy1[i]) + "\n" + str(vvx2[i]) + ";" + str(vvy2[i]) + "\n")
            steps_for_write += 1

        text_file.close()
        text_file3.close()

        U = f1 * (M0 * M1 / ((x1 ** 2 + y1 ** 2) ** (1 / 2)) + M0 * M2 / ((x2 ** 2 + y2 ** 2) ** (1 / 2)) + M2 * M1 / (
                ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)))  # полная силовая функция 14.2
        c3 = -1 / M * (
                    (M1 * x1 + M2 * x2) * (M1 * vy1 + M2 * vy2) - (M1 * y1 + M2 * y2) * (M1 * vx1 + M2 * vx2)) + M1 * (
                     x1 * vy1 - y1 * vx1) + M2 * (x2 * vy2 - y2 * vx2)
        h = -1 / 2 / M * ((M1 * vx1 + M2 * vx2) ** 2 + (M1 * vy1 + M2 * vy2) ** 2) + 1 / 2 * M1 * (
                vx1 ** 2 + vy1 ** 2) + 1 / 2 * M2 * (vx2 ** 2 + vy2 ** 2) - U

        text_file10 = open(str(text_cur_dir) + "DataEyler/k_data/k_NumOne_"+str(c)+".txt", "w")
        text_file11 = open(str(text_cur_dir) + "DataEyler/H_data/H_NumOne_" + str(c) + ".txt", "w")
        text_file12 = open(str(text_cur_dir) + "DataEyler/C_data/C_NumOne_" + str(c) + ".txt", "w")
        for i in range(len(t)):
            text_file10.write(str(round(t[i], 3)) + ";" + str(round(k_date[i], 3)) + "\n")
            text_file11.write(str(round(t[i], 3)) + ";" + str(round(h[i], 3)) + "\n")
            text_file12.write(str(round(t[i], 3)) + ";" + str(round(c3[i], 3)) + "\n")
        text_file10.close()
        text_file11.close()
        text_file12.close()
        fig = plt.figure(facecolor='white', figsize=(6, 6))
        plt.plot(xx1, yy1, linewidth=1, color='red')
        plt.plot(xx2, yy2, linewidth=1, color='blue')
        plt.plot(xx0, yy0, linewidth=1, color='black')
        plt.grid(True)
        plt.axis('scaled')
        plt.savefig(str(text_cur_dir) + f'DataEyler/Image_data/fig_{c}')
