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


class lagrange(tk.Frame):

    def _save_figure(self):
        if os.path.exists("Image"):
            print("Папка Image уже существует")
        else:
            os.mkdir("Image")
            print("Папка Image создана")
        time = datetime.today().strftime("%d%m%Y_%H%M%S")
        plt.savefig("Lagrange/Image/" + str(time) + "Image.png")



    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.init_ui()

    def _saveLog(self):
        if os.path.exists("Lagrange/Logs"):
            print("Папка Logs уже существует")
        else:
            os.mkdir("Lagrange/Logs")
            print("Папка Logs создана")
        text = self.LogText.get("1.0", "end-1c")
        time = datetime.today().strftime("%d%m%Y_%H%M%S")
        text_file = open("Lagrange/Logs/" + str(time) + "Log.txt", "w")
        text_file.write(str(text))
        text_file.close()

    def _useParams(self):
        M0, M1, M2, f1, c, e, F, vp, steps, t = self.InputText.get(), self.InputText2.get(), self.InputText3.get(), 1, 200000, self.InputText6.get(), 0, 0, self.InputText9.get(), self.InputText10.get()

        if os.path.exists("Lagrange/Params"):
            print("Папка Params уже существует")
        else:
            os.mkdir("Lagrange/Params")
            print("Папка Params создана")

        text_file, text_file1, text_file2, text_file3, text_file4 = open("Lagrange/Params/M0-M1.txt", "w"), open(
            "Lagrange/Params/M2-f.txt",
            "w"), open(
            "Lagrange/Params/c-e.txt", "w"), open("Lagrange/Params/F-vp.txt", "w"), open("Lagrange/Params/steps-t.txt", "w")

        text_file.write(str(M0) + ";" + str(M1) + "\n")
        text_file1.write(str(M2) + ";" + str(f1) + "\n")
        text_file2.write(str(c) + ";" + str(e) + "\n")
        text_file3.write(str(F) + ";" + str(vp) + "\n")
        text_file4.write(str(steps) + ";" + str(t) + "\n")
        text_file.close()
        text_file1.close()
        text_file2.close()
        text_file3.close()
        text_file4.close()
        with open("Lagrange/tel3_2_1.py", "r") as f:
            exec(f.read())
        with open("Lagrange/tel3_12lagr111.py", "r") as f:
            exec(f.read())
        with open("Lagrange/tel3_Lagrang3.py", "r") as f:
            exec(f.read())

    def _start_grath(self):
        k1_X_Y_data_NumOne = open("Lagrange/Coords/k_NumOne.txt", "r").read()
        k1_X_Y_data_NumTwo = open("Lagrange/Coords/k_NumTwo.txt", "r").read()
        k1_X_Y_data_NumThree = open("Lagrange/Coords/k_NumThree.txt", "r").read()

        k1_X_Y_data_NumOne = k1_X_Y_data_NumOne.split('\n')
        k1_X_Y_data_NumTwo = k1_X_Y_data_NumTwo.split('\n')
        k1_X_Y_data_NumThree = k1_X_Y_data_NumThree.split('\n')

        k1_x_NumOne, k1_y_NumOne, k1_x_NumTwo, k1_y_NumTwo, k1_x_NumThree, k1_y_NumThree = [], [], [], [], [], []

        for line in k1_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                k1_x_NumOne.append(float(x))
                k1_y_NumOne.append(float(y))
        for line in k1_X_Y_data_NumTwo:
            if len(line) > 1:
                x, y = line.split(';')
                k1_x_NumTwo.append(float(x))
                k1_y_NumTwo.append(float(y))
        for line in k1_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                k1_x_NumThree.append(float(x))
                k1_y_NumThree.append(float(y))

        H_X_Y_data_NumOne = open("Lagrange/Coords/H_NumOne.txt", "r").read()
        H_X_Y_data_NumTwo = open("Lagrange/Coords/H_NumTwo.txt", "r").read()
        H_X_Y_data_NumThree = open("Lagrange/Coords/H_NumThree.txt", "r").read()

        H_X_Y_data_NumOne = H_X_Y_data_NumOne.split('\n')
        H_X_Y_data_NumTwo = H_X_Y_data_NumTwo.split('\n')
        H_X_Y_data_NumThree = H_X_Y_data_NumThree.split('\n')

        H_x_NumOne, H_y_NumOne, H_x_NumTwo, H_y_NumTwo, H_x_NumThree, H_y_NumThree = [], [], [], [], [], []

        for line in H_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                H_x_NumOne.append(float(x))
                H_y_NumOne.append(float(y))
        for line in H_X_Y_data_NumTwo:
            if len(line) > 1:
                x, y = line.split(';')
                H_x_NumTwo.append(float(x))
                H_y_NumTwo.append(float(y))
        for line in H_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                H_x_NumThree.append(float(x))
                H_y_NumThree.append(float(y))

        C_X_Y_data_NumOne = open("Lagrange/Coords/C_NumOne.txt", "r").read()
        C_X_Y_data_NumTwo = open("Lagrange/Coords/C_NumTwo.txt", "r").read()
        C_X_Y_data_NumThree = open("Lagrange/Coords/C_NumThree.txt", "r").read()

        C_X_Y_data_NumOne = C_X_Y_data_NumOne.split('\n')
        C_X_Y_data_NumTwo = C_X_Y_data_NumTwo.split('\n')
        C_X_Y_data_NumThree = C_X_Y_data_NumThree.split('\n')

        C_x_NumOne, C_y_NumOne, C_x_NumTwo, C_y_NumTwo, C_x_NumThree, C_y_NumThree = [], [], [], [], [], []

        for line in C_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                C_x_NumOne.append(float(x))
                C_y_NumOne.append(float(y))
        for line in C_X_Y_data_NumTwo:
            if len(line) > 1:
                x, y = line.split(';')
                C_x_NumTwo.append(float(x))
                C_y_NumTwo.append(float(y))
        for line in C_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                C_x_NumThree.append(float(x))
                C_y_NumThree.append(float(y))

        M0_M1_data = open('Lagrange/Params/M0-M1.txt', 'r').read()
        M2_f_data = open('Lagrange/Params/M2-f.txt', 'r').read()
        c_e_data = open('Lagrange/Params/c-e.txt', 'r').read()
        F_vp_data = open('Lagrange/Params/F-vp.txt', 'r').read()
        steps_t_data = open('Lagrange/Params/steps-t.txt', 'r').read()

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

        r1_X_Y_data_NumOne, r2_X_Y_data_NumOne, r3_X_Y_data_NumOne = open('Lagrange/Coords/coord0_NumOne.txt', 'r').read(), open(
            'Lagrange/Coords/coord1_NumOne.txt', 'r').read(), open('Lagrange/Coords/coord2_NumOne.txt', 'r').read()
        r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = open('Lagrange/Coords/coord0_NumTwo.txt', 'r').read(), open(
            'Lagrange/Coords/coord1_NumTwo.txt', 'r').read(), open('Lagrange/Coords/coord2_NumTwo.txt', 'r').read()
        r1_X_Y_data_NumThree, r2_X_Y_data_NumThree, r3_X_Y_data_NumThree = open('Lagrange/Coords/coord0_NumThree.txt',
                                                                                'r').read(), open(
            'Lagrange/Coords/coord1_NumThree.txt', 'r').read(), open('Lagrange/Coords/coord2_NumThree.txt', 'r').read()
        v1_X_Y_data_NumOne, v2_X_Y_data_NumOne, v3_X_Y_data_NumOne = open('Lagrange/Coords/speed0_NumOne.txt', 'r').read(), open(
            'Lagrange/Coords/speed1_NumOne.txt', 'r').read(), open('Lagrange/Coords/speed2_NumOne.txt', 'r').read()

        r1_X_Y_data_NumOne, r2_X_Y_data_NumOne, r3_X_Y_data_NumOne = r1_X_Y_data_NumOne.split(
            '\n'), r2_X_Y_data_NumOne.split('\n'), r3_X_Y_data_NumOne.split('\n')
        r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = r1_X_Y_data_NumTwo.split(
            '\n'), r2_X_Y_data_NumTwo.split('\n'), r3_X_Y_data_NumTwo.split('\n')
        r1_X_Y_data_NumThree, r2_X_Y_data_NumThree, r3_X_Y_data_NumThree = r1_X_Y_data_NumThree.split(
            '\n'), r2_X_Y_data_NumThree.split('\n'), r3_X_Y_data_NumThree.split('\n')
        v1_X_Y_data_NumOne, v2_X_Y_data_NumOne, v3_X_Y_data_NumOne = v1_X_Y_data_NumOne.split(
            '\n'), v2_X_Y_data_NumOne.split('\n'), v3_X_Y_data_NumOne.split('\n')

        r1_x_new_NumOne, r1_y_new_NumOne, r2_x_new_NumOne, r2_y_new_NumOne, r3_x_new_NumOne, r3_y_new_NumOne = [], [], [], [], [], []
        r1_x_new_NumTwo, r1_y_new_NumTwo, r2_x_new_NumTwo, r2_y_new_NumTwo, r3_x_new_NumTwo, r3_y_new_NumTwo = [], [], [], [], [], []
        r1_x_new_NumThree, r1_y_new_NumThree, r2_x_new_NumThree, r2_y_new_NumThree, r3_x_new_NumThree, r3_y_new_NumThree = [], [], [], [], [], []
        v1_x_new_NumOne, v1_y_new_NumOne, v2_x_new_NumOne, v2_y_new_NumOne, v3_x_new_NumOne, v3_y_new_NumOne = [], [], [], [], [], []

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
        for line in v1_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                v1_x_new_NumOne.append(float(x))
                v1_y_new_NumOne.append(float(y))
        for line in v2_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                v2_x_new_NumOne.append(float(x))
                v2_y_new_NumOne.append(float(y))
        for line in v3_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                v3_x_new_NumOne.append(float(x))
                v3_y_new_NumOne.append(float(y))

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

        for line in r1_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                r1_x_new_NumThree.append(float(x))
                r1_y_new_NumThree.append(float(y))
        for line in r2_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                r2_x_new_NumThree.append(float(x))
                r2_y_new_NumThree.append(float(y))
        for line in r3_X_Y_data_NumThree:
            if len(line) > 1:
                x, y = line.split(';')
                r3_x_new_NumThree.append(float(x))
                r3_y_new_NumThree.append(float(y))

        time = datetime.now()

        #InpTxt, InpTxt2, InpTxt3, InpTxt4, InpTxt5, InpTxt6, InpTxt7, InpTxt8, InpTxt9, InpTxt10 = self.InputText.get(), self.InputText2.get(), self.InputText3.get(), self.InputText4.get(), self.InputText5.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get(), self.InputText9.get(), self.InputText10.get()

        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.ax5.clear()
        self.ax6.clear()

        self.ax1.set(title='#1 Плоское частное решение Лагранжа задачи трех тел,\n расчет уравнением Ляпунова')
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.ax1.plot(r1_x_new_NumOne, r1_y_new_NumOne, linewidth=1, color='black', label='r0')
        self.ax1.plot(r2_x_new_NumOne, r2_y_new_NumOne, linewidth=1, color='blue', label='r1')
        self.ax1.plot(r3_x_new_NumOne, r3_y_new_NumOne, linewidth=1, color='red', label='r2')
        self.ax1.legend()
        # ax1.legend(bbox_to_anchor=(0.165, 1.3))
        # ax1.set_aspect('equal', adjustable='box', anchor='C')

        self.ax2.set(title='#2 Плоское частное решение Лагранжа задачи трех тел,\n метод относительных координат')
        self.ax2.set_xlabel('x')
        self.ax2.set_ylabel('y')
        self.ax2.plot(r1_x_new_NumTwo, r1_y_new_NumTwo, linewidth=1, color='black', label='r0')
        self.ax2.plot(r2_x_new_NumTwo, r2_y_new_NumTwo, linewidth=1, color='blue', label='r1')
        self.ax2.plot(r3_x_new_NumTwo, r3_y_new_NumTwo, linewidth=1, color='red', label='r2')
        self.ax2.legend()
        # ax2.set_aspect('equal', adjustable='box', anchor='C')

        self.ax3.set(title='#3 Плоское частное решение Лагранжа задачи трех тел,\n метод барицентрических координат')
        self.ax3.set_xlabel('x')
        self.ax3.set_ylabel('y')
        self.ax3.plot(r1_x_new_NumThree, r1_y_new_NumThree, linewidth=1, color='black', label='r0')
        self.ax3.plot(r2_x_new_NumThree, r2_y_new_NumThree, linewidth=1, color='blue', label='r1')
        self.ax3.plot(r3_x_new_NumThree, r3_y_new_NumThree, linewidth=1, color='red', label='r2')
        self.ax3.legend()
        # ax3.set_aspect('equal', adjustable='box', anchor='C')

        self.ax4.set(title='#4 График отношения H по времени к начальным значениям')
        self.ax4.set_xlabel('t')
        self.ax4.set_ylabel('H')
        self.ax4.plot(H_x_NumOne, H_y_NumOne, linewidth=1, color='orange', label='h0')
        self.ax4.plot(H_x_NumTwo, H_y_NumTwo, linewidth=1, color='blue', label='h1')
        self.ax4.plot(H_x_NumThree, H_y_NumThree, linewidth=1, color='red', label='h2')
        self.ax4.legend()
        # ax4.set_aspect('equal', adjustable='box', anchor='C')

        self.ax5.set(title='#5 График отношения C по времени к начальным значениям')
        self.ax5.set_xlabel('t')
        self.ax5.set_ylabel('C')
        self.ax5.plot(C_x_NumOne, C_y_NumOne, linewidth=1, color='orange', label='c0')
        self.ax5.plot(C_x_NumTwo, C_y_NumTwo, linewidth=1, color='blue', label='c1')
        self.ax5.plot(C_x_NumThree, C_y_NumThree, linewidth=1, color='red', label='c2')
        self.ax5.legend()
        # ax4.set_aspect('equal', adjustable='box', anchor='C')

        self.ax6.set(title='#6 График отношения сторон треугольников')
        self.ax6.set_xlabel('t')
        self.ax6.set_ylabel('k')
        self.ax6.plot(k1_x_NumOne, k1_y_NumOne, linewidth=1, color='orange', label='k1')
        self.ax6.plot(k1_x_NumTwo, k1_y_NumTwo, linewidth=1, color='blue', label='k2')
        self.ax6.plot(k1_x_NumThree, k1_y_NumThree, linewidth=1, color='red', label='k3')
        self.ax6.legend()
        # ax5.set_aspect('equal', adjustable='box', anchor='C')

        self.canvas.draw_idle()
        text = f"{time}:\nM0 = {M0_date[0]} M1 = {M1_date[0]} M2 = {M2_date[0]}\nf = {f_date[0]} c = {c_date[0]} e = {e_date[0]}\nF = {F_date[0]} vp = {vp_date[0]}\nКоличество шагов = {steps_date[0]}\nШаг интегрирования = {t_date[0]}\n" \
               f"r_1=(x_1,y_1)=({round(r1_x_new_NumOne[0], 7)},{round(r1_y_new_NumOne[0], 7)})\nr_2=(x_2,y_2)=({round(r2_x_new_NumOne[0], 7)},{round(r2_y_new_NumOne[0], 7)})\nr_3=(x_3,y_3)=({round(r3_x_new_NumOne[0], 7)},{round(r3_y_new_NumOne[0], 7)})\n" \
               f"v_1=(xv_1,yv_1)=({round(v1_x_new_NumOne[0], 7)},{round(v1_y_new_NumOne[0], 7)})\nv_2=(xv_2,yv_2)=({round(v2_x_new_NumOne[0], 7)},{round(v2_y_new_NumOne[0], 7)})\nv_3=(xv_3,yv_3)=({round(v3_x_new_NumOne[0], 7)},{round(v3_y_new_NumOne[0], 7)})\n\n"

        self.LogText.insert(1.0, text)

    def init_ui(self):


        self.fig, (self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6) = plt.subplots(6)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relwidth=0.6, relheight=5, relx=0, rely=0)

        self.scrollbar = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        self.scrollbar["command"] = self.canvas.get_tk_widget().yview
        self.scrollbar.place(relwidth=0.02, relheight=1, relx=0.601, rely=0)

        self.scrollbar1 = tk.Scrollbar(master=self, orient=tk.HORIZONTAL)
        self.scrollbar1["command"] = self.canvas.get_tk_widget().xview
        self.scrollbar1.place(relwidth=0.6, relheight=0.03, relx=0, rely=0.972)

        self.InputText = tk.Entry(self)
        self.InputText.place(relwidth=0.05, relx=0.7, rely=0.05)
        self.MassLabel0 = tk.Label(self, text="M0=")
        self.MassLabel0.place(relwidth=0.03, relx=0.67, rely=0.05)

        self.InputText2 = tk.Entry(self)
        self.InputText2.place(relwidth=0.05, relx=0.8, rely=0.05)
        self.MassLabel1 = tk.Label(self, text="M1=")
        self.MassLabel1.place(relwidth=0.03, relx=0.77, rely=0.05)

        self.InputText3 = tk.Entry(self)
        self.InputText3.place(relwidth=0.05, relx=0.9, rely=0.05)
        self.MassLabel2 = tk.Label(self, text="M2=")
        self.MassLabel2.place(relwidth=0.03, relx=0.87, rely=0.05)

        #self.InputText4 = tk.Entry(self)
        #self.InputText4.place(relwidth=0.05, relx=0.7, rely=0.1)
        #self.MassLabel3 = tk.Label(self, text="f=")
        #self.MassLabel3.place(relwidth=0.03, relx=0.67, rely=0.1)

        #self.InputText5 = tk.Entry(self)
        #self.InputText5.place(relwidth=0.05, relx=0.8, rely=0.1)
        #self.MassLabel4 = tk.Label(self, text="c=")
        #self.MassLabel4.place(relwidth=0.03, relx=0.77, rely=0.1)

        self.InputText6 = tk.Entry(self)
        self.InputText6.place(relwidth=0.05, relx=0.8, rely=0.1)
        self.MassLabel5 = tk.Label(self, text="e=")
        self.MassLabel5.place(relwidth=0.03, relx=0.77, rely=0.1)

        #self.InputText7 = tk.Entry(self)
        #self.InputText7.place(relwidth=0.05, relx=0.7, rely=0.15)
        #self.MassLabel6 = tk.Label(self, text="F=")
        #self.MassLabel6.place(relwidth=0.03, relx=0.67, rely=0.15)

        #self.InputText8 = tk.Entry(self)
        #self.InputText8.place(relwidth=0.05, relx=0.9, rely=0.15)
        #self.MassLabel7 = tk.Label(self, text="vp=")
        #self.MassLabel7.place(relwidth=0.03, relx=0.87, rely=0.15)

        self.InputText9 = tk.Entry(self)
        self.InputText9.place(relwidth=0.05, relx=0.80, rely=0.22)
        self.MassLabel8 = tk.Label(self, text="Интервал")
        self.MassLabel8.place(relwidth=0.12, relx=0.765, rely=0.19)

        self.InputText10 = tk.Entry(self)
        self.InputText10.place(relwidth=0.05, relx=0.80, rely=0.29)
        self.MassLabel9 = tk.Label(self, text="Шаг")
        self.MassLabel9.place(relwidth=0.12, relx=0.765, rely=0.26)

        self.WelcomeLabel = tk.Label(self, text="Введите параметры!")
        self.WelcomeLabel.place(relwidth=0.12, relx=0.76, rely=0.01)

        self.StartButton = tk.Button(master=self, text='Построить графики!',
                                     command=self._start_grath)
        self.StartButton.place(relx=0.85, rely=0.33)

        self.TestButton = tk.Button(self, text="Применить параметры!", command=self._useParams).place(relx=0.68,
                                                                                                      rely=0.33)

        self.LogLabel = tk.Label(self,
                                 text="Здесь будет отображаться информация\n о введенных вами данными и начальные условия точек!")
        self.LogLabel.place(relwidth=0.35, relheight=0.05, relx=0.635, rely=0.69)

        self.SaveDataButton = tk.Button(master=self, text='Сохранить данные', command=self._saveLog)
        self.SaveDataButton.place(relx=0.65, rely=0.95)

        self.f = tk.Frame(self)
        self.f.place(relwidth=0.35, relheight=0.2, relx=0.65, rely=0.75)

        self.scrollbar = tk.Scrollbar(self.f)
        self.LogText = tk.Text(self.f, yscrollcommand=self.scrollbar.set)
        self.LogText.place(relwidth=0.899, relheight=0.9)
        self.scrollbar.config(command=self.LogText.yview)
        self.scrollbar.place(relwidth=0.07, relheight=0.9, relx=0.90, rely=0.005)

        plt.subplots_adjust(hspace=0.7)

