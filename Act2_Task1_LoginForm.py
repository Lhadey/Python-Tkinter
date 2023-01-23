from tkinter import *

root=Tk()

un=Label(root, text="Username:")
un.grid(row=0, column=0)

un_entry=Entry(root, width=10)
un_entry.grid(row=0, column=1)

p=Label(root, text="Password:")
p.grid(row=1, column=0)

p_entry=Entry(root, width=10, show="*")
p_entry.grid(row=1, column=1)

l=Button(root, text="Login")
l.grid(row=2, column=0, columnspan=2)


root.mainloop()
