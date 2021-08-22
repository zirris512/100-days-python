from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = (
        [choice(letters) for _ in range(randint(8, 10))]
        + [choice(symbols) for _ in range(randint(2, 4))]
        + [choice(numbers) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)

    random_password = "".join(password_list)
    pyperclip.copy(random_password)

    password_input.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if not website or not password:
        messagebox.showerror(title="Empty Fields", message="Please fill in all fields!")
    else:
        is_ok = messagebox.askyesno(
            title=website,
            message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?",
        )

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="w")

username_input = Entry(width=35)
username_input.insert(0, "steve@email.com")
username_input.grid(row=2, column=1, columnspan=2, sticky="w")

password_input = Entry(width=28)
password_input.grid(row=3, column=1, sticky="w")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
