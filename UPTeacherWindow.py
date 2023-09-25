from tkinter import *
import tkinter as tk
from UPFunctions import *
from tkinter import ttk
from UPEditDialogs import *


class GradesStudentWindow():
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

        group_list = groups_get_list()
        self.value_inside_group = tk.StringVar(self.root)
        self.value_inside_group.set(group_list[0])
        self.GroupList = tk.OptionMenu(self.Frame, self.value_inside_group, *group_list, command=self.GroupChanged)
        self.GroupList.place(x=700, y=10)

        student_list = group_special_string_get(self.value_inside_group.get())
        self.value_inside_student = tk.StringVar(self.root)
        self.value_inside_student.set(student_list[0])
        self.StudentList = tk.OptionMenu(self.Frame, self.value_inside_student, *student_list,
                                         command=self.StudentChanged)
        self.StudentList.place(x=700, y=50)

        subject_list = subjects_get_list()
        print(subject_list)
        self.value_inside_subject = tk.StringVar(self.root)
        if subject_list:
            self.value_inside_subject.set(subject_list[0])
        else:
            self.value_inside_subject.set("")

        self.SubjectList = tk.OptionMenu(self.Frame, self.value_inside_subject, *subject_list,
                                         command=self.SubjectChanged)
        self.SubjectList.place(x=700, y=90)

        self.GradesList = ttk.Treeview(self.Frame)
        self.GradesList.place(x=10, y=10, height=450, width=600)
        self.GradesList['columns'] = ('Date', 'Value')

        self.GradesList.column("#0", width=0, stretch=NO)
        self.GradesList.column('Date', stretch=NO, anchor=CENTER)
        self.GradesList.column('Value', stretch=NO, anchor=CENTER)

        self.GradesList.heading('Date', text='Дата')
        self.GradesList.heading('Value', text='Оценка')
        self.LoadList("")
        # self.StudentList.pack()

        self.ButtonGradeAdd = tk.Button(self.Frame)
        self.ButtonGradeAdd.place(x=800, y=10, height=35, width=100)
        self.ButtonGradeAdd.configure(activebackground="#d9d9d9")
        self.ButtonGradeAdd.configure(activeforeground="black")
        self.ButtonGradeAdd.configure(background="#d9d9d9")
        self.ButtonGradeAdd.configure(compound='left')
        self.ButtonGradeAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonGradeAdd.configure(foreground="#000000")
        self.ButtonGradeAdd.configure(highlightbackground="#d9d9d9")
        self.ButtonGradeAdd.configure(highlightcolor="black")
        self.ButtonGradeAdd.configure(pady="0")
        self.ButtonGradeAdd.configure(text='''Добавить оценку''')
        # self.ButtonGradeAdd.bind("<Button-1>", self.save_word)
        self.ButtonGradeAdd.configure(command=self.GradesCreate)

        self.ButtonGradeDelete = tk.Button(self.Frame)
        self.ButtonGradeDelete.place(x=800, y=50, height=35, width=100)
        self.ButtonGradeDelete.configure(activebackground="#d9d9d9")
        self.ButtonGradeDelete.configure(activeforeground="black")
        self.ButtonGradeDelete.configure(background="#d9d9d9")
        self.ButtonGradeDelete.configure(compound='left')
        self.ButtonGradeDelete.configure(disabledforeground="#a3a3a3")
        self.ButtonGradeDelete.configure(foreground="#000000")
        self.ButtonGradeDelete.configure(highlightbackground="#d9d9d9")
        self.ButtonGradeDelete.configure(highlightcolor="black")
        self.ButtonGradeDelete.configure(pady="0")
        self.ButtonGradeDelete.configure(text='''Удалить оценку''')
        self.ButtonGradeDelete.configure(command=self.GradesDelete)

        self.root.grab_set()
        self.ButtonGradeAdd.focus_set()
        self.root.wait_window()

    def LoadList(self, event):
        # self.GradesList.delete(0, END)
        # self.GradesList.insert(0, *get_grades_student_subject('1', 'Math'))

        # print(self.value_inside.get())
        # Чистит дерево
        for i in self.GradesList.get_children():
            self.GradesList.delete(i)

        student_id = self.scissors(self.value_inside_student.get())
        print(student_id, " ", self.value_inside_student.get())
        if student_id:
            for grade in get_grades_student_subject(student_id,
                                                    self.value_inside_subject.get()):
                self.GradesList.insert(parent='', index='end', iid=None, text='',
                                       values=(str(grade[0]), str(grade[1])))

        # for student in group_get_students_list(self.value_inside.get()):
        #    self.GradesList.insert(parent='', index='end', iid=student[0], text='',
        #                           values=(str(student[0]), str(student[1])))
        # self.StudentList.insert(0, *group_get_students_list(self.value_inside.get()))

    def GradesCreate(self):
        edit_dialog1 = EditDialog(self, "Оценка", "")
        edit_dialog1.show()

        edit_dialog2 = EditDialog(self, "Дата", "")
        edit_dialog2.show()

        if edit_dialog1.processed:
            if edit_dialog2.processed:
                text = grade_add(self.scissors(self.value_inside_student.get()), self.value_inside_subject.get(),
                                 edit_dialog1.new_parameter, edit_dialog2.new_parameter)
                print("Вывод: ", text)
                if text:
                    WarningWindow(self, text)
                self.LoadList("")

    def GradesDelete(self):
        print(self.GradesList.focus())
        print(self.GradesList.item(self.GradesList.focus()))
        print(self.GradesList.item(self.GradesList.focus())['values'])

        if len(self.GradesList.item(self.GradesList.focus())['values']) == 0:
            return
        print(self.GradesList.item(self.GradesList.focus())['values'][0])
        print(self.GradesList.item(self.GradesList.focus())['values'][1])

        text = grade_delete(self.scissors(self.value_inside_student.get()), self.value_inside_subject.get(),
                            self.GradesList.item(self.GradesList.focus())['values'][0])
        print("Вывод: ", text)
        if text:
            WarningWindow(self, text)
        self.LoadList("")

        '''
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
        '''

    def GroupChanged(self, event):
        print("Группа изменилась")

        menu = self.StudentList["menu"]
        menu.delete(0, "end")

        st_list = group_special_string_get(self.value_inside_group.get())
        for string in st_list:
            menu.add_command(label=string,
                             command=lambda value=string: self.StudentChanged(value))


        if st_list:
            self.value_inside_student.set(st_list[0])
        else:
            self.value_inside_student.set("")
        self.LoadList("")

    def StudentChanged(self, name, *event):
        print("Студент изменился")
        self.value_inside_student.set(name)
        self.LoadList("")

    def SubjectChanged(self, event):
        print("Предмет изменился")
        self.LoadList("")

    def scissors(self, parameter):
        if parameter:
            return parameter.split("(", 1)[1].split(")", 1)[0]
        else:
            return ""
