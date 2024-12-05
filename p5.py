from tkinter import *

root = Tk()
root.title("Program Elan Tombol Berwarna")
root.geometry("300x300")
root.configure(bg="lightgray")

top_frame = Frame(root, bg="red", pady=10)
top_frame.pack(fill=BOTH, expand=True)

bottom_frame = Frame(root, bg="white", pady=10)
bottom_frame.pack(fill=BOTH, expand=True)

red_button = Button(top_frame, text="Red", fg="white", bg="red", font=("Arial", 12, "bold"))
red_button.pack(side=LEFT, padx=10, pady=10)

green_button = Button(top_frame, text="Green", fg="white", bg="green", font=("Arial", 12, "bold"))
green_button.pack(side=LEFT, padx=10, pady=10)

blue_button = Button(top_frame, text="Blue", fg="white", bg="blue", font=("Arial", 12, "bold"))
blue_button.pack(side=LEFT, padx=10, pady=10)

yellow_button = Button(bottom_frame, text="Yellow", fg="black", bg="yellow", font=("Arial", 12, "bold"))
yellow_button.pack(side=LEFT, padx=10, pady=10)

black_button = Button(bottom_frame, text="Black", fg="white", bg="black", font=("Arial", 12, "bold"))
black_button.pack(side=LEFT, padx=10, pady=10)

purple_button = Button(bottom_frame, text="purple", fg="white", bg="purple", font=("Arial", 12, "bold"))
purple_button.pack(side=LEFT, padx=10, pady=10)


root.mainloop()
