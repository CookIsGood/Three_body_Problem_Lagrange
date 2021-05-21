import numpy as np
import random


def random_color():
    r, g, b = random.random(), random.random(), random.random()
    color = (r, g, b)
    return color


import os

if os.path.exists("demofile4.py"):
    os.remove("demofile4.py")
f = open("demofile4.py", "a")
f.write("import numpy as np\n")
f.write("import math as math\n")
f.write("from scipy.integrate import odeint\n")
f.write("from scipy.optimize import fsolve\n")
f.write("import matplotlib.pyplot as plt\n")
f.write("import sympy as sym\n")
f.write("from sympy import Symbol\n")
f.write("from sympy import simplify\n")
f.write("from sympy import re\n")
f.write("from sympy.solvers import solve\n")
f.write("import matplotlib.animation as animation\n")
f.write("from celluloid import Camera\n")

conditions = open("Nbody/bin/dir.txt", "r")
text = conditions.read()
cond = open(f"{text}", "r")
text_res = cond.read()
text_final = text_res.split("\n")
N = int(''.join([n for n in text_final[0] if n.isdigit()]))
for line in range(1, len(text_final)):
    f.write(str(text_final[line]) + "\n")

params = 'params=[M0'
for i in range(N - 1):
    params = params + ', M' + str(i + 1)
params = params + ', f1]\n'
f.write(params)
f.write('def f(y, t, params):\n')
params = 'vx0, vy0'
for i in range(N - 1):
    params = params + ', vx' + str(i + 1) + ', vy' + str(i + 1)
for i in range(N):
    params = params + ', x' + str(i) + ', y' + str(i)
params = params + '=y\n'
f.write('   ' + params)
params = 'M0'
for i in range(N - 1):
    params = params + ', M' + str(i + 1)
params = params + ',f1=params\n'
f.write('   ' + params)
f.write('   return[\n')

for j in range(N):
    k = 0
    for i in range(N - 1):
        if i == 0:
            if i == j:
                k = 1
                i = i + 1
            params = 'f1*M' + str(i) + '*(x' + str(i) + '-x' + str(j) + ')/(np.sqrt((x' + str(i) + '-x' + str(
                j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
            params2 = 'f1*M' + str(i) + '*(y' + str(i) + '-y' + str(j) + ')/(np.sqrt((x' + str(i) + '-x' + str(
                j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
        elif i == j:
            k = 1
            i = i + 1
            params = params + ' + f1*M' + str(i) + '*(x' + str(i) + '-x' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
            params2 = params2 + ' + f1*M' + str(i) + '*(y' + str(i) + '-y' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(
                j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
        elif k == 1:
            k = 1
            i = i + 1
            params = params + ' + f1*M' + str(i) + '*(x' + str(i) + '-x' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
            params2 = params2 + ' + f1*M' + str(i) + '*(y' + str(i) + '-y' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(
                j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'
        else:
            params = params + ' + f1*M' + str(i) + '*(x' + str(i) + '-x' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'

            params2 = params2 + ' + f1*M' + str(i) + '*(y' + str(i) + '-y' + str(j) + ')/(np.sqrt((x' + str(
                i) + '-x' + str(
                j) + ')**2+(y' + str(i) + '-y' + str(j) + ')**2))**3'

    params = params + ','
    params2 = params2 + ','
    f.write('       ' + params + '\n')
    f.write('       ' + params2 + '\n')
for i in range(N - 1):
    f.write('       vx' + str(i) + ',\n')
    f.write('       vy' + str(i) + ',\n')
f.write('       vx' + str(N - 1) + ',\n')
f.write('       vy' + str(N - 1) + '\n')
f.write('       ]\n')
params = 'y0=[vx0, vy0'
for i in range(N - 1):
    params = params + ', vx' + str(i + 1) + ', vy' + str(i + 1)
for i in range(N):
    params = params + ', x' + str(i) + ', y' + str(i)
f.write(params + ']\n')
params = '[vx0, vy0'
for i in range(N - 1):
    params = params + ', vx' + str(i + 1) + ', vy' + str(i + 1)
for i in range(N):
    params = params + ', x' + str(i) + ', y' + str(i)
f.write(params + ']= odeint(f, y0, t, args=(params,), full_output=False).T\n')
params = 'c1=M0*(x0*vy0-y0*vx0)'
for i in range(N - 1):
    params = params + '+M' + str(i + 1) + '*(x' + str(i + 1) + '*vy' + str(i + 1) + '-y' + str(i + 1) + '*vx' + str(
        i + 1) + ')'
f.write(params + '\n')

from itertools import *

spisok = []
for item in combinations(range(N), 2):
    spisok.append(item)
params = 'U=f1*(M0*M1/(np.sqrt((x1-x0)**2+(y1-y0)**2)))'
for j in range(len(spisok) - 1):
    params = params + ' + f1*(M' + str(spisok[j + 1][0]) + '*M' + str(spisok[j + 1][1]) + '/(np.sqrt((x' + str(
        spisok[j + 1][0]) + '-x' + str(spisok[j + 1][1]) + ')**2+(y' + str(spisok[j + 1][0]) + '-y' + str(
        spisok[j + 1][1]) + ')**2)))'
f.write(params + '\n')
params = 'H=M0/2*(vy0**2+vx0**2)'
for i in range(N - 1):
    params = params + ' +M' + str(i + 1) + '/2*(vy' + str(i + 1) + '**2+vx' + str(i + 1) + '**2)'
f.write(params + '-U\n')
f.write('HH=H[0]/H\n')
f.write('CC=c1[0]/c1\n')

for i in range(N):
    f.write("text_filec" + str(i) + " = open('Nbody/Coords/coord" + str(i) + "_NumOne.txt', 'w')\n")
    f.write("text_files" + str(i) + "=open('Nbody/Coords/speed" + str(i) + "_NumOne.txt', 'w')\n")

f.write("for i in range(len(x0)):\n")
for i in range(N):
    f.write(
        "   text_filec" + str(i) + ".write(str(x" + str(i) + "[i])+';'+str(y" + str(i) + "[i])+'" + chr(92) + "n')\n")
    f.write(
        "   text_files" + str(i) + ".write(str(vx" + str(i) + "[i])+';'+str(vy" + str(i) + "[i])+'" + chr(92) + "n')\n")
f.write("Hfile=open('Nbody/Coords/H_NumOne.txt', 'w')\n")
f.write("Cfile=open('Nbody/Coords/C_NumOne.txt', 'w')\n")

f.write('for i in range(len(t)):\n')
f.write("   Hfile.write(str(t[i])+';'+str(HH[i])+'" + chr(92) + "n')\n")
f.write("   Cfile.write(str(t[i])+';'+str(CC[i])+'" + chr(92) + "n')\n")

for i in range(N):
    f.write("text_filec" + str(i) + ".close()\n")
    f.write("text_files" + str(i) + ".close()\n")
f.write("Hfile.close()\n")
f.write("Cfile.close()\n")

f.close()

# os.startfile("demofile2.py")
dir_path = os.path.dirname(os.path.realpath('demofile4.py'))
file_path = os.path.join(dir_path, 'demofile4.py')

os.system(f'py {file_path}')
"""
text_file9 = open("Lagrange/Coords/speed02.txt", "w")
for i in range(len(xx0)):
text_file.write(str(xx0[i]) + ";" + str(yy0[i]) + "\n")
text_file1.write(str(xx1[i]) + ";" + str(yy1[i]) + "\n")
text_file2.write(str(xx2[i]) + ";" + str(yy2[i]) + "\n")
text_file3.write(str(vvx0[i]) + ";" + str(vvy0[i]) + "\n")
text_file4.write(str(vvx1[i]) + ";" + str(vvy1[i]) + "\n")
text_file5.write(str(vvx2[i]) + ";" + str(vvy2[i]) + "\n")

код для запизи координат

for i in range(len(t)):
text_file10.write(str(round(t[i],3)) + ";" + str(round(k1[i],3)) + "\n")
text_file11.write(str(round(t[i], 3)) + ";" + str(round(HH[i], 3)) + "\n")
text_file12.write(str(round(t[i], 3)) + ";" + str(round(c_data[i], 3)) + "\n")

код для записи доп графиков

text_file11 = open("Lagrange/Coords/H_NumOne.txt", "w")

"""