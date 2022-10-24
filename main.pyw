import tkinter as tk

bg_color = "#f5e6ef"

root = tk.Tk()
root.config(bg=bg_color)
number = tk.Entry(root, state = "disabled", disabledbackground=bg_color)
number.pack()

button = tk.Button(root, text = "Trill!!!!! tørning", bg =bg_color)
button.pack()


root.mainloop()