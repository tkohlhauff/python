from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def calculate(*args):
    try:
        complet=float(comp.get())
        attempt=float(att.get())
        yards=float(yds.get())
        tds=float(td.get())
        intercept=float(inte.get())
        a=((complet/attempt)-.3)*5
        b=((yards/attempt)-3)*.25
        c=(tds/attempt)*20
        d=2.375-((intercept/attempt)*25)
        a=checkNum(a)
        b=checkNum(b)
        c=checkNum(c)
        d=checkNum(d)
        qbr.set(((a+b+c+d)/6)*100.0)
    except ValueError:
        messagebox.showwarning(
            'QBR',
            'Check your inputs'
        )
def checkNum(x):
    y=x
    if y>2.375:
        y=2.375
        return(y)
    elif y<0:
        y=0
        return(y)
    else:
        return(y)
root = Tk()
root.title('Quarter Back Rating')
#configuring the mainframe
mainframe= ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
#defining the variables
comp=StringVar()
att=StringVar()
yds=StringVar()
td=StringVar()
inte=StringVar()
qbr=StringVar()
#inputs for the numbers
comp_entry= ttk.Entry(mainframe, width=7, textvariable=comp)
comp_entry.grid(column=2, row=2, sticky=(W, E))
att_entry= ttk.Entry(mainframe, width=7, textvariable=att)
att_entry.grid(column=2, row=3, sticky=(W, E))
yds_entry= ttk.Entry(mainframe, width=7, textvariable=yds)
yds_entry.grid(column=2, row=4, sticky=(W, E))
td_entry= ttk.Entry(mainframe, width=7, textvariable=td)
td_entry.grid(column=2, row=5, sticky=(W, E))
inte_entry= ttk.Entry(mainframe, width=7, textvariable=inte)
inte_entry.grid(column=2, row=6, sticky=(W, E))

ttk.Label(mainframe, textvariable=qbr).grid(column=2, row=7, sticky=(W, E))
#warning for inputs and greeting
ttk.Label(mainframe, text='Welcome to Yung TKs Quarterback Rating Calculator').grid(column=1, row=1, sticky=(W,E))
ttk.Label(mainframe, text='Please make sure to only enter numbers and fill out all inputs').grid(column=1,row=2,sticky=E)

#the labels for the inputs
ttk.Label(mainframe, text='Completions').grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text='Attempts').grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text='Yards').grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text='Touchdowns').grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text='Interceptions').grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text='QB Rating').grid(column=3, row=7, sticky=W)

#button for calculating
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=8, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)

comp_entry.focus()
root.bind('<Return>',calculate)

root.mainloop()


        
        

