from tkinter import *
import tkinter as tk
from tkinter import ttk
from UPFunctions import *
from UPEditDialogs import *


class StudentWindow():
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
        self.root.title("Студенты")
        self.root.resizable(False, False)  # Разрешение на мастштабирование

        self.Frame = tk.Frame(self.root)
        self.Frame.place(x=10, y=10, height=500, width=980)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        group_list = groups_get_list()

        self.value_inside = tk.StringVar(self.root)

        self.value_inside.set(group_list[0])

        self.GroupList = tk.OptionMenu(self.Frame, self.value_inside, *group_list, command=self.LoadList)
        self.GroupList.place(x=700, y=10)
        # self.GroupList.bind("<<OptionMenuChanged>>", self.LoadList)
        '''
        def create_virtual_event(varname, idx, mode):
            self.GroupList  .event_generate("<<OptionMenuChanged>>")

        self.value_inside.trace_add(("write", "unset"), create_virtual_event)
        '''
        # self.GroupList.pack()

        self.StudentList = ttk.Treeview(self.Frame)
        self.StudentList.place(x=10, y=10, height=450, width=600)
        self.StudentList['columns'] = ('ID', 'Name', 'Group')

        self.StudentList.column("#0", width=0, stretch=NO)
        self.StudentList.column('ID', stretch=NO, anchor=CENTER)
        self.StudentList.column('Name', stretch=NO, anchor=CENTER)

        self.StudentList.heading('ID', text='ID')
        self.StudentList.heading('Name', text='Имя')
        self.LoadList("")
        # self.StudentList.pack()

        self.ButtonStudentAdd = tk.Button(self.Frame)
        self.ButtonStudentAdd.place(x=800, y=10, height=35, width=150)
        self.ButtonStudentAdd.configure(activebackground="#d9d9d9")
        self.ButtonStudentAdd.configure(activeforeground="black")
        self.ButtonStudentAdd.configure(background="#d9d9d9")
        self.ButtonStudentAdd.configure(compound='left')
        self.ButtonStudentAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonStudentAdd.configure(foreground="#000000")
        self.ButtonStudentAdd.configure(highlightbackground="#d9d9d9")
        self.ButtonStudentAdd.configure(highlightcolor="black")
        self.ButtonStudentAdd.configure(pady="0")
        self.ButtonStudentAdd.configure(text='''Добавить студента''')
        # self.ButtonStudentAdd.bind("<Button-1>", self.save_word)
        self.ButtonStudentAdd.configure(command=self.StudentCreate)

        self.ButtonStudentDelete = tk.Button(self.Frame)
        self.ButtonStudentDelete.place(x=800, y=50, height=35, width=150)
        self.ButtonStudentDelete.configure(activebackground="#d9d9d9")
        self.ButtonStudentDelete.configure(activeforeground="black")
        self.ButtonStudentDelete.configure(background="#d9d9d9")
        self.ButtonStudentDelete.configure(compound='left')
        self.ButtonStudentDelete.configure(disabledforeground="#a3a3a3")
        self.ButtonStudentDelete.configure(foreground="#000000")
        self.ButtonStudentDelete.configure(highlightbackground="#d9d9d9")
        self.ButtonStudentDelete.configure(highlightcolor="black")
        self.ButtonStudentDelete.configure(pady="0")
        self.ButtonStudentDelete.configure(text='''Удалить студента''')
        self.ButtonStudentDelete.configure(command=self.StudentDelete)

        self.ButtonStudentRename = tk.Button(self.Frame)
        self.ButtonStudentRename.place(x=800, y=90, height=35, width=150)
        self.ButtonStudentRename.configure(activebackground="#d9d9d9")
        self.ButtonStudentRename.configure(activeforeground="black")
        self.ButtonStudentRename.configure(background="#d9d9d9")
        self.ButtonStudentRename.configure(compound='left')
        self.ButtonStudentRename.configure(disabledforeground="#a3a3a3")
        self.ButtonStudentRename.configure(foreground="#000000")
        self.ButtonStudentRename.configure(highlightbackground="#d9d9d9")
        self.ButtonStudentRename.configure(highlightcolor="black")
        self.ButtonStudentRename.configure(pady="0")
        self.ButtonStudentRename.configure(text='''Переименовать студента''')
        self.ButtonStudentRename.configure(command=self.StudentRename)

        self.ButtonStudentGroupChange = tk.Button(self.Frame)
        self.ButtonStudentGroupChange.place(x=800, y=130, height=35, width=150)
        self.ButtonStudentGroupChange.configure(activebackground="#d9d9d9")
        self.ButtonStudentGroupChange.configure(activeforeground="black")
        self.ButtonStudentGroupChange.configure(background="#d9d9d9")
        self.ButtonStudentGroupChange.configure(compound='left')
        self.ButtonStudentGroupChange.configure(disabledforeground="#a3a3a3")
        self.ButtonStudentGroupChange.configure(foreground="#000000")
        self.ButtonStudentGroupChange.configure(highlightbackground="#d9d9d9")
        self.ButtonStudentGroupChange.configure(highlightcolor="black")
        self.ButtonStudentGroupChange.configure(pady="0")
        self.ButtonStudentGroupChange.configure(text='''Изменить группу''')
        self.ButtonStudentGroupChange.configure(command=self.StudentGroupChange)

        self.root.grab_set()
        self.ButtonStudentAdd.focus_set()
        self.root.wait_window()

    def LoadList(self, event):
        print(self.value_inside.get())
        for i in self.StudentList.get_children():
            self.StudentList.delete(i)
        for student in group_get_students_list(self.value_inside.get()):
            self.StudentList.insert(parent='', index='end', iid=student[0], text='',
                                    values=(str(student[0]), str(student[1])))
        # self.StudentList.insert(0, *group_get_students_list(self.value_inside.get()))

    def StudentRename(self):
        print(self.StudentList.focus())

        if self.StudentList.focus() is None:
            return

        student_id = self.StudentList.focus()

        edit_dialog = EditDialog(self, "Переименование студента", "")
        edit_dialog.show()

        if edit_dialog.processed:
            text = student_rename(student_id=student_id, new_student_name=edit_dialog.new_parameter)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList("")

    def StudentGroupChange(self):
        print(self.StudentList.focus())

        if self.StudentList.focus() is None:
            return

        student_id = self.StudentList.focus()

        edit_dialog = EditDialog(self, "Новая группа", "")
        edit_dialog.show()

        if edit_dialog.processed:
            text = student_group_change(student_id=student_id, new_group_name=edit_dialog.new_parameter)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList("")

    def StudentCreate(self):
        edit_dialog = EditDialog(self, "Добавление студента", "")
        edit_dialog.show()

        if edit_dialog.processed:
            text = student_create(student_name=edit_dialog.new_parameter, group_name=self.value_inside.get())
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList("")

    def StudentDelete(self):
        print(self.StudentList.focus())

        if self.StudentList.focus() is None:
            return

        student_id = self.StudentList.focus()

        delete_dialog = DeleteDialog(self, "Удаление стулента", student_get_info(student_id))
        delete_dialog.show()

        if delete_dialog.processed:
            text = student_delete(student_id=student_id)
            print("Вывод: ", text)
            if text:
                WarningWindow(self, text)
            self.LoadList("")
