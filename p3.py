import tkinter as tk

def draw_star(canvas, x, y, size, color="gold"):
    """Fungsi untuk menggambar bintang pada canvas."""
    points = [
        x, y - size,  
        x + size * 0.4, y - size * 0.4,  
        x + size, y, 
        x + size * 0.4, y + size * 0.4, 
        x, y + size, 
        x - size * 0.4, y + size * 0.4, 
        x - size, y, 
        x - size * 0.4, y - size * 0.4, 
    ]
    canvas.create_polygon(points, fill=color, outline="black", width=1)

top = tk.Tk()
top.title("Gambar Bintang")
top.geometry("500x500")

C = tk.Canvas(top, bg="skyblue", height=500, width=500)
C.pack()

draw_star(C, 250, 250, 100)  
draw_star(C, 100, 100, 50, "yellow") 
draw_star(C, 400, 100, 50, "white")  
draw_star(C, 150, 400, 30, "orange") 
draw_star(C, 350, 400, 30, "pink")  
top.mainloop()
