import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('300x500')
app.title("c")
name=tk.StringVar()
namelbl = tk.Label(app,text = "name custmer:").grid(column=0, row=0)
nametxt=tk.Entry(app, width=20 ,textvariable=name).grid(column=1,row=0)
productname=tk.Label(app,text = "product name:").grid(column=0, row=1)
productnamecompo= ttk.Combobox(app).grid(column=1,row=1)
issue=tk.Label(app,text = "issue:").grid(column=0, row=2)
issuecompo= ttk.Combobox(app).grid(column=1,row=2)
palce=tk.Label(app,text = "palce:").grid(column=0, row=3)
palcetxt=tk.Entry(app).grid(column=1,row=3)
sendissue=tk.Button(app,text="send",width=15).grid(column=0,row=4)
#place = sendissue.place(relx=0.5, rely=0.75, anchor=CENTER)
app.mainloop()
