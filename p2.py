import tkinter as tk
from tkinter import messagebox
from tkinter import font


top = tk.Tk()
top.title("Program Elan GUI")
top.geometry("400x300") 
top.configure(bg="lightblue")  


custom_font = font.Font(family="Helvetica", size=14, weight="bold")


def helloCallBack():
    messagebox.showwarning("Pemberitahuan", "Halo ini aku Elan")


title_label = tk.Label(
    top, text="Selamat Datang di Program Elan!", bg="lightblue", fg="darkblue", font=("Helvetica", 16, "bold")
)
title_label.pack(pady=20)


B = tk.Button(
    top,
    text="Klik Dong",
    command=helloCallBack,
    bg="green",
    fg="white",
    font=custom_font,
    padx=20,
    pady=10,
    relief="raised",
    bd=3,
)
B.pack(pady=40)

top.mainloop()
