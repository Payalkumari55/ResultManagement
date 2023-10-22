from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk,messagebox
class Login: 
        def __init__(self,root):
                self.root=root
                self.root.title("Login System")
                self.root.geometry("1200x450+80+150")
                self.root.config(bg="white")

# /////////////////////////////////////////////////////////////////
                # #====content__Window====
                self.login_img=Image.open("images\login.jpg")
                self.login_img=self.login_img.resize((1270,450),Image.LANCZOS)
                self.login_img=ImageTk.PhotoImage(self.login_img)

                self.lbl_login=Label(self.root,image=self.login_img).place(x=0,y=0)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                Frame_login=Frame(self.root,bg="#FFE6E8",bd=5)
                Frame_login.place(x=100,y=70,height=340,width=550)
        
        #  //////////////////////////////////////////////////
                title=Label(Frame_login,text="LOGIN HERE",font=("ALGERIAN",30,"bold"),fg="#551606",bg="#FFE6E8").place(x=90,y=10)
                desc=Label(Frame_login,text="Student / Faculty Login Area",font=("Goudy old lady",14,"bold"),fg="#d25d17",bg="#FFE6E8").place(x=90,y=60)

                lbl_user=Label(Frame_login,text="Username",font=("goudy old lady",14),fg="Dark blue",bg="#DCD0FF").place(x=90,y=100)
                self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="#AB784E")
                self.txt_user.place(x=90,y=130,width=350,height=35)

                lbl_pass=Label(Frame_login,text="Password",font=("goudy old lady",14),fg="Dark blue",bg="#DCD0FF").place(x=90,y=170)
                self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="#AB784E")
                self.txt_pass.place(x=90,y=200,width=350,height=35)

                forget_btn=Button(Frame_login,text="Forget Password?",bg="#FFE6E8",fg="red",bd=0,cursor="hand2",font=("times new roman",12)).place(x=90,y=240)
                Login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#3B2F2F",cursor="hand2",font=("times new roman",22)).place(x=330,y=350,width=180,height=40)

        def login_function(self):
                
                if self.txt_pass.get()=="" or self.txt_user.get()=="":
                        messagebox.showerror("Error","All fields are required",parent=self.root)
                elif self.txt_pass.get()!="12345678" or self.txt_user.get()!="Payal":
                        messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
                else:
                        messagebox.showinfo("Welcome",f"Welcome{self.txt_user.get()}\nYour Password:{self.txt_pass.get()}" ,parent=self.root)

        




         
if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()