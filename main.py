from zipfile import ZipFile
from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Checkbutton
from tkinter import filedialog
from tkinter import messagebox as mb
import os

# coding: utf8

win = Tk()
win.title('Ziper')
win.iconbitmap('icon.ico')



def openFile():
    dialogOpen = filedialog.Open(filetypes = [('Zip архивы', '*.zip'), ('Rar архивы', '*.rar'), ('Все файлы', '*')])
    dialogOpen.show()
    global zipName
    zipName = dialogOpen.filename
    filename.configure(text=zipName)

def saveFile():
    dialogOpen = filedialog.askdirectory()
    global folderName
    folderName = dialogOpen
    filename2.configure(text=folderName)

def cutToName(string):
    while True:
        if '/' in string:
            string = string.partition('/')[2]

        else:
            break

    string = string[:-4]
    return string

def start():
    if filename.cget('text') == '':
        mb.showwarning("Укажите архив для распаковки", "Укажите архив для распаковки")
        return 0

    if filename2.cget('text') == '':
        mb.showwarning("Укажите место для распаковки", "Укажите место для распаковки")
        return 0

    z = ZipFile(zipName)
    if var1.get():
        archiveName = cutToName(zipName)
        os.mkdir(folderName + '/' + archiveName)
        z.extractall(folderName + '/' + archiveName)
    else:
        z.extractall(folderName)

    mb.showinfo("Распаковка завершена", "Распаковка завершена")

filename = Label(win, text='', font=('Arial', 15))
filename.grid(column=0, row=0)

select = Button(win, text="Выбрать архив", width=50, command=openFile)
select.grid(column=1, row=0)

filename2 = Label(win, text='', font=('Arial', 15))
filename2.grid(column=0, row=1)

select2 = Button(win, text="Выбрать место распаковки", width=50, command=saveFile)
select2.grid(column=1, row=1)

var1 = BooleanVar()
var1.set(1)
check = Checkbutton(text="Создать подпапку", variable=var1)
check.grid(column=0, row=2)

startbt = Button(win, text="Начать распаковку", width="50", command=start)
startbt.grid(column=0, row=3)


win.mainloop()