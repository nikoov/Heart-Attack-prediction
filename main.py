from tkinter import *
from tkinter.ttk import Combobox
import os
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

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


###########################Body##################################################4
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=450)


################ radio button ######################## 5
Label(Detail_entry,text= "sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text= "fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text= "exang:",font="arial 13",bg=framebg,fg=framefg).place(x=328,y=10)

def selection():
    if gen.get() == 1:
        Gender = 1
        return Gender
    elif gen.get() == 2:
        Gender = 0
        return Gender

def selection2():
    if Fbs.get() == 1:
        Fbs = 1
        return Fbs
    elif Fbs.get() == 2:
        Fbs = 0
        return Fbs

def selection3():
    if exang.get() == 1:
        Exang = 1
        return Exang
    elif exang.get() == 2:
        Exang = 0
        return Exang

gen = IntVar()
R1 = Radiobutton(Detail_entry, text='Female', variable=gen, value=1)
R2 = Radiobutton(Detail_entry, text='Male', variable=gen, value=2)
R1.place(x=42,y=10)
R2.place(x=113,y=10)

Fbs = IntVar()
R3 = Radiobutton(Detail_entry, text='True', variable=Fbs, value=1)
R4 = Radiobutton(Detail_entry, text='False', variable=Fbs, value=2)
R3.place(x=205,y=10)
R4.place(x=263,y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text='Yes', variable=exang, value=1)
R6 = Radiobutton(Detail_entry, text='No', variable=exang, value=2)
R5.place(x=370,y=10)
R6.place(x=422,y=10)



####################Comboboxx ############### 6
Label(Detail_entry,text="cp:" ,font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text= "restcg:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:" ,font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
   input=cp_combobox.get()
   if input=="0 = typical angina":
    return(0)
   elif input=="1 =atypical angina":
       return(1)
   elif input=="2 = non-anginal pain":
       print(2)
   elif input=="3 =asymptomatic":
       return(3)
   else:
       print(Exang)

def selection5():
   input=slope_combobox.get()
   if input=="0 = upsloping":
    return(0)
   elif input=="1 =flat":
       return(1)
   elif input=="2 = downsloping":
       print(2)
   else:
       print(Exang)
       











cp_combobox=Combobox(Detail_entry,values=['0=typical angina','1=atypical angina','2=non-anginal pain','3=asymptomatic'],font="arial 12",state="r",width=11)
restcg_combobox=Combobox(Detail_entry,values=['0','1','2'],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry,values=['0=upsoloping','1=flat','2=downsloping'],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry,values=[ '0','1','2','3','4'],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry,values=['0','1','2','3'],font="arial 12",state="r",width=14)

cp_combobox.place(x=50 , y=50)
restcg_combobox.place(x=50 , y=90)
slope_combobox.place(x=50 , y=130)
ca_combobox.place(x=50 , y=170)
thal_combobox.place(x=50 , y=210)


################Data Entry box ########## 7
Label(Detail_entry,text="Smoking:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=90)
Label(Detail_entry,text="chol:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=130)
Label(Detail_entry,text="thalach:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=170)
Label(Detail_entry,text="oldpeak:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=210)

trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)

#######################################################################

############################## Report ########################## 8

square_report_image = PhotoImage(file="Images/Report.png")
# Resize the image to half its original size (adjust the value as needed)
resized_report_image = square_report_image.subsample(2, 2)
# Adjust x and y coordinates to position the image more upwards and slightly to the left
report_background = Label(image=resized_report_image, bg=background)
report_background.place(x=1100, y=300)

# Adjust x and y coordinates to position the report label more upwards and slightly to the left
report = Label(root, font="arial 25 bold", bg="white", fg="#8dc63f")
report.place(x=1100, y=300)

# Adjust x and y coordinates to position the report1 label more upwards and slightly to the left
report1 = Label(root, font="arial 10 bold", bg="white")
report1.place(x=1060, y=360)

######################################################


############# Graph ############################### 9

graph_image = PhotoImage(file="Images/graph.png")
# Resize the image
small_graph_image = graph_image.subsample(4, 4)  # Adjust the subsampling factor as needed
Label(image=small_graph_image).place(x=620, y=270)
Label(image=small_graph_image).place(x=880, y=270)
Label(image=small_graph_image).place(x=620, y=500)
Label(image=small_graph_image).place(x=880, y=500)



#########Button########################## 10

# Load the analysis button image
analysis_button_image = PhotoImage(file="Images/Analysis.png")
# Resize the image (adjust the subsampling factor as needed)
small_analysis_button_image = analysis_button_image.subsample(10, 10)
# Adjust x and y coordinates to position the button on top of the report image
Button(root, image=small_analysis_button_image, bd=0, bg=background, cursor='hand2').place(x=1160, y=550)

############ Save button ################## 11
analysis_button_image = PhotoImage(file="Images/Save.png")
# Resize the image (adjust the subsampling factor as needed)
small_analysis_button_image = analysis_button_image.subsample(5, 5)
# Adjust x and y coordinates to position the button on top of the report image
Button(root, image=small_analysis_button_image, bd=0, bg=background, cursor='hand2').place(x=1255, y=575)


################ Smoker sign ################### 12

button_mode=True
choice="smoking"
def changemode():
    global button_mode
    global choice

    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = False
    print(choice)

# Create the smoking and non-smoking icons
smoking_icon = PhotoImage(file="Images/Smoker.png").subsample(18, 18)  # Adjust subsampling factor as needed
non_smoking_icon = PhotoImage(file="Images/Non-smoker.png").subsample(18, 18)  # Adjust subsampling factor as needed

# Create the mode button with the smoking icon
mode = Button(root, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2", command=changemode)
mode.place(x=370, y=487)  # Adjust the position of the smoking signs as needed

# Create the logout button
logout_icon = PhotoImage(file="Images/Logout.png").subsample(10, 10)  # Adjust subsampling factor as needed
logout_button = Button(root, image=logout_icon, bg="#df2d4b", cursor="hand2", bd=0)
logout_button.place(x=1170, y=670)  # Adjust the position of the logout button as needed

####################################################

root.mainloop()





