from tkinter import *  

top = Tk()
top.title("Genre Film Kesukaan")

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()

C1 = Checkbutton(top, text="Horror", variable=CheckVar1, 
                 onvalue=1, offvalue=0, height=2, width=20)
C1.pack()


C2 = Checkbutton(top, text="Comedy", variable=CheckVar2, 
                 onvalue=1, offvalue=0, height=2, width=20)
C2.pack()

C3 = Checkbutton(top, text="Animasi", variable=CheckVar2, 
                 onvalue=1, offvalue=0, height=2, width=20)
C3.pack()


top.mainloop()