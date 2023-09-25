import tkinter as tk
from tkinter import *

from UPAdminWindow import *
from UPTeacherWindow import *


class TopLevelWindow:
    def __init__(self, root):
        # Создаем основное окно
        root.geometry("400x270")  # Размеры окна
        root.resizable(False, False)  # Может ли изменять размер
        root.title("Приложение")  # Заголовок окна
        root.configure(background="#d9d9d9")  # Фоновый цвет окна
        root.configure(highlightbackground="#d9d9d9")  # Фоновый цвет текста
        root.configure(highlightcolor="black")  # Цвет текста

        self.root = root

        # Создаем рамку
        self.Frame1 = tk.Frame(self.root)  # Создаем окно, наследник приложения
        self.Frame1.place(x=10, y=10, height=250, width=385)  # Размеры окна
        self.Frame1.configure(relief='groove')  # Рельеф границ окна
        self.Frame1.configure(borderwidth="2")  # Ширина границ окна
        self.Frame1.configure(background="#d9d9d9")  # Фоновый цвет окна
        self.Frame1.configure(highlightbackground="#d9d9d9")  # Фоновый цвет текста
        self.Frame1.configure(highlightcolor="black")  # Цвет текста

        # Создаем кнопку (Администратора)
        self.ButtonAdmin = tk.Button(self.Frame1)  # Привязывается к рамке
        self.ButtonAdmin.place(x=10, y=10, height=100, width=365)  # Размеры
        self.ButtonAdmin.configure(activebackground="#d9d9d9")  # Фон активной кнопки
        self.ButtonAdmin.configure(activeforeground="black")  # Цвет фона активной кнопки
        self.ButtonAdmin.configure(background="#d9d9d9")  # Цвет фона пассивной кнопки
        self.ButtonAdmin.configure(compound='left')
        self.ButtonAdmin.configure(disabledforeground="#a3a3a3")  # Цвет нерабочей кнопки
        self.ButtonAdmin.configure(foreground="#000000")  # Цвет текста
        self.ButtonAdmin.configure(highlightbackground="#d9d9d9")  # Прицелился на кнопку
        self.ButtonAdmin.configure(highlightcolor="black")
        self.ButtonAdmin.configure(pady="0")  # Отступ по y
        self.ButtonAdmin.configure(text='''Администратор''')
        self.ButtonAdmin.configure(command=self.CreateAdminWindow)  # Сюда закидываем еще одно окно

        # Создаем кнопку (Учителя)
        self.ButtonTutor = tk.Button(self.Frame1)  # Привязывается к рамке
        self.ButtonTutor.place(x=10, y=110, height=100, width=365)  # Размеры
        self.ButtonTutor.configure(activebackground="#d9d9d9")  # Фон активной кнопки
        self.ButtonTutor.configure(activeforeground="black")  # Цвет фона активной кнопки
        self.ButtonTutor.configure(background="#d9d9d9")  # Цвет фона пассивной кнопки
        self.ButtonTutor.configure(compound='left')
        self.ButtonTutor.configure(disabledforeground="#a3a3a3")  # Цвет нерабочей кнопки
        self.ButtonTutor.configure(foreground="#000000")  # Цвет текста
        self.ButtonTutor.configure(highlightbackground="#d9d9d9")  # Прицелился на кнопку
        self.ButtonTutor.configure(highlightcolor="black")
        self.ButtonTutor.configure(pady="0")  # Отступ по y
        self.ButtonTutor.configure(text='''Учитель''')
        self.ButtonTutor.configure(command=self.CreateTeacherWindow)
        # self.ButtonAdmin.configure(command=fw_support.next_word)

    def CreateAdminWindow(self, *args):
        dialog = AdminWindow(self)

        dialog.show()

    def CreateTeacherWindow(self, *args):
        dialog = GradesStudentWindow(self)
        dialog.show()


root = Tk()

mainWindow = TopLevelWindow(root)

root.mainloop()
