from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import re
import pymysql.cursors

############# HERE [0] MEANS 1ST POSTION IN A LIST ############### 

class Login_System:
    global db
    db=pymysql.connect("localhost","root","root","DATA")
    print("connected")

    ###### LOGIN PAGE #######
    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #=======All Images=============
        self.bg_icon=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\bg.jpg"))
        self.user_icon=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\man-user.png"))
        self.pass_icon=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\password.png"))
        self.logo_icon=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\logo.png"))
        #========Variables=============
        self.uname=StringVar()
        self.pass_=StringVar()
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        developers=Label(self.root, text="Developed by: Aakash Verma, Akash Tiwari, Siddhesh Upadhyay",font=("comic sans ms",10)).place(x=1138,y=780)

        ###### FRAME ########
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=480,y=80)

        lbllogin=Label(Login_Frame, text="LOGIN",compound=TOP,font=("comic sans ms",50,"bold"),bg="white").grid(row=0,columnspan=3,padx=10,pady=5)
        lbllogin1=Label(Login_Frame, text="=============== OR ===============",compound=TOP,font=("comic sans ms",20),bg="white").grid(row=5,column=0,columnspan=4,padx=10,pady=5)
        #lbllogin2=Label(Login_Frame, text="Developed by: Aakash Verma, Akash Tiwari, Siddhesh Upadhyay",compound=LEFT,font=("comic sans ms",10),bg="white").grid(row=7,column=0,columnspan=5,pady=5)

        Logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=1,columnspan=3,pady=15)

        lbluser=Label(Login_Frame, text="STUDENT NAME :",compound=LEFT,font=("comic sans ms",20,"bold"),bg="white").grid(row=2,column=0,padx=5,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("comic sans ms",15)).grid(row=2,column=1,padx=8)
        lblpass=Label(Login_Frame, text=" STUDENT  ID    :",compound=LEFT,font=("comic sans ms",20,"bold"),bg="white").grid(row=3,column=0,padx=5,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("comic sans ms",15)).grid(row=3,column=1,padx=8)

        
        def register():
            global register_screen
            register_screen = Toplevel()
            register_screen.title("Register")
            register_screen.geometry("500x660+0+0")

            #register_screen.attributes("-transparent", 'red')
            
            register_screen.bg_icon2=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\bg15.jpg"))
            bg_lbl2=Label(register_screen,image=register_screen.bg_icon2).pack()
            
            global stud_name_entry
            global stud_id_entry
            global gender_entry
            global class_entry
            global year_entry
            global contact_entry
            global email_entry 

            stud_name = StringVar()
            stud_id = StringVar()
            gender = tk.StringVar()
            Class = tk.StringVar()
            year = tk.StringVar()
            contact = StringVar()
            email = StringVar()
            
            tk.Label(register_screen, text="PLEASE ENTER DETAILS BELOW",width=350,height=12, compound=CENTER, image=register_screen.bg_icon2, font=("comic sans ms",16,"bold"),fg="white").place(x=80,y=5)

            pic1 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\pic1.png")
            b11=Button(register_screen,text="SELECT IMAGE", font=( 'comic sans ms', 10,'bold'),command=fileDialog, image = pic1,compound=TOP)
            b11.image=pic1
            b11.place(x=180,y=40)

            stud_name_lable = Label(register_screen, text="Student Name :", font=("comic sans ms",14,"bold"),fg="black")
            stud_name_lable.place(x=10,y=222)
            stud_name_entry =tk.Entry(register_screen, textvariable=stud_name, font=("comic sans ms",14),bg="white",fg="black")
            stud_name_entry.place(x=180,y=222)

            stud_id_lable = Label(register_screen, text="Student ID    :", font=("comic sans ms",14,"bold"),fg="black")
            stud_id_lable.place(x=10,y=265)
            stud_id_entry = Entry(register_screen, textvariable=stud_id, font=("comic sans ms",14),fg="black",bg="white")
            stud_id_entry.place(x=180,y=265)
    

            gender_lable = Label(register_screen, text="Gender         :", font=("comic sans ms",14,"bold"),fg="black")
            gender_lable.place(x=10,y=310 )
            gender_entry = ttk.Combobox(register_screen, textvariable=gender,font=("comic sans ms",14))
            gender_entry['values'] = ("Male", "Female", "Others")
            gender_entry.place(x=180,y=310)
            
            class_lable = Label(register_screen, text="Class           :", font=("comic sans ms",14,"bold"),fg="black")
            class_lable.place(x=10,y=355)
            class_entry = ttk.Combobox(register_screen, textvariable=Class,font=("comic sans ms",14))
            class_entry['values'] = ("B.Sc. Computer Science", "B.Sc Information Technology", "B.Sc. Biotechnology","B.Sc. Microbiology","B.Sc. Plain PCM","Bachelor Of Commerce","Bachelor Of Accountancy & Finance","Bachelor Of Finance Management","Bachelor Of Mass Media","Bachelor Of Management Studies")
            class_entry.place(x=180,y=355)

            year_lable = Label(register_screen, text="Year            :", font=("comic sans ms",14,"bold"),fg="black")
            year_lable.place(x=10,y=400)
            year_entry = ttk.Combobox(register_screen, textvariable=year,font=("comic sans ms",14))
            year_entry['values'] = ("First Year", "Second Year", "Third Year")
            year_entry.place(x=180,y=400)

            contact_lable = Label(register_screen, text="Contact No.   :", font=("comic sans ms",14,"bold"),fg="black")
            contact_lable.place(x=10,y=445)
            contact_entry = Entry(register_screen, textvariable=contact, font=("comic sans ms",14),fg="black",bg="white")
            contact_entry.place(x=180,y=445)

            email_lable = Label(register_screen, text="Email ID       :", font=("comic sans ms",14,"bold"),fg="black")
            email_lable.place(x=10,y=490)
            email_entry = Entry(register_screen, textvariable=email, font=("comic sans ms",14),fg="black",bg="white")
            email_entry.place(x=180,y=490)

            Button(register_screen, text="REGISTER", width=10, height=1, font=("comic sans ms",14,"bold"), bg="black", fg="white", command = register_user).place(x=180,y=580)

            
         ######## OPENS FILE EXPLORER ######## 
        def fileDialog():
            global label_insert
            global s_pic
            pic_insert=tk.StringVar()
            filename = filedialog.askopenfilename(initialdir =  "//", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")) )
            label_insert = ttk.Label(register_screen,width=35, text = "",font=("comic sans ms",10))
            label_insert.place(x=100,y=180)
            label_insert.configure(text = filename)
            s_pic=label_insert.cget('text')
            
            
        ########## DATA ENTRY IN MYSQL TABLE ##########
        def register_user():
            s_name = stud_name_entry.get()
            s_id = stud_id_entry.get()
            s_gender = gender_entry.get()
            s_class = class_entry.get()
            s_year = year_entry.get()
            s_contact = contact_entry.get()
            s_email = email_entry.get()

            try:
                try:
                    if s_name=="" or s_id=="" or s_gender=="" or s_class=="" or s_year=="" or s_contact=="" or s_email=="":
                        messagebox.showerror("DB error","Data not inserted completely")
                    elif len(s_id)!=5:
                        messagebox.showerror("DB error","ID should contain only 5 numbers")
                    elif len(s_contact)!=10:
                        messagebox.showerror("DB error","CONTACT should contain only 10 numbers")
                    else:
                        stud_query = "INSERT INTO student(name,id,gender,class,year,contact,email,image) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (s_name,s_id,s_gender,s_class,s_year,s_contact,s_email,s_pic)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Registered Successful")
                        register_screen.destroy()
                except:
                    stud_query = "INSERT INTO student(name,id,gender,class,year,contact,email) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (s_name,s_id,s_gender,s_class,s_year,s_contact,s_email)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Registered Successful")
                    register_screen.destroy()
            except:
                messagebox.showerror("DB error","ID/Contact Already Registered")
            register_screen.destroy()
                
    
        btn_reg=Button(Login_Frame,text="REGISTER",width=14,command=register, font=("comic sans ms",16,"bold"),bg="black",fg="white").grid(row=6,columnspan=4,pady=15)
        

        ######## STUDENT PROFILE #########
        def Main():
            global Main_Screen
            Main_Screen= Toplevel(bg="black")
            Main_Screen.state("zoomed")
            Main_Screen.title("Student Profile")
            Main_Screen.geometry("1350x700+0+0")

            #Main_Screen.bg_icon2=ImageTk.PhotoImage(Image.open(r"C:\Users\Shweta\Pictures\images\bg21.jpg"))
            #Label(Main_Screen,image=Main_Screen.bg_icon2).pack()

            #Main_Screen.attributes("-transparent","black")
            
            l_id=self.pass_.get()
       
        #========Variables=============
            Main_Screen.uname=StringVar()
            Main_Screen.pass_=StringVar()

            cursor=db.cursor()
            display="SELECT image FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            img=cursor.fetchone()[0]
            
            

            if img==None:
                disclaimer=Label(Main_Screen,text="Contact the ADMIN for \ninserting/updating profile pic", font=("comic sans ms",20),bg="black",fg="blue").place(x=600,y=210)
            else:
                img=Image.open(img).resize((360,410), Image.ANTIALIAS) #RESIZING IMAGE IN PIXELS
                Main_Screen.logo_icon1=ImageTk.PhotoImage(img)
                Logolbl1=tk.Label(Main_Screen,image=Main_Screen.logo_icon1,bd=0,width=360,height=410,bg="black").place(x=590,y=70)
                
                
        ############ FRAME 1 #############
            stud_title=Label(Main_Screen,text="STUD-DLE",font=("algeria",30),bg="black",fg="dark orange").place(x=670,y=10)

            def home():
                Main_Screen.destroy()
                
            frame_home=Button(Main_Screen,text="HOME",width=9,font=("comic sans ms",12,"bold"),command=home,bg="black",fg="white").place(x=1430,y=10)    
           
 
        ############ FRAME 2 ##############
            stud_name=Label(Main_Screen,text="NAME             : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=500)
            cursor=db.cursor()
            display="SELECT name FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            name1=cursor.fetchone()
            name1=str(name1).strip("''[](),{}")
            stud_name1=Label(Main_Screen,text=name1, font=("comic sans ms",24),bg="black",fg="firebrick1").place(x=710,y=495)
            
            stud_id=Label(Main_Screen,text="STUDENT ID : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=550)
            cursor=db.cursor()
            display="SELECT id FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            id1=cursor.fetchone()
            stud_id1=Label(Main_Screen,text=id1, font=("comic sans ms",24),bg="black",fg="yellow").place(x=710,y=545)
            
            stud_class=Label(Main_Screen,text="CLASS            : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=600)
            cursor=db.cursor()
            display="SELECT class FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            class1=cursor.fetchone()
            class1=str(class1).strip("''[](),{}")
            stud_class1=Label(Main_Screen,text=class1, font=("comic sans ms",24),bg="black",fg="firebrick1").place(x=710,y=595)
            
            #stud_dob=Label(Main_Screen,text="BIRTH DATE : ", font=("comic sans ms",20),bg="black",fg="white").place(x=770,y=450)

            
            stud_year=Label(Main_Screen,text="YEAR              : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=650)
            cursor=db.cursor()
            display="SELECT year FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            year1=cursor.fetchone()
            year1=str(year1).strip("''[](),{}")
            stud_year1=Label(Main_Screen,text=year1, font=("comic sans ms",24),bg="black",fg="yellow").place(x=710,y=645)

            stud_gender=Label(Main_Screen,text="GENDER : ", font=("comic sans ms",20),bg="black",fg="white").place(x=930,y=650)
            cursor=db.cursor()
            display="SELECT gender FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            gender1=cursor.fetchone()
            gender1=str(gender1).strip("''[](),{}")
            stud_gender1=Label(Main_Screen,text=gender1, font=("comic sans ms",24),bg="black",fg="yellow").place(x=1070,y=645)
            
            stud_email=Label(Main_Screen,text="EMAIL ID       : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=700)
            cursor=db.cursor()
            display="SELECT email FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            email1=cursor.fetchone()
            email1=str(email1).strip("''[](),{}")
            stud_email1=Label(Main_Screen,text=email1, font=("comic sans ms",24),bg="black",fg="firebrick1").place(x=710,y=695)
            
            stud_contact=Label(Main_Screen,text="CONTACT       : ", font=("comic sans ms",20),bg="black",fg="white").place(x=500,y=750)
            cursor=db.cursor()
            display="SELECT contact FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            contact1=cursor.fetchone()
            stud_contact1=Label(Main_Screen,text=contact1, font=("comic sans ms",24),bg="black",fg="yellow").place(x=710,y=745)

        ############ FRAME 3 ###############
            stud_grades=Label(Main_Screen,text="GRADES ",font=("comic sans ms",28),bg="black",fg="white").place(x=1250,y=80)
            
            stud_10th=Label(Main_Screen,text="PERCENTAGE IN 10th STD : ",font=("comic sans ms",16),bg="black",fg="white").place(x=1100,y=150)
            cursor=db.cursor()
            display="SELECT 10th FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            stud_10th1=cursor.fetchone()[0]
            stud_10th1=str(stud_10th1).strip("''[](),{}")
            stud_10th2=Label(Main_Screen,text=stud_10th1, font=("comic sans ms",16),bg="black",fg="firebrick1").place(x=1410,y=150)
            
            stud_12th=Label(Main_Screen,text="PERCENTAGE IN 12th STD : ",font=("comic sans ms",16),bg="black",fg="white").place(x=1100,y=190)
            cursor=db.cursor()
            display="SELECT 12th FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            stud_12th1=cursor.fetchone()[0]
            stud_12th1=str(stud_12th1).strip("''[](),{}")
            stud_12th2=Label(Main_Screen,text=stud_12th1, font=("comic sans ms",16),bg="black",fg="yellow").place(x=1410,y=190)
            
            stud_1sem=Label(Main_Screen,text="CGPA IN FIRST SEM          : ",font=("comic sans ms",16),bg="black",fg="white").place(x=1100,y=230)
            cursor=db.cursor()
            display="SELECT first_sem FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            stud_1sem1=cursor.fetchone()[0]
            stud_1sem1=str(stud_1sem1).strip("''[](),{}")
            stud_1sem2=Label(Main_Screen,text=stud_1sem1, font=("comic sans ms",16),bg="black",fg="firebrick1").place(x=1410,y=230)
            
            stud_2sem=Label(Main_Screen,text="CGPA IN SECOND SEM       : ",font=("comic sans ms",16),bg="black",fg="white").place(x=1100,y=270)
            cursor=db.cursor()
            display="SELECT second_sem FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            stud_2sem1=cursor.fetchone()[0]
            stud_2sem1=str(stud_2sem1).strip("''[](),{}")
            stud_2sem2=Label(Main_Screen,text=stud_2sem1, font=("comic sans ms",16),bg="black",fg="yellow").place(x=1410,y=270)

            stud_review=Label(Main_Screen,text="Overall Review", font=("comic sans ms",30),bg="black",fg="white").place(x=1180,y=400)
            cursor=db.cursor()
            display="SELECT review FROM student WHERE id=%s" % (l_id)
            cursor.execute(display)
            review1=cursor.fetchone()[0]
            review1=str(review1).strip("''[](),{}")
            if review1=="None":
                stud_review1=Label(Main_Screen,text="No reviews yet", font=("comic sans ms",16),bg="black",fg="yellow").place(x=1250,y=500)
            elif review1=="":
                stud_review1=Label(Main_Screen,text="No reviews yet", font=("comic sans ms",16),bg="black",fg="yellow").place(x=1250,y=500)
            else:
                stud_review1=Label(Main_Screen,text=review1, font=("comic sans ms",16),bg="black",fg="yellow").place(x=1100,y=500)

            contact_admin=Label(Main_Screen,text="CONTACT ADMIN: ",font=("comic sans ms",14),bg="black",fg="white").place(x=1350,y=710)
            admin1=Label(Main_Screen,text="Akash  Tiwari :8850285090 \nAakash Verma :8355868664 \nSiddhesh Upadhyay :9082513253 ",font=("comic sans ms",8),bg="black",fg="white").place(x=1350,y=740)
            

           ########## FRAME 4 ############
            faculties=Label(Main_Screen,text="FACULTIES ",font=("comic sans ms",28),bg="black",fg="white").place(x=70,y=80)

            if class1=="B.Sc. Computer Science":
                f1=Label(Main_Screen,text="Kamlakar Bopatkar (HOD)",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=150)
                con1=Label(Main_Screen,text="Contact: 9819815108",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=183)
                mail1=Label(Main_Screen,text="Email: kamlakar.bopatkar@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=210)

                f2=Label(Main_Screen,text="Madhavi Vaidya ",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=250)
                con2=Label(Main_Screen,text="Contact: 9869026553",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=283)
                mail2=Label(Main_Screen,text="Email: madhavi.vaidya@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=310)
                
                f3=Label(Main_Screen,text="Sujit Chavan",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=350)
                con3=Label(Main_Screen,text="Contact: 8850172221",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=383)
                mail3=Label(Main_Screen,text="Email: sujit.chavan@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=410)
                
                f4=Label(Main_Screen,text="Neha Narne",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=450)
                con4=Label(Main_Screen,text="Contact: 7666532405",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=483)
                mail4=Label(Main_Screen,text="Email: neha.narne@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=510)
                
                f5=Label(Main_Screen,text="Laxmi Tiwari",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=550)
                con5=Label(Main_Screen,text="Contact: 9594536396",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=583)
                mail5=Label(Main_Screen,text="Email: laxmi.tiwari@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=610)
                
                f6=Label(Main_Screen,text="Rajashree Date",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=650)
                con6=Label(Main_Screen,text="Contact: 8425899501",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=683)
                mail6=Label(Main_Screen,text="Email: rajashree.date@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=710)


            elif  class1=="B.Sc Information Technology":
                f1=Label(Main_Screen,text="Shital Patil (HOD) ",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=150)
                con1=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=183)
                mail1=Label(Main_Screen,text="Email: shital.patil@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=210)
                
                f2=Label(Main_Screen,text="Ganesh Anadraj ",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=250)
                con2=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=283)
                mail2=Label(Main_Screen,text="Email: ganesh.anadraj@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=310)
                
                f3=Label(Main_Screen,text="Divya Shetty",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=350)
                con3=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=383)
                mail3=Label(Main_Screen,text="Email: divya.shetty@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=410)
                
                f4=Label(Main_Screen,text="Prajesha Jitesh",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=450)
                con4=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=483)
                mail4=Label(Main_Screen,text="Email: prajesha.jitesh@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=510)
                
                f5=Label(Main_Screen,text="Gitanjali Yatnalkar",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=550)
                con5=Label(Main_Screen,text="Contact: 9594536396",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=583)
                mail5=Label(Main_Screen,text="Email: gitanjali.yatnalkar@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=610)


            else:
                f1=Label(Main_Screen,text="Shantini Nair (HOD)",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=150)
                con1=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=183)
                mail1=Label(Main_Screen,text="Email: shantini.nair@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=210)
                
                f2=Label(Main_Screen,text="Shweta Patil ",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=250)
                con2=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=283)
                mail2=Label(Main_Screen,text="Email: shweta.patil@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=310)
                
                f3=Label(Main_Screen,text="Suman Ganger",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=350)
                con3=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=383)
                mail3=Label(Main_Screen,text="Email: suman.ganger@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=410)
                
                f4=Label(Main_Screen,text="Amrin Gaonkar",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=450)
                con4=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=483)
                mail4=Label(Main_Screen,text="Email: amrin.gaonkar@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=510)
                
                f5=Label(Main_Screen,text="Dona Joseph",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=550)
                con5=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=583)
                mail5=Label(Main_Screen,text="Email: dona.joseph@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=610)
                
                f6=Label(Main_Screen,text="Malay Shah",font=("comic sans ms",12),bg="black",fg="white").place(x=60,y=650)
                con6=Label(Main_Screen,text="Contact: ",font=("comic sans ms",12),bg="black",fg="firebrick1").place(x=60,y=683)
                mail6=Label(Main_Screen,text="Email: malay.shah@ves.ac.in",font=("comic sans ms",12),bg="black",fg="yellow").place(x=60,y=710)
                
                #f7=Label(Main_Screen,text="Ketaki Joshi",font=("comic sans ms",16),bg="black",fg="white").place(x=60,y=790)
                

        ########## MATCHES DATA ENTERED IN LOGIN PAGE WITH DATA STORED MYSQL TABLE ###########   
        def login():
            l_name=self.uname.get()
            l_id=self.pass_.get()
            if l_name=="":
                messagebox.showerror("DB error","Please enter STUDENT NAME")
            elif l_id=="":
                messagebox.showerror("DB error","Please enter STUDENT ID")
            else:
                cursor=db.cursor()
                data="SELECT name FROM student WHERE id=%s" % (l_id)
                cursor.execute(data)
                x=cursor.fetchone()
                x1=str(x).strip("''[](),{}")
        
                cursor=db.cursor()
                cursor.execute("SELECT id FROM student")
                x2=cursor.fetchall()
                x3=str(x2)
                search1=re.search(l_id,x3)

                if search1 and len(l_id)==5 and x1==l_name:
                    Main()
                else:
                    messagebox.showerror("DB error","Invalid name/id or name/id not registered")
        btn_log=Button(Login_Frame,text="LOGIN",width=10,command=login, font=("comic sans ms",16,"bold"),bg="black",fg="white").grid(row=4,column=1,pady=10)


        ######### LOGIN PAGE ADMIN ##########
        def admin_login():
            global admin_screen
            admin_screen=Toplevel()
            admin_screen.title("ADMIN LOGIN")
            admin_screen.geometry("500x600+0+0")
            admin_screen.bg_icon4=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\bg8.png"))
            bg_lbl4=Label(admin_screen,image=admin_screen.bg_icon4).pack()
            admin_screen.logo_icon4=ImageTk.PhotoImage(Image.open(r"C:\Users\shwet\Pictures\images\logo4.jpg"))
            
            global admin_name
            global admin_pass
            
            admin_name=StringVar()
            admin_pass=StringVar()

            admin_Frame=Frame(admin_screen,bg="white")
            admin_Frame.place(x=90,y=50)
            lbladmin=Label(admin_Frame, text="ADMIN",compound=TOP,font=("comic sans ms",30,"bold"),bg="white").grid(row=0,columnspan=3,padx=10,pady=5)
            
            Logolbl4=Label(admin_Frame,image=admin_screen.logo_icon4,bd=0).grid(row=1,columnspan=3,pady=5)
        
            lbluser4=Label(admin_Frame, text="USERNAME",compound=LEFT,font=("comic sans ms",16,"bold"),bg="white").grid(row=2,column=1,padx=10)
            txtuser4=Entry(admin_Frame,bd=5,textvariable=admin_name,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=40,pady=10)

            lblpass4=Label(admin_Frame, text="PASSWORD",compound=LEFT,font=("comic sans ms",16,"bold"),bg="white").grid(row=4,column=1,padx=10)
            txtpass4=Entry(admin_Frame,bd=5,textvariable=admin_pass,relief=GROOVE,font=("",15)).grid(row=5,column=1,padx=40,pady=10)

            btn_log4=Button(admin_Frame,text="LOGIN",command=a_login,width=8, font=("comic sans ms",16,"bold"),bg="black",fg="white").grid(row=6,column=1,pady=20)
        
        btn_admin=Button(Login_Frame,text="ADMIN", command=admin_login,width=10, font=("comic sans ms",16,"bold"),bg="black",fg="white").grid(row=4,column=0,pady=10)


        ########## ADMIN PAGE ###########
        def main1():
            global main_admin
            main_admin= Toplevel(bg="black")
            main_admin.state("zoomed")
            main_admin.title("Student Profile")
            main_admin.geometry("1350x700+0+0")
            
            #main_admin.bg_icon6=ImageTk.PhotoImage(Image.open(r"C:\Users\Shweta\Pictures\images\bg16.jpg"))
            #bg_lbl6=Label(main_admin,image=main_admin.bg_icon6).pack()

            d1=Label(main_admin, text = 'SCIENCE DEPARTMENT',font =( 'comic sans ms', 30,'bold'),fg="white",bg="black")
            d1.pack(side="top")

            photo1 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b1.png")
            b1=Button(main_admin,text="B.Sc. Computer \n Science", font=( 'comic sans ms', 10,'bold'),command=view1, image = photo1,bg="white", compound=TOP)
            b1.image=photo1
            b1.place(x=140,y=120)

            photo2 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b2.png")
            b2=Button(main_admin,text="B.Sc. Information \n Technology", font=( 'comic sans ms', 10,'bold'),command=view2, image = photo2,bg="white", compound=TOP)
            b2.image=photo2
            b2.place(x=380,y=130)

            photo3 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b3.png")
            b3=Button(main_admin,text="B.Sc. Biotechnology", font=( 'comic sans ms', 10,'bold'),command=view3, image = photo3,bg="white",compound=TOP)
            b3.image=photo3
            b3.place(x=660,y=130)

            photo4 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b4.png")
            b4=Button(main_admin,text="B.Sc. Microbiology", font=( 'comic sans ms', 10,'bold'),command=view4, image = photo4,bg="white",compound=TOP)
            b4.image=photo4
            b4.place(x=945,y=132)

            photo5 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b5.jpg")
            b5=Button(main_admin,text="B.Sc. Plain PCM", font=( 'comic sans ms', 10,'bold'),command=view5, image = photo5,bg="white",compound=TOP)
            b5.image=photo5
            b5.place(x=1210,y=132)
            
            d2=Label(main_admin, text = 'COMMERCE DEPARTMENT',font =( 'comic sans ms', 30,'bold'),fg="white",bg="black")
            d2.place(x=500,y=400)

            photo6 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b6.jpg")
            b6=Button(main_admin,text="Bachelor Of\n Commerce", font=( 'comic sans ms', 10,'bold'),command=view6, image = photo6,bg="white",compound=TOP)
            b6.image=photo6
            b6.place(x=130,y=510)

            photo7 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b7.jpg")
            b7=Button(main_admin,text="Bachelor Of \nAccountancy & Finance", font=( 'comic sans ms', 10,'bold'),command=view7, image = photo7,bg="white",compound=TOP)
            b7.image=photo7
            b7.place(x=380,y=515)

            photo8 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b8.jpg")
            b8=Button(main_admin,text="Bachelor Of Finance\n Management ", font=( 'comic sans ms', 10,'bold'),command=view8, image = photo8,bg="white",compound=TOP)
            b8.image=photo8
            b8.place(x=665,y=515)

            photo9 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b9.jpg")
            b9=Button(main_admin,text="Bachelor Of Mass\n Media ", font=( 'comic sans ms', 10,'bold'),command=view9, image = photo9,bg="white",compound=TOP)
            b9.image=photo9
            b9.place(x=940,y=515)

            photo10 = ImageTk.PhotoImage(file = r"C:\Users\shwet\Pictures\images\b10.jpg")
            b10=Button(main_admin,text="Bachelor Of \nManagement Studies", font=( 'comic sans ms', 10,'bold'),command=view10, image = photo10,bg="white",compound=TOP)
            b10.image=photo10
            b10.place(x=1210,y=515)

            #scrollbar = Scrollbar(main_admin)
            #scrollbar.pack( side = RIGHT, fill = Y )

        ########## ADMIN LOGIN MATCH ##########    
        def a_login():
           a_name=admin_name.get()
           a_id=admin_pass.get()
           if a_name=="student" and a_id=="student":
               main1()
           elif a_name=="" and a_id=="":
               messagebox.showerror("DB error","PLEASE FILL IN DATA")
           else:
               messagebox.showerror("DB error","INVALID USERNAME OR PASSWORD")

           admin_screen.destroy()                


################################  VIEW ALL DATA #####################################
               
        def view1():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1300x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept1
            dept1=tk.Label(view,text="B.Sc. Computer Science",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
                  
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)  
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bsc_cs = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='B.Sc. Computer Science' order by name" 
            cursor.execute(bsc_cs)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update1,bg="black",fg="white").place(x=1440,y=630)    
            
            def refresh():
                view.destroy()
                view1()
                
            def home1():
                view.destroy()    

            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home1,bg="black",fg="white").place(x=1445,y=10)
            
        def view2():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept2
            dept2=tk.Label(view,text="B.Sc. Computer Science",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150,stretch=True, anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bsc_it = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='B.Sc Information Technology' order by name" 
            cursor.execute(bsc_it)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update2,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view2()

            def home2():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home2,bg="black",fg="white").place(x=1445,y=10)
       
        def view3():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()
        
            global dept3
            dept3=tk.Label(view,text="B.Sc. Biotechnology",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)

            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bsc_bt = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='B.Sc. Biotechnology' order by name" 
            cursor.execute(bsc_bt)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update3,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view3()

            def home3():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home3,bg="black",fg="white").place(x=1445,y=10)
            
        def view4():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept4
            dept4=tk.Label(view,text="B.Sc. Microbiology",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bsc_mic = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='B.Sc. Microbiology' order by name" 
            cursor.execute(bsc_mic)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update4,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view4()

            def home4():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home4,bg="black",fg="white").place(x=1445,y=10)

        def view5():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept5
            dept5=tk.Label(view,text="B.Sc. Plain PCM",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bsc_pcm = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='B.Sc. Plain PCM' order by name" 
            cursor.execute(bsc_pcm)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update5,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view5()

            def home5():
                view.destroy()    

            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home5,bg="black",fg="white").place(x=1445,y=10)

        def view6():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept6
            dept6=tk.Label(view,text="Bachelor Of Commerce",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bcom = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='Bachelor Of Commerce' order by name" 
            cursor.execute(bcom)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update6,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view6()

            def home6():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home6,bg="black",fg="white").place(x=1445,y=10)


        def view7():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept7
            dept7=tk.Label(view,text="Bachelor Of Accountancy & Finance",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            baf = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='Bachelor Of Accountancy & Finance' order by name" 
            cursor.execute(baf)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update7,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view7()

            def home7():
                view.destroy()    

            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home7,bg="black",fg="white").place(x=1445,y=10)

        def view8():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept8
            dept8=tk.Label(view,text="Bachelor Of Finance Management",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bfm = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='Bachelor Of Finance Management' order by name" 
            cursor.execute(bfm)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update8,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view8()

            def home8():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home8,bg="black",fg="white").place(x=1445,y=10)

        def view9():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept9
            dept9=tk.Label(view,text="Bachelor Of Mass Media",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bmm = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='Bachelor Of Mass Media' order by name" 
            cursor.execute(bmm)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)       

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update9,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view9()

            def home9():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home9,bg="black",fg="white").place(x=1445,y=10)

        def view10():
            view = Toplevel()
            view.state("zoomed")
            view.title("admin")
            view.geometry("1700x700+0+0")
            bg_img =  Image.open(r'C:\Users\shwet\Pictures\images\bg18.jpg')
            photo = ImageTk.PhotoImage(bg_img)
            img_label = Label(view,image = photo)
            img_label.image = photo
            img_label.pack()

            global dept10
            dept10=tk.Label(view,text="Bachelor Of Management Studies",font=("comic sans ms",30),bg="black",fg="white").place(x=460,y=0)
        
            #scrollbar
            scr_bar = tk.Scrollbar(view, orient="vertical")
            scr_bar.place(x=1515,y=200,height=426)

            #mention number of columns
            cols=("column1", "column2", "column3", "column4","column5","column6", "column7", "column8","column9", "column10", "column11","column12")
            tree = ttk.Treeview(view, column = cols, show = 'headings' , height=20 , selectmode='browse',yscrollcommand = scr_bar.set ) 

            #treeview styling

            #print(ttk.Style().theme_names()) '''(lists all treeview styles available)'''
            ttk.Style().theme_use('classic')
            ttk.Style().configure('Treeview',bg= "black",fg='white',font=('comic sans ms',8))
            ttk.Style().configure("Treeview.Heading", background= 'grey',foreground="white",font=('comic sans ms',10,'bold'))
        
            tree.heading("#1",text="Student Name")
            tree.heading("#2",text="Student ID")
            tree.heading("#3",text="Gender")
            #tree.heading("#4",text="Class")
            tree.heading("#4",text="Year")
            tree.heading("#5",text="Contact")
            tree.heading("#6",text="Email")
            tree.heading("#7",text="Image")
            tree.heading("#8",text="10th percentage")
            tree.heading("#9",text="12th percentage")
            tree.heading("#10",text="CGPA 1st sem")
            tree.heading("#11",text="CGPA 2nd sem")
            tree.heading("#12",text="Overall review")
        
            tree.place(x=160,y=200)

            #configuration of scroll bar
            scr_bar.config(command = tree.yview)

            #updating window and adjusting column size
            for col in cols:
                tree.column(col, width=150, stretch=True,anchor="center")
                tree.column("column1",width=110)
                tree.column("column2",width=90)
                tree.column("column3",width=90)
                tree.column("column4",width=90)
                tree.column("column5",width=100)
                tree.column("column8",width=110)
                tree.column("column9",width=110)
                tree.column("column10",width=100)
                tree.column("column11",width=100)
            view.update()

            #fetching data from db and storing it in variable
            cursor=db.cursor()
            bms = "select name,id,gender,year,contact,email,image,10th,12th,first_sem,second_sem,review from student where class='Bachelor Of Management Studies' order by name" 
            cursor.execute(bms)
            rows = cursor.fetchall()
            #print(rows)
            for row in rows:
                tree.insert("",END,values=row)

            updat=Button(view,text="UPDATE DATA",width=12,font=("comic sans ms",8,"bold"),command=update10,bg="black",fg="white").place(x=1440,y=630)    

            def refresh():
                view.destroy()
                view10()
                
            def home10():
                view.destroy()
                
            refresh=Button(view,text="REFRESH",width=10,font=("comic sans ms",12,"bold"),command=refresh,bg="black",fg="white").place(x=1427,y=155)
            HOME=Button(view,text="HOME",width=8,font=("comic sans ms",12,"bold"),command=home10,bg="black",fg="white").place(x=1445,y=10)

##################### UPDATE FRAME STUDENT DATA TABLE############################
            

        def update1():
            global update
            update = Toplevel()
            update.title("update")
            update.geometry("350x480+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)
            
        def update2():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update3():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update4():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)
            
        def update5():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)            

        def update6():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update7():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update8():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update9():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

        def update10():
            update = Toplevel()
            update.title("update")
            update.geometry("350x300+0+0")

            global th10
            global th12
            global first_sem
            global second_sem
            global id1
            global rev

            th10=DoubleVar()
            th12=DoubleVar()
            first_sem=DoubleVar()
            second_sem=DoubleVar()
            id1=StringVar()
            rev=StringVar()


            ida= Label(update ,text = "Student ID",font=('comic sans ms',16)).place(x=10,y=10)
            a = Label(update ,text = "10th Percentage",font=('comic sans ms',16)).place(x=10,y=50)
            b = Label(update ,text = "12th Percentage",font=('comic sans ms',16)).place(x=10,y=90)
            c = Label(update ,text = "CGPA First Sem",font=('comic sans ms',16)).place(x=10,y=130)
            d = Label(update ,text = "CGPA Second Sem",font=('comic sans ms',16)).place(x=10,y=170)
            e = Label(update ,text = "Overall Review",font=('comic sans ms',16)).place(x=10,y=210)
            

            ida1 = Entry(update,textvariable=id1).place(x=200,y=20)
            a1 = Entry(update,textvariable=th10).place(x=200,y=60)
            b1 = Entry(update,textvariable=th12).place(x=200,y=100)
            c1 = Entry(update,textvariable=first_sem).place(x=200,y=140)
            d1 = Entry(update,textvariable=second_sem).place(x=200,y=180)
            e1 = ttk.Combobox(update,textvariable=rev)
            e1['values'] = ("Excelent in studies as well as in sports\n and extra-curricular activities", "Good student but need to focus\n on extra-curricular activities too", "Need to be attentive and\n focus on studies a lot")
            e1.place(x=200,y=220)

            b12=Button(update,text="UPDATE IMAGE", font=( 'comic sans ms', 8,'bold'),bg="black",fg="white",command=fileDialog1).place(x=120,y=280)

            up_but=Button(update,text="SUBMIT",width=12,font=("comic sans ms",12,"bold"),command=depart1,bg="black",fg="white")
            up_but.place(x=105,y=380)

##################### UPDATE DATA QUERY ########################
      
        def depart1():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart2():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()        

        def depart3():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart4():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart5():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart6():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart7():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart8():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart9():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def depart10():
            a2=th10.get()
            b2=th12.get()
            c2=first_sem.get()
            d2=second_sem.get()
            e2=rev.get()
            ida2=id1.get()
            


            try:
                try:
                    if len(ida2)==5 and (e2=="None" or e2=="" or e2==None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    elif len(ida2)==5 and (e2!="None" or e2!="" or e2!=None):
                        stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,s_pic1,ida2)
                        cursor=db.cursor()
                        cursor.execute(stud_query)
                        db.commit()
                        messagebox.showinfo("Success","Updated Successful")
                    else:
                        messagebox.showerror("Error","No such ID in this Department")
                except:
                    stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',image='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,s_pic1,ida2)
                    cursor=db.cursor()
                    cursor.execute(stud_query)
                    db.commit()
                    messagebox.showinfo("Success","Updated Successful")
            except:
                stud_query = "UPDATE student SET 10th='%s', 12th='%s', first_sem='%s', second_sem='%s',review='%s' WHERE id='%s' and class='B.Sc. Computer Science' " % (a2,b2,c2,d2,e2,ida2)
                cursor=db.cursor()
                cursor.execute(stud_query)
                db.commit()
                messagebox.showinfo("Success","Updated Successful")
            update.destroy()

        def fileDialog1():
            global label_insert1
            global s_pic1
            pic_insert1=tk.StringVar()
            filename1 = filedialog.askopenfilename(initialdir =  "//", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")) )
            label_insert1 = ttk.Label(update,width=35, text = "",font=("comic sans ms",10))
            label_insert1.place(x=50,y=320)
            label_insert1.configure(text = filename1)
            s_pic1=label_insert1.cget('text')   
                
################## END OF PROGRAM ###################

root=Tk()
obj=Login_System(root)
root.mainloop()
