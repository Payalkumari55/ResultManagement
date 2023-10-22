from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk,messagebox
class Exit: 
        def __init__(self,root):
                self.root=root
                self.root.title("Exit System")
                self.root.geometry("400x150+500+200")
                self.root.config(bg="white")

        # =========================================================
                result=messagebox.askyesno(
                       title='Yes No Demo',
                       message='Do you want to exit?',
                       detail='Click yes to quit'
                )
                if not result:
                       exit()

                
if __name__=="__main__":
    root=Tk()
    obj=Exit(root)
    root.mainloop()