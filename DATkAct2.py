import tkinter as tk
import random

def roll_dice():
    roll = random.randint(1, 6)
    user_label.config(text="You rolled a " + str(roll) + "!")
    c_roll=random.randint(1, 6)
    computer_label.config(text="Computer rolled a " + str(c_roll) + "!")
    if roll > c_roll:
        result.config(text="You won!")
    elif c_roll> roll:
        result.config(text="Computer won!")
    else:
        result.config(text="It's a tie!")
    

root = tk.Tk()
root.title("Dice Roller")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Roll the dice!")
label.pack()

roll_button = tk.Button(frame, text="Roll", command=roll_dice)
roll_button.pack()

user_label= tk.Label(root, text="")
user_label.pack()

computer_label=tk.Label(root, text="")
computer_label.pack()

result=tk.Label(root, text="")
result.pack()

root.mainloop()
