import tkinter as tk
from tkinter import messagebox

def submit_username():
    username = username_entry.get()
    if username:
        messagebox.showinfo("Welcome!", f"Halo, {username}! Selamat datang!")
    else:
        messagebox.showwarning("Error", "Mohon masukkan username Anda.")

top = tk.Tk()
top.title("Login Username")
top.geometry("400x200")
top.configure(bg="lightblue")

title_label = tk.Label(top, text="Masukkan Username Anda", font=("Helvetica", 16, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=10)

username_label = tk.Label(top, text="Username:", font=("Arial", 12), bg="lightblue")
username_label.pack(pady=5)
username_entry = tk.Entry(top, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

submit_button = tk.Button(top, text="Submit", font=("Arial", 12), bg="green", fg="white", command=submit_username)
submit_button.pack(pady=20)

top.mainloop()
