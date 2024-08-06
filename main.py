import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Function

def convert():
    mile_int = entry_float.get()
    kilometer_float = f"{mile_int * 1.60934:.2f}"
    output_string.set(f"{kilometer_float} km")


# create main window
window = ttk.Window(themename="litera")
window.title("Demo")
window.geometry("300x150")

# Title
title_label = ttk.Label(master=window, text="Miles to kilometres", font="Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_float = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_float)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# Output label
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 24", textvariable=output_string)
output_label.pack(pady=5)


# Run
window.mainloop()
