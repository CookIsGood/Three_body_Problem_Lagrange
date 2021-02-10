from tkinter import Tk, ttk
import tkinter as tk
from lagrangeMain import lagrange as TabA
from CommonMain import Example as TabB
from EylerMain import Example as TabC


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


def _startGrathOne():
    with open("Lagrange/GrathOne/Grath#1.py", "r") as f:
        exec(f.read())


def _startGrathOne1():
    with open("Lagrange/GrathOne/Grath#2.py", "r") as f:
        exec(f.read())


def _startGrathOne2():
    with open("Lagrange/GrathOne/Grath#3.py", "r") as f:
        exec(f.read())


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

        self.notebook.add(b_tab, text="Общее")
        self.notebook.add(a_tab, text="Лагранж")
        self.notebook.add(c_tab, text="Эйлер")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Плоские частные решения в задаче трех тел.')
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

    animationmenu1 = tk.Menu(grathmenu, tearoff=0)
    animationmenu2 = tk.Menu(grathmenu, tearoff=0)
    animationmenu3 = tk.Menu(grathmenu, tearoff=0)

    mainmenu.add_cascade(label="Инструменты", menu=filemenu)
    mainmenu.add_cascade(label="Графики", menu=grathmenu)
    grathmenu.add_cascade(label="Общая", menu=grathmenu1)
    grathmenu.add_cascade(label="Лагранж", menu=grathmenu2)
    grathmenu.add_cascade(label="Эйлер", menu=grathmenu3)

    mainmenu.add_cascade(label="Анимация", menu=animationmenu)
    animationmenu.add_cascade(label="Общая", menu=animationmenu1)
    animationmenu.add_cascade(label="Лагранж", menu=animationmenu2)
    animationmenu.add_cascade(label="Эйлер", menu=animationmenu3)

    grathmenu2.add_command(label="#1", command=_startGrathOne)
    grathmenu2.add_command(label="#2", command=_startGrathOne1)
    grathmenu2.add_command(label="#3", command=_startGrathOne2)
    grathmenu1.add_command(label="#1")
    grathmenu1.add_command(label="#2")
    grathmenu1.add_command(label="#3")
    grathmenu3.add_command(label="#1")
    grathmenu3.add_command(label="#2")
    grathmenu3.add_command(label="#3")

    animationmenu2.add_command(label="#1", command=_startAnimate)
    animationmenu2.add_command(label="#2", command=_startAnimate1)
    animationmenu2.add_command(label="#3", command=_startAnimate2)
    animationmenu1.add_command(label="#1")
    animationmenu1.add_command(label="#2")
    animationmenu1.add_command(label="#3")
    animationmenu3.add_command(label="#1")
    animationmenu3.add_command(label="#2")
    animationmenu3.add_command(label="#3")
    root.geometry("1000x700")
    root.mainloop()
