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


class common(tk.Frame):



    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.init_ui()

    def _saveLog(self):
        if os.path.exists("CommonProblem/Logs"):
            print("Папка Logs уже существует")
        else:
            os.mkdir("CommonProblem/Logs")
            print("Папка Logs создана")
        text = self.LogText.get("1.0", "end-1c")
        time = datetime.today().strftime("%d%m%Y_%H%M%S")
        text_file = open("CommonProblem/Logs/" + str(time) + "Log.txt", "w")
        text_file.write(str(text))
        text_file.close()

    def _useParams(self):

        M0, M1, M2, steps, t, f1 = self.InputText.get(), self.InputText2.get(), self.InputText3.get(), self.InputText9.get(), self.InputText10.get(), 1
        r1x, r1y, r2x, r2y  = self.InputText4.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get()
        v1x, v1y, v2x, v2y = self.InputText01.get(), self.InputText02.get(), self.InputText03.get(), self.InputText04.get()
        if os.path.exists("CommonProblem/Params"):
            print("Папка Params уже существует")
        else:
            os.mkdir("CommonProblem/Params")
            print("Папка Params создана")

        text_file, text_file1, text_file01= open("CommonProblem/Params/M0-M1.txt", "w"), open(
            "CommonProblem/Params/M2-f.txt",
            "w"), open("CommonProblem/Params/steps-t.txt", "w")
        text_file2, text_file3 = open("CommonProblem/Params/r1x-r1y.txt", "w"),open("CommonProblem/Params/r2x-r2y.txt", "w")
        text_file4, text_file5 = open("CommonProblem/Params/v1x-v1y.txt", "w"),open("CommonProblem/Params/v2x-v2y.txt", "w")
        text_file.write(str(M0) + ";" + str(M1) + "\n")
        text_file1.write(str(M2) + ";" + str(f1) + "\n")
        text_file01.write(str(steps) + ";" + str(t) + "\n")
        text_file2.write(str(r1x) + ";" + str(r1y) + "\n")
        text_file3.write(str(r2x) + ";" + str(r2y) + "\n")
        text_file4.write(str(v1x) + ";" + str(v1y) + "\n")
        text_file5.write(str(v2x) + ";" + str(v2y) + "\n")

        text_file.close()
        text_file1.close()
        text_file2.close()
        text_file3.close()
        text_file4.close()
        text_file5.close()
        text_file01.close()

        with open("CommonProblem/tel3_0.py", "r") as f:
            exec(f.read())


    def _start_grath(self):

        H_X_Y_data_NumOne = open("CommonProblem/Coords/H_NumOne.txt", "r").read()

        H_X_Y_data_NumOne = H_X_Y_data_NumOne.split('\n')

        H_x_NumOne, H_y_NumOne = [], []

        for line in H_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                H_x_NumOne.append(float(x))
                H_y_NumOne.append(float(y))

        C_X_Y_data_NumOne = open("CommonProblem/Coords/C_NumOne.txt", "r").read()

        C_X_Y_data_NumOne = C_X_Y_data_NumOne.split('\n')

        C_x_NumOne, C_y_NumOne = [], []

        for line in C_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                C_x_NumOne.append(float(x))
                C_y_NumOne.append(float(y))

        M0_M1_data = open('CommonProblem/Params/M0-M1.txt', 'r').read()
        M2_f_data = open('CommonProblem/Params/M2-f.txt', 'r').read()
        steps_t_data = open('CommonProblem/Params/steps-t.txt', 'r').read()
        r0x_r0y_data = open('CommonProblem/Coords/coord0_NumOne.txt', 'r').read()
        r1x_r1y_data = open('CommonProblem/Coords/coord1_NumOne.txt', 'r').read()
        r2x_r2y_data = open('CommonProblem/Coords/coord2_NumOne.txt', 'r').read()
        v0x_v0y_data = open('CommonProblem/Coords/speed0_NumOne.txt', 'r').read()
        v1x_v1y_data = open('CommonProblem/Coords/speed1_NumOne.txt', 'r').read()
        v2x_v2y_data = open('CommonProblem/Coords/speed2_NumOne.txt', 'r').read()

        M0_M1 = M0_M1_data.split('\n')
        M2_f = M2_f_data.split('\n')
        steps_t = steps_t_data.split('\n')

        r1x_r1y = r1x_r1y_data.split('\n')
        r2x_r2y = r2x_r2y_data.split('\n')
        v1x_v1y = v1x_v1y_data.split('\n')
        v2x_v2y = v2x_v2y_data.split('\n')
        r0x_r0y = r0x_r0y_data.split('\n')
        v0x_v0y = v0x_v0y_data.split('\n')

        M0_date,M1_date, M2_date, f_date, steps_date,t_date = [],[],[],[],[],[]

        r1x_date, r1y_date, r2x_date, r2y_date, r0x_date, r0y_date = [],[],[],[], [], []
        v1x_date, v1y_date, v2x_date, v2y_date, v0x_date, v0y_date = [],[],[],[], [],[]

        for line in r1x_r1y:
            if len(line) > 1:
                x, y = line.split(';')
                r1x_date.append(float(x))
                r1y_date.append(float(y))
        for line in r2x_r2y:
            if len(line) > 1:
                x, y = line.split(';')
                r2x_date.append(float(x))
                r2y_date.append(float(y))
        for line in r0x_r0y:
            if len(line) > 1:
                x, y = line.split(';')
                r0x_date.append(float(x))
                r0y_date.append(float(y))
        for line in v1x_v1y:
            if len(line) > 1:
                x, y = line.split(';')
                v1x_date.append(float(x))
                v1y_date.append(float(y))
        for line in v2x_v2y:
            if len(line) > 1:
                x, y = line.split(';')
                v2x_date.append(float(x))
                v2y_date.append(float(y))
        for line in v0x_v0y:
            if len(line) > 1:
                x, y = line.split(';')
                v0x_date.append(float(x))
                v0y_date.append(float(y))

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
        for line in steps_t:
            if len(line) > 1:
                x, y = line.split(';')
                steps_date.append(float(x))
                t_date.append(float(y))



        time = datetime.now()


        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()


        self.ax1.set(title='#1 Общее решение задачи трех тел.')
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.ax1.plot(r0x_date, r0y_date, linewidth=1, color='black', label='r0')
        self.ax1.plot(r1x_date, r1y_date, linewidth=1, color='blue', label='r1')
        self.ax1.plot(r2x_date, r2y_date, linewidth=1, color='red', label='r2')
        self.ax1.legend()
        # ax1.legend(bbox_to_anchor=(0.165, 1.3))
        # ax1.set_aspect('equal', adjustable='box', anchor='C')

        self.ax2.set(title='#2 График  H по времени')
        self.ax2.set_xlabel('t')
        self.ax2.set_ylabel('H')
        self.ax2.plot(H_x_NumOne, H_y_NumOne, linewidth=1, color='orange', label='h0')
        self.ax2.legend()
        # ax4.set_aspect('equal', adjustable='box', anchor='C')

        self.ax3.set(title='#3 График  C по времени')
        self.ax3.set_xlabel('t')
        self.ax3.set_ylabel('C')
        self.ax3.plot(C_x_NumOne, C_y_NumOne, linewidth=1, color='orange', label='c0')
        self.ax3.legend()
        # ax4.set_aspect('equal', adjustable='box', anchor='C')

        self.canvas.draw_idle()
        text = f"{time}:\nM0 = {M0_date[0]} M1 = {M1_date[0]} M2 = {M2_date[0]}\nr0(x,y) = ({round(r0x_date[0],6)},{round(r0y_date[0],6)})\nr1(x,y) = ({round(r1x_date[0],6)},{round(r1y_date[0],6)})\nr2(x,y) = ({round(r2x_date[0],)},{round(r2y_date[0],6)})\nКоличество шагов = {steps_date[0]}\nШаг интегрирования = {t_date[0]}\n"

        self.LogText.insert(1.0, text)

    def init_ui(self):


        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relwidth=0.6, relheight=4, relx=0, rely=0)

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

        #self.InputText11 = tk.Entry(self)
        #self.InputText11.place(relwidth=0.05, relx=0.8, rely=0.1)
        #self.MassLabel11 = tk.Label(self, text="f=")
        #self.MassLabel11.place(relwidth=0.03, relx=0.77, rely=0.1)

        self.InputText4 = tk.Entry(self)
        self.InputText4.place(relwidth=0.05, relx=0.7, rely=0.1)
        self.MassLabel3 = tk.Label(self, text="r1x=")
        self.MassLabel3.place(relwidth=0.03, relx=0.67, rely=0.1)

        self.InputText6 = tk.Entry(self)
        self.InputText6.place(relwidth=0.05, relx=0.9, rely=0.1)
        self.MassLabel5 = tk.Label(self, text="r1y=")
        self.MassLabel5.place(relwidth=0.03, relx=0.87, rely=0.1)

        self.InputText7 = tk.Entry(self)
        self.InputText7.place(relwidth=0.05, relx=0.7, rely=0.15)
        self.MassLabel6 = tk.Label(self, text="r2x=")
        self.MassLabel6.place(relwidth=0.03, relx=0.67, rely=0.15)

        self.InputText8 = tk.Entry(self)
        self.InputText8.place(relwidth=0.05, relx=0.9, rely=0.15)
        self.MassLabel7 = tk.Label(self, text="r2y=")
        self.MassLabel7.place(relwidth=0.03, relx=0.87, rely=0.15)



        self.InputText01 = tk.Entry(self)
        self.InputText01.place(relwidth=0.05, relx=0.7, rely=0.2)
        self.MassLabel01 = tk.Label(self, text="v1x=")
        self.MassLabel01.place(relwidth=0.03, relx=0.67, rely=0.2)

        self.InputText02 = tk.Entry(self)
        self.InputText02.place(relwidth=0.05, relx=0.9, rely=0.2)
        self.MassLabel02 = tk.Label(self, text="v1y=")
        self.MassLabel02.place(relwidth=0.03, relx=0.87, rely=0.2)

        self.InputText03 = tk.Entry(self)
        self.InputText03.place(relwidth=0.05, relx=0.7, rely=0.25)
        self.MassLabel03 = tk.Label(self, text="v2x=")
        self.MassLabel03.place(relwidth=0.03, relx=0.67, rely=0.25)

        self.InputText04 = tk.Entry(self)
        self.InputText04.place(relwidth=0.05, relx=0.9, rely=0.25)
        self.MassLabel04 = tk.Label(self, text="v2y=")
        self.MassLabel04.place(relwidth=0.03, relx=0.87, rely=0.25)


        self.InputText9 = tk.Entry(self)
        self.InputText9.place(relwidth=0.05, relx=0.80, rely=0.32)
        self.MassLabel8 = tk.Label(self, text="Интервал")
        self.MassLabel8.place(relwidth=0.12, relx=0.765, rely=0.29)

        self.InputText10 = tk.Entry(self)
        self.InputText10.place(relwidth=0.05, relx=0.80, rely=0.39)
        self.MassLabel9 = tk.Label(self, text="Шаг")
        self.MassLabel9.place(relwidth=0.12, relx=0.765, rely=0.36)

        self.WelcomeLabel = tk.Label(self, text="Введите параметры!")
        self.WelcomeLabel.place(relwidth=0.12, relx=0.76, rely=0.00)

        self.StartButton = tk.Button(master=self, text='Построить графики!',
                                     command=self._start_grath)
        self.StartButton.place(relx=0.85, rely=0.43)

        self.TestButton = tk.Button(self, text="Применить параметры!", command=self._useParams).place(relx=0.68,
                                                                                                      rely=0.43)

        self.LogLabel = tk.Label(self,
                                 text="Здесь будет отображаться информация\n о введенных вами данных!")
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