# Create a program that calculate simple interest using GUI
# p * t * r/100
import tkinter as tk
from tkinter import messagebox
from main import create_connection

def save_data():
    # Get value from textbox
    name =entry1.get()
    phone =entry2.get()
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO contacts (name,phone) VALUES (%s,%s)", (name, phone))
    con.commit()
    con.close()
    messagebox.showinfo("Result", f" {name} added successfully.")

root = tk.Tk()
root.title("Contact Saver")
root.geometry("300x300")

# For First Number
label1 = tk.Label(root, text="Enter Name: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)


# For Second Number
label2 = tk.Label(root, text="Enter Phone: ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)


### Button
button = tk.Button(root, text="Save", command=save_data)
button.pack(pady=5)


# Run
root.mainloop()

### Create a Software that find sum, diff, mul, div of two 
### 