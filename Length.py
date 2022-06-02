from tkinter import *

App=Tk()
App.title('Length Converter')
App.geometry('350x150')
scales=['Meters','Inches','Foot']

_from=StringVar()
from_menu=OptionMenu(App,_from,*scales)
from_menu.grid(row=0,column=0,pady=5)

lbl=Label(App,text='Convert to ')
lbl.grid(row=0,column=1,pady=5)

to_=StringVar()
to_menu=OptionMenu(App,to_,*scales)
to_menu.grid(row=0,column=2,pady=5)

enter=Label(App,text='Enter your Length ')
enter.grid(row=1,column=0,columnspan=2,pady=5)

numE=Entry(App)
numE.grid(row=1,column=2,columnspan=2,pady=5)

def converter():
    From=_from.get()
    To=to_.get()
    num=int(numE.get())

    if From=='Meters' and To=='Inches':
        conv_num=num * 39.37
    elif From=='Meters' and To=='Foot':
        conv_num=num * 3.28
    elif From=='Inches' and To=='Meters':
        conv_num=num / 39.37
    elif From=='Inches' and To=='Foot':
        conv_num=num / 12
    elif From=='Foot' and To=='Meters':
        conv_num=num / 3.28
    elif From=='Foot' and To=='Inches':
        conv_num=num * 12
    else:
        conv_num=num

    numL=Label(App,text=round(conv_num,2),width=10)
    numL.grid(row=1,column=4,pady=5)


conB=Button(App,text='Convert',command=converter)
conB.grid(row=2,column=0,pady=5)

App.mainloop()