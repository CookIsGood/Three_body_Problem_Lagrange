import numpy as np
import math as math
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from sympy import *

M0_M1_data = open('Eyler/Params/M0-M1.txt', 'r').read()
M2_f_data = open('Eyler/Params/M2-f.txt', 'r').read()
c_e_data = open('Eyler/Params/c-e.txt', 'r').read()
F_vp_data = open('Eyler/Params/F-vp.txt', 'r').read()
steps_t_data = open('Eyler/Params/steps-t.txt', 'r').read()

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
M=M0+M1+M2
a= Symbol('a', real=True)
eq1 = (M0+M2)*a**5+(2*M0+3*M2)*a**4+(M0+3*M2)*a**3-(M0+3*M1)*a**2-(2*M0+3*M1)*a-(M0+M1)
solve_a=solve(eq1, a)
B=solve_a[0]
A=N(B)
nu1=f1*((M0+M2)-M1/(A)**2+M1/(A+1)**2)
c = c_date[0] # произвольная постоянная
po=c**2/nu1
e = e_date[0]
p=po/(1+e)




phi=math.pi #задано
vp = vp_date[0]  # скорость изменения стороны треугольника
F = F_date[0]  # угол собственного вращения
params = [M0, M1, M2,f1,c, nu1]
t = np.arange(0, steps_date[0], t_date[0])
def f(y, t, params): #формула 14.26
    vp,p,F= y
    M0,M1,M2, f1,c, nu1 = params
    return [c**2/p**3-nu1/p**2,
            vp,
            c/(p**2)
            ]




y0 = [vp,p,F]
[vp,p,F] = odeint(f, y0, t, args=(params,), full_output=False).T
r2=p
r1=A*p
a11=np.cos(F)#направляющие косинусы из Маркеева с 50 51
a12=-np.sin(F)
a21=np.sin(F)
a22=np.cos(F)
#подвижная система координат с 741 14.13
x1=a11*r1 #vx1=da11*p+vp*a11
y1=a21*r1
x2=a11*r2*np.cos(phi)+a12*r2*np.sin(phi)
y2=a21*r2*np.cos(phi)+a22*r2*np.sin(phi)
w=c/(p**2)
da11=-np.sin(F)*w# #направляющие косинусы из Маркеева для скоростей(производные а)
da12=-np.cos(F)*w
da21=np.cos(F)*w
da22=-np.sin(F)*w
vx1=da11*r1+vp*a11 #производные координат
vy1=da21*r1+vp*a21
vx2=(da11*r2+vp*a11)*np.cos(phi)+np.sin(phi)*(da12*r2+vp*a12)
vy2=(da21*r2+vp*a21)*np.cos(phi)+np.sin(phi)*(da22*r2+vp*a22)

#главная система координат переход с 735 ниже 14.7'
xx0=-M1/M*x1-M2/M*x2
xx1=(M2+M0)/M*x1-M2/M*x2
xx2=-M1/M*x1+(M1+M0)/M*x2
yy0=-M1/M*y1-M2/M*y2
yy1=(M2+M0)/M*y1-M2/M*y2
yy2=-M1/M*y1+(M1+M0)/M*y2

vvx0=-M1/M*vx1-M2/M*vx2
vvx1=(M2+M0)/M*vx1-M2/M*vx2
vvx2=-M1/M*vx1+(M1+M0)/M*vx2
vvy0=-M1/M*vy1-M2/M*vy2
vvy1=(M2+M0)/M*vy1-M2/M*vy2
vvy2=-M1/M*vy1+(M1+M0)/M*vy2


def coordseyl1(xx0,xx1,xx2,yy0,yy1,yy2):
    y=[xx0,xx1,xx2,yy0,yy1,yy2]
    return y
def speeddseyl1(vvx0,vvx1,vvx2,vvy0,vvy1,vvy2):
    y=[vvx0,vvx1,vvx2,vvy0,vvy1,vvy2]
    return y


#Create text file
if os.path.exists("Eyler/Coords"):
    print("Папка Coords уже существует")
else:
    os.mkdir("Eyler/Coords")
    print("Папка Coords создана")
text_file = open("Eyler/Coords/coord0_NumOne.txt", "w")
text_file1 = open("Eyler/Coords/coord1_NumOne.txt", "w")
text_file2 = open("Eyler/Coords/coord2_NumOne.txt", "w")
text_file3 = open("Eyler/Coords/speed0_NumOne.txt", "w")
text_file4 = open("Eyler/Coords/speed1_NumOne.txt", "w")
text_file5 = open("Eyler/Coords/speed2_NumOne.txt", "w")

text_file6 = open("Eyler/Coords/coord01.txt", "w")
text_file7 = open("Eyler/Coords/coord02.txt", "w")
text_file8 = open("Eyler/Coords/speed01.txt", "w")
text_file9 = open("Eyler/Coords/speed02.txt", "w")
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



rr1 = (yy1 - yy0)/(xx1 - xx0)
rr2 = (yy1 - yy2)/(xx1 - xx2)
rr3 = (yy2 - yy0)/(xx2 - xx0)
#усредненный общий коэффицент
k1=(rr1/rr2+rr2/rr3+rr1/rr3)/3
k_date =k1
U=f1*(M0*M1/((x1**2+y1**2)**(1/2))+M0*M2/((x2**2+y2**2)**(1/2))+M2*M1/(((x1-x2)**2+(y1-y2)**2)**(1/2)))#полная силовая функция 14.2
c3=-1/M*((M1*x1+M2*x2)*(M1*vy1+M2*vy2)-(M1*y1+M2*y2)*(M1*vx1+M2*vx2))+M1*(x1*vy1-y1*vx1)+M2*(x2*vy2-y2*vx2)
h=-1/2/M*((M1*vx1+M2*vx2)**2+(M1*vy1+M2*vy2)**2)+1/2*M1*(vx1**2+vy1**2)+1/2*M2*(vx2**2+vy2**2)-U
cc = c3/c3[0]
hh = h/h[0]
text_file10 = open("Eyler/Coords/k_NumOne.txt", "w")
k_date[0]=1
for i in range(len(t)):
    text_file10.write(str(round(t[i],3)) + ";" + str(round(k_date[i],3)) + "\n")
text_file10.close()
text_file11 = open("Eyler/Coords/H_NumOne.txt", "w")
text_file12 = open("Eyler/Coords/C_NumOne.txt", "w")
for i in range(len(t)):
    text_file11.write(str(round(t[i], 3)) + ";" + str(round(cc[i], 3)) + "\n")
    text_file12.write(str(round(t[i], 3)) + ";" + str(round(hh[i], 3)) + "\n")
text_file11.close()
text_file12.close()
