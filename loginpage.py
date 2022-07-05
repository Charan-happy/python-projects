#login page using python
from tkinter import *#importing of tkinter module
from tkinter.font import BOLD
class login:
    def __init__(self,root): #defining init function
        self.root=root
        self.root.title("login page by G.Nagacharan")
        self.root.geometry("1199*600+100+50")
        self.root.resizable(False,False)
        #bg image
        self.bg=PhotoImage(file="_pngtree-dark vector abstract background_1159556.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #login frame
        Frame_login=Frame(self.root,bg="light blue")
        Frame_login.place(x=150,y=150,height=340,width=500)
        title=Label(Frame_login,text="Login Here",font=("poppins",40,"bold"),fg="#000000",bg="light blue").place(x=90,y=30)
        desc=Label(Frame_login,text="Nagacharan's college student login portal",font=("goudy old style",15,"bold"),fg="#464646",bg="light blue").place(x=90,y=100)
        usr_lbl=Label(Frame_login,text="username:",font=("goudy old style",15,"bold"),fg="#404040",bg="light blue").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font("poppins",15))
        self.txt_user.place(x=190,y=140)
        usr_lbl=Label(Frame_login,text="password:",font=("goudy old style",15,"bold"),fg="#404040",bg="light blue").place(x=90,y=180)
        self.txt_user=Entry(Frame_login,font=("poppins",15))
        self.txt_user.place(x=190,y=180)
        forget_pass=Button(Frame_login,text="Forget Password?",bg="light blue",fg="#000000",bd=0,font=("quicksand",10,BOLD)).place(x=85,y=210)
        login_btn=Button(Frame_login,text="login",bg="light blue",fg="purple",bd=0,font=("quicksand",11,BOLD)).place(x=330,y=210)
        signup_btn=Button(Frame_login,text="sign up",bg="light blue",fg="purple",bd=0,font=("quicksand",11,BOLD)).place(x=230,y=210)
        root=TK()
        obj = Login(root)
        root.mainloop()
