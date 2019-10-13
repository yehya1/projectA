from tkinter import *
import Funcfile
from technician import printf
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import messagebox

#reading and checking username and password from excel file
def connectoin(name,password):
    df = pd.read_excel('UsersList.xlsx','users')
    for i in df.index:
        if df['UserName'][i] == name :
            if str(df['password'][i]) == password:
                return True
            else:
                return False
    return False
#checking the user details , printing a message according to the function result
def checkUser():
    userN=UN.get()
    userP=UP.get()
    if userN=="*":
        if userP =="":
            root.destroy()
            Funcfile.load_admin_screen()
        else:
            messagebox.showinfo(title="hello admin", message="Login failed: Invalid password")
    else:
        #call connection function to verify if the user & the password saved in the system database
        data=connectoin(userN,userP)
        #print(data)
        if data==True:
            root.destroy()
            Funcfile.load_tech_screen()
        else:
            messagebox.showinfo(title="hello user", message="Login failed: Invalid username or password")


#form design
cal_travel_time(31.3238353,35.0711483,31.3856301,34.7637722)
root=Tk()
UN=StringVar()
UP=StringVar()
root.geometry("500x650")
root.title("System Login")
root.configure(bg='white')
t=Label(root,text="Login Form",font=('Times New Roman',30),bd=20,fg='green',bg='white',height=1)
t.pack()
form=Frame(root)
form.pack(side=LEFT)
form.configure(bg='white')
name1=Label(form,text="Username:",font=('Times New Roman',20),bg='white',bd=30).grid(row=1,sticky=W)
password1=Label(form,text="password:",font=('Times New Roman',20),bg='white',bd=30).grid(row=2,sticky=W)
name2=Entry(form,textvariable=UN).grid(row=1,column=2)
password2=Entry(form,textvariable=UP,show=("*")).grid(row=2,column=2)
login=Button(root,text="Login",font=('Times New Roman',14),bg='green',fg='white',padx=10,command=checkUser)
place = login.place(relx=0.5, rely=0.75, anchor=CENTER)
canvas = Canvas(root, width = 208, height = 204)
canvas.place(relx = 0.5, rely = 0.3, anchor = CENTER)
img = PhotoImage(file="images.png")
canvas.create_image(10,5, anchor=NW, image=img)
canvas.configure(bg='white')
root.mainloop()