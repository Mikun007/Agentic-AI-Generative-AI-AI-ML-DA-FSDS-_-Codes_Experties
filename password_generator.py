from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("PYTHON PROJECT  - PASSWORD GENERATOR")

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()

Label(root, text="Python", font='arial 20 bold').pack(side=BOTTOM)

Label(root, text="PASSWORD LENGTH", font="arial 10 bold").pack()

pass_len = IntVar()
Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()

def password_generator():
    password = []

    if pass_len.get() >= 4:
        # At least one of the (uppercase, lowercase, digits and punctuation is in the string)
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        # if it is greater than 4 then add rest
        for _ in range(pass_len.get() - 4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                          string.digits + string.punctuation))
        # Shuffling the characters for more security
        random.shuffle(password)
    else:
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                          string.digits + string.punctuation))

    pass_str.set("".join(password))

def copy():
    pyperclip.copy(pass_str.get())
Button(root, text="GENERATE", command=password_generator).pack(pady=10)
Entry(root, textvariable=pass_str, state="disabled").pack()
Button(root, text="Copy", command=copy).pack(pady=10)
root.mainloop()
