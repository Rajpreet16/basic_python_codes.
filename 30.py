from tkinter import *
from tkinter import messagebox

root=Tk()

def Ack():
    messagebox.showinfo("Done","Done")

def exit():
    root.destroy()

root.title("Data")

frame = Frame(root,bd='4',relief='groove',width='100').grid(sticky='n')

menubar = Menu(root)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Open")
menubar.add_cascade(label="File",menu=filemenu)

name = Label(frame, text="Name",width='15',height='2').grid(row='0',column='0')
email = Label(frame, text="Email",width='15',height='2').grid(row='1',column='0')
gender = Label(frame, text="Gender",width='15',height='2').grid(row='2',column='0')
pno = Label(frame, text="Contact No.",width='15',height='2').grid(row='5',column='0')

e1 = Entry(frame,width='25').grid(row='0',column='1')
e2 = Entry(frame,width='25').grid(row='1',column='1')
var = IntVar()
R1 = Radiobutton(frame, text="Male", variable=var, value=1,height='2').grid(row='2',column='1')
R2 = Radiobutton(frame, text="Female", variable=var, value=2,height='2').grid(row='2',column='2')
e3 = Entry(frame,width='25').grid(row='5',column='1')

lang = Label(frame, text="No. of Known Languages",width='25',height='2').grid(row='6',column='0')
w = Spinbox(frame, from_=0, to=5).grid(row='6',column='1')
Country = Label(frame, text="Country",width='15',height='2').grid(row='7',column='0')
var=StringVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
choices = ['India', 'USA']
option = OptionMenu(frame, var, *choices)
option.place(x=190,y=190, height=25, width=100)
interest = Label(frame, text="Interests",width='15',height='2').grid(row='8',column='0')
C1 = Checkbutton(frame, text = "Painting", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C2 = Checkbutton(frame, text = "Acting", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C3 = Checkbutton(frame, text = "Others", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C1.grid(row='8',column='1')
C2.grid(row='8',column='2')
C3.grid(row='8',column='3')




B1 = Button(frame, text ="Submit", command = Ack,width='15',height='2',relief='raised').grid(row='9',column='1')
B2 = Button(frame, text ="Exit", command = exit,width='15',height='2').grid(row='9',column='2')
