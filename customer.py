import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import time
from pandas import DataFrame
#reading single line from csv file
def readcsv(num):
    #openning file out of the function
    cols=pd.read_csv("IssueLocation.csv")
    cols.iloc[num]

def fillcombobox():
    import pandas as pd
    xl=pd.read_csv("IssueTime.csv")
    lst=[]
    for i in range(1,len(xl['product'])):
        if not(xl['product'][i] in lst):
            lst.append(xl['product'][i])
    return lst
def callback(events):
    import pandas as pd
    xl=pd.read_csv("IssueTime.csv")
    lst1=[]
    for i in range(len(xl['discription'])):
        if compo1.get()==xl['product'][i]:
            lst1.append(xl['discription'][i])
    tk.Label(app, text="issue:").grid(column=0, row=2, padx=x, pady=y)
    global compo2
    compo2 = ttk.Combobox(app,textvariable=issue, values=lst1)
    compo2.update()
    compo2.current(0)
    compo2.grid(column=1, row=2, padx=x, pady=y)

def click():
    customerIssue={"name":name.get(),
                   "product":product.get(),
                   "issue":issue.get(),
                   "place":place.get(),
                   "time":time.asctime()}
    df=pd.DataFrame([customerIssue])
    df.to_csv('customerissue.csv', mode='a',index=False)

global lst1
#readcsv(3)
app = tk.Tk()
x=10
y=10
app.geometry('320x250')
app.title("customer")

name=tk.StringVar()
product=tk.StringVar()
issue=tk.StringVar()
place=tk.StringVar()

tk.Label(app,text = "name customer:").grid(column=0,row=0,padx=x,pady=y)
tk.Entry(app,textvariable=name).grid(column=1,row=0,padx=x,pady=y)



tk.Label(app,text = "product name:").grid(column=0, row=1,padx=x,pady=y)
lst=fillcombobox()
compo1=ttk.Combobox(app,textvariable=product,values=lst)
compo1.current(0)
compo1.bind("<<ComboboxSelected>>", callback)
compo1.grid(column=1,row=1,padx=x,pady=y)


tk.Label(app,text = "place:").grid(column=0, row=3,padx=x,pady=y)
tk.Entry(app,textvariable=place).grid(column=1,row=3,padx=x,pady=y)
tk.Button(app,text="send",width=15,command=click).grid(column=0,row=4,padx=x+5,pady=y+5)

app.mainloop()
