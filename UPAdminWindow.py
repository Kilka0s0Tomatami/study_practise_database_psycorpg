from tkinter import *
import tkinter as tk

from UPStudentWindow import *
from UPGroupsWindow import *
from UPSubjectsWindow import *


class AdminWindow():
    def __init__(self, parentWin):  # Родительское окно
        self.parent = parentWin
        self.processed = False

    def show(self, settings=False):
        self.root = Toplevel(self.parent.root)  # Задается родительское окно
        x = self.parent.root.winfo_x() + 410
        y = self.parent.root.winfo_y() + 0
        self.root.geometry(f"245x180+{x}+{y}")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.title("Админинстратор")
        self.root.resizable(False, False)  # Разрешение на мастштабирование

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=160, width=225)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.ButtonStudents = tk.Button(self.Frame)
        self.ButtonStudents.place(x=10, y=10, height=35, width=100)
        self.ButtonStudents.configure(activebackground="#d9d9d9")
        self.ButtonStudents.configure(activeforeground="black")
        self.ButtonStudents.configure(background="#d9d9d9")
        self.ButtonStudents.configure(compound='left')
        self.ButtonStudents.configure(disabledforeground="#a3a3a3")
        self.ButtonStudents.configure(foreground="#000000")
        self.ButtonStudents.configure(highlightbackground="#d9d9d9")
        self.ButtonStudents.configure(highlightcolor="black")
        self.ButtonStudents.configure(pady="0")
        self.ButtonStudents.configure(text='''Студенты''')
        # self.ButtonStudents.bind("<Button-1>", self.save_word)
        self.ButtonStudents.configure(command=self.StudentWindow)

        self.ButtonGroups = tk.Button(self.Frame)
        self.ButtonGroups.place(x=10, y=50, height=35, width=100)
        self.ButtonGroups.configure(activebackground="#d9d9d9")
        self.ButtonGroups.configure(activeforeground="black")
        self.ButtonGroups.configure(background="#d9d9d9")
        self.ButtonGroups.configure(compound='left')
        self.ButtonGroups.configure(disabledforeground="#a3a3a3")
        self.ButtonGroups.configure(foreground="#000000")
        self.ButtonGroups.configure(highlightbackground="#d9d9d9")
        self.ButtonGroups.configure(highlightcolor="black")
        self.ButtonGroups.configure(pady="0")
        self.ButtonGroups.configure(text='''Группы''')
        self.ButtonGroups.configure(command=self.GroupsWindow)

        self.ButtonSubjects = tk.Button(self.Frame)
        self.ButtonSubjects.place(x=10, y=90, height=35, width=100)
        self.ButtonSubjects.configure(activebackground="#d9d9d9")
        self.ButtonSubjects.configure(activeforeground="black")
        self.ButtonSubjects.configure(background="#d9d9d9")
        self.ButtonSubjects.configure(compound='left')
        self.ButtonSubjects.configure(disabledforeground="#a3a3a3")
        self.ButtonSubjects.configure(foreground="#000000")
        self.ButtonSubjects.configure(highlightbackground="#d9d9d9")
        self.ButtonSubjects.configure(highlightcolor="black")
        self.ButtonSubjects.configure(pady="0")
        self.ButtonSubjects.configure(text='''Предметы''')
        self.ButtonSubjects.configure(command=self.SubjectsWindow)

        self.root.grab_set()
        self.ButtonStudents.focus_set()
        self.root.wait_window()

    def SubjectsWindow(self, *args):
        dialog = SubjectsWindow(self)
        dialog.show()

    def StudentWindow(self, *args):
        dialog = StudentWindow(self)
        dialog.show()

    def GroupsWindow(self, *args):
        dialog = GroupsWindow(self)
        dialog.show()
