from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk 
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recogination_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongination System")
        #first
        img = Image.open(r"C:\\Users\\HP\\OneDrive\Desktop\\Face recogination system\\college_images\\download.jpg")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)
        #second
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height = 130)

        img2 = Image.open(r"C:\\Users\\HP\\OneDrive\Desktop\\Face recogination system\\college_images\\images (1).jpg")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
    
        f_lbl2 = Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=520,y=0,width=500,height = 130)

        #third
        img3 = Image.open(r"C:\\Users\\HP\\OneDrive\Desktop\\Face recogination system\\college_images\\images.jpg")
        img3 = img3.resize((500,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=1000,y=0,width=500,height = 130)

        #background
        img4 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\360_F_287071353_WXFljgcyA6kHEniBIKCyqRYaviBZTS4p.jpg")
        img4 = img4.resize((500,130) )
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image = Label(self.root,image=self.photoimg4,bg="black")
        bg_image.place(x=0,y=130,width=1530,height = 790)

        title_lbl = Label(bg_image,text="FACE RECOGINATION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #-------------time--------------
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=45)
        time()

        #student button
        img5 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\istockphoto-1438437093-612x612.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(bg_image,image =self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button
        img6 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\shutterstock_1191637648-1.png")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2=Button(bg_image,image =self.photoimg6,command=self.face_data,cursor="hand2")
        b2.place(x=480,y=100,width=220,height=220)
        b2_1=Button(bg_image,text="Face detector",command=self.face_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=480,y=300,width=220,height=40)

        #attendance button
        img7 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\Choosing-The-Right-Attendance-Management-System-839x480.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b2=Button(bg_image,image =self.photoimg7,cursor="hand2",command=self.attendance_data)
        b2.place(x=780,y=100,width=220,height=220)
        b2_1=Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=780,y=300,width=220,height=40)

        #help button
        img8 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\images.png")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b2=Button(bg_image,image =self.photoimg8,cursor="hand2",command=self.help_data)
        b2.place(x=1080,y=100,width=220,height=220)
        b2_1=Button(bg_image,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=1080,y=300,width=220,height=40)

        #trian face button
        img9 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\images (2).jpg")
        img9 = img9.resize((220,220) )
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b2=Button(bg_image,image =self.photoimg9,command=self.train_data,cursor="hand2")
        b2.place(x=200,y=400,width=220,height=220)
        b2_1=Button(bg_image,text="Train data ",command=self.train_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=200,y=600,width=220,height=40)

        #photos button
        img10 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\how-do-i-use-google-face-recognition.jpg")
        img10= img10.resize((220,220) )
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b2=Button(bg_image,image =self.photoimg10,cursor="hand2",command=self.open_image)
        b2.place(x=480,y=400,width=220,height=220)
        b2_1=Button(bg_image,text="Photos ",cursor="hand2",command=self.open_image,font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=480,y=600,width=220,height=40)

        #Developer button
        img11 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\face-biometric-database-1024x418.jpeg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b2=Button(bg_image,image =self.photoimg11,cursor="hand2",command=self.developer_data)
        b2.place(x=780,y=400,width=220,height=220)
        b2_1=Button(bg_image,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=780,y=600,width=220,height=40)

        #Exit button
        img12 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recogination system\college_images\download (2).jpg")
        img12= img12.resize((220,220))
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b2=Button(bg_image,image =self.photoimg12,cursor="hand2",command=self.iExit)
        b2.place(x=1080,y=400,width=220,height=220)
        b2_1=Button(bg_image,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="darkBlue",fg="white")
        b2_1.place(x=1080,y=600,width=220,height=40)

    def open_image(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Fac Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


        #------------------Function buttons-------------------

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj = Face_Recogination_System(root)
    root.mainloop()