from tkinter import *

root=Tk()
root.title("Currency & Distance Converter")
root.geometry("380x330")
root.configure(bg="light green")

nu=StringVar()
usd=StringVar()
km=StringVar()
miles=StringVar()

def nu_usd():
    x=float(nu.get())
    y=x*0.012
    usd.set(y)

def km_miles():
    a=float(km.get())
    b=a*0.621371
    miles.set(b)
    
Label(root, text="Currency & Distance Converter", font=("Candara",14,"bold"), bg="pink").grid(row=0, column=0, columnspan=3, padx=10, pady=10)

Label(root, text="Currency: ", font=("Times New Roman",12), bg="light green").grid(row=1, column=0, columnspan=2)
lb1=Label(root, text="Enter currency in nu and click the button to convert to usd.", font=("Segoe Print",8), bg="light green")
lb1.grid(row=2,column=0, columnspan=3, sticky=W, padx=10)
Label(root, text="* 1 USD = 82.03 Nu", font=("Segoe Print",8), bg="light green").grid(row=3,column=0, columnspan=3, sticky=EW, padx=10)
Label(root, text="Nu: ", font=("Times New Roman",12), bg="light green").grid(row=4, column=0, padx=5, sticky=EW)
Entry(root, width=10, textvariable=nu).grid(row=4, column=1, padx=5, sticky=EW)
Button(root, text="Convert", bg='gray', fg='yellow', command=nu_usd).grid(row=4, column=2, rowspan=2, sticky=EW)
Label(root, text="US $: ", font=("Times New Roman",12), bg="light green").grid(row=5, column=0, padx=5, sticky=EW)
Entry(root, width=10, textvariable=usd).grid(row=5, column=1, padx=5, sticky=EW)

Label(root, text="Distance: ", font=("Times New Roman",12), bg="light green").grid(row=6, column=0, columnspan=2, pady=5)
lb2=Label(root, text="Enter distance in km box and click the button to convert to miles.", font=("Segoe Print",8), bg="light green")
lb2.grid(row=7,column=0, columnspan=3)
Label(root, text="* 1 Mile = 1.61 Km", font=("Segoe Print",8), bg="light green").grid(row=8,column=0, columnspan=3, sticky=EW, padx=10)
Label(root, text="Km: ", font=("Times New Roman",12), bg="light green").grid(row=9, column=0, padx=5, sticky=EW)
Entry(root, width=10, textvariable=km).grid(row=9, column=1, padx=5, sticky=EW)
Button(root, text="Convert", bg='gray', fg='yellow', command=km_miles).grid(row=9, column=2, rowspan=2, sticky=EW)
Label(root, text="Miles: ", font=("Times New Roman",12), bg="light green").grid(row=10, column=0, padx=5, sticky=EW)
Entry(root, width=10, textvariable=miles).grid(row=10, column=1, padx=5, sticky=EW)

root.mainloop()
