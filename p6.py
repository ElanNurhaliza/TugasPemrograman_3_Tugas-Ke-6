from tkinter import *
from tkinter import messagebox

def show_selection():
    selected = listbox.get(ACTIVE)
    if selected:
        messagebox.showinfo("Pilihan Anda", f"Bahasa pemrograman yang Anda pilih: {selected}")
    else:
        messagebox.showwarning("Pilih Bahasa", "Silakan pilih bahasa pemrograman terlebih dahulu!")

top = Tk()
top.title("Bahasa Pemrograman Favorit")
top.geometry("350x400")
top.configure(bg="#f0f8ff")

title_label = Label(top, text="Pilih Bahasa Pemrograman", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#00008b")
title_label.pack(pady=15)

frame = Frame(top, bg="#add8e6", bd=2, relief=RIDGE)
frame.pack(pady=10)

listbox = Listbox(frame, width=25, height=8, font=("Arial", 12), bg="#e6f7ff", selectbackground="#b3e0ff")
listbox.insert(1, "Python")
listbox.insert(2, "JavaScript")
listbox.insert(3, "Java")
listbox.insert(4, "C++")
listbox.insert(5, "C#")
listbox.insert(6, "Ruby")
listbox.insert(7, "Go")
listbox.insert(8, "Swift")
listbox.insert(9, "PHP")
listbox.pack(pady=5, padx=5)

select_button = Button(top, text="Pilih Bahasa", command=show_selection, font=("Arial", 12), bg="#4682b4", fg="white")
select_button.pack(pady=20)

top.mainloop()
