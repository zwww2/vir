from tkinter import *
from tkinter import ttk
import os
from time import sleep

window = Tk()
window.title("Таймер")
a = 301

label = ttk.Label(text="300 секунд")
label.pack()

def Tumer():
    global a
    a-=1
    label.config(text=a)
    window.after(1000, Tumer)
    
Tumer()

window.mainloop()