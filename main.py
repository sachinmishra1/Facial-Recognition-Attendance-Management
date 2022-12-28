from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from chatbot import ChatBot



class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x670+0+0")
        self.root.title("Face Recognition System")


        #first image
        img = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\f3.jpg")
        img = img.resize((420,100),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=100)


        #second image
        img1 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\train.jpg")
        img1 = img1.resize((420,100),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=100)


        #third image
        img2 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\f3.jpg")
        img2 = img2.resize((420,100),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=840,y=0,width=420,height=100)

        
        #bg image
        img3 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\b4.jpg")
        img3 = img3.resize((1280,670),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=670)



        title_lbl = Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",30,"bold"),bg = "white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="black", fg="white")
        lbl.place(x=50,y=0,width=110,height=30)
        time()


        #student button
        img4 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\Students.jpg")
        img4 = img4.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=160,height=160)
        
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x=100,y=220,width=160,height=40)




        #detect face button
        img5 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\face_detector.png")
        img5 = img5.resize((160,160),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=360,y=80,width=160,height=160)
        
        
        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b2_1.place(x=360,y=220,width=160,height=40)



        #Attendance face button
        img6 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\attendance.jpeg")
        img6 = img6.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=620,y=80,width=160,height=160)
        
        
        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b3_1.place(x=620,y=220,width=160,height=40)


        

        
        #Chatbot face button
        img7 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\Help_desk2.png")
        img7 = img7.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b4.place(x=880,y=80,width=160,height=160)
        
        
        b4_1=Button(bg_img,text="Chatbot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b4_1.place(x=880,y=220,width=160,height=40)




        #train data button
        img8 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\face_detector2.jpg")
        img8 = img8.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=100,y=300,width=160,height=160)
        
        
        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b5_1.place(x=100,y=460,width=160,height=40)




        #Photos button
        img9 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\faces2.jpg")
        img9 = img9.resize((160,160),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=360,y=300,width=160,height=160)
        
        
        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b6_1.place(x=360,y=460,width=160,height=40)



        #Developer face button
        img10 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\developer.jpg")
        img10 = img10.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev)
        b7.place(x=620,y=300,width=160,height=160)
        
        
        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.dev,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b7_1.place(x=620,y=460,width=160,height=40)


        

        
        #Exit button
        img11 = Image.open(r"C:\Users\sachi\Desktop\Face Recognition Attendance Management\Photos\exit.jpg")
        img11 = img11.resize((160,160),Image.ANTIALIAS) #ANTIALIAS converts high lvl image to low lvl image
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=880,y=300,width=160,height=160)
        
        
        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg = "darkblue",fg="white")
        b8_1.place(x=880,y=460,width=160,height=40)


    def open_img(self):
        os.startfile('data')

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit this program?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return





    #==============FUNCTIONS BUTTON==================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def dev(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app=ChatBot(self.new_window)


        
        






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()