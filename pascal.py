from tkinter import *

root = Tk()

scroll = Scrollbar(root,orient=HORIZONTAL)
txt = Text(root,wrap = NONE)

scroll.config(command=txt.xview)
txt.config(xscrollcommand = scroll.set)
scroll.pack(fill=BOTTOM)
txt.pack()

for i in range(400):
	txt.insert(END,"This is line %d \t"%i)

root.mainloop()
