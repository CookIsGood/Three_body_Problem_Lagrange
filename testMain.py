import tkinter as tk
import tkinter.filedialog as fd
import os, fnmatch
import tkinter.messagebox as box
from datetime import datetime
import time


class testmain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.init_ui()



    def init_ui(self):
        var = tk.IntVar()
        var.set(0)

        def _saveLog():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            if os.path.exists(str(text1)+"Logs"):
                print("Папка Logs уже существует")
            else:
                os.mkdir(str(text1)+"Logs")
                print("Папка Logs создана")
            text = self.LogText.get("1.0", "end-1c")
            time = datetime.today().strftime("%d%m%Y_%H%M%S")
            text_file = open(str(text1)+"Logs" + str(time) + "Log.txt", "w")
            text_file.write(str(text))
            text_file.close()

        def change():

            M0, M1, M2, f1, e, F, vp, steps, t = self.InputText.get(), self.InputText2.get(), self.InputText3.get(), self.InputText4.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get(), self.InputText9.get(), self.InputText10.get()
            c_before, c_after, steps_c = self.InputText5.get(), self.InputText51.get(), self.InputText52.get()

            if os.path.exists("Test/Params"):
                print("Папка Test уже существует")
            else:
                os.mkdir("Test/Params")
                print("Папка Test создана")

            text_file, text_file1, text_file2, text_file3, text_file4 = open("Test/Params/M0-M1.txt", "w"), open(
                "Test/Params/M2-f.txt",
                "w"), open(
                "Test/Params/c-e.txt", "w"), open("Test/Params/F-vp.txt", "w"), open(
                "Test/Params/steps-t.txt", "w")
            text_file_cbefore_after, text_file_stepsc = open("Test/Params/cbefore-cafter.txt", "w"), open("Test/Params/stepsc-stepsc.txt", "w")
            text_file.write(str(M0) + ";" + str(M1) + "\n")
            text_file1.write(str(M2) + ";" + str(f1) + "\n")
            text_file2.write(str(e) + ";" + str(e) + "\n")
            text_file3.write(str(F) + ";" + str(vp) + "\n")
            text_file4.write(str(steps) + ";" + str(t) + "\n")
            text_file_cbefore_after.write(str(c_before) + ";" + str(c_after) + "\n")
            text_file_stepsc.write(str(steps_c) + ";" + str(steps_c) + "\n")

            text_file.close()
            text_file1.close()
            text_file2.close()
            text_file3.close()
            text_file4.close()
            text_file_cbefore_after.close()
            text_file_stepsc.close()

            if var.get() == 0:
                with open("Test/Lagrange/LagrangeTel3_2_1.py", "r") as f:
                    exec(f.read())
            elif var.get() == 1:
                with open("Test/Eyler/EylerTel3_2_1.py", "r") as f:
                    exec(f.read())

        def choose_directory():

            directory = fd.askdirectory(title="Открыть папку", initialdir="/")
            current_dir_file = open("CurDir.txt", "w")
            current_dir_file.write(str(directory) + "/")
            current_dir_file.close()
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            label['text'] = str(text1)
            self.listbox.delete(0, tk.END)
            myList = os.listdir(str(text1))
            pattern = "*.txt"
            pattern1 = "*.png"
            for file in myList:
                if fnmatch.fnmatch(file, pattern) or fnmatch.fnmatch(file, pattern1):
                    self.listbox.insert(tk.END, file)

        def dialog():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            os.startfile(text1 + self.listbox.get(self.listbox.curselection()))

        def refresh():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            label['text'] = str(text1)
            self.listbox.delete(0, tk.END)
            myList = os.listdir(str(text1))
            pattern = "*.txt"
            pattern1 = "*.png"
            for file in myList:
                if fnmatch.fnmatch(file, pattern) or fnmatch.fnmatch(file, pattern1):
                    self.listbox.insert(tk.END, file)

        curr_dir_read = open('CurDir.txt', 'r')
        text = curr_dir_read.read()
        label = tk.Label(self, text=str(text), bg='white', justify='left', anchor='w')
        label.place(relwidth=1, relheight=0.037, relx=0.095, rely=0)
        self.ChangeDir = tk.Button(master=self, text='Выбрать папку',
                                   command=choose_directory)
        self.ChangeDir.place(relx=0, rely=0)

        self.f = tk.Frame(self)
        self.f.place(relwidth=0.4, relheight=0.7, relx=0.03, rely=0.1)
        self.scrollbar = tk.Scrollbar(self.f)
        self.listbox = tk.Listbox(self.f, yscrollcommand=self.scrollbar.set)
        self.listbox.place(relwidth=0.899, relheight=0.9)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.place(relwidth=0.07, relheight=0.9, relx=0.90, rely=0.005)

        info_btn = tk.Button(self, text='Открыть файл!', command=dialog)
        info_btn.place(relx=0.04, rely=0.75)
        refresh_btn = tk.Button(self, text='Обновить!', command=refresh)
        refresh_btn.place(relx=0.3, rely=0.75)

        self.lagrange = tk.Radiobutton(self, text="Лагранж",
                                       variable=var, value=0)
        self.eyler = tk.Radiobutton(self, text="Эйлер",
                                    variable=var, value=1)
        self.button = tk.Button(self, text="Выбрать модуль!",
                                command=change)
        self.lagrange.place(relwidth=0.1, relx=0.87, rely=0.1)
        self.eyler.place(relwidth=0.1, relx=0.67, rely=0.1)
        self.button.place(relx=0.76, rely=0.15)

        # ------------------------------------------------
        self.LogLabel = tk.Label(self,
                                 text="Здесь будет отображаться информация\n о введенных вами данными и начальные условия точек!")
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

        self.InputText = tk.Entry(self)
        self.InputText.place(relwidth=0.05, relx=0.7, rely=0.3)
        self.MassLabel0 = tk.Label(self, text="M0=")
        self.MassLabel0.place(relwidth=0.03, relx=0.67, rely=0.3)

        self.InputText2 = tk.Entry(self)
        self.InputText2.place(relwidth=0.05, relx=0.8, rely=0.3)
        self.MassLabel1 = tk.Label(self, text="M1=")
        self.MassLabel1.place(relwidth=0.03, relx=0.77, rely=0.3)

        self.InputText3 = tk.Entry(self)
        self.InputText3.place(relwidth=0.05, relx=0.9, rely=0.3)
        self.MassLabel2 = tk.Label(self, text="M2=")
        self.MassLabel2.place(relwidth=0.03, relx=0.87, rely=0.3)

        self.InputText4 = tk.Entry(self)
        self.InputText4.place(relwidth=0.05, relx=0.7, rely=0.4)
        self.MassLabel3 = tk.Label(self, text="f=")
        self.MassLabel3.place(relwidth=0.03, relx=0.67, rely=0.4)

        self.InputText5 = tk.Entry(self)
        self.InputText5.place(relwidth=0.05, relx=0.45, rely=0.4)
        self.MassLabel41 = tk.Label(self, text="От")
        self.MassLabel41.place(relwidth=0.03, relx=0.42, rely=0.4)

        self.InputText51 = tk.Entry(self)
        self.InputText51.place(relwidth=0.05, relx=0.55, rely=0.4)
        self.MassLabel42 = tk.Label(self, text="До")
        self.MassLabel42.place(relwidth=0.03, relx=0.52, rely=0.4)

        self.InputText52 = tk.Entry(self)
        self.InputText52.place(relwidth=0.05, relx=0.5, rely=0.5)
        self.MassLabel43 = tk.Label(self, text="Шаг c")
        self.MassLabel43.place(relwidth=0.03, relx=0.505, rely=0.46)

        self.MassLabel4 = tk.Label(self, text="c")
        self.MassLabel4.place(relwidth=0.03, relx=0.51, rely=0.34)

        self.InputText6 = tk.Entry(self)
        self.InputText6.place(relwidth=0.05, relx=0.8, rely=0.4)
        self.MassLabel5 = tk.Label(self, text="e=")
        self.MassLabel5.place(relwidth=0.03, relx=0.77, rely=0.4)

        self.InputText7 = tk.Entry(self)
        self.InputText7.place(relwidth=0.05, relx=0.7, rely=0.49)
        self.MassLabel6 = tk.Label(self, text="F=")
        self.MassLabel6.place(relwidth=0.03, relx=0.67, rely=0.49)

        self.InputText8 = tk.Entry(self)
        self.InputText8.place(relwidth=0.05, relx=0.9, rely=0.4)
        self.MassLabel7 = tk.Label(self, text="vp=")
        self.MassLabel7.place(relwidth=0.03, relx=0.87, rely=0.4)

        self.InputText9 = tk.Entry(self)
        self.InputText9.place(relwidth=0.05, relx=0.80, rely=0.49)
        self.MassLabel8 = tk.Label(self, text="Интервал")
        self.MassLabel8.place(relwidth=0.12, relx=0.765, rely=0.46)

        self.InputText10 = tk.Entry(self)
        self.InputText10.place(relwidth=0.05, relx=0.80, rely=0.57)
        self.MassLabel9 = tk.Label(self, text="Шаг")
        self.MassLabel9.place(relwidth=0.12, relx=0.765, rely=0.54)

        self.WelcomeLabel = tk.Label(self, text="Введите параметры!")
        self.WelcomeLabel.place(relwidth=0.12, relx=0.76, rely=0.25)


