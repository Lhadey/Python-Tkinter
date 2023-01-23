from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height/100) ** 2
    bmi_label.config(text=f"Your BMI is {bmi:.2f}")
    bmi_index(bmi)
    
def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-measure', f'BMI = {bmi:.2f} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-measure', f'BMI = {bmi:.2f} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-measure', f'BMI = {bmi:.2f} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-measure', f'BMI = {bmi:.2f} is Obesity') 
    else:
        messagebox.showerror('bmi-measure', 'something went wrong!')
    
root=Tk()
root.title("BMI Calculator")
root.geometry("600x300")
root.configure(bg="azure")

image= Image.open("gho.jpg")
img=image.resize((100,100))
my_img=ImageTk.PhotoImage(img)

Label(root, image=my_img).grid(row=1, column=2,rowspan=5, padx=10)
Label(root, text="BMI Calculator!",bg="azure",font=('Times New Roman',20,'bold')).grid(row=0, column=1, padx=10, pady=10)
Label(root, text="Enter your weight and height to calculate your BMI!",bg="azure",font=('Times New Roman',17)).grid(row=1, column=1, padx=10,pady=10)

Label(root, text="Weight (kg):",bg="azure",font=('Times New Roman',14)).grid(row=2, column=0)
weight_entry = Entry(root)
weight_entry.grid(row=2, column=1)

Label(root, text="Height (cm):",bg="azure",font=('Times New Roman',14)).grid(row=3, column=0)
height_entry = Entry(root)
height_entry.grid(row=3, column=1)

Button(root, text="Calculate",bg="azure", command=calculate_bmi).grid(row=4, column=0, columnspan=2, pady=10)

bmi_label = Label(root, text="",bg="azure")
bmi_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
