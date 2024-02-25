from tkinter import *
from tkinter.ttk import Combobox
import os
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x800+60+80")  # Adjusted window size
root.resizable(False, False)

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"
white_color = "#ffffff"  # Plain white color

root.config(bg=background)

# Load the Header.png image
header_path = "Images/Header.png"
header_image = PhotoImage(file=header_path)

# Create a label for the header image
header_label = Label(root, image=header_image, bg=background)
header_label.place(x=0, y=0)  # Adjust x and y coordinates as needed

# New registration block
registration_frame = Frame(root, width=600, height=70, bg=framebg)  # Adjust width, height, and background color
registration_frame.place(relx=0.7, rely=0.2, anchor=CENTER)  # Shift more towards the right

# Labels for registration details
Label(registration_frame, text="Registration No.", font="Arial 13", bg=framebg, fg=white_color).place(x=30, y=0)
Label(registration_frame, text="Patient name", font="Arial 13", bg=framebg, fg=white_color).place(x=30, y=35)

Label(registration_frame, text="Date", font="Arial 13", bg=framebg, fg=white_color).place(x=320, y=0)
Label(registration_frame, text="Birth Year", font="Arial 13", bg=framebg, fg=white_color).place(x=320, y=35)

# Entry boxes for data entry
entry_reg_no = Entry(registration_frame, font="Arial 12", bg=white_color)
entry_reg_no.place(x=130, y=0)  # Adjusted x-coordinate

entry_patient_name = Entry(registration_frame, font="Arial 12", bg=white_color)
entry_patient_name.place(x=130, y=35)  # Adjusted x-coordinate

entry_date = Entry(registration_frame, font="Arial 12", bg=white_color)
entry_date.place(x=420, y=0)  # Adjusted x-coordinate

entry_birth_year = Entry(registration_frame, font="Arial 12", bg=white_color)
entry_birth_year.place(x=420, y=35)  # Adjusted x-coordinate

root.mainloop()
