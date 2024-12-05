from tkinter import *

def sel():
   selection = "Pilihan Kamu " + str(var.get())
   label.config(text = selection)
root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Money", variable=var, value=1,
                  command=sel)
R1.pack(anchor = W )

R2 = Radiobutton(root, text="Uang", variable=var, value=2,
                  command=sel)
R2.pack(anchor = W)

R3 = Radiobutton(root, text="Duit", variable=var, value=3,
                  command=sel)
R3.pack(anchor = W)
label = Label(root)
label.pack()
root.mainloop()