from tkinter import Tk, ttk
import tkinter as tk
from lagrangeMain import lagrange as TabA
from CommonMain import common as TabB
from EylerMain import eyler as TabC
from testMain import testmain as TabD
from nbodyMain import nbody as TabF
import random
import os
def _quit():
    root.destroy()


def _startAnimate():
    with open("Lagrange/tel3_2_1_anim.py", "r") as f:
        exec(f.read())


def _startAnimate1():
    with open("Lagrange/tel3_12lagr_anim.py", "r") as f:
        exec(f.read())


def _startAnimate2():
    with open("Lagrange/tel3_Lagrang3anim.py", "r") as f:
        exec(f.read())

def _startAnimate3():
    with open("Eyler/tel3_2Eyler1_anim.py", "r") as f:
        exec(f.read())


def _startAnimate4():
    with open("Eyler/tel3_Eyler12anim.py", "r") as f:
        exec(f.read())


def _startAnimate5():
    with open("Eyler/tel3_Eyler13anim.py", "r") as f:
        exec(f.read())


def _startGrathOne():
    with open("Lagrange/GrathOne/Grath#1.py", "r") as f:
        exec(f.read())


def _startGrathOne1():
    with open("Lagrange/GrathOne/Grath#2.py", "r") as f:
        exec(f.read())


def _startGrathOne2():
    with open("Lagrange/GrathOne/Grath#3.py", "r") as f:
        exec(f.read())
def _startGrathOne3():
    with open("Eyler/GrathOne/Grath#1.py", "r") as f:
        exec(f.read())


def _startGrathOne4():
    with open("Eyler/GrathOne/Grath#2.py", "r") as f:
        exec(f.read())


def _startGrathOne5():
    with open("Eyler/GrathOne/Grath#3.py", "r") as f:
        exec(f.read())

def _startGrathOne6():
    with open("CommonProblem/GrathOne/Grath#1.py", "r") as f:
        exec(f.read())

def _startGrathOne7():
    with open("Nbody/GrathOne/Grath#1.py", "r") as f:
        exec(f.read())
def _startAnimate6():
    with open("Nbody/nbody_anim.py", "r") as f:
        exec(f.read())
def _trash():
    pass
class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('Плоские частные решения в задаче трех тел.')

        self.init_ui()

    def init_ui(self):
        # self.parent['padx'] = 10
        # self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1000, height=700)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)
        c_tab = TabC(self.notebook)
        d_tab = TabD(self.notebook)
        f_tab = TabF(self.notebook)

        self.notebook.add(b_tab, text="Общее")
        self.notebook.add(a_tab, text="Лагранж")
        self.notebook.add(c_tab, text="Эйлер")
        self.notebook.add(f_tab, text="N тел")
        self.notebook.add(d_tab, text="Тестирование")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Плоские частные решения в задаче трех тел.')
    if os.path.exists("Lagrange"):
        print("Папка Lagrange уже существует")
    else:
        os.mkdir("Lagrange")
        print("Папка Lagrange создана")
    if os.path.exists("Eyler"):
        print("Папка Eyler уже существует")
    else:
        os.mkdir("Eyler")
        print("Папка Eyler создана")
    if os.path.exists("CommonProblem"):
        print("Папка CommonProblem уже существует")
    else:
        os.mkdir("CommonProblem")
        print("Папка CommonProblem создана")
    if os.path.exists("Nbody"):
        print("Папка Nbody уже существует")
    else:
        os.mkdir("Nbody")
        print("Папка Nbody создана")
    ex = MainWindow(root)
    mainmenu = tk.Menu(root)
    root.config(menu=mainmenu)
    filemenu = tk.Menu(mainmenu, tearoff=0)

    #filemenu.add_command(label="Сохранить графики...")
    filemenu.add_command(label="Выход", command=_quit)

    grathmenu = tk.Menu(mainmenu, tearoff=0)
    animationmenu = tk.Menu(mainmenu, tearoff=0)
    grathmenu1 = tk.Menu(grathmenu, tearoff=0)
    grathmenu2 = tk.Menu(grathmenu, tearoff=0)
    grathmenu3 = tk.Menu(grathmenu, tearoff=0)
    grathmenu4 = tk.Menu(grathmenu, tearoff=0)

    animationmenu1 = tk.Menu(grathmenu, tearoff=0)
    animationmenu2 = tk.Menu(grathmenu, tearoff=0)
    animationmenu3 = tk.Menu(grathmenu, tearoff=0)
    animationmenu4 = tk.Menu(grathmenu, tearoff=0)

    mainmenu.add_cascade(label="Инструменты", menu=filemenu)
    mainmenu.add_cascade(label="Графики", menu=grathmenu)
    grathmenu.add_cascade(label="Общая", menu=grathmenu1)
    grathmenu.add_cascade(label="Лагранж", menu=grathmenu2)
    grathmenu.add_cascade(label="Эйлер", menu=grathmenu3)
    grathmenu.add_cascade(label="N тел", menu=grathmenu4)

    mainmenu.add_cascade(label="Анимация", menu=animationmenu)
    animationmenu.add_cascade(label="Общая", menu=animationmenu1)
    animationmenu.add_cascade(label="Лагранж", menu=animationmenu2)
    animationmenu.add_cascade(label="Эйлер", menu=animationmenu3)
    animationmenu.add_cascade(label="N тел", menu=animationmenu4)

    grathmenu2.add_command(label="#1", command=_startGrathOne)
    grathmenu2.add_command(label="#2", command=_startGrathOne1)
    grathmenu2.add_command(label="#3", command=_startGrathOne2)
    grathmenu1.add_command(label="#1", command=_startGrathOne6)
    grathmenu3.add_command(label="#1", command=_startGrathOne3)
    grathmenu3.add_command(label="#2", command=_startGrathOne4)
    grathmenu3.add_command(label="#3", command=_startGrathOne5)
    grathmenu4.add_command(label="#1", command=_startGrathOne7)

    animationmenu2.add_command(label="#1", command=_startAnimate)
    animationmenu2.add_command(label="#2", command=_startAnimate1)
    animationmenu2.add_command(label="#3", command=_startAnimate2)
    animationmenu1.add_command(label="#1")
    animationmenu3.add_command(label="#1", command=_startAnimate3)
    animationmenu3.add_command(label="#2", command=_startAnimate4)
    animationmenu3.add_command(label="#3", command=_startAnimate5)
    animationmenu4.add_command(label="#1", command=_startAnimate6)
    root.geometry("1000x700")
    root.mainloop()
