from tkinter import *
from tkinter import ttk

def calculate():
    rice=rice_p.get()*rice_q.get()
    rice_amt.set(rice)
    oil=oil_p.get()*oil_q.get()
    oil_amt.set(oil)
    biscuits=biscuits_p.get()*biscuits_q.get()
    biscuits_amt.set(biscuits)
    cheese=cheese_p.get()*cheese_q.get()
    cheese_amt.set(cheese)
    milk=milk_p.get()*milk_q.get()
    milk_amt.set(milk)
    total_amt.set(rice+oil+biscuits+cheese+milk)
    
root=Tk()
root.title("Shopping Bill")
root.geometry("440x300")
root.configure(bg='light yellow')

rice_p=DoubleVar()
rice_q=DoubleVar()
rice_amt=DoubleVar()

oil_p=DoubleVar()
oil_q=DoubleVar()
oil_amt=DoubleVar()

biscuits_p=DoubleVar()
biscuits_q=DoubleVar()
biscuits_amt=DoubleVar()

cheese_p=DoubleVar()
cheese_q=DoubleVar()
cheese_amt=DoubleVar()
milk_p=DoubleVar()
milk_q=DoubleVar()
milk_amt=DoubleVar()
total_amt=DoubleVar()


Label(root, text="Karma Tshongkhang", fg="dark red", font=("Impact",18), bg="light yellow").grid(row=0, column=0,  padx=10, columnspan=4, pady=10)

Label(root, text="Item Name: ", font=("Cambria",11,"bold"), bg="light yellow").grid(row=1, column=0, sticky=W, padx=10)
Label(root, text="Quantity", font=("Cambria",11,"bold"), bg="light yellow").grid(row=1, column=1)
Label(root, text="Price", font=("Cambria",11,"bold"), bg="light yellow").grid(row=1, column=2)
Label(root, text="Amount", font=("Cambria",11,"bold"), bg="light yellow").grid(row=1, column=3)

Label(root, text="1. Rice", font=("Calibri",11), bg="light yellow").grid(row=2, column=0, sticky=W, padx=10)
Entry(root, width=15, textvariable=rice_p).grid(row=2, column=1, sticky=W, padx=3)
Entry(root, width=15, textvariable=rice_q).grid(row=2, column=2, sticky=W, padx=3)
Label(root, width=15, textvariable=rice_amt).grid(row=2, column=3, sticky=W, padx=3)

Label(root, text="2. Oil", font=("Calibri",11), bg="light yellow").grid(row=3, column=0, sticky=W, padx=10)
Entry(root, width=15, textvariable=oil_p).grid(row=3, column=1, sticky=W, padx=3)
Entry(root, width=15, textvariable=oil_q).grid(row=3, column=2, sticky=W, padx=3)
Label(root, width=15, textvariable=oil_amt).grid(row=3, column=3, sticky=W, padx=3)

Label(root, text="3. Biscuits", font=("Calibri",11), bg="light yellow").grid(row=4, column=0, sticky=W, padx=10)
Entry(root, width=15, textvariable=biscuits_p).grid(row=4, column=1, sticky=W, padx=3)
Entry(root, width=15, textvariable=biscuits_q).grid(row=4, column=2, sticky=W, padx=3)
Label(root, width=15, textvariable=biscuits_amt).grid(row=4, column=3, sticky=W, padx=3)

Label(root, text="4. Cheese", font=("Calibri",11), bg="light yellow").grid(row=5, column=0, sticky=W, padx=10)
Entry(root, width=15, textvariable=cheese_p).grid(row=5, column=1, sticky=W, padx=3)
Entry(root, width=15, textvariable=cheese_q).grid(row=5, column=2, sticky=W, padx=3)
Label(root, width=15, textvariable=cheese_amt).grid(row=5, column=3, sticky=W, padx=3)

Label(root, text="5. Milk Powder", font=("Calibri",11), bg="light yellow").grid(row=6, column=0, sticky=W, padx=10)
Entry(root, width=15, textvariable=milk_p).grid(row=6, column=1, sticky=W, padx=3)
Entry(root, width=15, textvariable=milk_q).grid(row=6, column=2, sticky=W, padx=3)
Label(root, width=15, textvariable=milk_amt).grid(row=6, column=3, sticky=W, padx=3)

Button(root, text="Total Amount: ", font=("Cambria",11), command=calculate).grid(row=7, column=1, sticky=EW, columnspan=2)
Label(root, font=('Cambria',12,'bold'),textvariable=total_amt).grid(row=7, column=3, sticky=EW, padx=3)

def receipt():
    receipt=Tk()
    receipt.geometry("800x250")
    
    def done():
        receipt.destroy()
        
    Label(receipt, text="Karma Tshongkhang", fg="dark red", font=("Impact",18), bg="light yellow").grid(row=0,
        column=0,  padx=10, columnspan=4, pady=10)
    Button(receipt, text="Done", font=("Cambria",11), command=done).grid(row=2, column=0,  pady=10)
    
    tree=ttk.Treeview(receipt, columns=("Quantity","Price", "Amount"))

    tree.heading("#0", text="Item Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Amount", text="Amount")
    tree.insert("", "end", text="Rice", values=(rice_q.get(), rice_p.get(), rice_amt.get()))
    tree.insert("", "end", text="Oil", values=(oil_q.get(), oil_p.get(), oil_amt.get()))
    tree.insert("", "end", text="Biscuits", values=(biscuits_q.get(), biscuits_p.get(), biscuits_amt.get()))
    tree.insert("", "end", text="Cheese", values=(cheese_q.get(), cheese_p.get(), cheese_amt.get()))
    tree.insert("", "end", text="Milk Powder", values=(milk_q.get(), milk_p.get(), milk_amt.get()))
    
    tree.grid(row=3, column=0)

Button(root, text="Generate Receipt", font=("Cambria",11), command=receipt).grid(row=8, column=1, columnspan=2, sticky=EW, pady=10)

root.mainloop()
