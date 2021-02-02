import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import gridspec
root = tkinter.Tk()

data = np.random.rand(100)
t = np.arange(0, 100, 1)

fig = plt.figure(figsize=(10, 6))
spec2 = gridspec.GridSpec(ncols=3, nrows=1, figure=fig)

f2_ax1 = fig.add_subplot(spec2[0, 0])
f2_ax2 = fig.add_subplot(spec2[0, 1])
#f2_ax3 = fig.add_subplot(spec2[1, 0])



f2_ax1.plot(data, t)

f2_ax2.plot(data, t)

#f2_ax3.plot(data, t)
#fig.set_size_inches(18.5, 10.5, forward=True)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

scrollbar = tkinter.Scrollbar(master=root, orient=VERTICAL)
scrollbar["command"] = canvas.get_tk_widget().yview
#canvas.get_tk_widget()["xscrollcommand"] = scrollbar.set
scrollbar.pack(side=tkinter.RIGHT, fill=Y)

tkinter.mainloop()