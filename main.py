from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np
import os
from datetime import datetime
import time


def _refresh():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def _quit():
    root.destroy()


def _save_figure():
    if os.path.exists("Image"):
        print("Папка Image уже существует")
    else:
        os.mkdir("Image")
        print("Папка Image создана")
    time = datetime.today().strftime("%d%m%Y_%H%M%S")
    plt.savefig("Image/" + str(time) + "Image.png")


root = Tk()
root.geometry('1000x700')
root.title("Плоское частное решение Лагранжа задачи трех тел.")
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Сохранить графики...", command=_save_figure)
# filemenu.add_command(label="Перезапуск", command=_refresh)
filemenu.add_command(label="Выход", command=_quit)

helpmenu = Menu(mainmenu, tearoff=0)
testmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Инструменты", menu=filemenu)
mainmenu.add_cascade(label="Тестирование", menu=testmenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

data = np.random.rand(100)
t = np.arange(0, 100, 1)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)


def _saveLog():
    if os.path.exists("Logs"):
        print("Папка Logs уже существует")
    else:
        os.mkdir("Logs")
        print("Папка Logs создана")
    text = LogText.get("1.0", "end-1c")
    time = datetime.today().strftime("%d%m%Y_%H%M%S")
    text_file = open("Logs/" + str(time) + "Log.txt", "w")
    text_file.write(str(text))
    text_file.close()


def _useParams():
    M0, M1, M2, f, c, e, F, vp, steps, t = InputText.get(), InputText2.get(), InputText3.get(), InputText4.get(), InputText5.get(), InputText6.get(), InputText7.get(), InputText8.get(), InputText9.get(), InputText10.get()

    if os.path.exists("Params"):
        print("Папка Params уже существует")
    else:
        os.mkdir("Params")
        print("Папка Params создана")
    text_file, text_file1, text_file2, text_file3, text_file4 = open("Params/M0-M1.txt", "w"), open("Params/M2-f.txt",
                                                                                                    "w"), open(
        "Params/c-e.txt", "w"), open("Params/F-vp.txt", "w"), open("Params/steps-t.txt", "w")

    text_file.write(str(M0) + ";" + str(M1) + "\n")
    text_file1.write(str(M2) + ";" + str(f) + "\n")
    text_file2.write(str(c) + ";" + str(e) + "\n")
    text_file3.write(str(F) + ";" + str(vp) + "\n")
    text_file4.write(str(steps) + ";" + str(t) + "\n")
    text_file.close()
    text_file1.close()
    text_file2.close()
    text_file3.close()
    text_file4.close()
    with open("tel3_2_1.py", "r") as f:
        exec(f.read())
    with open("tel3_12lagr111.py", "r") as f:
        exec(f.read())
    with open("tel3_Lagrang3.py", "r") as f:
        exec(f.read())


def _start_grath():
    r1_X_Y_data_NumOne, r2_X_Y_data_NumOne, r3_X_Y_data_NumOne = open('Coords/coord0_NumOne.txt', 'r').read(), open(
        'Coords/coord1_NumOne.txt', 'r').read(), open('Coords/coord2_NumOne.txt', 'r').read()
    r1_X_Y_data_NumTwo, r2_X_Y_data_NumTwo, r3_X_Y_data_NumTwo = open('Coords/coord0_NumTwo.txt', 'r').read(), open(
        'Coords/coord1_NumTwo.txt', 'r').read(), open('Coords/coord2_NumTwo.txt', 'r').read()
    r1_X_Y_data_NumThree, r2_X_Y_data_NumThree, r3_X_Y_data_NumThree = open('Coords/coord0_NumThree.txt',
                                                                            'r').read(), open(
        'Coords/coord1_NumThree.txt', 'r').read(), open('Coords/coord2_NumThree.txt', 'r').read()
    v1_X_Y_data_NumOne, v2_X_Y_data_NumOne, v3_X_Y_data_NumOne = open('Coords/speed0_NumOne.txt', 'r').read(), open(
        'Coords/speed1_NumOne.txt', 'r').read(), open('Coords/speed2_NumOne.txt', 'r').read()

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

    InpTxt, InpTxt2, InpTxt3, InpTxt4, InpTxt5, InpTxt6, InpTxt7, InpTxt8, InpTxt9, InpTxt10 = InputText.get(), InputText2.get(), InputText3.get(), InputText4.get(), InputText5.get(), InputText6.get(), InputText7.get(), InputText8.get(), InputText9.get(), InputText10.get()

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.set(title='1')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.plot(r1_x_new_NumOne, r1_y_new_NumOne, linewidth=1, color='red')
    ax1.plot(r2_x_new_NumOne, r2_y_new_NumOne, linewidth=1, color='blue')
    ax1.plot(r3_x_new_NumOne, r3_y_new_NumOne, linewidth=1, color='black')
    ax1.set_aspect('equal', adjustable='box', anchor='C')

    ax2.set(title='2')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.plot(r1_x_new_NumTwo, r1_y_new_NumTwo, linewidth=1, color='red')
    ax2.plot(r2_x_new_NumTwo, r2_y_new_NumTwo, linewidth=1, color='blue')
    ax2.plot(r3_x_new_NumTwo, r3_y_new_NumTwo, linewidth=1, color='black')
    ax2.set_aspect('equal', adjustable='box', anchor='C')

    ax3.set(title='3')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.plot(r1_x_new_NumThree, r1_y_new_NumThree, linewidth=1, color='red')
    ax3.plot(r2_x_new_NumThree, r2_y_new_NumThree, linewidth=1, color='blue')
    ax3.plot(r3_x_new_NumThree, r3_y_new_NumThree, linewidth=1, color='black')
    ax3.set_aspect('equal', adjustable='box', anchor='C')

    ax4.set(title='4')
    ax4.set_xlabel('t')
    ax4.set_ylabel('U')
    ax4.plot(r1_x_new_NumOne, r1_y_new_NumOne, linewidth=1, color='red')
    ax4.plot(r2_x_new_NumOne, r2_y_new_NumOne, linewidth=1, color='blue')
    ax4.plot(r3_x_new_NumOne, r3_y_new_NumOne, linewidth=1, color='black')
    ax4.set_aspect('equal', adjustable='box', anchor='C')

    canvas.draw_idle()
    text = f"{time}:\nM0 = {InpTxt} M1 = {InpTxt2} M2 = {InpTxt3}\nf = {InpTxt4} c = {InpTxt5} e = {InpTxt6}\nF = {InpTxt7} vp = {InpTxt8}\nКоличество шагов = {InpTxt9}\nШаг интегрирования = {InpTxt10}\n" \
           f"r_1=(x_1,y_1)=({round(r1_x_new_NumOne[0], 7)},{round(r1_y_new_NumOne[0], 7)})\nr_2=(x_2,y_2)=({round(r2_x_new_NumOne[0], 7)},{round(r2_y_new_NumOne[0], 7)})\nr_3=(x_3,y_3)=({round(r3_x_new_NumOne[0], 7)},{round(r3_y_new_NumOne[0], 7)})\n" \
           f"v_1=(xv_1,yv_1)=({round(v1_x_new_NumOne[0], 7)},{round(v1_y_new_NumOne[0], 7)})\nv_2=(xv_2,yv_2)=({round(v2_x_new_NumOne[0], 7)},{round(v2_y_new_NumOne[0], 7)})\nv_3=(xv_3,yv_3)=({round(v3_x_new_NumOne[0], 7)},{round(v3_y_new_NumOne[0], 7)})\n"

    LogText.insert(1.0, text)


canvas = FigureCanvasTkAgg(fig, master=root)


def combineFunc(*funcs):
    def combinedFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combinedFunc


def _startAnimate():
    with open("tel3_2_1_anim.py", "r") as f:
        exec(f.read())


def _startAnimate1():
    with open("tel3_12lagr_anim.py", "r") as f:
        exec(f.read())


def _startAnimate2():
    with open("tel3_Lagrang3anim.py", "r") as f:
        exec(f.read())


canvas.get_tk_widget().place(relwidth=0.6, relheight=3, relx=0, rely=0)

scrollbar = Scrollbar(master=root, orient=VERTICAL)
scrollbar["command"] = canvas.get_tk_widget().yview
scrollbar.place(relwidth=0.02, relheight=1, relx=0.601, rely=0)

InputText = Entry(root)
InputText.place(relwidth=0.05, relx=0.7, rely=0.05)
MassLabel0 = Label(root, text="M0=")
MassLabel0.place(relwidth=0.03, relx=0.67, rely=0.05)

InputText2 = Entry(root)
InputText2.place(relwidth=0.05, relx=0.8, rely=0.05)
MassLabel1 = Label(root, text="M1=")
MassLabel1.place(relwidth=0.03, relx=0.77, rely=0.05)

InputText3 = Entry(root)
InputText3.place(relwidth=0.05, relx=0.9, rely=0.05)
MassLabel2 = Label(root, text="M2=")
MassLabel2.place(relwidth=0.03, relx=0.87, rely=0.05)

InputText4 = Entry(root)
InputText4.place(relwidth=0.05, relx=0.7, rely=0.1)
MassLabel3 = Label(root, text="f=")
MassLabel3.place(relwidth=0.03, relx=0.67, rely=0.1)

InputText5 = Entry(root)
InputText5.place(relwidth=0.05, relx=0.8, rely=0.1)
MassLabel4 = Label(root, text="c=")
MassLabel4.place(relwidth=0.03, relx=0.77, rely=0.1)

InputText6 = Entry(root)
InputText6.place(relwidth=0.05, relx=0.9, rely=0.1)
MassLabel5 = Label(root, text="e=")
MassLabel5.place(relwidth=0.03, relx=0.87, rely=0.1)

InputText7 = Entry(root)
InputText7.place(relwidth=0.05, relx=0.7, rely=0.15)
MassLabel6 = Label(root, text="F=")
MassLabel6.place(relwidth=0.03, relx=0.67, rely=0.15)

InputText8 = Entry(root)
InputText8.place(relwidth=0.05, relx=0.9, rely=0.15)
MassLabel7 = Label(root, text="vp=")
MassLabel7.place(relwidth=0.03, relx=0.87, rely=0.15)

InputText9 = Entry(root)
InputText9.place(relwidth=0.05, relx=0.80, rely=0.22)
MassLabel8 = Label(root, text="Количество шагов")
MassLabel8.place(relwidth=0.12, relx=0.76, rely=0.19)

InputText10 = Entry(root)
InputText10.place(relwidth=0.05, relx=0.80, rely=0.29)
MassLabel9 = Label(root, text="Шаг интегрирования")
MassLabel9.place(relwidth=0.12, relx=0.76, rely=0.26)

WelcomeLabel = Label(root, text="Введите параметры!")
WelcomeLabel.place(relwidth=0.12, relx=0.76, rely=0.01)

StartButton = Button(master=root, text='Построить графики!',
                     command=_start_grath)
StartButton.place(relx=0.85, rely=0.33)

StartAnimationButton = Button(master=root, text='Анимация #1',
                              command=combineFunc(_startAnimate))
StartAnimationButton.place(relx=0.65, rely=0.60)

StartAnimationButton1 = Button(master=root, text='Анимация #2',
                               command=combineFunc(_startAnimate1))
StartAnimationButton1.place(relx=0.768, rely=0.60)

StartAnimationButton2 = Button(master=root, text='Анимация #3',
                               command=combineFunc(_startAnimate2))
StartAnimationButton2.place(relx=0.885, rely=0.60)

TestButton = Button(root, text="Применить параметры!", command=_useParams).place(relx=0.68, rely=0.33)

LogLabel = Label(root, text="Здесь будет отображаться информация\n о введенных вами данными и начальные условия точек!")
LogLabel.place(relwidth=0.35, relheight=0.05, relx=0.635, rely=0.69)

SaveDataButton = Button(master=root, text='Сохранить данные', command=_saveLog)
SaveDataButton.place(relx=0.65, rely=0.95)

f = Frame(root)
f.place(relwidth=0.35, relheight=0.2, relx=0.65, rely=0.75)

scrollbar = Scrollbar(f)
LogText = Text(f, yscrollcommand=scrollbar.set)
LogText.place(relwidth=0.899, relheight=0.9)
scrollbar.config(command=LogText.yview)
scrollbar.place(relwidth=0.07, relheight=0.9, relx=0.90, rely=0.005)

plt.grid(True)
plt.subplots_adjust(hspace=0.7)

root.minsize(950, 600)
root.maxsize(1000, 700)
# plt.close()

root.mainloop()
