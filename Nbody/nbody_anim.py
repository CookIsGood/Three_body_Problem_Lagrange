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
canvas.get_tk_widget().place(relx=0, rely=0)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
text='#1'
ax_1 = fig.add_subplot(111)
ax_1.set(title=text)
ax_1.set_xlabel('x')
ax_1.set_ylabel('y')

def random_color():
    r, g, b = random.random(), random.random(), random.random()
    color = (r, g, b)
    return color

r_list = []
color_list = []
for i in range(N):
    r_list.append(((max(res_for_plot_x[i])-min(res_for_plot_x[i]))/2+(max(res_for_plot_y[i])-min(res_for_plot_y[i]))/2)/100*2.5)
    color_list.append(random_color())

camera = Camera(fig)
for i in range(len(res_for_plot_x[0])):
    for k in range(N):
        pc1 = plt.Circle((res_for_plot_x[k][i], res_for_plot_y[k][i]), r_list[k], fc=color_list[k])
        ax_1.add_patch(pc1)
        ax_1.plot(res_for_plot_x[k], res_for_plot_y[k], linewidth=1,
                  color=color_list[k])
    camera.snap()

animation = camera.animate()
ax_1.grid(True)
plt.axis('scaled')
root.maxsize(1000, 900)
# plt.close()

root.mainloop()



