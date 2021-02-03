import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = Tk()
root.geometry('650x500')
root.title("AnimateTwo")
r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = open('Coords/coord0_NumTwo.txt', 'r').read(), open(
        'Coords/coord1_NumTwo.txt', 'r').read(), open('Coords/coord2_NumTwo.txt', 'r').read()
r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = r1_X_Y_data_NumTwo.split(
        '\n'), r2_X_Y_data_NumTwo.split('\n'), r3_X_Y_data_NumTwo.split('\n')
r1_x_new_NumTwo, r1_y_new_NumTwo, r2_x_new_NumTwo, r2_y_new_NumTwo, r3_x_new_NumTwo, r3_y_new_NumTwo = [], [], [], [], [], []

steps_t_data = open('Params/steps-t.txt', 'r').read()
steps_t = steps_t_data.split('\n')
steps_date = []
t_date = []

for line in steps_t:
    if len(line) > 1:
        x, y = line.split(';')
        steps_date.append(float(x))
        t_date.append(float(y))
for line in r1_X_Y_data_NumTwo:
    if len(line) > 1:
        x, y = line.split(';')
        r1_x_new_NumTwo.append(float(x))
        r1_y_new_NumTwo.append(float(y))
for line in r2_X_Y_data_NumTwo:
    if len(line) > 1:
        x, y = line.split(';')
        r2_x_new_NumTwo.append(float(x))
        r2_y_new_NumTwo.append(float(y))
for line in r3_X_Y_data_NumTwo:
    if len(line) > 1:
        x, y = line.split(';')
        r3_x_new_NumTwo.append(float(x))
        r3_y_new_NumTwo.append(float(y))
fig = plt.figure()

canvas = FigureCanvasTkAgg(fig, master=root)
#canvas.get_tk_widget().place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
canvas.get_tk_widget().place(relx=0, rely=0)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

ax_1 = fig.add_subplot(111)
camera = Camera(fig)

for i in range(len(np.arange(0, steps_date[0], t_date[0]))):
    #plt.plot([i] * 10)
    pc1 = plt.Circle((r1_x_new_NumTwo[i], r1_y_new_NumTwo[i]), 1, fc='black')
    pc2= plt.Circle((r2_x_new_NumTwo[i], r2_y_new_NumTwo[i]), 1, fc='red')
    pc3=plt.Circle((r3_x_new_NumTwo[i], r3_y_new_NumTwo[i]), 1, fc='blue')
    plt.plot((r1_x_new_NumTwo[i], r2_x_new_NumTwo[i], r3_x_new_NumTwo[i], r1_x_new_NumTwo[i]), (r1_y_new_NumTwo[i], r2_y_new_NumTwo[i], r3_y_new_NumTwo[i], r1_y_new_NumTwo[i]), linewidth=1, color='magenta')
    ax_1.add_patch(pc1)
    ax_1.add_patch(pc2)
    ax_1.add_patch(pc3)
    plt.plot(r2_x_new_NumTwo, r2_y_new_NumTwo, linewidth=1, color='red')
    plt.plot(r3_x_new_NumTwo, r3_y_new_NumTwo, linewidth=1, color='blue')
    plt.plot(r1_x_new_NumTwo, r1_y_new_NumTwo, linewidth=1, color='black')
    camera.snap()
animation = camera.animate()
#animation.save('celluloid_minimal.gif')
root.maxsize(1000, 900)
# plt.close()
plt.axis('scaled')
ax_1.grid(True)
root.mainloop()
