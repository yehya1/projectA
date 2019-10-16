from tkinter import *
from tkinter import messagebox
def cal_travel_time(x1,y1,x2,y2):
    import math
    speed=30000
    a=x2-x1
    b=y2-y1
    distance=math.sqrt(a*a+b*b)
    time=distance/speed
    return time
def asd():
    pass
def Shibuts():

    messagebox.showinfo(title="ok", message="shibuts is ok")
    print("Hello")
def addIssue():
    pass


def addFault():
    pass


def addProduct():
    pass


def load_admin_screen():
    root=Tk()
    root.geometry("500x250")
    root.title("Admin")
    root.configure(bg='white')
    shibuts=Button(root,text="Shibuts",font=('Times New Roman',14),bg='red',fg='white',padx=10,command=Shibuts)
    shibuts.place(relx=0.5, rely=0.75, anchor=CENTER)
    AddIssue = Button(root, text="AddIssue", font=('Times New Roman', 14), bg='dark green', fg='white', padx=10,command=addIssue)
    AddIssue.place(relx=0.5, rely=0.45, anchor=CENTER)
    AddFault = Button(root, text="AddFault", font=('Times New Roman', 14), bg='blue4', fg='white', padx=10,command=addFault)
    AddFault.place(relx=0.25, rely=0.45, anchor=CENTER)
    AddProduct = Button(root, text="AddProduct", font=('Times New Roman', 14), bg='goldenrod', fg='white', padx=10,command=addProduct)
    AddProduct.place(relx=0.75, rely=0.45, anchor=CENTER)
    root.mainloop()
def load_tech_screen():
    root1=Tk()
    root1.geometry("500x500")
    root1.title("tech")
    root1.mainloop()
