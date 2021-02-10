import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np
import os
from datetime import datetime
import time

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.text = tk.Text(self, width=20, height=10)
        self.text.pack()
        self.text.insert(1.0, 'Hello World!\nFoo\nBar\n\n123\n')

        self.button = tk.Button(self, text='Append', command=self.on_append)
        self.button.pack()

        self.pack()

    def on_append(self):
        self.text.insert(tk.END, 'Go-go-go!\n')