from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongination System")

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\Aditya\Desktop\projects\Face recogination system\\college_images\software-developer-6521720_1280.jpg")
        img_top = img_top.resize((1530,720)  )
        self.photoimg_top = ImageTk.PhotoImage(img_top)
    
        f_lbl2 = Label(self.root,image=self.photoimg_top)
        f_lbl2.place(x=0,y=55,width=1530,height =720)

        #frame
        main_frame = Frame(f_lbl2,bd=2,bg="White")
        main_frame.place(x=1000,y=0,width=500,height=600)

        #frame img
        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top1 = Image.open(r"C:\Users\HP\OneDrive\Desktop\PHOTO.jpg")
        img_top1 = img_top1.resize((200,200)  )
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
    
        f_lbl2 = Label(main_frame,image=self.photoimg_top1)
        f_lbl2.place(x=300,y=10,width=200,height =200)

        #Developer info
        dep_label = Label(main_frame,text="Hello My name is Aditya",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=5)

        dep_label = Label(main_frame,text="I am Python Developer",font=("times new roman",18,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=40)

        dep_label = Label(main_frame,text="Also a Cybersecurity expert",font=("times new roman",18,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=85)

        img5 = Image.open(r"college_images\download (4).jpg")
        img5 = img5.resize((500,390)  )
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl = Label(main_frame,image=self.photoimg5)
        f_lbl.place(x=0,y=210,width=500,height = 390)




if __name__ == "__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()