import random
from tkinter import *
from PIL import Image, ImageTk

def move_button():
    global time_left
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    image.place(x=x, y=y)
    if time_left > 0:
        root.after(1000, move_button)
    else:
        game_over()
        
def increase_score(event):
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

def decrease_time():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Time: {time_left}")
        root.after(1000, decrease_time)
    else:
        game_over()

def game_over():
    image.place_forget()
    game_over_label.config(text="Game Over! Your score is: " + str(score))
         
root = Tk()
root.geometry("400x400")

score = 0
score_label = Label(root, text="Score: 0", font=("Calibri 13"))
score_label.pack()
time_left = 10
time_label = Label(root, text="Time: 10", font=("Calibri 13"))
time_label.pack()
game_over_label = Label(root, text="", font=("Cambria 13"))
game_over_label.pack()

img=Image.open('cheese.png')
img_1=ImageTk.PhotoImage(img.resize((30,30)))
image=Label(root, text='cheese', image=img_1)
image.pack()
image.bind('<Button-1>',increase_score)

root.after(1000, move_button)
root.after(1000, decrease_time)
root.mainloop()
