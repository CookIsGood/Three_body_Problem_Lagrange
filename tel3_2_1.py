import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import os

M0_M1_data = open('Params/M0-M1.txt', 'r').read()
M2_f_data = open('Params/M2-f.txt', 'r').read()
c_e_data = open('Params/c-e.txt', 'r').read()
F_vp_data = open('Params/F-vp.txt', 'r').read()
steps_t_data = open('Params/steps-t.txt', 'r').read()

M0_M1 = M0_M1_data.split('\n')
M2_f = M2_f_data.split('\n')
c_e = c_e_data.split('\n')
F_vp = F_vp_data.split('\n')
steps_t = steps_t_data.split('\n')

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


f1 = f_date[0]
M0 = M0_date[0]
M1 = M1_date[0]
M2 = M2_date[0]
M = M0 + M1 + M2
c = c_date[0] # произвольная постоянная
po = c ** 2 / (f1 * M)  # из формулы 14.28
e = e_date[0]
p = po / (1 + e)  # из формулы 14.28'

phi = np.pi / 3  # задано
vp = vp_date[0]  # скорость изменения стороны треугольника
F = F_date[0]  # угол собственного вращения
params = [M0, M1, M2, f1, c]
#t = np.linspace(0, steps_date[0], int(t_date[0]))
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

if os.path.exists("Coords"):
    print("Папка Coords уже существует")
else:
    os.mkdir("Coords")
    print("Папка Coords создана")
text_file = open("Coords/coord0_NumOne.txt", "w")
text_file1 = open("Coords/coord1_NumOne.txt", "w")
text_file2 = open("Coords/coord2_NumOne.txt", "w")
text_file3 = open("Coords/speed0_NumOne.txt", "w")
text_file4 = open("Coords/speed1_NumOne.txt", "w")
text_file5 = open("Coords/speed2_NumOne.txt", "w")

text_file6 = open("Coords/coord01.txt", "w")
text_file7 = open("Coords/coord02.txt", "w")
text_file8 = open("Coords/speed01.txt", "w")
text_file9 = open("Coords/speed02.txt", "w")
for i in range(len(xx0)):
    text_file.write(str(xx0[i]) + ";" + str(yy0[i]) + "\n")
    text_file1.write(str(xx1[i]) + ";" + str(yy1[i]) + "\n")
    text_file2.write(str(xx2[i]) + ";" + str(yy2[i]) + "\n")
    text_file3.write(str(vvx0[i]) + ";" + str(vvy0[i]) + "\n")
    text_file4.write(str(vvx1[i]) + ";" + str(vvy1[i]) + "\n")
    text_file5.write(str(vvx2[i]) + ";" + str(vvy2[i]) + "\n")

text_file6.write(str(x1[0]) + ";" + str(y1[0]) + "\n")
text_file7.write(str(x2[0]) + ";" + str(y2[0]) + "\n")
text_file8.write(str(vx1[0]) + ";" + str(vy1[0]) + "\n")
text_file9.write(str(vx2[0]) + ";" + str(vy2[0]) + "\n")
text_file.close()
text_file1.close()
text_file2.close()
text_file3.close()
text_file4.close()
text_file5.close()

text_file6.close()
text_file7.close()
text_file8.close()
text_file9.close()

print(np.sqrt((xx1 - xx2) ** 2 + (yy1 - yy2) ** 2))  # проверка равенства сторон
print(np.sqrt((xx0 - xx2) ** 2 + (yy0 - yy2) ** 2))
print(np.sqrt((xx1 - xx0) ** 2 + (yy1 - yy0) ** 2))
#plt.plot(xx1, yy1, linewidth=1, color='red')
#plt.plot(xx2, yy2, linewidth=1, color='blue')
#plt.plot(xx0, yy0, linewidth=1, color='black')
#plt.grid(True)

#plt.axis('scaled')


#plt.show()
