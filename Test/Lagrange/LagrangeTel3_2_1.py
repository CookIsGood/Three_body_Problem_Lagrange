import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import os

M0_M1_data = open('Lagrange/Params/M0-M1.txt', 'r').read()
M2_f_data = open('Lagrange/Params/M2-f.txt', 'r').read()
c_e_data = open('Lagrange/Params/c-e.txt', 'r').read()
F_vp_data = open('Lagrange/Params/F-vp.txt', 'r').read()
steps_t_data = open('Lagrange/Params/steps-t.txt', 'r').read()
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
e = e_date[0]
# c = c_date[0] # произвольная постоянная
for c in range(int(c_before[0]), int(c_after[0]), int(c_steps2[0])):
    po = c ** 2 / (f1 * M)  # из формулы 14.28

    p = po / (1 + e)  # из формулы 14.28'

    phi = np.pi / 3  # задано
    vp = vp_date[0]  # скорость изменения стороны треугольника
    F = F_date[0]  # угол собственного вращения
    params = [M0, M1, M2, f1, c]
    # t = np.linspace(0, steps_date[0], int(t_date[0]))
    t = np.arange(0, steps_date[0], t_date[0])


    def f(y, t, params):  # формула 14.26
        vp, p, F = y
        M0, M1, M2, f1, c = params
        return [((c / (p ** 2)) ** 2) * p - f1 * (M0 + M1 + M2) / p ** 2,
                vp,
                c / (p ** 2)
                ]


    y0 = [vp, p, F]
    [vp, p, F] = odeint(f, y0, t, args=(params,), full_output=False).T
    a11 = np.cos(F)  # направляющие косинусы из Маркеева с 50 51
    a12 = -np.sin(F)
    a21 = np.sin(F)
    a22 = np.cos(F)
    # подвижная система координат с 741 14.13
    x1 = a11 * p  # vx1=da11*p+vp*a11
    y1 = a21 * p
    x2 = a11 * p * np.cos(phi) + a12 * p * np.sin(phi)
    y2 = a21 * p * np.cos(phi) + a22 * p * np.sin(phi)
    w = c / p ** 2
    da11 = -np.sin(F) * w  # #направляющие косинусы из Маркеева для скоростей(производные а)
    da12 = -np.cos(F) * w
    da21 = np.cos(F) * w
    da22 = -np.sin(F) * w
    vx1 = da11 * p + vp * a11  # производные координат
    vy1 = da21 * p + vp * a21
    vx2 = (da11 * p + vp * a11) * np.cos(phi) + np.sin(phi) * (da12 * p + vp * a12)
    vy2 = (da21 * p + vp * a21) * np.cos(phi) + np.sin(phi) * (da22 * p + vp * a22)

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

    rr1 = np.sqrt((xx1 - xx2) ** 2 + (yy1 - yy2) ** 2)
    rr2 = np.sqrt((xx0 - xx2) ** 2 + (yy0 - yy2) ** 2)
    rr3 = np.sqrt((xx1 - xx0) ** 2 + (yy1 - yy0) ** 2)
    # усредненный общий коэффицент
    k1 = (rr1 / rr2 + rr2 / rr3 + rr3 / rr1) / 3
    # Create text file
    if os.path.exists(str(text_cur_dir) + "DataLagr"):
        print(str(text_cur_dir) + "DataLagr")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr")
        print(str(text_cur_dir) + "DataLagr")

    if os.path.exists(str(text_cur_dir) + "DataLagr/Coords"):
        print(str(text_cur_dir) + "DataLagr/Coords")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/Coords")
        print(str(text_cur_dir) + "DataLagr/Coords")

    if os.path.exists(str(text_cur_dir) + "DataLagr/Speed"):
        print(str(text_cur_dir) + "DataLagr/Speed")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/Speed")
        print(str(text_cur_dir) + "DataLagr/Speed")

    if os.path.exists(str(text_cur_dir) + "DataLagr/k_data"):
        print(str(text_cur_dir) + "DataLagr/k_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/k_data")
        print(str(text_cur_dir) + "DataLagr/k_data")

    if os.path.exists(str(text_cur_dir) + "DataLagr/H_data"):
        print(str(text_cur_dir) + "DataLagr/H_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/H_data")
        print(str(text_cur_dir) + "DataLagr/H_data")

    if os.path.exists(str(text_cur_dir) + "DataLagr/C_data"):
        print(str(text_cur_dir) + "DataLagr/C_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/C_data")
        print(str(text_cur_dir) + "DataLagr/C_data")

    if os.path.exists(str(text_cur_dir) + "DataLagr/Image_data"):
        print(str(text_cur_dir) + "DataLagr/Image_data")
    else:
        os.mkdir(str(text_cur_dir) + "DataLagr/Image_data")
        print(str(text_cur_dir) + "DataLagr/Image_data")
    if k1[1] != k1[-1]:
        print(f"{k1[1]} не равно {k1[-1]}")
        text_file = open(str(text_cur_dir) + "DataLagr/Coords/coord0_NumOneTwoThree_" + str(c) + ".txt", "w")
        text_file3 = open(str(text_cur_dir) + "DataLagr/Speed/speed0_NumOneTwoThree_" + str(c) + ".txt", "w")
        steps_for_write = 0

        for i in range(len(xx0)):
            text_file.write(
                f"step = {i}" + "\n" + str(xx0[i]) + ";" + str(yy0[i]) + "\n" + str(xx1[i]) + ";" + str(
                    yy1[i]) + "\n" + str(xx2[i]) + ";" + str(yy2[i]) + "\n")
            text_file3.write(
                f"step = {i}" + "\n" + str(vvx0[i]) + ";" + str(vvy0[i]) + "\n" + str(vvx1[i]) + ";" + str(
                    vvy1[i]) + "\n" + str(vvx2[i]) + ";" + str(vvy2[i]) + "\n")
            steps_for_write += 1

        text_file.close()
        text_file3.close()

        U = f1 * (M0 * M1 / (np.sqrt((x1) ** 2 + (y1) ** 2)) + M0 * M2 / (np.sqrt((x2) ** 2 + (y2) ** 2)) + M2 * M1 / (
            np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))  # полная силовая функция 14.2
        c3 = -1 / M * (
                    (M1 * x1 + M2 * x2) * (M1 * vy1 + M2 * vy2) - (M1 * y1 + M2 * y2) * (M1 * vx1 + M2 * vx2)) + M1 * (
                     x1 * vy1 - y1 * vx1) + M2 * (x2 * vy2 - y2 * vx2)
        h = -1 / 2 / M * ((M1 * vx1 + M2 * vx2) ** 2 + (M1 * vy1 + M2 * vy2) ** 2) + 1 / 2 * M1 * (
                vx1 ** 2 + vy1 ** 2) + 1 / 2 * M2 * (vx2 ** 2 + vy2 ** 2) - U
        HH = h[0] / h
        c_data = c3[0] / c3
        text_file10 = open(str(text_cur_dir) + "DataLagr/k_data/k_NumOne_" + str(c) + ".txt", "w")
        text_file11 = open(str(text_cur_dir) + "DataLagr/H_data/H_NumOne_" + str(c) + ".txt", "w")
        text_file12 = open(str(text_cur_dir) + "DataLagr/C_data/C_NumOne_" + str(c) + ".txt", "w")
        for i in range(len(t)):
            text_file10.write(str(round(t[i], 3)) + ";" + str(round(k1[i], 3)) + "\n")
            text_file11.write(str(round(t[i], 3)) + ";" + str(round(HH[i], 3)) + "\n")
            text_file12.write(str(round(t[i], 3)) + ";" + str(round(c_data[i], 3)) + "\n")
        text_file10.close()
        text_file11.close()
        text_file12.close()
        fig = plt.figure(facecolor='white', figsize=(6, 6))
        plt.plot(xx1, yy1, linewidth=1, color='red')
        plt.plot(xx2, yy2, linewidth=1, color='blue')
        plt.plot(xx0, yy0, linewidth=1, color='black')
        plt.grid(True)
        plt.axis('scaled')
        plt.savefig(str(text_cur_dir) + f'DataLagr/Image_data/fig_{c}')
