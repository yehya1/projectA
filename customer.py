import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import time
from pandas import DataFrame
#reading single line from csv file
def readcsv(num):
    count=0
    cols=pd.read_csv("IssueLocation.csv")
    c1=cols[num:num+1]
    #d1=list(c1)
    d2=c1.values[0]
    print(d2)
    print(d2[0])
    print(c1)
    c2=cols[num-1:num]
    print(c2)

def fillcombobox():
    import pandas as pd
    xl=pd.read_excel("IssueTime.xlsx","IssueTime")
    lst=[]
    #lst.append(xl['product'][0])
    for i in range(1,len(xl['product'])):
        if not(xl['product'][i] in lst):
            lst.append(xl['product'][i])
    return lst
def callback(events):
    import pandas as pd
    xl=pd.read_excel("IssueTime.xlsx","IssueTime")
    lst1=[]
    for i in range(len(xl['discription'])):
        if compo1.get()==xl['product'][i]:
            lst1.append(xl['discription'][i])
    tk.Label(app, text="issue:").grid(column=0, row=2, padx=x, pady=y)
    global compo2
    compo2 = ttk.Combobox(app,textvariable=issue, values=lst1)
    #compo2 = ttk.Combobox(app, values=[1, 2, 3, 4, 5, 6])
    compo2.update()
    compo2.current(0)
    compo2.grid(column=1, row=2, padx=x, pady=y)
    print(lst1)
def click():

    lstporolem=[]
    lstporolem.append(name.get())
    lstporolem.append(product.get())
    lstporolem.append(issue.get())
    lstporolem.append(place.get())
    lstporolem.append(time.asctime())
    customerIssue={"name":[lstporolem[0]],
                   "product":[lstporolem[1]],
                   "issue":[lstporolem[2]],
                   "place":[lstporolem[3]],
                   "time":[lstporolem[4]]}
    df=pd.DataFrame(customerIssue,columns=["name","product","issue","place","time"])
    print(df)
    df.to_csv('customerissue.csv',header=False, mode='a',index=False)
global lst1

app = tk.Tk()
x=10
y=10
app.geometry('320x250')
app.title("customer")

name=tk.StringVar()
product=tk.StringVar()
issue=tk.StringVar()
place=tk.StringVar()

tk.Label(app,text = "name custmer:").grid(column=0,row=0,padx=x,pady=y)
tk.Entry(app,textvariable=name).grid(column=1,row=0,padx=x,pady=y)



tk.Label(app,text = "product name:").grid(column=0, row=1,padx=x,pady=y)
lst=fillcombobox()
compo1=ttk.Combobox(app,textvariable=product,values=lst)
compo1.current(0)
compo1.bind("<<ComboboxSelected>>", callback)
compo1.grid(column=1,row=1,padx=x,pady=y)


tk.Label(app,text = "palce:").grid(column=0, row=3,padx=x,pady=y)
tk.Entry(app,textvariable=place).grid(column=1,row=3,padx=x,pady=y)
tk.Button(app,text="send",width=15,command=click).grid(column=0,row=4,padx=x+5,pady=y+5)

app.mainloop()
