from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#B0CFDE")
        self.root.focus_force()

        # #====content__Window====
        self.bg_img=Image.open("images/rp.jpg")
        self.bg_img=self.bg_img.resize((1300,500),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=5,y=5)

      # # =====title=====#
        title=Label(self.root,text="VIEW STUDENT CARD",font=("goudy old style",20,"bold"),bg="#033E3E",fg="white").place(x=10,y=15,width=1180,height=30)

    
        # ==================Search============
        self.var_search=StringVar()
        self.var_id=StringVar()
        lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old style",15,'bold'),bg='lightyellow').place(x=320,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,),bg='#E8ADAA').place(x=500,y=100,width=250)
        btn_search=Button(self.root,text='Search',font=("goudy old style",18,"bold"),bg="#FF6347",fg="Black",cursor="hand2",command=self.search).place(x=780,y=100,width=100,height=30)
        btn_clear=Button(self.root,text='Clear',font=("goudy old style",18,"bold"),bg="#E41B17",fg="black",cursor="hand2",command=self.clear).place(x=920,y=100,width=100,height=30)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # =======result_labels======================
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=130,y=200,width=150,height=50)
        lbl_first_name=Label(self.root,text="First Name",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=260,y=200,width=150,height=50)
        lbl_last_name=Label(self.root,text="Last Name",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=390,y=200,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=520,y=200,width=150,height=50)
        lbl_marks_obt=Label(self.root,text="Marks Obtained",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=650,y=200,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=800,y=200,width=150,height=50)
        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=930,y=200,width=150,height=50)
        lbl_remarks=Label(self.root,text="Remarks",font=("goudy old style",15,'bold'),bg='#BCB88A',bd=2,relief=GROOVE).place(x=1060,y=200,width=150,height=50)


        self.lbl_roll=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_roll.place(x=130,y=250,width=150,height=50)

        self.lbl_first_name=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_first_name.place(x=260,y=250,width=150,height=50)

        self.lbl_last_name=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_last_name.place(x=390,y=250,width=150,height=50)

        self.lbl_course=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_course.place(x=520,y=250,width=150,height=50)

        self.lbl_marks_obt=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_marks_obt.place(x=650,y=250,width=150,height=50)

        self.lbl_full_marks=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_full_marks.place(x=800,y=250,width=150,height=50)

        self.lbl_percentage=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_percentage.place(x=930,y=250,width=150,height=50)

        self.lbl_remarks=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.lbl_remarks.place(x=1060,y=250,width=150,height=50)

        # ////////////////////////Delete//////////////////////////////////////////////////////////////////////////////////////////////
        btn_delete=Button(self.root,text='Delete',font=("goudy old style",20,"bold"),bg="#550A35",fg="white",cursor="hand2",command=self.delete).place(x=500,y=400,width=200,height=40)

# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]4\
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
           if self.var_search.get()=="":
               messagebox.showerror("Error","Roll No. should be required",parent=self.root)
           else:
               cur.execute(f"select * from student where roll=?",(self.var_search.get(),))
               row=cur.fetchone()
                #    print(row)
               if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[0])
                    self.first_name.config(text=row[1])
                    self.last_name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks_obt.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.percentage.config(text=row[6])
                    self.remarks.config(text=row[7])
               else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.first_name.config(text="")
        self.last_name.config(text="")
        self.course.config(text="")
        self.marks_obt.config(text="")
        self.full_marks.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student result",parent=self.root)
            else:
                cur.execute("select * from result where id=?",(self.var_id,))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where id=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        


if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()        