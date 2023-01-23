from tkinter import *

root=Tk()
root.title("Sign Up Form")
root.geometry("300x300")
root.configure(bg="cyan")

gender=IntVar()

title_label=Label(root, text="Sign Up Form")
title_label.grid(row=0, column=0, columnspan=3)

name_label=Label(root, text="Name: ")
name_label.grid(row=1, column=0)
name_entry=Entry(root, width=15)
name_entry.grid(row=1, column=1)

pw_label=Label(root, text="Password: ")
pw_label.grid(row=3, column=0)
pw_entry=Entry(root, width=15, show="*")
pw_entry.grid(row=3, column=1)

gender_label=Label(root, text="Gender: ")
gender_label.grid(row=4, column=0)

male_rdbtn=Radiobutton(root, text="Male", variable=gender, value=1)
male_rdbtn.grid(row=4, column=1)

female_rdbtn=Radiobutton(root, text="Female", variable=gender, value=2)
female_rdbtn.grid(row=4, column=2)

bio_label=Label(root, text="Share Your Bio here...")
bio_label.grid(row=5, column=0)
bio_text=Text(root, height=4, width=35)
bio_text.grid(row=6, column=0, columnspan=3)

ckbtn=Checkbutton(root, text="I agree to the terms and privacy policy")
ckbtn.grid(row=7, column=0, columnspan=3)

signup_btn=Button(root, text="Sign Up")
signup_btn.grid(row=8, column=0, columnspan=3)

root.mainloop()
