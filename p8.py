from tkinter import *  
from tkinter import messagebox  

top = Tk()


mb = Menubutton(top, text="Pilihan", relief=RAISED)
mb.grid()

mb.menu = Menu(mb, tearoff=0) 
mb["menu"] = mb.menu

PyhtonVar = IntVar()
CVar = IntVar()

mb.menu.add_checkbutton(label="Benar", variable=PyhtonVar)
mb.menu.add_checkbutton(label="Salah", variable=CVar)

mb.pack()

top.mainloop()