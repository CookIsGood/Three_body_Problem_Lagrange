from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import random
import matplotlib.pyplot as plt

root = Tk()
root.geometry('650x500')
root.title("GrathOne")

conditions = open("Nbody/bin/dir.txt", "r")
text = conditions.read()
cond = open(f"{text}", "r")
text_res = cond.read()
text_final = text_res.split("\n")
N = int(''.join([n for n in text_final[0] if n.isdigit()]))
res_for_plot_x = [[] for n in range(N)]
res_for_plot_y = [[] for n in range(N)]
for i in range(N):
    text = open("Nbody/Coords/coord" + str(i) + "_NumOne.txt", "r")
    tt = text.read()
    tt1 = tt.split("\n")
    for line in tt1:
        if len(line) > 1:
            x, y = line.split(';')
            res_for_plot_x[i].append(float(x))
            res_for_plot_y[i].append(float(y))
text.close()
cond.close()
conditions.close()

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
canvas.get_tk_widget().place(relx=0, rely=0)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
text = '#1'
ax_1 = fig.add_subplot(111)
ax_1.set(title=text)
ax_1.set_xlabel('x')
ax_1.set_ylabel('y')

for i in range(N):
    ax_1.plot(res_for_plot_x[i], res_for_plot_y[i], linewidth=1,
             color=(random.random(), random.random(), random.random()))

ax_1.grid(True)
plt.axis('scaled')
root.maxsize(1000, 900)

root.mainloop()
