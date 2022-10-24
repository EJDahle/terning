import tkinter as tk
import random as rn

def trill_terning():
    n = rn.randint(1, 6)
    number.config(state = "normal")
    number.delete(0, "end")
    number.insert(0, n)
    number.config(state = "disabled")


bg_color = "#f5e6ef"
fg_color = "#ffffff"
font1 = ("Arial", 20)
font2 = ("Arial", 100)

root = tk.Tk()
root.config(bg=bg_color)
number = tk.Entry(root, state = "disabled", disabledbackground=bg_color,font = font2, width = 1, fg = fg_color, highlightthickness=0, borderwidth=0)
number.pack()

button = tk.Button(root, command=trill_terning, text = "Trill!!!!! tørning", bg =bg_color, font = font1, fg = fg_color, highlightthickness=0, borderwidth=0)
button.pack()


root.mainloop()