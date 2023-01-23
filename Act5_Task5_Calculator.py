from tkinter import *
from PIL import Image, ImageTk
'''Image is a special class in pillow module that help us perform operations on images,
ImageTk is another image module in pillow especially built to work for tkinter'''
from tkinter import messagebox

root=Tk()
root.title("Simple Calculator")
root.geometry("370x220")

first_num=IntVar()
second_num=IntVar()

def add():
    sum=first_num.get() + second_num.get()
    messagebox.showinfo('Result', f"The sum is: {sum}")
    
def multiply():
    product=first_num.get() * second_num.get()
    messagebox.showinfo('Result', f"The product is: {product}")

Label(root, text="Simple Calculator", fg="dark blue", font=("Cambria",20)).grid(row=0, column=0,  padx=10)

image=Image.open('calc.png')
img=image.resize((30, 30))
my_img=ImageTk.PhotoImage(img) #converting pillow compatible image to tkinter compatible image
Label(root, text='Calculator', image=my_img).grid(row=0, column=1, sticky=EW, padx=5)

Label(root, text="""Enter two numbers and click on the buttons
      below to perform the Mathematical Operations. """, font=("Segoe Print",9)).grid(row=1, column=0, columnspan=2)

Label(root, text="Enter the first number: ", font=("Times New Roman",11)).grid(row=2, column=0, sticky=W, padx=10, pady=10)
Entry(root, width=20, justify=CENTER, textvariable=first_num).grid(row=2, column=1, pady=10)

Label(root, text="Enter the second number: ", font=("Times New Roman",11)).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Entry(root, width=20, justify=CENTER, textvariable=second_num).grid(row=3, column=1, pady=5)

Button(root, text="Add", fg="red", font=("Times New Roman",11), command=add).grid(row=4, column=0, padx=18, pady=10, sticky=EW)
Button(root, text="Multiply", fg="red", font=("Times New Roman",11), command=multiply).grid(row=4, column=1, pady=10, sticky=EW)

root.mainloop()
