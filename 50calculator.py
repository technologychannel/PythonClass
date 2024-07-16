import tkinter as tk
from tkinter import messagebox

def get_sum():
    # Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 + value2
    messagebox.showinfo("Result", f"The sum is {result}")

root = tk.Tk()
root.title("TC Calculator")
root.geometry("300x200")

# For First Number
label1 = tk.Label(root, text="Enter first number: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)


# For Second Number
label2 = tk.Label(root, text="Enter second number: ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

### Button
button = tk.Button(root, text="Find Sum", command=get_sum)
button.pack(pady=5)


# Run
root.mainloop()

### Create a Software that find sum, diff, mul, div of two 
### Numbers using tkinter