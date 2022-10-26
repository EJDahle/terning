import tkinter as tk
import random as rn
from stil import *


def trill_terning():
    n = rn.randint(1, 6)
    number.config(state = "normal")
    number.delete(0, "end")
    number.insert(0, n)
    number.config(state = "disabled")




root = tk.Tk()
root.config(bg=bg_color)
number = tk.Entry(root, state = "disabled", disabledforeground=fg_color, disabledbackground=bg_color,font = stor_font, width = 1, fg = fg_color, highlightthickness=0, borderwidth=0)
number.pack()

button = tk.Button(root, command=trill_terning,  text = "Trill!!!!! tørning", bg =bg_color, font = liten_font, fg = fg_color, highlightthickness=0, borderwidth=0)
button.pack()


root.mainloop()