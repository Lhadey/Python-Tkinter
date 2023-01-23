from tkinter import *

root = Tk()
root.title("Favorite Comedian")
root.geometry("300x200")
root.configure(bg="sky blue")

actor = IntVar()

Label(root, text="Choose your favourite Bhutanese Comedian:", bg="sky blue").pack()

Radiobutton(root, text="Gyem Dorji", padx=20, bg="sky blue", variable=actor, value=1).pack(anchor=W)
Radiobutton(root, text="Gyem Tshering", padx=20,bg="sky blue", variable=actor, value=2).pack(anchor=W)
Radiobutton(root, text="Phurba Thinley", padx=20, bg="sky blue", variable=actor, value=3).pack(anchor=W)
Radiobutton(root, text="Khengtala", padx=20, bg="sky blue", variable=actor, value=4).pack(anchor=W)
Radiobutton(root, text="Horgola", padx=20, bg="sky blue", variable=actor, value=5).pack(anchor=W)

root.mainloop()
