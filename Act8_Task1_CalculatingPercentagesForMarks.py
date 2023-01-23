from tkinter import*

def calculate():
    Eng = float(English.get())
    Dzo = float(Dzongkha.get())
    His = float(History.get())
    Geo = float(Geography.get())
    Eco = float(Economics.get())
    total_marks = Eng  + Dzo + His + Geo + Eco
    percentage = (total_marks / 500) * 100
    total_label.configure(text="Total Marks: " + str(total_marks))
    percentage_label.configure(text=f"Percentage: {percentage:.2f}  %")
    if percentage > 39.9:
        remarks='Pass'
    else:
        remarks= 'Fail' 
    remark_label.configure(text="Remark: " + str(remarks))
    
root=Tk()
root.title("Mark Calculation")
root.geometry("600x600")

x=IntVar()
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()

Label(root, text="Calculating Percentages for Mark!",font=('Times New Roman',20,'bold')).grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Std_code:").grid(row=1, column=0, padx=5, pady=5)
Std_code_entry = Entry(root,textvariable=x).grid(row=1, column=1,padx=5, pady=5)

Label(root, text="Name").grid(row=2, column=0,padx=5, pady=5)
Name_entry = Entry(root,textvariable=a).grid(row=2, column=1,padx=5, pady=5)

Label(root, text="Class").grid(row=3, column=0,padx=5, pady=5)
Class_entry = Entry(root,textvariable=b).grid(row=3, column=1,padx=5, pady=5)

Label(root, text="Section:").grid(row=4, column=0,padx=5, pady=5)
Section_entry = Entry(root,textvariable=c).grid(row=4, column=1,padx=5, pady=5)

Label(root, text="Gender:").grid(row=5, column=0,padx=5, pady=5)
Gender_entry = Entry(root,textvariable=d).grid(row=5, column=1,padx=5, pady=5)


Label(root, text="English:").grid(row=6, column=0, padx=5, pady=5)
English = Entry(root)
English.grid(row=6, column=1, padx=5, pady=5)

Label(root, text="Dzongkha :").grid(row=7, column=0, padx=5, pady=5)
Dzongkha =Entry(root)
Dzongkha.grid(row=7, column=1, padx=5, pady=5)

Label(root, text="History:").grid(row=8, column=0, padx=5, pady=5)
History = Entry(root)
History.grid(row=8, column=1, padx=5, pady=5)

Label(root, text="Geography:").grid(row=9, column=0, padx=5, pady=5)
Geography = Entry(root)
Geography.grid(row=9, column=1, padx=5, pady=5)

Label(root, text="Economics:").grid(row=10, column=0, padx=5, pady=5)
Economics = Entry(root)
Economics.grid(row=10, column=1, padx=5, pady=5)

calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

total_label = Label(root, text="Total Marks: ")
total_label.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

percentage_label = Label(root, text="Percentage: ")
percentage_label.grid(row=13, column=0, columnspan=2, padx=5, pady=5)

remark_label = Label(root, text="Remark: ")
remark_label.grid(row=14, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
