import tkinter as tk
import tkinter.filedialog as fd
import os, fnmatch
import tkinter.messagebox as box


class testmain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        var = tk.IntVar()
        var.set(0)

        def change():
            label = tk.Label(self, width=20, height=10)
            label.place(relwidth=0.05, relx=0.7, rely=0.2)
            if var.get() == 0:
                label['bg'] = 'red'
            elif var.get() == 1:
                label['bg'] = 'green'

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
            for file in myList:
                if fnmatch.fnmatch(file, pattern):
                    self.listbox.insert(tk.END, file)

        def dialog():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            os.startfile(text1 + self.listbox.get(self.listbox.curselection()))
            print(self.listbox.get(self.listbox.curselection()))

        def refresh():
            curr_dir_read1 = open('CurDir.txt', 'r')
            text1 = curr_dir_read1.read()
            label['text'] = str(text1)
            self.listbox.delete(0, tk.END)
            myList = os.listdir(str(text1))
            pattern = "*.txt"
            for file in myList:
                if fnmatch.fnmatch(file, pattern):
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
        self.lagrange.place(relwidth=0.05, relx=0.87, rely=0.1)
        self.eyler.place(relwidth=0.05, relx=0.67, rely=0.15)
        self.button.place(relx=0.85, rely=0.43)
