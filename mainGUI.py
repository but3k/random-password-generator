import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry.get())
        characters = string.ascii_letters

        if symbols_var.get():
            characters += string.punctuation
        if digits_var.get():
            characters += string.digits

        if not characters:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

root = tk.Tk()
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.title("Password Generator")

tk.Label(root, text="Enter password length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

symbols_var = tk.BooleanVar()
digits_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include symbols", variable=symbols_var).pack()
tk.Checkbutton(root, text="Include digits", variable=digits_var).pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()