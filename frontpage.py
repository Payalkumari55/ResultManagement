from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from course import CourseClass
from student import Student
from subject import Subject
from result import ResultClass
from report import ReportClass
from login import Login
from exit import Exit
class RMS: 
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x600+0+0")
        self.root.config(bg="pink")

        # ========icons====== 
        self.logo__dash=ImageTk.PhotoImage(file="images\logo.png") 

        # # =====title=====#
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo__dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        # ========Menu======
        M_Frame=LabelFrame(self.root,text="Menus",font=("Arial",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=15,y=5,width=160,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=195,y=5,width=160,height=40)
        btn_subject=Button(M_Frame,text="Subject",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_subject).place(x=375,y=5,width=160,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=555,y=5,width=160,height=40)
        btn_viewstudentresult=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=735,y=5,width=180,height=40)
        btn_login=Button(M_Frame,text="Login",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_login).place(x=935,y=5,width=160,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_exit).place(x=1115,y=5,width=160,height=40)

        # #====content__Window====
        self.pk_img=Image.open("images\pk.jpg")
        self.pk_img=self.pk_img.resize((1270,550),Image.LANCZOS)
        self.pk_img=ImageTk.PhotoImage(self.pk_img)

        self.lbl_pk=Label(self.root,image=self.pk_img).place(x=10,y=155)

        # ===============================================================================
        self.lbl_welcome=Label(self.root,text="WELCOME ALL",font=("Times new roman",40),bg="white",fg="dark red")
        self.lbl_welcome.place(x=380,y=200,width=450,height=90)

        # ===update_details====
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("Times new roman",20),bd=10,relief=RIDGE,bg="green",fg="white")
        self.lbl_course.place(x=400,y=460,width=300,height=90)

        self.lbl_student=Label(self.root,text="Total Student\n[0]",font=("Times new roman",20),bd=10,relief=RIDGE,bg="sky blue",fg="white")
        self.lbl_student.place(x=710,y=460,width=300,height=90)

        self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("Times new roman",20),bd=10,relief=RIDGE,bg="red",fg="white")
        self.lbl_result.place(x=1020,y=460,width=300,height=90)

        
        # # =====footer=====#
        footer=Label(self.root,text="SRMS- Student Result Management System\nContact us for any Technical Issue :9955449849",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill="x")
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
         
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Student(self.new_win)

    def add_subject(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Subject(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def add_login(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Login(self.new_win)
    
    def add_exit(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Exit(self.new_win)
 
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
