from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongination System")

        title_lbl = Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"college_images\360_F_111727438_NlxFzKgcakuH31GvVutWN0kVpulxMqka.jpg")
        img_top = img_top.resize((1530,720)  )
        self.photoimg_top = ImageTk.PhotoImage(img_top)
    
        f_lbl2 = Label(self.root,image=self.photoimg_top)
        f_lbl2.place(x=0,y=55,width=1530,height =720)

        #Help label
        dep_label = Label(f_lbl2,text="Email:aditya@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=600,y=400)


if __name__ == "__main__":
    root=Tk()
    obj = Help(root)
    root.mainloop()