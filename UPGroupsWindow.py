from tkinter import *
import tkinter as tk
from UPFunctions import *
from UPEditDialogs import *


class GroupsWindow():
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
        self.root.title("Группы")
        self.root.resizable(False, False)  # Разрешение на мастштабирование

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=500, width=980)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.GroupsList = tk.Listbox(self.Frame)
        self.GroupsList.place(x=10, y=10, height=450, width=600)
        print(groups_get_list())
        self.LoadList()

        self.ButtonGroupAdd = tk.Button(self.Frame)
        self.ButtonGroupAdd.place(x=800, y=10, height=35, width=100)
        self.ButtonGroupAdd.configure(activebackground="#d9d9d9")
        self.ButtonGroupAdd.configure(activeforeground="black")
        self.ButtonGroupAdd.configure(background="#d9d9d9")
        self.ButtonGroupAdd.configure(compound='left')
        self.ButtonGroupAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonGroupAdd.configure(foreground="#000000")
        self.ButtonGroupAdd.configure(highlightbackground="#d9d9d9")
        self.ButtonGroupAdd.configure(highlightcolor="black")
        self.ButtonGroupAdd.configure(pady="0")
        self.ButtonGroupAdd.configure(text='''Добавить группу''')
        # self.ButtonGroupAdd.bind("<Button-1>", self.save_word)
        self.ButtonGroupAdd.configure(command=self.GroupCreate)

        self.ButtonGroupDelete = tk.Button(self.Frame)
        self.ButtonGroupDelete.place(x=800, y=50, height=35, width=100)
        self.ButtonGroupDelete.configure(activebackground="#d9d9d9")
        self.ButtonGroupDelete.configure(activeforeground="black")
        self.ButtonGroupDelete.configure(background="#d9d9d9")
        self.ButtonGroupDelete.configure(compound='left')
        self.ButtonGroupDelete.configure(disabledforeground="#a3a3a3")
        self.ButtonGroupDelete.configure(foreground="#000000")
        self.ButtonGroupDelete.configure(highlightbackground="#d9d9d9")
        self.ButtonGroupDelete.configure(highlightcolor="black")
        self.ButtonGroupDelete.configure(pady="0")
        self.ButtonGroupDelete.configure(text='''Удалить группу''')
        self.ButtonGroupDelete.configure(command=self.GroupDelete)

        self.ButtonGroupEdit = tk.Button(self.Frame)
        self.ButtonGroupEdit.place(x=800, y=90, height=35, width=100)
        self.ButtonGroupEdit.configure(activebackground="#d9d9d9")
        self.ButtonGroupEdit.configure(activeforeground="black")
        self.ButtonGroupEdit.configure(background="#d9d9d9")
        self.ButtonGroupEdit.configure(compound='left')
        self.ButtonGroupEdit.configure(disabledforeground="#a3a3a3")
        self.ButtonGroupEdit.configure(foreground="#000000")
        self.ButtonGroupEdit.configure(highlightbackground="#d9d9d9")
        self.ButtonGroupEdit.configure(highlightcolor="black")
        self.ButtonGroupEdit.configure(pady="0")
        self.ButtonGroupEdit.configure(text='''Изменить группу''')
        self.ButtonGroupEdit.configure(command=self.GroupEdit)

        self.root.grab_set()
        self.ButtonGroupAdd.focus_set()
        self.root.wait_window()

    def LoadList(self):
        self.GroupsList.delete(0, END)
        self.GroupsList.insert(0, *groups_get_list())

    def GroupEdit(self):
        if len(self.GroupsList.curselection()) == 0:
            return

        group_name = self.GroupsList.get(self.GroupsList.curselection()[0])

        edit_dialog = EditDialog(self, "Редактирование группы", group_name)
        edit_dialog.show()

        if edit_dialog.processed:
            text = group_rename(group_name=group_name, new_group_name=edit_dialog.new_parameter)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList()

    def GroupCreate(self):
        edit_dialog = EditDialog(self, "Создаение группы", "")
        edit_dialog.show()

        if edit_dialog.processed:
            group_create(group_name=edit_dialog.new_parameter)
            self.LoadList()

    def GroupDelete(self):
        if len(self.GroupsList.curselection()) == 0:
            return

        group_name = self.GroupsList.get(self.GroupsList.curselection()[0])

        delete_dialog = DeleteDialog(self, "Удаление группы", group_name)
        delete_dialog.show()

        if delete_dialog.processed:
            text = group_delete(group_name=group_name)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList()
