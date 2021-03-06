import tkinter as tk
import tkinter.filedialog as fd
import random
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np
import os
from datetime import datetime
import time



class nbody(tk.Frame):

    def _save_figure(self):
        if os.path.exists("Image"):
            print("Папка Image уже существует")
        else:
            os.mkdir("Image")
            print("Папка Image создана")
        time = datetime.today().strftime("%d%m%Y_%H%M%S")
        plt.savefig("Nbody/Image/" + str(time) + "Image.png")



    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.init_ui()

    def _useParams(self):
        if os.path.exists("Nbody/Params"):
            print("Папка Params уже существует")
        else:
            os.mkdir("Nbody/Params")
            print("Папка Params создана")

    def plot_grath(self):
        conditions = open("Nbody/bin/dir.txt", "r")
        text = conditions.read()
        cond = open(f"{text}", "r")
        text_res = cond.read()
        text_final = text_res.split("\n")
        N = int(''.join([n for n in text_final[0] if n.isdigit()]))

        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()

        self.ax1.set(title='#1 Задача N тел.')
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')

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
        #print(f",y ={res_for_plot_y}")
        for i in range(N):
               self.ax1.plot(res_for_plot_x[i], res_for_plot_y[i], linewidth=1, color=(random.random(), random.random(), random.random()))
        self.ax1.set_aspect('equal', adjustable='box', anchor='C')


        C_data_NumOne, H_data_NumOne = open('Nbody/Coords/C_NumOne.txt', 'r').read(), open(
            'Nbody/Coords/H_NumOne.txt', 'r').read()
        C_X_Y_data_NumOne, H_X_Y_data_NumOne = C_data_NumOne.split(
            '\n'), H_data_NumOne.split('\n')
        c_x_new_NumOne, c_y_new_NumOne, h_x_new_NumOne, h_y_new_NumOne = [], [], [], []
        for line in C_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                c_x_new_NumOne.append(float(x))
                c_y_new_NumOne.append(float(y))
        for line in H_X_Y_data_NumOne:
            if len(line) > 1:
                x, y = line.split(';')
                h_x_new_NumOne.append(float(x))
                h_y_new_NumOne.append(float(y))

        self.ax2.set(title='#2 График H.')
        self.ax2.set_xlabel('t')
        self.ax2.set_ylabel('h')
        self.ax2.plot(h_x_new_NumOne, h_y_new_NumOne, linewidth=1,
                      color="orange")


        self.ax3.set(title='#3 График C.')
        self.ax3.set_xlabel('t')
        self.ax3.set_ylabel('c')
        self.ax3.plot(c_x_new_NumOne, c_y_new_NumOne, linewidth=1,
                      color="orange")




        self.canvas.draw_idle()

        conditions1 = open("Nbody/bin/dir.txt", "r")
        text4 = conditions1.read()
        cond1 = open(f"{text4}", "r")
        text_res = cond1.read()
        self.LogText.insert(1.0, text_res)
        conditions1.close()
        cond1.close()


    def _start_grath(self):
        pass

    def init_ui(self):
        def trash():
            pass


        def generate_equation(N, R):
            X = 0
            Y = 0
            file = open("Nbody/start_condions.txt", "w")
            file.write('N=' + str(N) + '\n')
            file.write('f1=' + str(1) + '\n')
            file.write('t = np.arange(' + str(0) + ', ' + str(10) + ', ' + str(0.01) + ')\n')
            for i in range(N):
                angle = 2 * np.pi * i / N
                x = R * np.cos(angle) + X
                y = R * np.sin(angle) + Y
                vx = -y
                vy = x
                file.write(
                    'M' + str(i) + ',' + 'x' + str(i) + ',' + 'vx' + str(i) + ',' + 'y' + str(i) + ',' + 'vy' + str(
                        i) + '=' + str(1) + ',' + str(x) + ',' + str(vx) + ',' + str(y) + ',' + str(vy) + '\n')

        def choose_directory():

            directory = fd.askdirectory(title="Открыть папку", initialdir="/")
            current_dir_file = open("CurDir.txt", "w")
            current_dir_file.write(str(directory) + "/")
            current_dir_file.close()
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            label['text'] = str(text1)
            curr_dir_read1.close()


        def choose_file():
            filepath = fd.askopenfilename(title="Выбрать файл")
            filedir = open("Nbody/bin/dir.txt","w")
            filedir.write(filepath)
            filedir.close()
            with open("Nbody/nbody.py", "r") as f:
                exec(f.read())
        def automatic_cond():
            N = int(self.InputText.get())
            R = float(self.InputText2.get())
            generate_equation(N=N,R=R)

        def _saveLog():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            curr_dir_read1.close()
            if os.path.exists(str(text1) + "Logs"):
                print("Папка Logs уже существует")
            else:
                os.mkdir(str(text1) + "Logs")
                print("Папка Logs создана")
            text = self.LogText.get("1.0", "end-1c")
            time = datetime.today().strftime("%d%m%Y_%H%M%S")
            text_file = open(str(text1) + "Logs/" + str(time) + "Log.txt", "w")
            text_file.write(str(text))
            text_file.close()

        curr_dir_read = open('CurDir.txt', 'r')
        text = curr_dir_read.read()
        label = tk.Label(self, text=str(text), bg='white', justify='left', anchor='w')
        label.place(relwidth=1, relheight=0.037, relx=0.095, rely=0)
        self.ChangeDir = tk.Button(master=self, text='Выбрать папку',
                                   command=choose_directory)
        self.ChangeDir.place(relx=0, rely=0)
        curr_dir_read.close()

        # Холст
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relwidth=0.6, relheight=3, relx=0, rely=0.039)

        self.scrollbar = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        self.scrollbar["command"] = self.canvas.get_tk_widget().yview
        self.scrollbar.place(relwidth=0.02, relheight=0.96, relx=0.601, rely=0.039)

        self.scrollbar1 = tk.Scrollbar(master=self, orient=tk.HORIZONTAL)
        self.scrollbar1["command"] = self.canvas.get_tk_widget().xview
        self.scrollbar1.place(relwidth=0.6, relheight=0.03, relx=0, rely=0.972)
        #Автоматический режим
        self.Label2 = tk.Label(self,
                               text="Чтобы создать файл необходимо указать \n количество тел и параметр.")
        self.Label2.place(relwidth=0.38, relheight=0.05, relx=0.635, rely=0.05)

        self.InputText = tk.Entry(self)
        self.InputText.place(relwidth=0.05, relx=0.73, rely=0.13)
        self.MassLabel0 = tk.Label(self, text="N=")
        self.MassLabel0.place(relwidth=0.03, relx=0.7, rely=0.13)

        self.InputText2 = tk.Entry(self)
        self.InputText2.place(relwidth=0.05, relx=0.83, rely=0.13)
        self.MassLabel1 = tk.Label(self, text="R=")
        self.MassLabel1.place(relwidth=0.03, relx=0.8, rely=0.13)

        self.StartButton = tk.Button(master=self, text='Загрузить файл!',
                                     command=choose_file)
        self.StartButton.place(relx=0.85, rely=0.18)
        self.TestButton = tk.Button(self, text="Создать файл!", command=automatic_cond).place(relx=0.68, rely=0.18)

        self.TestButton1 = tk.Button(self, text="Построить графики!", command=self.plot_grath).place(relx=0.74, rely=0.25)

        # Логи
        self.LogLabel = tk.Label(self,text="Здесь будет отображаться информация\n о введенных вами данными и начальные условия точек!")
        self.LogLabel.place(relwidth=0.35, relheight=0.05, relx=0.635, rely=0.69)

        self.SaveDataButton = tk.Button(master=self, text='Сохранить данные', command=_saveLog)
        self.SaveDataButton.place(relx=0.65, rely=0.95)

        self.f = tk.Frame(self)
        self.f.place(relwidth=0.35, relheight=0.2, relx=0.65, rely=0.75)

        self.scrollbar = tk.Scrollbar(self.f)
        self.LogText = tk.Text(self.f, yscrollcommand=self.scrollbar.set)
        self.LogText.place(relwidth=0.899, relheight=0.9)
        self.scrollbar.config(command=self.LogText.yview)
        self.scrollbar.place(relwidth=0.07, relheight=0.9, relx=0.90, rely=0.005)
        plt.subplots_adjust(hspace=0.4)