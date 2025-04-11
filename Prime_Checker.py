import tkinter as tk
from tkinter import messagebox

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_prime():
    try:
        number = int(entry.get())
        if is_prime(number):
            messagebox.showinfo("Result", f"{number} is a Prime Number")
        else:
            messagebox.showinfo("Result", f"{number} is Not a Prime Number")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer")

# Tkinter GUI
root = tk.Tk()
root.title("Prime Number Checker")



label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_prime)
check_button.pack()

root.mainloop()

