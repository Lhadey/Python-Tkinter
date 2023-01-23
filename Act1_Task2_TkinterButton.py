from tkinter import *

root = Tk()

def button_clicked():
    print("Button clicked!")

# Create the button
button = Button(root, text="Click me!", command=button_clicked)

# Add the button to the window
button.pack()

# Run the Tkinter event loop
root.mainloop()
