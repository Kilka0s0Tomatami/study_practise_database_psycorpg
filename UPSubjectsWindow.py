from tkinter import *
import tkinter as tk
from UPFunctions import *
from UPEditDialogs import *


class SubjectsWindow():
    def __init__(self, parentWin):  # Родительское окно
        self.parent = parentWin
        self.processed = False

    def show(self, settings=False):
        self.root = Toplevel(self.parent.root)  # Задается родительское окно
        x = self.parent.root.winfo_x() - 410
        y = self.parent.root.winfo_y() + 330
        self.root.geometry(f"1000x530+{x}+{y}")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.title("Предметы")
        self.root.resizable(False, False)  # Разрешение на мастштабирование

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=500, width=980)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.SubjectsList = tk.Listbox(self.Frame)
        self.SubjectsList.place(x=10, y=10, height=450, width=600)
        print(subjects_get_list())
        self.LoadList()

        self.ButtonSubjectAdd = tk.Button(self.Frame)
        self.ButtonSubjectAdd.place(x=800, y=10, height=35, width=100)
        self.ButtonSubjectAdd.configure(activebackground="#d9d9d9")
        self.ButtonSubjectAdd.configure(activeforeground="black")
        self.ButtonSubjectAdd.configure(background="#d9d9d9")
        self.ButtonSubjectAdd.configure(compound='left')
        self.ButtonSubjectAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonSubjectAdd.configure(foreground="#000000")
        self.ButtonSubjectAdd.configure(highlightbackground="#d9d9d9")
        self.ButtonSubjectAdd.configure(highlightcolor="black")
        self.ButtonSubjectAdd.configure(pady="0")
        self.ButtonSubjectAdd.configure(text='''Добавить предмет''')
        # self.ButtonStudents.bind("<Button-1>", self.save_word)
        self.ButtonSubjectAdd.configure(command=self.SubjectCreate)

        self.ButtonSubjectDelete = tk.Button(self.Frame)
        self.ButtonSubjectDelete.place(x=800, y=50, height=35, width=100)
        self.ButtonSubjectDelete.configure(activebackground="#d9d9d9")
        self.ButtonSubjectDelete.configure(activeforeground="black")
        self.ButtonSubjectDelete.configure(background="#d9d9d9")
        self.ButtonSubjectDelete.configure(compound='left')
        self.ButtonSubjectDelete.configure(disabledforeground="#a3a3a3")
        self.ButtonSubjectDelete.configure(foreground="#000000")
        self.ButtonSubjectDelete.configure(highlightbackground="#d9d9d9")
        self.ButtonSubjectDelete.configure(highlightcolor="black")
        self.ButtonSubjectDelete.configure(pady="0")
        self.ButtonSubjectDelete.configure(text='''Удалить предмет''')
        self.ButtonSubjectDelete.configure(command=self.SubjectDelete)

        self.ButtonSubjectEdit = tk.Button(self.Frame)
        self.ButtonSubjectEdit.place(x=800, y=90, height=35, width=100)
        self.ButtonSubjectEdit.configure(activebackground="#d9d9d9")
        self.ButtonSubjectEdit.configure(activeforeground="black")
        self.ButtonSubjectEdit.configure(background="#d9d9d9")
        self.ButtonSubjectEdit.configure(compound='left')
        self.ButtonSubjectEdit.configure(disabledforeground="#a3a3a3")
        self.ButtonSubjectEdit.configure(foreground="#000000")
        self.ButtonSubjectEdit.configure(highlightbackground="#d9d9d9")
        self.ButtonSubjectEdit.configure(highlightcolor="black")
        self.ButtonSubjectEdit.configure(pady="0")
        self.ButtonSubjectEdit.configure(text='''Изменить предмет''')
        self.ButtonSubjectEdit.configure(command=self.SubjectEdit)

        self.root.grab_set()
        self.ButtonSubjectAdd.focus_set()
        self.root.wait_window()

    def LoadList(self):
        self.SubjectsList.delete(0, END)
        self.SubjectsList.insert(0, *subjects_get_list())

    def SubjectEdit(self):
        if len(self.SubjectsList.curselection()) == 0:
            return

        subject_name = self.SubjectsList.get(self.SubjectsList.curselection()[0])

        edit_dialog = EditDialog(self, "Редактирование предмета", subject_name)
        edit_dialog.show()

        if edit_dialog.processed:
            text = subject_rename(subject_name=subject_name, new_subject_name=edit_dialog.new_parameter)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList()

    def SubjectCreate(self):
        edit_dialog = EditDialog(self, "Создаение предмета", "")
        edit_dialog.show()

        if edit_dialog.processed:
            text = subject_create(subject_name=edit_dialog.new_parameter)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList()

    def SubjectDelete(self):
        if len(self.SubjectsList.curselection()) == 0:
            return

        subject_name = self.SubjectsList.get(self.SubjectsList.curselection()[0])

        delete_dialog = DeleteDialog(self, "Удаление предмета", subject_name)
        delete_dialog.show()

        if delete_dialog.processed:
            text = subject_delete(subject_name=subject_name)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList()
