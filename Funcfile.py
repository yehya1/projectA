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
def Shibuts():
    #messagebox.showinfo(title="ok", message="shibuts is ok")
    print("Hello")

def load_admin_screen():
    root=Tk()
    root.geometry("500x500")
    root.title("Admin")
    shibuts=Button(root,text="Shibuts",font=('Times New Roman',14),bg='green',fg='white',padx=10,command=Shibuts)
    shibuts.place(relx=0.5, rely=0.75, anchor=CENTER)
    root.mainloop()
def load_tech_screen():
    root1=Tk()
    root1.geometry("500x500")
    root1.title("tech")
    root1.mainloop()
