
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""

root = tk.Tk()
root.configure(background="brown")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Alzheimer Disease detection ")


img=ImageTk.PhotoImage(Image.open("s1.jpg"))

img2=ImageTk.PhotoImage(Image.open("s2.jpg"))

img3=ImageTk.PhotoImage(Image.open("s3.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=100)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()



label_l1 = tk.Label(root, text="Alzheimer Disease detection",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)



def GUI_Master_old():
    from subprocess import call
    call(["python","GUI_Master_old.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Alzheimer Disease detection", command=GUI_Master_old, height=1,font=('times', 20, ' bold '), bg="#fff80a", fg="black")
button1.place(x=100, y=200)


button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=155, y=320)

root.mainloop()