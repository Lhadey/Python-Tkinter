import tkinter as tk

def check_answer():
    global score
    if (entry.get()).lower() == questions[current_question][1].lower():
        score+=10
        score_label.config(text=f"Score: {score}")
        label.config(text="Correct!")
    else:
        label.config(text="Incorrect. The correct answer is " + questions[current_question][1])

def next_question():
    global current_question
    current_question += 1
    if current_question >= len(questions):
        label.config(text="Quiz completed!")
        check_button.pack_forget()
        next_button.pack_forget()
        entry.pack_forget()
        return
    label.config(text=questions[current_question][0])
    entry.delete(0, tk.END)

questions = [["What is the capital of Bhutan?", "Thimphu"],
    ["What is the largest Dzongkhag in Bhutan?", "Trashigang"],
    ["What is the name of the major river that runs through Trashiyangtse and Trashigang?", "Drangmechhu"]]

current_question = 0

root = tk.Tk()
root.title("Quiz Game")

score=0
score_label=tk.Label(root, text="Score: 0")
score_label.pack()

label = tk.Label(root, text=questions[current_question][0])
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack()

root.mainloop()
