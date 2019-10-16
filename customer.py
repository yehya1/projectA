import tkinter as tk
from tkinter import ttk
from tkinter import *
def click():
    str=name.get(),',',compo1.get(),',',compo2.get(),',',place.get()
    tk.Label(app,text=str,).grid(column=1,row=4)
app = tk.Tk()
x=10
y=10
app.geometry('320x250')
app.title("customer")

name=tk.StringVar()
product=tk.IntVar()
issue=tk.IntVar()
place=tk.StringVar()

tk.Label(app,text = "name custmer:").grid(column=0,row=0,padx=x,pady=y)
tk.Entry(app,textvariable=name).grid(column=1,row=0,padx=x,pady=y)
tk.Label(app,text = "product name:").grid(column=0, row=1,padx=x,pady=y)

compo1=ttk.Combobox(app,values=[1,2,3,4,5,6,7,8,9,10])
compo1.current(0)
#compo1.bind("<<ComboboxSelected>>", callbackFunc1)
compo1.grid(column=1,row=1,padx=x,pady=y)


tk.Label(app,text = "issue:").grid(column=0, row=2,padx=x,pady=y)

compo2=ttk.Combobox(app,values=[1,2,3,4,5,6,7,8,9,10])
compo2.current(0)
#compo2.bind("<<ComboboxSelected>>", callbackFunc2)
compo2.grid(column=1,row=2,padx=x,pady=y)

tk.Label(app,text = "palce:").grid(column=0, row=3,padx=x,pady=y)
tk.Entry(app,textvariable=place).grid(column=1,row=3,padx=x,pady=y)
tk.Button(app,text="send",width=15,command=click).grid(column=0,row=4,padx=x+5,pady=y+5)

app.mainloop()
