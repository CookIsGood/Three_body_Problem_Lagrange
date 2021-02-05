from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

root = Tk()
root.geometry('650x500')
root.title("AnimateOne")


r1_X_Y_data_NumOne, r2_X_Y_data_NumOne, r3_X_Y_data_NumOne = open('Coords/coord0_NumOne.txt', 'r').read(), open(
        'Coords/coord1_NumOne.txt', 'r').read(), open('Coords/coord2_NumOne.txt', 'r').read()
r1_X_Y_data_NumOne, r2_X_Y_data_NumOne, r3_X_Y_data_NumOne = r1_X_Y_data_NumOne.split(
        '\n'), r2_X_Y_data_NumOne.split('\n'), r3_X_Y_data_NumOne.split('\n')
r1_x_new_NumOne, r1_y_new_NumOne, r2_x_new_NumOne, r2_y_new_NumOne, r3_x_new_NumOne, r3_y_new_NumOne = [], [], [], [], [], []

steps_t_data = open('Params/steps-t.txt', 'r').read()
steps_t = steps_t_data.split('\n')
steps_date = []
t_date = []
for line in steps_t:
    if len(line) > 1:
        x, y = line.split(';')
        steps_date.append(float(x))
        t_date.append(float(y))
for line in r1_X_Y_data_NumOne:
    if len(line) > 1:
        x, y = line.split(';')
        r1_x_new_NumOne.append(float(x))
        r1_y_new_NumOne.append(float(y))
for line in r2_X_Y_data_NumOne:
    if len(line) > 1:
        x, y = line.split(';')
        r2_x_new_NumOne.append(float(x))
        r2_y_new_NumOne.append(float(y))

for line in r3_X_Y_data_NumOne:
    if len(line) > 1:
        x, y = line.split(';')
        r3_x_new_NumOne.append(float(x))
        r3_y_new_NumOne.append(float(y))
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=root)
#canvas.get_tk_widget().place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
canvas.get_tk_widget().place(relx=0, rely=0)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
text='#1'
ax_1 = fig.add_subplot(111)
ax_1.set(title=text)
ax_1.set_xlabel('x')
ax_1.set_ylabel('y')
camera = Camera(fig)
r0=((max(r1_x_new_NumOne)-min(r1_x_new_NumOne))/2+(max(r1_y_new_NumOne)-min(r1_y_new_NumOne))/2)/100*2.5
r1=((max(r2_x_new_NumOne)-min(r2_x_new_NumOne))/2+(max(r2_y_new_NumOne)-min(r2_y_new_NumOne))/2)/100*2.5
r2=((max(r3_x_new_NumOne)-min(r3_x_new_NumOne))/2+(max(r3_x_new_NumOne)-min(r3_x_new_NumOne))/2)/100*2.5
for i in range(len(np.arange(0, steps_date[0], t_date[0]))):
    #plt.plot([i] * 10)
    pc1 = plt.Circle((r1_x_new_NumOne[i], r1_y_new_NumOne[i]), r0, fc='black')
    pc2= plt.Circle((r2_x_new_NumOne[i], r2_y_new_NumOne[i]), r1, fc='blue')
    pc3=plt.Circle((r3_x_new_NumOne[i], r3_y_new_NumOne[i]), r2, fc='red')
    ax_1.plot((r1_x_new_NumOne[i], r2_x_new_NumOne[i], r3_x_new_NumOne[i], r1_x_new_NumOne[i]), (r1_y_new_NumOne[i], r2_y_new_NumOne[i], r3_y_new_NumOne[i], r1_y_new_NumOne[i]), linewidth=1, color='magenta')
    ax_1.add_patch(pc1)
    ax_1.add_patch(pc2)
    ax_1.add_patch(pc3)
    ax_1.plot(r1_x_new_NumOne, r1_y_new_NumOne, linewidth=1, color='black', label = 'r0')
    ax_1.plot(r2_x_new_NumOne, r2_y_new_NumOne, linewidth=1, color='blue', label = 'r1')
    ax_1.plot(r3_x_new_NumOne, r3_y_new_NumOne, linewidth=1, color='red', label = 'r2')
    camera.snap()

animation = camera.animate()
#animation.save('celluloid_minimal.gif')
ax_1.grid(True)
plt.axis('scaled')
root.maxsize(1000, 900)
# plt.close()

root.mainloop()



