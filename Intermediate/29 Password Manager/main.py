from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.askokcancel(
            title="Error", message="Please don't leave any fields blank!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nUsername: {username} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open("Intermediate/29 Password Manager/data.txt", "a") as text_file:
                text_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="Intermediate/29 Password Manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "exampleemail@awesome.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
generatepass_button = Button(text="Generate Password", command=generate_password)
generatepass_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
