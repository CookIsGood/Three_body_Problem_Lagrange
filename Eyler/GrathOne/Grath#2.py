import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = Tk()
root.geometry('650x500')
root.title("GrathTwo")
r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = open('Eyler/Coords/coord0_NumTwo.txt', 'r').read(), open(
        'Eyler/Coords/coord1_NumTwo.txt', 'r').read(), open('Eyler/Coords/coord2_NumTwo.txt', 'r').read()
r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = r1_X_Y_data_NumTwo.split(
        '\n'), r2_X_Y_data_NumTwo.split('\n'), r3_X_Y_data_NumTwo.split('\n')
r1_x_new_NumTwo, r1_y_new_NumTwo, r2_x_new_NumTwo, r2_y_new_NumTwo, r3_x_new_NumTwo, r3_y_new_NumTwo = [], [], [], [], [], []

steps_t_data = open('Eyler/Params/steps-t.txt', 'r').read()
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
canvas.get_tk_widget().place(relx=0, rely=0)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

ax_1 = fig.add_subplot(111)
ax_1.set(title='#2')
ax_1.set_xlabel('x')
ax_1.set_ylabel('y')
plt.plot(r2_x_new_NumTwo, r2_y_new_NumTwo, linewidth=1, color='blue', label = 'r1')
plt.plot(r3_x_new_NumTwo, r3_y_new_NumTwo, linewidth=1, color='red', label = 'r2')
plt.plot(r1_x_new_NumTwo, r1_y_new_NumTwo, linewidth=1, color='black', label = 'r0')
root.maxsize(1000, 900)
plt.axis('scaled')
ax_1.grid(True)
root.mainloop()