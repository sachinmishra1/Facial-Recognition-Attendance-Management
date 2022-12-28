from os import pardir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1280x670+0+0")
        self.root.title("Face Recognition System")
        # self.root.wm_iconbitmap('icon.ico')

        title_lb = Label(self.root, text="DEVELOPER",font=("times new roman",33,"bold"),bg="white", fg="darkblue")
        title_lb.place(x=0, y=1, width=1280 , height=45)

        img_top = Image.open(r"photos/white.jpg")
        img_top = img_top.resize((1280,670),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        lb_top = Label(self.root,image=self.photoimg_top)
        lb_top.place(x=0, y=45, width=1280, height=670)

        main_frame=Frame(lb_top,bd=2,bg='white')
        main_frame.place(x=350,y=50,width=700,height=250)


        img = Image.open(r"photos/sachin.jpeg")
        img = img.resize((250,250),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        lb = Label(main_frame,image=self.photoimg)
        lb.place(x=0, y=-1, width=250, height=250)

        detail=Label(main_frame,text='Hi , I\'m Sachin Mishra and I am ',font=("times new roman",20,"bold"),fg="black",bg='white')
        detail.place(x=270,y=4)

        detail=Label(main_frame,text='Python Developer',font=("times new roman",20,"bold"),fg="white",bg='black')
        detail.place(x=270,y=40)

        detail=Label(main_frame,text='I am a Python Developer and currenty a 3rd year college',font=("times new roman",12),fg="black",bg='white')
        detail.place(x=270,y=80)

        detail=Label(main_frame,text='student in DTU, Delhi. I have 1 year of experience in',font=("times new roman",12),fg="black",bg='white')
        detail.place(x=270,y=100)

        detail=Label(main_frame,text='Python Programming. I am open for new opportunities',font=("times new roman",12),fg="black",bg='white')
        detail.place(x=270,y=120)

        detail=Label(main_frame,text='and interesting projects.',font=("times new roman",12),fg="black",bg='white')
        detail.place(x=270,y=140)

        detail=Label(main_frame,text='   EMAIL :   ',font=("times new roman",16,"bold"),fg="white",bg='black')
        detail.place(x=270,y=170)

        detail=Label(main_frame,text='sachinmishra.rrps@gmail.com',font=("times new roman",14),fg="black",bg='white')
        detail.place(x=400,y=170)

        detail=Label(main_frame,text='CONTACT:',font=("times new roman",16,"bold"),fg="white",bg='black')
        detail.place(x=270,y=210)

        detail=Label(main_frame,text='9958440674',font=("times new roman",14),fg="black",bg='white')
        detail.place(x=400,y=210)


if __name__=="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()