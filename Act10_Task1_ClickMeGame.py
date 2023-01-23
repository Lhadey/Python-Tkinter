import random
from tkinter import *

def move_button():
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    target_button.place(x=x, y=y)
    root.after(1000, move_button)

def increase_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

root = Tk()
root.geometry("400x400")

score = 0
score_label = Label(root, text="Score: 0")
score_label.pack()

target_button = Button(root, text="Click Me!", command=increase_score)
target_button.pack()

root.after(1000, move_button)
root.mainloop()
