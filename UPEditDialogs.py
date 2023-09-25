from tkinter import *
import tkinter as tk
from UPFunctions import *


class EditDialog():
    def __init__(self, parentWin, parameter_name, parameter=''):
        self.parent = parentWin
        self.parameter_name = parameter_name
        self.parameter = parameter
        self.processed = False

    def show(self, settings=False):
        self.root = Toplevel(self.parent.root)
        x = self.parent.root.winfo_x() + 260
        y = self.parent.root.winfo_y() + 260
        self.root.geometry(f"245x180+{x}+{y}")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.title(self.parameter_name)
        self.root.resizable(False, False)

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=160, width=225)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.ButtonOk = tk.Button(self.Frame)
        self.ButtonOk.place(x=10, y=110, height=35, width=100)
        self.ButtonOk.configure(activebackground="#d9d9d9")
        self.ButtonOk.configure(activeforeground="black")
        self.ButtonOk.configure(background="#d9d9d9")
        self.ButtonOk.configure(compound='left')
        self.ButtonOk.configure(disabledforeground="#a3a3a3")
        self.ButtonOk.configure(foreground="#000000")
        self.ButtonOk.configure(highlightbackground="#d9d9d9")
        self.ButtonOk.configure(highlightcolor="black")
        self.ButtonOk.configure(pady="0")
        self.ButtonOk.configure(text='''Save''')
        self.ButtonOk.bind("<Button-1>", self.save_parameter)

        self.ButtonCancel = tk.Button(self.Frame)
        self.ButtonCancel.place(x=110, y=110, height=35, width=100)
        self.ButtonCancel.configure(activebackground="#d9d9d9")
        self.ButtonCancel.configure(activeforeground="black")
        self.ButtonCancel.configure(background="#d9d9d9")
        self.ButtonCancel.configure(compound='left')
        self.ButtonCancel.configure(disabledforeground="#a3a3a3")
        self.ButtonCancel.configure(foreground="#000000")
        self.ButtonCancel.configure(highlightbackground="#d9d9d9")
        self.ButtonCancel.configure(highlightcolor="black")
        self.ButtonCancel.configure(pady="0")
        self.ButtonCancel.configure(text='''Cancel''')
        self.ButtonCancel.configure(command=self.root.destroy)

        self.Text = tk.Text(self.Frame)
        self.Text.place(x=10, y=10, height=90, width=200)
        self.Text.configure(font=("Arial", 15))
        self.Text.configure(background="#FFFFFF")
        self.Text.configure(foreground="#000000")
        self.Text.configure(highlightbackground="#d9d9d9")
        self.Text.configure(highlightcolor="black")
        self.Text.configure(pady="0")
        self.Text.delete("1.0", END)
        self.Text.insert("1.0", self.parameter)

        self.root.grab_set()
        self.Text.focus_set()
        self.root.wait_window()

    def save_parameter(self, *args):
        self.processed = True
        self.new_parameter = self.Text.get(1.0, END).replace("\n", "")
        self.root.grab_release()
        self.root.destroy()


class DeleteDialog():
    def __init__(self, parentWin, parameter_name, parameter=''):
        self.parent = parentWin
        self.parameter_name = parameter_name
        self.parameter = parameter
        self.processed = False

    def show(self, settings=False):
        self.root = Toplevel(self.parent.root)
        x = self.parent.root.winfo_x() + 260
        y = self.parent.root.winfo_y() + 260
        self.root.geometry(f"245x180+{x}+{y}")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.title(self.parameter_name)
        self.root.resizable(False, False)

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=160, width=225)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.ButtonOk = tk.Button(self.Frame)
        self.ButtonOk.place(x=10, y=110, height=35, width=100)
        self.ButtonOk.configure(activebackground="#d9d9d9")
        self.ButtonOk.configure(activeforeground="black")
        self.ButtonOk.configure(background="#d9d9d9")
        self.ButtonOk.configure(compound='left')
        self.ButtonOk.configure(disabledforeground="#a3a3a3")
        self.ButtonOk.configure(foreground="#000000")
        self.ButtonOk.configure(highlightbackground="#d9d9d9")
        self.ButtonOk.configure(highlightcolor="black")
        self.ButtonOk.configure(pady="0")
        self.ButtonOk.configure(text='''Delete''')
        self.ButtonOk.bind("<Button-1>", self.save_parameter)

        self.ButtonCancel = tk.Button(self.Frame)
        self.ButtonCancel.place(x=110, y=110, height=35, width=100)
        self.ButtonCancel.configure(activebackground="#d9d9d9")
        self.ButtonCancel.configure(activeforeground="black")
        self.ButtonCancel.configure(background="#d9d9d9")
        self.ButtonCancel.configure(compound='left')
        self.ButtonCancel.configure(disabledforeground="#a3a3a3")
        self.ButtonCancel.configure(foreground="#000000")
        self.ButtonCancel.configure(highlightbackground="#d9d9d9")
        self.ButtonCancel.configure(highlightcolor="black")
        self.ButtonCancel.configure(pady="0")
        self.ButtonCancel.configure(text='''Cancel''')
        self.ButtonCancel.configure(command=self.root.destroy)

        self.Text = tk.Label(self.Frame)
        self.Text.place(x=10, y=10, height=90, width=200)
        self.Text.configure(font=("Arial", 15))
        self.Text.configure(background="#FFFFFF")
        self.Text.configure(foreground="#000000")
        self.Text.configure(highlightbackground="#d9d9d9")
        self.Text.configure(highlightcolor="black")
        self.Text.configure(text=self.parameter)

        self.root.grab_set()
        self.Text.focus_set()
        self.root.wait_window()

    def save_parameter(self, *args):
        self.processed = True
        self.root.grab_release()
        self.root.destroy()


class WarningWindow():

    def __init__(self, parentWin, text):
        self.parent = parentWin

        self.root = Toplevel(self.parent.root)
        x = self.parent.root.winfo_x() + 260
        y = self.parent.root.winfo_y() + 200
        self.root.geometry(f"500x130+{x}+{y}")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.resizable(False, False)

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=110, width=480)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.Text = tk.Label(self.Frame)
        self.Text.place(x=10, y=10, height=90, width=460)
        self.Text.configure(font=("Arial", 15))
        self.Text.configure(background="#FFFFFF")
        self.Text.configure(foreground="#000000")
        self.Text.configure(highlightbackground="#d9d9d9")
        self.Text.configure(highlightcolor="black")
        self.Text.configure(text=text)
        self.Text.configure(wraplength=450)

        self.root.grab_set()
        self.Text.focus_set()
        self.root.wait_window()
